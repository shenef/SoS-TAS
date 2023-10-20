from typing import Self

from memory.core import mem_handle


class InventoryManagerMem:
    def __init__(self: Self) -> None:
        """Initialize a new InventoryManagerMem object."""
        self.memory = mem_handle()
        self.base = None
        # TODO(orkaboy): Declare data fields

    def update(self: Self) -> None:
        if self.memory.ready_for_updates:
            try:
                if self.base is None:
                    # singleton_ptr = self.memory.get_singleton_by_class_name("BoatManager")
                    # if singleton_ptr is None:
                    #     return

                    # self.base = self.memory.get_class_base(singleton_ptr)
                    # if self.base == 0x0:
                    #     return
                    pass

                else:
                    # TODO(orkaboy): Update fields
                    # self._read_position()
                    pass
            except Exception as _e:
                # logger.debug(f"BoatManager Reloading {type(_e)}")
                self.__init__()

    # def _read_position(self: Self) -> None:
    #     if self.memory.ready_for_updates:
    #         # (BoatInstance) k__BackingField -> boatController -> currentTargetPosition
    #         ptr = self.memory.follow_pointer(self.base, [0x40, 0x40, 0x84])
    #         if ptr:
    #             x = self.memory.read_float(ptr + 0x0)
    #             y = self.memory.read_float(ptr + 0x4)
    #             z = self.memory.read_float(ptr + 0x8)

    #             self.position = Vec3(x, y, z)
    #             return

    #     self.position = Vec3(None, None, None)


_inventory_manager_mem = InventoryManagerMem()


def inventory_manager_handle() -> InventoryManagerMem:
    return _inventory_manager_mem
