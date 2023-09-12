import contextlib
from enum import Enum, auto

from memory.core import mem_handle
from memory.mappers.enemy_name import EnemyName
from memory.mappers.player_party_character import PlayerPartyCharacter


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


class CombatTutorialState(Enum):
    NONE = auto()
    SecondEncounter = auto()


class CombatSpellLock:
    def __init__(self):
        self.name_loc_id = None
        self.damage_type = CombatDamageType.NONE


class CombatCastingData:
    def __init__(self):
        self.spell_locks = []


class CombatEnemyTarget:
    def __init__(self):
        self.max_hp = None
        self.current_hp = None
        self.physical_attack = None
        self.physical_defense = None
        self.magic_attack = None
        self.magic_defense = None
        self.speed = None
        self.guid = None
        self.name = None
        self.casting_data = CombatCastingData()
        self.turns_to_action = None
        self.unique_id = None
        self.total_spell_locks = 0
        self.spell_locks = []


class CombatPlayer:
    def __init__(self):
        self.max_hp = None
        self.current_hp = None
        self.current_mp = None
        self.physical_attack = None
        self.selected = False
        self.definition_id = None
        self.timed_attack_ready = False
        self.dead = False
        self.character = PlayerPartyCharacter.NONE
        self.enabled = None
        self.mana_charge_count = None


