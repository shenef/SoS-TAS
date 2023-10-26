import logging
from typing import Self

from engine.inventory.item import Item, ItemType
from memory.core import mem_handle
from memory.mappers.items import ItemMapper

logger = logging.getLogger(__name__)


class ItemReference:
    def __init__(self: Self, guid: str, quantity: int) -> None:
        self.guid = guid
        self.quantity = quantity

    def __repr__(self: Self) -> str:
        return f"ItemRef[{self.guid}, {self.quantity}]"


class InventoryManagerMem:
    INVENTORY_ITEM_OFFSET = 0x18
    UPDATE_FREQUENCY = 0.0

    def __init__(self: Self) -> None:
        """Initialize a new InventoryManagerMem object."""
        self.memory = mem_handle()
        self.base = None
        self.items: list[ItemReference] = []
        # Dictionary of Items and amounts carried
        self.items_mapped: dict[Item | str, int] = {}

    def get_items_by_type(self: Self, item_type: ItemType) -> list[tuple[Item | str, int]]:
        """Return a list of items held, based on item type."""
        ret: list[tuple[Item | str, int]] = []
        for item, amount in self.items_mapped.items():
            if isinstance(item, Item):
                if item.item_type == item_type:
                    ret.append((item, amount))
            elif item_type == ItemType.UNKNOWN:
                ret.append((item, amount))
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
                    pass

                else:
                    self._read_items()
                    self.items_mapped = {
                        ItemMapper.items.get(item_ref.guid, item_ref.guid): item_ref.quantity
                        for item_ref in self.items
                    }
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


_inventory_manager_mem = InventoryManagerMem()


def inventory_manager_mem_handle() -> InventoryManagerMem:
    return _inventory_manager_mem
