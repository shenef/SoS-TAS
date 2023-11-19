from typing import Self

from memory.core import mem_handle


# ShopManager is the internal naming for the class that handles shops in the game.
# The class has a currentShop -> itemsToSell definition that we will use to traverse
# items in the shop.
class ShopManager:
    NULL_POINTER = 0xFFFFFFFF
    ZERO_NULL_POINTER = 0x0
    ITEM_OBJECT_OFFSET = 0x8
    ITEM_INDEX_0_ADDRESS = 0x20

    def __init__(self: Self) -> None:
        """Initialize a new ShopManager object."""
        self.memory = mem_handle()
        self.base = None
        self.shop_items: list[str] = []

    def update(self: Self) -> None:
        if self.memory.ready_for_updates:
            try:
                if self.base is None:
                    singleton_ptr = self.memory.get_singleton_by_class_name("ShopManager")
                    if singleton_ptr is None:
                        return
                    self.base = self.memory.get_class_base(singleton_ptr)
                    if self.base == 0x0:
                        return

                else:
                    self._get_shop_items()
            except Exception as _e:
                # logger.debug(f"ShopManager Reloading {type(_e)}")
                self.__init__()

    def _get_shop_items(self: Self) -> None:
        shop_items = []
        try:
            items_to_sell = self.memory.follow_pointer(self.base, [0x20, 0x30, 0x10, 0x0])
        except Exception:
            self.shop_items = []
            return
        if items_to_sell:
            # Item objects are as follows:
            # Items
            #   - 0x18 - count
            #   - 0x20 - Item[0]
            #   - 0x28 - Item[1]
            count = self.memory.read_int(items_to_sell + 0x18)
            address = self.ITEM_INDEX_0_ADDRESS
            for _item in range(count):
                item_ptr = self.memory.follow_pointer(items_to_sell, [address, 0x0])
                guid = self.memory.read_guid(item_ptr + 0x14)
                shop_items.append(guid.replace("\x00", ""))
                address += self.ITEM_OBJECT_OFFSET
        self.shop_items = shop_items


_shop_manager_mem = ShopManager()


def shop_manager_handle() -> ShopManager:
    return _shop_manager_mem
