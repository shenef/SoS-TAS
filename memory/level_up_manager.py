from enum import Enum
from typing import Self

from memory.core import mem_handle
from memory.mappers.player_party_character import PlayerPartyCharacter


class LevelUpUpgradeType(Enum):
    NONE = -1
    HitPoint = 0
    SkillPoint = 1
    # ComboPoint  = 2
    PhysicalAttack = 3
    PhysicalDefense = 4
    MagicAttack = 5
    MagicDefense = 6


class LevelUpUpgrade:
    def __init__(self: Self, upgrade_type: LevelUpUpgradeType, active: bool) -> None:
        self.upgrade_type = upgrade_type
        self.active = active


# This is actually called LevelUpSceneController, but its a manager
# class, so we'll call it that here.
class LevelUpManager:
    NULL_POINTER = 0xFFFFFFFF
    ZERO_NULL_POINTER = 0x0
    ITEM_OBJECT_OFFSET = 0x8
    ITEM_INDEX_0_ADDRESS = 0x20

    def __init__(self: Self) -> None:
        self.memory = mem_handle()
        self.base = None
        self.fields_base = None
        self.level_up_screen_active = False
        self.current_upgrades = []
        self.active_index = None
        self.current_character = PlayerPartyCharacter.NONE

    def update(self: Self) -> None:
        if self.memory.ready_for_updates:
            try:
                if self.base is None or self.fields_base is None:
                    singleton_ptr = self.memory.get_singleton_by_class_name(
                        "LevelUpSceneController"
                    )
                    if singleton_ptr is None:
                        return
                    self.base = self.memory.get_class_base(singleton_ptr)
                    if self.base == 0x0:
                        return
                    self.fields_base = self.memory.get_class_fields_base(singleton_ptr)

                else:
                    self._read_level_up_screen_active()
                    if self._read_level_up_screen_active:
                        self._read_current_level_up_upgrades()
                        self._read_current_character()
            except Exception as _e:  # noqa: F841
                # logger.debug(f"Level Up Manager Reloading {type(_e)}")
                self.__init__()

    def _read_level_up_screen_active(self: Self) -> None:
        ptr = self.memory.follow_pointer(self.base, [0x20, 0x0])
        if ptr == 0x0:
            self.level_up_screen_active = False
        else:
            self.level_up_screen_active = True

    def _read_current_character(self: Self) -> None:
        try:
            definition_id_ptr = self.memory.follow_pointer(
                self.base, [0x88, 0x88, 0x50, 0x58, 0x40, 0x0]
            )
            definition_id = self.memory.read_string(definition_id_ptr + 0x14, 8)
            # LevelUpSceneController -> currentCharacter -> stateMachine -> currentState...
            # -> player -> characterDefinitionId
            definition_id_ptr = self.memory.follow_pointer(self.base, [0x88, 0x0])
            character = PlayerPartyCharacter.parse_definition_id(definition_id)
            self.current_character = character
        except Exception:
            self.current_character = PlayerPartyCharacter.NONE

    def _read_current_level_up_upgrades(self: Self) -> None:
        # LevelUpSceneController -> currentLevelUpUpgrades -> _items -> item[x]
        self.memory.follow_pointer(self.base, [0xB0, 0x0])
        try:
            items = self.memory.follow_pointer(self.base, [0xB0, 0x10, 0x0])
        except Exception:
            self.current_level_up_upgrades = []
            return

        if items in {self.NULL_POINTER, self.ZERO_NULL_POINTER}:
            self.current_level_up_upgrades = []
            return
        # Item is an array of pointers of size 0x08
        upgrades = []
        if items:
            # Item objects are as follows:
            # Items
            #   - 0x18 - count
            #   - 0x20 - Item[0]
            #   - 0x28 - Item[1]
            count = self.memory.read_int(items + 0x18)
            address = self.ITEM_INDEX_0_ADDRESS
            for _item in range(count):
                item_ptr = self.memory.follow_pointer(items, [address, 0x0])
                upgrade_type = LevelUpUpgradeType(self.memory.read_int(item_ptr + 0x38))
                active_ptr = self.memory.follow_pointer(item_ptr, [0x50, 0x0])
                active = not self.memory.read_bool(active_ptr + 0xA0)
                upgrades.append(LevelUpUpgrade(upgrade_type, active))
                address += self.ITEM_OBJECT_OFFSET
        self.current_level_up_upgrades = upgrades
        pass


_level_up_manager_mem = LevelUpManager()


def level_up_manager_handle() -> LevelUpManager:
    return _level_up_manager_mem
