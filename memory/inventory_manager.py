import logging
from typing import Self

from engine.inventory.item import Item, ItemType
from memory.core import mem_handle
from memory.mappers.items import ItemMapper

logger = logging.getLogger(__name__)


class ItemReference:
    """Item, guid and quantity (one entry in the memory inventory list)."""

    def __init__(self: Self, guid: str, quantity: int, item: Item = None) -> None:
        """Initialize a new ItemReference object."""
        self.guid = guid
        self.quantity = quantity
        self.item = item

    def __repr__(self: Self) -> str:
        return f"ItemRef[{self.guid} ({self.item}), {self.quantity}]"

    def __lt__(self: Self, other: Self) -> bool:
        if self.item is None or other.item is None:
            return False
        return self.item.order_prio < other.item.order_prio


class InventoryManager:
    """Memory manager that handles items."""

    INVENTORY_ITEM_OFFSET = 0x18
    UPDATE_FREQUENCY = 0.0

    def __init__(self: Self) -> None:
        """Initialize a new InventoryManager object."""
        self.memory = mem_handle()
        self.base = None
        self.items: list[ItemReference] = []
        # Dictionary of Items and amounts carried
        self.items_mapped: list[ItemReference] = []

    def get_items_by_type(self: Self, item_type: ItemType) -> list[ItemReference]:
        """Return a list of items held, based on item type."""
        ret: list[ItemReference] = []
        for item_ref in self.items_mapped:
            item = item_ref.item
            if item is not None:
                if item.item_type == item_type:
                    ret.append(item_ref)
            elif item_type == ItemType.UNKNOWN:
                ret.append(item_ref)
        if item_type != ItemType.UNKNOWN:
            return sorted(ret, reverse=True)
        return ret

    def update(self: Self) -> None:
        if self.memory.ready_for_updates:
            try:
                if self.base is None:
                    singleton_ptr = self.memory.get_singleton_by_class_name("InventoryManager")
                    if singleton_ptr is None:
                        return

                    self.base = self.memory.get_class_base(singleton_ptr)
                    if self.base == 0x0:
                        return
                else:
                    self._read_items()
                    self.items_mapped = [
                        ItemReference(
                            guid=item_ref.guid,
                            quantity=item_ref.quantity,
                            item=ItemMapper.items.get(item_ref.guid),
                        )
                        for item_ref in self.items
                    ]
            except Exception as _e:
                logger.debug(f"InventoryManager Reloading {type(_e)}")
                self.__init__()

    def _read_items(self: Self) -> None:
        items: list[ItemReference] = []
        address = 0x0
        if self.memory.ready_for_updates:
            try:
                # ownedInventoryItems -> dictionary -> _entries + 0x20 for first entry
                count_ptr = self.memory.follow_pointer(self.base, [0x70, 0x20, 0x20])
                count = self.memory.read_int(count_ptr)
                for _i in range(count):
                    ptr = self.memory.follow_pointer(self.base, [0x70, 0x20, 0x18, 0x20 + address])
                    if ptr:
                        guid_ptr = self.memory.follow_pointer(ptr, [0x8, 0x0])
                        if guid_ptr == 0x0:
                            break
                        guid = self.memory.read_guid(guid_ptr + 0x14).replace("\x00", "")
                        quantity = self.memory.read_int(ptr + 0x10)
                        items.append(ItemReference(guid, quantity))
                        address += self.INVENTORY_ITEM_OFFSET
                    else:
                        break
            except Exception:
                self.items = []
                return
        self.items = items


_inventory_manager = InventoryManager()


def inventory_manager_handle() -> InventoryManager:
    """Return a handle to the inventory manager."""
    return _inventory_manager
