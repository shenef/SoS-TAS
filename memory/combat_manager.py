import contextlib
import logging
from enum import Enum, auto
from typing import Self

from memory.core import mem_handle
from memory.mappers.enemy_name import EnemyName
from memory.mappers.player_party_character import PlayerPartyCharacter

logger = logging.getLogger(__name__)


class CombatEncounter(Enum):
    Basic = auto()
    FirstEncounter = auto()
    SecondEncounter = auto()
    DwellerOfStrife = auto()
    DwellerOfDread = auto()
    KOTutorial = auto()
    LiveManaTutorial = auto()
    ManaRegenTutorial = auto()
    RoundsTutorial = auto()
    SpellLockTutorial = auto()
    TimedBlocksTutorial = auto()
    TimedHitsTutorial = auto()


class CombatDamageType(Enum):
    NONE = 0
    Any = 1
    Sword = 2
    Sun = 4
    Moon = 8
    Eclipse = 16
    Poison = 32
    Arcane = 64
    Stun = 128
    Blunt = 256
    Magical = 252


class CombatEnemyTarget:
    def __init__(self: Self) -> None:
        """Initialize a new CombatEnemyTarget object."""
        self.max_hp: int = None
        self.current_hp: int = None
        self.physical_attack: int = None
        self.physical_defense: int = None
        self.magic_attack: int = None
        self.magic_defense: int = None
        self.speed: int = None
        self.guid: str = None
        self.name: str = None
        self.turns_to_action: int = None
        self.unique_id: str = None
        self.total_spell_locks: int = 0
        self.spell_locks: list[CombatDamageType] = []


class NextCombatAction(Enum):
    NONE = auto()
    Casting = auto()
    Attacking = auto()


class NextCombatEnemy:
    def __init__(
        self: Self,
        enemy: CombatEnemyTarget,
        state_type: NextCombatAction,
        move_name: str,
        movement_done: bool,
    ) -> None:
        self.enemy = enemy
        self.state_type = state_type
        self.move_name = move_name
        self.movement_done = movement_done


class CombatPlayer:
    def __init__(self: Self) -> None:
        """Initialize a new CombatPlayer object."""
        self.max_hp: int = None
        self.current_hp: int = None
        self.current_mp: int = None
        self.physical_attack: int = None
        self.magical_attack: int = None
        self.selected = False
        self.definition_id: str = None
        self.timed_attack_ready = False
        self.dead = False
        self.character = PlayerPartyCharacter.NONE
        self.enabled: bool = None
        self.combo_points: int = 0
        self.ultimate_gauge: float = 0.0
        self.mana_charge_count: int = None


