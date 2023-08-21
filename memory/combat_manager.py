from enum import Enum

from memory.core import mem_handle


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
        self.casting_data = CombatCastingData()
        self.turns_to_action = None
        self.unique_id = None
        self.total_spell_locks = 0
        self.spell_locks = []


class CombatPlayer:
    def __init__(self, params=dict):
        self.max_hp = None
        self.current_hp = None
        self.current_mp = None
        self.selected = False
        self.definition_id = None
        self.enabled = None
        self.mana_charge_count = None


class CombatManager:
    def __init__(self):
        self.memory = mem_handle()
        self.base = None
        self.fields_base = None
        self.selector_base = None
        self.enemies = []
        self.players = []
        self.current_encounter_base = None
        self.encounter_done = True
        self.small_live_mana = None
        self.big_live_mana = None
        self.battle_command_has_focus = False
        self.battle_command_index = None
        self.skill_command_has_focus = False
        self.skill_command_index = None
        self.selected_target_guid = None

    def update(self):
        # try:
        self.memory.update()

        if self.memory.ready_for_updates():
            if self.base is None or self.fields_base is None:
                singleton_ptr = self.memory.get_singleton_by_class_name("CombatManager")
                self.base = self.memory.get_class_base(singleton_ptr)
                self.fields_base = self.memory.get_class_fields_base(singleton_ptr)
                self.current_encounter_base = self.memory.get_field(
                    self.fields_base, "currentEncounter"
                )

            # Update fields
            self._read_encounter_done()
            self._read_live_mana()
            self._read_players()
            self._read_enemies()
            self._read_battle_commands()
            self._read_skill_commands()
        else:
            self.__init__()

    # except Exception:
    #     return

    # Battle Commands are the Main menu of commands (Attack, Skills, Combo, Items)
    def _read_battle_commands(self):
        if self.memory.ready_for_updates():
            battle_command_selector = self.memory.follow_pointer(
                self.base, [self.current_encounter_base, 0xF8, 0x50, 0x60, 0x0]
            )
            if battle_command_selector:
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
        self.battle_command_has_focus = False
        self.battle_command_index = None

    # Skill Commands are the menu of the "skills" command (ie Healing Light, Sunball)
    def _read_skill_commands(self):
        if self.memory.ready_for_updates():
            skill_command_selector = self.memory.follow_pointer(
                self.base, [self.current_encounter_base, 0xF8, 0x50, 0x58, 0x0]
            )
            if skill_command_selector:
                has_focus = self.memory.read_bool(skill_command_selector + 0x3C)
                selected_item_index = self.memory.read_longlong(
                    skill_command_selector + 0x40
                )
                self.skill_command_has_focus = has_focus
                self.skill_command_index = selected_item_index
                if has_focus:
                    selected_item_index = self.memory.read_longlong(
                        skill_command_selector + 0x40
                    )
                    self.skill_command_index = selected_item_index
                else:
                    self.skill_command_index = None
                return
        self.skill_command_has_focus = False
        self.skill_command_index = None

    def _read_encounter_done(self):
        if self.memory.ready_for_updates():
            current_encounter = self.memory.follow_pointer(
                self.base, [self.current_encounter_base, 0x0]
            )
            if current_encounter:
                done = self.memory.read_bool(current_encounter + 0x110)
                self.encounter_done = done
                return
        self.counter_done = True

    def _read_live_mana(self):
        if self.memory.ready_for_updates():
            small_live_mana = self.memory.follow_pointer(
                self.base, [self.current_encounter_base, 0x60, 0x20, 0x0]
            )
            big_live_mana = self.memory.follow_pointer(
                self.base, [self.current_encounter_base, 0x60, 0x28, 0x0]
            )
            if small_live_mana and big_live_mana:
                self.small_live_mana = self.memory.read_int(small_live_mana + 0x18)
                self.big_live_mana = self.memory.read_int(big_live_mana + 0x18)
                return
        self.size = 0

    def _read_players(self):
        if self.memory.ready_for_updates():
            player_panels_list = self.memory.follow_pointer(
                self.base, [self.current_encounter_base, 0xE0, 0x80, 0x40, 0x0]
            )
            # item is a list of pointers of size 0x08
            items = self.memory.follow_pointer(
                player_panels_list,
                [0x10, 0x0],
            )
            players = []
            if items:
                count = self.memory.read_int(items + 0x18)
                address = 0x20
                for _x in range(count):
                    item = self.memory.follow_pointer(items, [address, 0x0])
                    if hex(item) != "0x0":
                        definition_id = self.memory.read_longlong(item + 0x70)
                        selected = self.memory.read_bool(item + 0x78)

                        hp_text_field = self.memory.follow_pointer(item, [0x28, 0x0])
                        current_hp = self.memory.read_int(hp_text_field + 0x54)

                        portrait = self.memory.follow_pointer(item, [0x68, 0x0])
                        enabled = self.memory.read_bool(portrait + 0x20)
                        live_mana_handler = self.memory.follow_pointer(
                            item, [0x68, 0x28, 0x118, 0x0]
                        )
                        mana_charge_count = self.memory.read_int(
                            live_mana_handler + 0x58
                        )

                        target_unique_id_base = self.memory.follow_pointer(
                            item,
                            [
                                0x68,
                                0x28,
                                0x150,
                                0x30,
                                0x90,
                                0x80,
                                0x40,
                                0x80,
                                0x58,
                                0xF0,
                                0xD8,
                                0x18,
                                0x0,
                            ],
                        )

                        selected_target_guid = self.memory.read_guid(
                            target_unique_id_base + 0x14
                        )

                        mp_text_field = self.memory.follow_pointer(item, [0x30, 0x0])
                        current_mp = self.memory.read_int(mp_text_field + 0x54)
                        player = CombatPlayer()
                        player.current_hp = current_hp
                        player.current_mp = current_mp
                        player.definition_id = definition_id
                        player.selected = selected
                        player.enabled = enabled
                        player.mana_charge_count = mana_charge_count
                        players.append(player)
                        self.selected_target_guid = selected_target_guid

                    address += 0x8

            self.players = players
            return
        self.players = []

    def _read_enemies(self):
        if self.memory.ready_for_updates():
            enemy_targets = self.memory.follow_pointer(
                self.base, [self.current_encounter_base, 0x130, 0x0]
            )
            # item is a list of pointers of size 0x08
            items = self.memory.follow_pointer(
                enemy_targets,
                [0x10, 0x0],
            )
            enemies = []
            if items:
                count = self.memory.read_int(items + 0x18)
                address = 0x20

                for _x in range(count):
                    item = self.memory.follow_pointer(items, [address, 0x0])
                    if hex(item) != "0x0":
                        current_hp = self.memory.read_int(item + 0x6C)
                        casting_data = self.memory.follow_pointer(
                            items, [address, 0x58, 0x118, 0x0]
                        )
                        unique_id = self.memory.follow_pointer(
                            items, [address, 0x58, 0xF0, 0xD8, 0x18, 0x0]
                        )
                        enemy_unique_id = self.memory.read_guid(unique_id + 0x14)
                        turns_to_action = self.memory.read_short(casting_data + 0x24)
                        total_spell_locks = self.memory.read_short(casting_data + 0x28)

                        spell_locks = []
                        spell_locks_addr = 0x20

                        for _s in range(total_spell_locks):
                            spell_locks_base = self.memory.follow_pointer(
                                casting_data, [0x18, 0x10, spell_locks_addr, 0x0]
                            )
                            lock = self.memory.read_int(spell_locks_base + 0x38)
                            spell_locks.append(CombatDamageType(lock))
                            spell_locks_addr += 0x8

                        enemy = CombatEnemyTarget()
                        enemy.current_hp = current_hp
                        enemy.unique_id = enemy_unique_id
                        enemy.turns_to_action = turns_to_action
                        enemy.total_spell_locks = total_spell_locks
                        enemy.spell_locks = spell_locks

                        enemies.append(enemy)
                    address += 0x8

            self.enemies = enemies
            return
        self.enemies = []
