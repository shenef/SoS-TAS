import logging
from typing import Self

from memory.core import mem_handle

logger = logging.getLogger(__name__)


class ItemReference:
    def __init__(self: Self, guid: str, quantity: int) -> None:
        self.guid = guid
        self.quantity = quantity


class InventoryManagerMem:
    INVENTORY_ITEM_OFFSET = 0x18

    def __init__(self: Self) -> None:
        """Initialize a new InventoryManagerMem object."""
        self.memory = mem_handle()
        self.base = None
        self.items: list[ItemReference] = []

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
                    pass
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
                        guid = self.memory.read_guid(guid_ptr + 0x14)
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