class CombatManager:
    # The null pointer here is a const for the pointer we see provided
    # When the selectors drop from memory for brief periods - Its more of
    # a magic number than anything.
    NULL_POINTER = 0xFFFFFFFF
    ITEM_OBJECT_OFFSET = 0x8
    ITEM_INDEX_0_ADDRESS = 0x20
    SPELLPOWER_ZERO = 0.0

    def __init__(self: Self) -> None:
        """Initialize a new CombatManager object."""
        self.memory = mem_handle()
        self.base: int = None
        self.fields_base: int = None
        self.selector_base: int = None
        self.enemies: list[CombatEnemyTarget] = []
        self.players: list[CombatPlayer] = []
        self.selected_character = PlayerPartyCharacter.NONE
        self.combat_controller = CombatEncounter.Basic
        self.current_encounter_base: int = None
        self.encounter_done: bool = None
        self.small_live_mana: int = None
        self.big_live_mana: int = None
        self.battle_command_has_focus = False
        self.battle_command_index: int = None
        self.skill_command_has_focus = False
        self.skill_command_index: int = None
        self.selected_attack_target_guid: str = None
        self.selected_skill_target_guid: str = None
        self.next_combat_enemy: NextCombatEnemy = None
        self.current_combo_points: int = 0
        self.current_filled_combo_points: int = 0
        self.ultimate_progress: float = 0.0
        # Moonerang
        self.projectile_hit_count = 0
        self.projectile_speed = 0.0

    def update(self: Self) -> None:
        # try:
        if self.memory.ready_for_updates:
            if self.base is None or self.fields_base is None:
                self.encounter_done = True
                singleton_ptr = self.memory.get_singleton_by_class_name("CombatManager")

                if singleton_ptr is None:
                    return
                self.base = self.memory.get_class_base(singleton_ptr)
                self.fields_base = self.memory.get_class_fields_base(singleton_ptr)
                self.current_encounter_base = self.memory.get_field(
                    self.fields_base, "currentEncounter"
                )

            else:
                self._read_encounter_done()

                if self.encounter_done is True:
                    self.combat_controller = CombatEncounter.Basic
                    return

                self._read_combat_controller()
                self._read_combo_and_ultimates()
                self._read_players()
                self._read_enemies()
                self._read_battle_commands()
                if not self.battle_command_has_focus:
                    self._read_skill_commands()
                self._read_live_mana()
                self._read_current_target()
                self.projectile_hit_count = self.read_projectile_hit_count()
                self.projectile_speed = self.read_projectile_speed()

    # except Exception as _e:
    #     # logger.debug(f"Combat Manager Reloading - {type(_e)}")
    #     self.__init__()

    def _read_combo_and_ultimates(self: Self) -> None:
        if self._should_update():
            try:
                combo_points_panel_ptr = self.memory.follow_pointer(
                    self.base,
                    [
                        self.current_encounter_base,
                        0x128,
                        0x98,
                        0x50,
                        0x0,
                    ],
                )
                ult_meter_ptr = self.memory.follow_pointer(combo_points_panel_ptr, [0x28, 0x0])
                combo_points_meter_ptr = self.memory.follow_pointer(
                    combo_points_panel_ptr, [0x30, 0x0]
                )

                ult_progress = self.memory.read_float(ult_meter_ptr + 0x40)
                combo_points = self.memory.read_int(combo_points_meter_ptr + 0x58)
                filled_combo_points = self.memory.read_int(combo_points_meter_ptr + 0x5C)

                self.ultimate_progress = ult_progress
                self.current_combo_points = combo_points
                self.current_filled_combo_points = filled_combo_points
            except Exception:
                self.current_combo_points = 0
                self.current_filled_combo_points = 0
                self.ultimate_progress = 0.0

    def read_next_combat_enemy(self: Self) -> None:
        if self._should_update():
            try:
                ongoing_move_ptr = self.memory.follow_pointer(
                    self.base,
                    [
                        self.current_encounter_base,
                        0x128,
                        0x58,
                        0x10,
                        0x20,
                        0x68,
                        0x0,
                    ],
                )
                combat_move_ptr = self.memory.follow_pointer(
                    self.base,
                    [
                        self.current_encounter_base,
                        0x128,
                        0x58,
                        0x10,
                        0x20,
                        0x58,
                        0x0,
                    ],
                )

                is_player = self.memory.read_bool(ongoing_move_ptr + 0xB8)
                if is_player:
                    self.next_combat_enemy = None
                    return
                spell_power = self.memory.read_float(combat_move_ptr + 0x30)
                guid_ptr = self.memory.follow_pointer(ongoing_move_ptr, [0xF8, 0xF0, 0x18, 0x0])
                guid = self.memory.read_uuid(guid_ptr + 0x14)

                current_state_ptr = self.memory.follow_pointer(
                    ongoing_move_ptr,
                    [0x80, 0x50, 0x0],
                )

                move_ptr = self.memory.follow_pointer(
                    combat_move_ptr, [0x90, 0x18, 0x10, 0x20, 0x18, 0x0]
                )
                move_length = self.memory.read_int(move_ptr + 0x10)
                move_name = self.memory.read_string(move_ptr + 0x14, move_length * 2)

                next_enemy = None
                for enemy in self.enemies:
                    if enemy.unique_id == guid:
                        next_enemy = enemy

                # if the next move has spell power assume its a cast
                state_type = NextCombatAction.NONE
                movement_done = False
                if next_enemy and spell_power > self.SPELLPOWER_ZERO:
                    state_type = NextCombatAction.Casting
                else:
                    state_type = NextCombatAction.Attacking
                    movement_done = self.memory.read_bool(current_state_ptr + 0x11A)
                self.next_combat_enemy = NextCombatEnemy(
                    enemy=next_enemy,
                    state_type=state_type,
                    move_name=move_name.replace("\x00", ""),
                    movement_done=movement_done,
                )
                return
            except Exception:
                self.next_combat_enemy = None
                return
        self.next_combat_enemy = None

    def _should_update(self: Self) -> None:
        # Helper function for updating itself and ensuring an internal function doesn't run without
        # the base. This is different than other modules as an attempt to improve performance of the
        # combat manager module.
        return self.memory.ready_for_updates and self.current_encounter_base is not None

    def _read_current_target(self: Self) -> None:
        target_unique_id_base = None

        selected_attack_target_guid = ""
        selected_skill_target_guid = ""
        selected_target_ptr = None

        # Finds the player that is currently selected and uses their controller for selection.
        with contextlib.suppress(Exception):
            items_ptr = self.memory.follow_pointer(
                self.base,
                [
                    self.current_encounter_base,
                    0x128,
                    0x98,
                    0x40,
                    0x10,
                    0x0,
                ],
            )
            if items_ptr:
                count = self.memory.read_int(items_ptr + 0x18)
                address = self.ITEM_INDEX_0_ADDRESS
                for _item in range(count):
                    item_ptr = self.memory.follow_pointer(items_ptr, [address, 0x0])
                    selected = self.memory.read_bool(item_ptr + 0x78)
                    if selected:
                        selected_target_ptr = item_ptr
                        break
                    address += self.ITEM_OBJECT_OFFSET
            else:
                return
        if not selected_target_ptr:
            return

        with contextlib.suppress(Exception):
            target_unique_id_base = self.memory.follow_pointer(
                selected_target_ptr,
                [
                    0x68,
                    0x38,
                    0x190,
                    0x30,
                    0xA8,
                    0x80,
                    0x48,
                    0x100,
                    0x80,
                    0xF8,
                    0xF0,
                    0x18,
                    0x0,
                ],
            )

        # This check was added due to the pointer not falling off in time,
        # referencing an enemy that just died
        try:
            selected_attack_target_guid = self.memory.read_uuid(target_unique_id_base + 0x14)
        except Exception:
            selected_attack_target_guid = ""

        # Separate Skill section lookup
        # TODO(eein): This is currently not correct as it does consider the
        # skill target, but gets a bit washed out if there are AOE targets.
        with contextlib.suppress(Exception):
            target_unique_id_base = self.memory.follow_pointer(
                selected_target_ptr,
                [
                    0x68,
                    0x38,
                    0x190,
                    0x28,
                    0x10,
                    0x20,
                    0xA8,
                    0x80,
                    0x48,
                    0x100,
                    0x80,
                    0xF8,
                    0xF0,
                    0x18,
                    0x0,
                ],
            )

        # This check was added due to the pointer not falling off in time,
        # referencing an enemy that just died
        try:
            selected_skill_target_guid = self.memory.read_uuid(target_unique_id_base + 0x14)
        except Exception:
            selected_skill_target_guid = ""

        # if the current player is selected, set it to the main combat manager state
        # this will help us prevent scanning lists later on
        self.selected_attack_target_guid = selected_attack_target_guid
        self.selected_skill_target_guid = selected_skill_target_guid

    def _read_combat_controller(self: Self) -> None:
        if self._should_update():
            try:
                combat_controller_ptr = self.memory.follow_pointer(
                    self.base,
                    [self.current_encounter_base, 0x128, 0x0, 0x78, 0x10, 0x0],
                )

                controller = self.memory.read_string(combat_controller_ptr + 0x0, 25)
                match controller:
                    case s if s.startswith("FirstEncounter"):
                        self.combat_controller = CombatEncounter.FirstEncounter
                        return
                    case s if s.startswith("SecondEncounter"):
                        self.combat_controller = CombatEncounter.SecondEncounter
                    case s if s.startswith("DwellerOfStrife"):
                        self.combat_controller = CombatEncounter.DwellerOfStrife
                    case s if s.startswith("DwellerOfDread"):
                        self.combat_controller = CombatEncounter.DwellerOfDread
                    case s if s.startswith("KOTutorial"):
                        self.combat_controller = CombatEncounter.KOTutorial
                    case s if s.startswith("LiveManaTutorial"):
                        self.combat_controller = CombatEncounter.LiveManaTutorial
                    case s if s.startswith("ManaRegenTutorial"):
                        self.combat_controller = CombatEncounter.ManaRegenTutorial
                    case s if s.startswith("RoundsTutorial"):
                        self.combat_controller = CombatEncounter.RoundsTutorial
                    case s if s.startswith("SpellLockTutorial"):
                        self.combat_controller = CombatEncounter.SpellLockTutorial
                    case s if s.startswith("TimedBlocksTutorial"):
                        self.combat_controller = CombatEncounter.TimedBlocksTutorial
                    case s if s.startswith("TimedHitsTutorial"):
                        self.combat_controller = CombatEncounter.TimedHitsTutorial
                    case _:
                        self.combat_controller = CombatEncounter.Basic

            except Exception:
                self.combat_controller = CombatEncounter.Basic

    def read_projectile_is_current_player(self: Self) -> bool:
        if self._should_update():
            try:
                progress_ptr = self.memory.follow_pointer(
                    self.base, [0x168, 0x18, 0x20, 0x128, 0x80, 0x0]
                )

                return self.memory.read_bool(progress_ptr + 0xB8)

            except Exception:
                return False
        return False

    def read_projectile_position(self: Self) -> float:
        if self._should_update():
            try:
                progress_ptr = self.memory.follow_pointer(
                    self.base, [0x168, 0x18, 0x20, 0x118, 0x60, 0x0]
                )

                return self.memory.read_float(progress_ptr + 0xAC)

            except Exception:
                return 0.0
        return 0.0

    def read_projectile_bounce_count(self: Self) -> int:
        """How many times the projectile has been sent back to the enemy."""
        if self._should_update():
            try:
                progress_ptr = self.memory.follow_pointer(self.base, [0x168, 0x18, 0x20, 0x0])

                return self.memory.read_int(progress_ptr + 0x15C)

            except Exception:
                return 0
        return 0

    def read_projectile_hit_count(self: Self) -> int:
        """How many times the projectile has hit something (usually 1 more than bounce count)."""
        if self._should_update():
            try:
                progress_ptr = self.memory.follow_pointer(self.base, [0x168, 0x18, 0x20, 0x0])

                return self.memory.read_int(progress_ptr + 0x158)

            except Exception:
                return 0
        return 0

    def read_projectile_speed(self: Self) -> float:
        if self._should_update():
            try:
                progress_ptr = self.memory.follow_pointer(
                    self.base, [0x168, 0x18, 0x20, 0x118, 0x0]
                )

                return self.memory.read_float(progress_ptr + 0xC8)

            except Exception:
                return 0.0
        return 0.0

    def read_back_to_slot(self: Self) -> bool:
        if self._should_update():
            try:
                back_to_slot_ptr = self.memory.follow_pointer(self.base, [0x168, 0x18, 0x20, 0x0])
                # this is now actually finalHitDelayDone instead of moongirlBackToSlot
                back_to_slot = self.memory.read_bool(back_to_slot_ptr + 0x160)
                if back_to_slot:
                    return True

            except Exception:
                return False
        return False

    # Battle Commands are the Main menu of commands (Attack, Skills, Combo, Items)
    def _read_battle_commands(self: Self) -> None:
        if self._should_update():
            battle_command_selector = self.memory.follow_pointer(
                self.base, [self.current_encounter_base, 0x140, 0x50, 0x68, 0x0]
            )
            # Checks if we lost access to the selector pointer for a brief period as the UI changes.
            if battle_command_selector == self.NULL_POINTER:
                self.battle_command_has_focus = False
                self.battle_command_index = None
                return

            try:
                if battle_command_selector:
                    # Checks an address to see if the battle command menu is visible
                    # and read the index for it if it is available, otherwise set it
                    # back to a NoneType for safety
                    has_focus = self.memory.read_bool(battle_command_selector + 0x3C)

                    self.battle_command_has_focus = has_focus
                    if has_focus:
                        selected_item_index = self.memory.read_longlong(
                            battle_command_selector + 0x40
                        )
                        self.battle_command_index = selected_item_index
                    else:
                        self.battle_command_index = None
                    return
            except Exception:
                # Not sure what to do here until i figure out the state machines...
                self.battle_command_has_focus = False
                self.battle_command_index = None
        self.battle_command_has_focus = False
        self.battle_command_index = None

    # Skill Commands are the menu of the "skills" command (ie Healing Light, Sunball)
    # This also applies to combos.
    # TODO(eein): We need a way to differentiate between the combos and skills menu.
    def _read_skill_commands(self: Self) -> None:
        if self._should_update():
            skill_command_selector = self.memory.follow_pointer(
                self.base, [self.current_encounter_base, 0x140, 0x50, 0x78, 0x0]
            )
            # Checks if we lost access to the selector pointer for a brief period as the UI changes.
            if skill_command_selector == self.NULL_POINTER:
                self.skill_command_has_focus = False
                self.skill_command_index = None
                return

            if skill_command_selector:
                try:
                    # Checks an address to see if the skill command menu is visible
                    # and read the index for it if it is available, otherwise set it
                    # back to a NoneType for safety. This method is wrapped in a try
                    # as it seems to lose its pointer quite often, especially when the
                    # item menu is open
                    # TODO(eein): Does the skill_command_selector apply to the items menu as well?
                    has_focus = self.memory.read_bool(skill_command_selector + 0x3C)
                    selected_item_index = self.memory.read_longlong(skill_command_selector + 0x40)
                    self.skill_command_has_focus = has_focus
                    self.skill_command_index = selected_item_index
                    if has_focus:
                        self.skill_command_index = selected_item_index
                    else:
                        self.skill_command_index = None
                    return
                except Exception:
                    self.skill_command_has_focus = False
                    self.skill_command_index = None
        self.skill_command_has_focus = False
        self.skill_command_index = None

    # Reads whether the encounter is done - this reads negative to standard development
    # as this is what the game provides as a value.
    # For example:
    # `Encounter Done: True`` means there is no battle going on.
    # This makes it a bit frustrating to use in conditional statements, so be wary.
    def _read_encounter_done(self: Self) -> None:
        if self._should_update():
            try:
                current_encounter = self.memory.follow_pointer(
                    self.base, [self.current_encounter_base, 0x0]
                )
                if current_encounter:
                    done = self.memory.read_bool(current_encounter + 0x16A)
                    self.encounter_done = done
                    return
            except Exception:
                return

        self.encounter_done = True

    # Reads the `small mana` on the ground and the `big mana` being charged for Boost
    # The small mana value increases incrementally over a short period of time, so if
    # it is needing to be used, it must be done carefully.
    # Small live mana has a max value of 15.
    # As boost is charged, 5 small live mana is consumed per level, the value is immediately
    # deducted, and the big_live_mana field increases by 1. Reversing a big live mana immediately
    # returns 5 back to the small_live_mana field.
    # When a boost is consumed, the player received the total big live mana as a mana_charge.
    def _read_live_mana(self: Self) -> None:
        if self._should_update():
            small_live_mana = self.memory.follow_pointer(
                self.base, [self.current_encounter_base, 0x80, 0x20, 0x0]
            )
            if small_live_mana == self.NULL_POINTER:
                self.small_live_mana = 0
                self.big_live_mana = 0
                return
            big_live_mana = self.memory.follow_pointer(
                self.base, [self.current_encounter_base, 0x80, 0x28, 0x0]
            )
            if big_live_mana == self.NULL_POINTER:
                self.small_live_mana = 0
                self.big_live_mana = 0
                return
            if small_live_mana and big_live_mana:
                self.small_live_mana = self.memory.read_int(small_live_mana + 0x18)
                self.big_live_mana = self.memory.read_int(big_live_mana + 0x18)
                return

    # Reads information about players, see details below:
    def _read_players(self: Self) -> None:
        if self._should_update():
            selected_character = PlayerPartyCharacter.NONE
            try:
                panel_count_ptr = self.memory.follow_pointer(
                    self.base, [self.current_encounter_base, 0x128, 0x98, 0x0]
                )
                panel_count = self.memory.read_int(panel_count_ptr + 0x5C)
                player_panels_list = self.memory.follow_pointer(
                    self.base, [self.current_encounter_base, 0x128, 0x98, 0x40, 0x0]
                )
            except Exception:
                self.players = []
                return

            if player_panels_list == self.NULL_POINTER:
                self.players = []
                return
            # Item is an array of pointers of size 0x08
            items = self.memory.follow_pointer(
                player_panels_list,
                [0x10, 0x0],
            )
            players = []
            if items:
                address = self.ITEM_INDEX_0_ADDRESS

                for _item in range(panel_count):
                    character = PlayerPartyCharacter.NONE
                    item = self.memory.follow_pointer(items, [address, 0x0])

                    # There will be times when there is an empty pointer in a list of items,
                    # This checks for that case and skips that record.
                    # For example:
                    # Items
                    #    - 0x20 - Item[0] -> Pointer 0xF30d0930
                    #    - 0x20 - Item[0] -> Pointer 0xF30d0930
                    #    - 0x20 - Item[0] -> Pointer 0x00000000
                    #    - 0x20 - Item[0] -> Pointer 0xF30d0930

                    # TODO(eein): Switch "0x0" to another NULL_POINTER type of 0x00000000
                    if hex(item) == "0x0":
                        address += self.ITEM_OBJECT_OFFSET
                        continue

                    # Check if the character definition id is 0, and return as the
                    # character cannot be queried against
                    character_definition_id = self.memory.read_longlong(item + 0x70)

                    # If the character isn't loaded, ignore.
                    if character_definition_id == 0:
                        address += self.ITEM_OBJECT_OFFSET
                        continue

                    dead_ptr = self.memory.follow_pointer(item, [0x68, 0x38, 0x0])
                    dead = self.memory.read_bool(dead_ptr + 0xD0)

                    # tracks timed attacks maybe
                    # timedAttackHandler -> trackingAfterHit
                    try:
                        timed_attack_ptr = self.memory.follow_pointer(dead_ptr, [0x160, 0x0])
                        timed_attack_value = self.memory.read_bool(timed_attack_ptr + 0x3A)
                    except Exception:
                        timed_attack_value = False

                    definition_id_ptr = self.memory.follow_pointer(item, [0x70, 0x0])
                    # 4 Chars * 2 for utf
                    definition_id = self.memory.read_string(definition_id_ptr + 0x14, 8)

                    # Definition IDS are stored as some goofy serialized utf encoded string
                    # We just do our best with the values that are provided to
                    # Determine the character we are looking at
                    character = PlayerPartyCharacter.parse_definition_id(definition_id)

                    selected = self.memory.read_bool(item + 0x78)
                    hp_text_field = self.memory.follow_pointer(item, [0x28, 0x0])
                    current_hp = self.memory.read_int(hp_text_field + 0x58)

                    portrait = self.memory.follow_pointer(item, [0x68, 0x0])
                    enabled = self.memory.read_bool(portrait + 0x30)

                    live_mana_handler = self.memory.follow_pointer(item, [0x68, 0x38, 0x148, 0x0])
                    mana_charge_count = self.memory.read_int(live_mana_handler + 0x58)

                    if selected:
                        selected_character = character

                    player = CombatPlayer()

                    mp_text_field = self.memory.follow_pointer(item, [0x30, 0x0])

                    current_mp = self.memory.read_int(mp_text_field + 0x58)

                    # TODO(eein): hardcode these for now - we need to extract these players into
                    # something more global and only update them as required.
                    match character:
                        case PlayerPartyCharacter.Zale:
                            player.physical_attack = 20
                            player.magical_attack = 25  # TODO(orkaboy): Maybe not correct
                        case PlayerPartyCharacter.Valere:
                            player.physical_attack = 22
                            player.magical_attack = 20  # TODO(orkaboy): Maybe not correct
                        case PlayerPartyCharacter.Garl:
                            player.physical_attack = 26
                            player.magical_attack = 10  # TODO(orkaboy): Maybe not correct
                        case _:
                            player.physical_attack = 1
                            player.magical_attack = 1  # TODO(orkaboy): Not correct

                    player.current_hp = current_hp
                    player.current_mp = current_mp
                    player.definition_id = definition_id
                    player.character = character
                    player.selected = selected
                    player.ultimate_gauge = self.ultimate_progress
                    player.combo_points = self.current_filled_combo_points
                    player.dead = dead
                    player.enabled = enabled
                    player.timed_attack_ready = timed_attack_value
                    player.mana_charge_count = mana_charge_count
                    players.append(player)

                    address += self.ITEM_OBJECT_OFFSET

            self.players = players
            self.selected_character = selected_character
            return
        self.players = []

    def _read_enemies(self: Self) -> None:
        if self._should_update():
            enemy_targets = self.memory.follow_pointer(
                self.base, [self.current_encounter_base, 0x188, 0x0]
            )
            # item is a list of pointers of size 0x08
            items = self.memory.follow_pointer(
                enemy_targets,
                [0x10, 0x0],
            )
            enemies = []
            if items:
                # Item objects are as follows:
                # Items
                #   - 0x18 - count
                #   - 0x20 - Item[0]
                #   - 0x28 - Item[1]
                count = self.memory.read_int(items + 0x18)
                address = self.ITEM_INDEX_0_ADDRESS

                for _item in range(count):
                    item = self.memory.follow_pointer(items, [address, 0x0])
                    # There will be times when there is an empty pointer in a list of items,
                    # This checks for that case and skips that record.
                    # For example:
                    # Items
                    #    - 0x20 - Item[0] -> Pointer 0xF30d0930
                    #    - 0x20 - Item[0] -> Pointer 0xF30d0930
                    #    - 0x20 - Item[0] -> Pointer 0x00000000
                    #    - 0x20 - Item[0] -> Pointer 0xF30d0930
                    if hex(item) == "0x0" or hex(item) == "0":
                        address += self.ITEM_OBJECT_OFFSET
                        continue

                    current_hp = self.memory.read_int(item + 0x94)
                    casting_data = self.memory.follow_pointer(items, [address, 0x80, 0x120, 0x0])
                    unique_id = self.memory.follow_pointer(
                        items, [address, 0x80, 0xF8, 0xF0, 0x18, 0x0]
                    )
                    enemy_data = self.memory.follow_pointer(items, [address, 0x80, 0x108, 0x0])

                    guid = self.memory.follow_pointer(enemy_data, [0x18, 0x0])
                    max_hp = self.memory.read_int(enemy_data + 0x20)
                    speed = self.memory.read_int(enemy_data + 0x24)
                    physical_attack = self.memory.read_int(enemy_data + 0x2C)
                    physical_defense = self.memory.read_int(enemy_data + 0x28)
                    magic_attack = self.memory.read_int(enemy_data + 0x30)
                    magic_defense = self.memory.read_int(enemy_data + 0x34)
                    enemy_guid = self.memory.read_guid(guid + 0x14)
                    enemy_unique_id = self.memory.read_uuid(unique_id + 0x14)
                    turns_to_action = self.memory.read_short(casting_data + 0x24)
                    total_spell_locks = self.memory.read_short(casting_data + 0x28)

                    spell_locks: list[CombatDamageType] = []

                    # A try is used here due to enemy dropping the spell lock when it starts to
                    # attack. This prevents the edge case and safely returns.
                    try:
                        spell_locks_addr = self.ITEM_INDEX_0_ADDRESS

                        for _spell_lock in range(total_spell_locks):
                            # Spell Locks are Item Objects and are as follows:
                            # Items
                            #   - 0x18 - count
                            #   - 0x20 - Item[0]
                            #   - 0x28 - Item[1]
                            spell_locks_base = self.memory.follow_pointer(
                                casting_data, [0x18, 0x10, spell_locks_addr, 0x0]
                            )

                            if spell_locks_base == 0x0:
                                continue

                            lock = self.memory.read_int(spell_locks_base + 0x40)
                            spell_locks.append(CombatDamageType(lock))

                            spell_locks_addr += self.ITEM_OBJECT_OFFSET
                    except Exception:
                        spell_locks = []

                    enemy = CombatEnemyTarget()
                    enemy.guid = enemy_guid.replace("\x00", "")
                    enemy.name = EnemyName.get(enemy.guid)
                    enemy.current_hp = current_hp
                    enemy.max_hp = max_hp
                    enemy.physical_attack = physical_attack
                    enemy.physical_defense = physical_defense
                    enemy.magic_attack = magic_attack
                    enemy.magic_defense = magic_defense
                    enemy.speed = speed
                    enemy.unique_id = enemy_unique_id
                    enemy.turns_to_action = turns_to_action
                    enemy.total_spell_locks = total_spell_locks
                    enemy.spell_locks = spell_locks

                    enemies.append(enemy)
                    address += self.ITEM_OBJECT_OFFSET

            self.enemies = enemies
            return
        self.enemies = []


_combat_manager = CombatManager()


def combat_manager_handle() -> CombatManager:
    return _combat_manager