class CombatManager:
    # The null pointer here is a const for the pointer we see provided
    # When the selectors drop from memory for breif periods - Its more of
    # a magic number than anything.
    NULL_POINTER = 0xFFFFFFFF
    ITEM_OBJECT_OFFSET = 0x8
    ITEM_INDEX_0_ADDRESS = 0x20

    def __init__(self):
        self.memory = mem_handle()
        self.base = None
        self.fields_base = None
        self.selector_base = None
        self.enemies = []
        self.players = []
        self.selected_character = PlayerPartyCharacter.NONE
        self.tutorial_state = CombatTutorialState.NONE
        self.current_encounter_base = None
        self.encounter_done = None
        self.small_live_mana = None
        self.big_live_mana = None
        self.battle_command_has_focus = False
        self.battle_command_index = None
        self.skill_command_has_focus = False
        self.skill_command_index = None
        self.selected_attack_target_guid = None
        self.selected_skill_target_guid = None

    def update(self):
        try:
            if self.memory.ready_for_updates:
                if self.base is None or self.fields_base is None:
                    self.encounter_done = True
                    singleton_ptr = self.memory.get_singleton_by_class_name(
                        "CombatManager"
                    )

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
                        self.tutorial_state = CombatTutorialState.NONE
                        return

                    self._read_tutorial_state()
                    self._read_players()
                    self._read_enemies()
                    self._read_battle_commands()
                    if not self.battle_command_has_focus:
                        self._read_skill_commands()
                    self._read_live_mana()

        except Exception as e:  # noqa: F841
            # logger.debug(f"Combat Manager Reloading - {type(e)}")
            self.__init__()

    # Helper function for updating itself and ensuring an internal function doesn't run without
    # the base. This is different than other modules as an attempt to improve performance of the
    # combat manager module.
    def _should_update(self):
        return self.memory.ready_for_updates and self.current_encounter_base is not None

    def _read_tutorial_state(self):
        if self._should_update():
            try:
                tutorial_state_ptr = self.memory.follow_pointer(
                    self.base, [self.current_encounter_base, 0x120, 0x0]
                )

                moongirl_skill_ptr = self.memory.follow_pointer(
                    tutorial_state_ptr, [0xB0, 0x18, 0x0]
                )

                sunboy_skill_ptr = self.memory.follow_pointer(
                    tutorial_state_ptr, [0xA8, 0x18, 0x0]
                )

                moongirl_str = self.memory.read_string(moongirl_skill_ptr + 0x14, 8)
                sunboy_str = self.memory.read_string(sunboy_skill_ptr + 0x14, 8)

                if (
                    moongirl_str.replace("\x00", "") == "Cres"
                    and sunboy_str.replace("\x00", "") == "Sunb"
                ):
                    self.tutorial_state = CombatTutorialState.SecondEncounter
                    return

                self.tutorial_state = CombatTutorialState.NONE
            except Exception:
                self.tutorial_state = CombatTutorialState.NONE

    # Battle Commands are the Main menu of commands (Attack, Skills, Combo, Items)
    def _read_battle_commands(self):
        if self._should_update():
            battle_command_selector = self.memory.follow_pointer(
                self.base, [self.current_encounter_base, 0x138, 0x50, 0x68, 0x0]
            )
            # Checks if we lost access to the selector pointer for a breif period as the UI changes.
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
    # TODO: We need a way to differentiate between the combos and skills menu.
    def _read_skill_commands(self):
        if self._should_update():
            skill_command_selector = self.memory.follow_pointer(
                self.base, [self.current_encounter_base, 0x138, 0x50, 0x78, 0x0]
            )
            # Checks if we lost access to the selector pointer for a breif period as the UI changes.
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
                    # TODO: Does the skill_command_selector apply to the items menu as well?
                    has_focus = self.memory.read_bool(skill_command_selector + 0x3C)
                    selected_item_index = self.memory.read_longlong(
                        skill_command_selector + 0x40
                    )
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
    # TODO: Reverse _read_encounter_done to make it more friendly for use.
    def _read_encounter_done(self):
        if self._should_update():
            current_encounter = self.memory.follow_pointer(
                self.base, [self.current_encounter_base, 0x0]
            )
            if current_encounter:
                done = self.memory.read_bool(current_encounter + 0x162)
                self.encounter_done = done
                return
        self.encounter_done = True

    # Reads the `small mana` on the ground and the `big mana` being charged for Boost
    # The small mana value increases incrementally over a short period of time, so if
    # it is needing to be used, it must be done carefully.
    # Small live mana has a max value of 15.
    # As boost is charged, 5 small live mana is consumed per level, the value is immediately
    # deducted, and the big_live_mana field increases by 1. Reversing a big live mana immediately
    # returns 5 back to the small_live_mana field.
    # When a boost is consumed, the player recieved the total big live mana as a mana_charge.
    def _read_live_mana(self):
        if self._should_update():
            small_live_mana = self.memory.follow_pointer(
                self.base, [self.current_encounter_base, 0x78, 0x20, 0x0]
            )
            if small_live_mana == self.NULL_POINTER:
                self.small_live_mana = 0
                self.big_live_mana = 0
                return
            big_live_mana = self.memory.follow_pointer(
                self.base, [self.current_encounter_base, 0x78, 0x28, 0x0]
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
    def _read_players(self):
        if self._should_update():
            selected_character = PlayerPartyCharacter.NONE
            try:
                player_panels_list = self.memory.follow_pointer(
                    self.base, [self.current_encounter_base, 0x120, 0x98, 0x40, 0x0]
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
                # Item objects are as follows:
                # Items
                #   - 0x18 - count
                #   - 0x20 - Item[0]
                #   - 0x28 - Item[1]
                count = self.memory.read_int(items + 0x18)
                address = self.ITEM_INDEX_0_ADDRESS

                for _item in range(count):
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

                    # TODO: Switch "0x0" to another NULL_POINTER type of 0x00000000
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
                        timed_attack_ptr = self.memory.follow_pointer(
                            dead_ptr, [0x160, 0x0]
                        )
                        timed_attack_value = self.memory.read_bool(
                            timed_attack_ptr + 0x3A
                        )
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

                    live_mana_handler = self.memory.follow_pointer(
                        item, [0x68, 0x38, 0x148, 0x0]
                    )
                    mana_charge_count = self.memory.read_int(live_mana_handler + 0x58)
                    target_unique_id_base = None
                    # A try is used here, because this pointer tends to fall out in quick
                    # play. This just returns safely and attempts again.

                    selected_attack_target_guid = ""
                    selected_skill_target_guid = ""
                    if selected:
                        with contextlib.suppress(Exception):
                            target_unique_id_base = self.memory.follow_pointer(
                                item,
                                [
                                    0x68,
                                    0x38,
                                    0x190,
                                    0x30,
                                    0xA8,
                                    0x80,
                                    0x40,
                                    0xA8,
                                    0x80,
                                    0xF8,
                                    0xF0,
                                    0x18,
                                    0x0,
                                ],
                            )

                        # This check was added due to the pointer not falling off in time, referencing
                        # an enemy that just died
                        try:
                            selected_attack_target_guid = self.memory.read_uuid(
                                target_unique_id_base + 0x14
                            )
                        except Exception:
                            selected_attack_target_guid = ""

                        # Separate Skill section lookup
                        # This is currently not correct as it considers the skill target, but gets a
                        # bit washed out if there are AOE targets.
                        # TODO:
                        with contextlib.suppress(Exception):
                            target_unique_id_base = self.memory.follow_pointer(
                                item,
                                [
                                    0x68,
                                    0x38,
                                    0x190,
                                    0x28,
                                    0x10,
                                    0x20,
                                    0xA8,
                                    0x80,
                                    0x40,
                                    0xA8,
                                    0x80,
                                    0xF8,
                                    0xF0,
                                    0x18,
                                    0x0,
                                ],
                            )

                        # This check was added due to the pointer not falling off in time, referencing
                        # an enemy that just died
                        try:
                            selected_skill_target_guid = self.memory.read_uuid(
                                target_unique_id_base + 0x14
                            )
                        except Exception:
                            selected_skill_target_guid = ""

                    mp_text_field = self.memory.follow_pointer(item, [0x30, 0x0])

                    current_mp = self.memory.read_int(mp_text_field + 0x58)

                    # if the current player is selected, set it to the main combat manager state
                    # this will help us prevent scanning lists later on
                    if selected:
                        selected_character = character
                        self.selected_attack_target_guid = selected_attack_target_guid
                        self.selected_skill_target_guid = selected_skill_target_guid

                    player = CombatPlayer()

                    # TODO: hardcode these for now - we need to extract these players into
                    # something more global and only update them as required.
                    match character:
                        case PlayerPartyCharacter.Zale:
                            player.physical_attack = 20
                        case PlayerPartyCharacter.Valere:
                            player.physical_attack = 22
                        case PlayerPartyCharacter.Garl:
                            player.physical_attack = 26
                        case _:
                            player.physical_attack = 1

                    player.current_hp = current_hp
                    player.current_mp = current_mp
                    player.definition_id = definition_id
                    player.character = character
                    player.selected = selected
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

    def _read_enemies(self):
        if self._should_update():
            enemy_targets = self.memory.follow_pointer(
                self.base, [self.current_encounter_base, 0x180, 0x0]
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
                    # TODO: Switch "0x0" to another NULL_POINTER type of 0x00000000
                    if hex(item) == "0x0":
                        address += self.ITEM_OBJECT_OFFSET
                        continue

                    current_hp = self.memory.read_int(item + 0x94)
                    casting_data = self.memory.follow_pointer(
                        items, [address, 0x80, 0x120, 0x0]
                    )
                    unique_id = self.memory.follow_pointer(
                        items, [address, 0x80, 0xF8, 0xF0, 0x18, 0x0]
                    )
                    enemy_data = self.memory.follow_pointer(
                        items, [address, 0x80, 0x108, 0x0]
                    )

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

                    spell_locks = []

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
                    enemy.name = EnemyName().get(enemy.guid)
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
