"""Base class for items that can be tracked by the `InventoryManager`."""

from enum import Enum, auto
from typing import Self

# TODO(orkaboy): Create item base class (What fields are relevant?)


class ItemType(Enum):
    """Menu that the item belongs to."""

    VALUABLE = auto()
    WEAPON = auto()
    ARMOR = auto()
    FOOD = auto()


class Item:
    """An Item that can be tracked, picked up, bought, sold and equipped."""

    def __init__(
        self: Self, guid: str, item_type: ItemType, name: str, cost: int = 0, sell_value: int = 0
    ) -> None:
        self.guid = guid
        self.item_type = item_type
        self.name = name
        self.cost = cost
        self.sell_value = sell_value

    def __hash__(self: Self) -> int:
        return hash(self.guid)

    def __repr__(self: Self) -> str:
        return f"{self.name}({self.item_type.name})"
