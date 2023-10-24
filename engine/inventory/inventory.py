"""Inventory management related code."""

from typing import Self

from engine.inventory.item import Item, ItemType
from memory import inventory_manager_mem_handle
from memory.mappers.items import ItemMapper

inventory_manager_mem = inventory_manager_mem_handle()


# TODO(orkaboy): Add validation when removing/buying/selling stuff
# TODO(orkaboy): Grab some of these things from memory
class InventoryManager:
    """A class that manages items held by the party."""

    def __init__(self: Self) -> None:
        # Dictionary of Items and amounts carried
        self.items: dict[Item | str, int] = {}
        self.money: int = 0

    def reset(self: Self) -> None:
        """Reset inventory state."""
        self.items.clear()
        self.money = 0

    def add_item(self: Self, item: Item, amount: int = 1) -> None:
        """Add an item to the inventory."""
        old_amount = self.items.get(item, 0)
        self.items[item] = old_amount + amount

    def remove_item(self: Self, item: Item, amount: int = 1) -> None:
        """Remove an item from the inventory."""
        old_amount = self.items.get(item, 0)
        new_amount = old_amount - amount
        if new_amount <= 0:
            del self.items[item]
        else:
            self.items[item] = new_amount

    def buy_item(self: Self, item: Item, amount: int = 1) -> None:
        """Add a number of items and remove their cost from the wallet."""
        self.money -= amount * item.cost
        self.add_item(item, amount)

    def sell_item(self: Self, item: Item, amount: int = 1) -> None:
        """Sells a number of items and add their value to the wallet."""
        self.money += amount * item.sell_value
        self.remove_item(item, amount)

    def add_money(self: Self, amount: int) -> None:
        """Increase money held in wallet."""
        self.money += amount

    # TODO(orkaboy): Move elsewhere; code above is not needed anymore
    def update(self: Self) -> None:
        self.items = {
            ItemMapper.items.get(item_ref.guid, item_ref.guid): item_ref.quantity
            for item_ref in inventory_manager_mem.items
        }

    def get_items_by_type(self: Self, item_type: ItemType) -> list[tuple[Item | str, int]]:
        """Return a list of items held, based on item type."""
        ret: list[tuple[Item | str, int]] = []
        for item, amount in self.items.items():
            if isinstance(item, Item):
                if item.item_type == item_type:
                    ret.append((item, amount))
            elif item_type == ItemType.UNKNOWN:
                ret.append((item, amount))
        return ret


_inventory_manager = InventoryManager()


def get_inventory_manager() -> InventoryManager:
    """Return a handle to the inventory manager."""
    return _inventory_manager
