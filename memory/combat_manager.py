from enum import Enum

from memory.core import mem_handle


class CombatDamageType(Enum):
    NONE = 0
    _unknown = 1
    Sword = 2
    _unknown2 = 3
    _unknown3 = 4
    _unknown4 = 5
    _unknown5 = 6
    _unknown6 = 7
    Moon = 8


class CombatSpellLock:
    def __init__(self):
        self.name_loc_id = None
        self.damage_type = CombatDamageType.NONE


class CombatCastingData:
    def __init__(self):
        self.spell_locks = []


class CombatEnemy:
    def __init__(self, params=dict):
        self.max_hp = None
        self.dead = params["dead"]
        self.current_hp = params["current_hp"]
        self.speed = None
        self.base_physical_defense = None
        self.base_physical_attack = None
        self.base_magic_attack = None
        self.casting_data = CombatCastingData()


class CombatPlayer:
    def __init__(self, params=dict):
        self.max_hp = None
        self.current_hp = params["current_hp"]
        self.current_mp = params["current_mp"]
        self.selected = params["selected"]
        self.definition_id = params["definition_id"]
        self.enabled = params["enabled"]


class CombatManager:
    def __init__(self):
        self.memory = mem_handle()
        self.base = None
        self.fields_base = None
        self.enemies = []
        self.players = []
        self.current_encounter_base = None

    def update(self):
        try:
            self.memory.update()

            if self.memory.ready_for_updates():
                if self.base is None or self.fields_base is None:
                    singleton_ptr = self.memory.get_singleton_by_class_name(
                        "CombatManager"
                    )
                    self.base = self.memory.get_class_base(singleton_ptr)
                    self.fields_base = self.memory.get_class_fields_base(singleton_ptr)
                    self.current_encounter_base = self.memory.get_field(
                        self.fields_base, "currentEncounter"
                    )

                # Update fields
                self._read_players()
                self._read_enemies()
            else:
                self.__init__()

        except Exception:
            return

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

                        mp_text_field = self.memory.follow_pointer(item, [0x30, 0x0])
                        current_mp = self.memory.read_int(mp_text_field + 0x54)
                        players.append(
                            {
                                "current_hp": current_hp,
                                "current_mp": current_mp,
                                "definition_id": definition_id,
                                "selected": selected,
                                "enabled": enabled,
                            }
                        )
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
                        hp = self.memory.read_int(item + 0x6C)
                        enemies.append({"current_hp": hp})
                    address += 0x8

            self.enemies = enemies
            return
        self.enemies = []
