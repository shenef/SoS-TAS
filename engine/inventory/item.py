"""Base class for items that can be tracked by the `InventoryManager`."""

from enum import Enum, auto
from typing import Self

from memory.mappers.player_party_character import PlayerPartyCharacter

# TODO(orkaboy): Create item base class (What fields are relevant?)


class ItemType(Enum):
    """Menu that the item belongs to."""

    VALUABLE = auto()
    WEAPON = auto()
    ARMOR = auto()
    TRINKET = auto()
    GROUPTRINKET = auto()
    FOOD = auto()
    KEY = auto()
    INGREDIENT = auto()
    RECIPE = auto()
    UNKNOWN = auto()


class Item:
    """An Item that can be tracked, picked up, bought and sold."""

    def __init__(
        self: Self,
        guid: str,
        item_type: ItemType,
        name: str,
        order_prio: int,
        cost: int = 0,
        sell_value: int = 0,
    ) -> None:
        self.guid = guid
        self.item_type = item_type
        self.name = name
        self.order_prio = order_prio
        self.cost = cost
        self.sell_value = sell_value

    def __eq__(self: Self, other: Self) -> bool:
        return other and self.guid == other.guid

    def __hash__(self: Self) -> int:
        return hash(self.guid)

    def __repr__(self: Self) -> str:
        return f"{self.name} ({self.item_type.name})"


class EquippableItem(Item):
    """An Item that can be equipped."""

    def __init__(
        self: Self,
        guid: str,
        item_type: ItemType,
        name: str,
        order_prio: int,
        equippable_by: list[PlayerPartyCharacter] = None,
        cost: int = 0,
        sell_value: int = 0,
        phy_def: int = 0,
        mag_def: int = 0,
        phy_atk: int = 0,
        mag_atk: int = 0,
    ) -> None:
        super().__init__(
            guid=guid,
            item_type=item_type,
            name=name,
            order_prio=order_prio,
            cost=cost,
            sell_value=sell_value,
        )
        self.phy_def = phy_def
        self.phy_atk = phy_atk
        self.mag_def = mag_def
        self.mag_atk = mag_atk
        # If set to None, all characters can equip it
        self.equippable_by = equippable_by


class FoodItem(Item):
    """An Item that can be eaten."""

    def __init__(
        self: Self,
        guid: str,
        name: str,
        order_prio: int,
        cost: int = 0,
        sell_value: int = 0,
        is_aoe: bool = False,
        hp_to_restore: int = 0,
        mp_to_restore: int = 0,
        # Restore mode
        hp_use_percent: bool = False,
        mp_use_percent: bool = False,
        # 0.0-1.0
        hp_percent_to_restore: float = 0.0,
        mp_percent_to_restore: float = 0.0,
    ) -> None:
        super().__init__(
            guid=guid,
            item_type=ItemType.FOOD,
            name=name,
            order_prio=order_prio,
            cost=cost,
            sell_value=sell_value,
        )
        self.is_aoe = is_aoe
        self.hp_to_restore = hp_to_restore
        self.mp_to_restore = mp_to_restore
        self.hp_use_percent = hp_use_percent
        self.mp_use_percent = mp_use_percent
        self.hp_percent_to_restore = hp_percent_to_restore
        self.mp_percent_to_restore = mp_percent_to_restore
