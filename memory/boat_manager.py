from engine.mathlib import Vec3
from memory.core import mem_handle


class BoatManager:
    def __init__(self):
        self.memory = mem_handle()
        self.base = None
        self.position = Vec3(None, None, None)
        self.rotation_x = None
        self.rotation_y = None

    def update(self):
        if self.memory.ready_for_updates:
            try:
                if self.base is None:
                    singleton_ptr = self.memory.get_singleton_by_class_name(
                        "BoatManager"
                    )
                    if singleton_ptr is None:
                        return

                    self.base = self.memory.get_class_base(singleton_ptr)

                    if self.base == 0x0:
                        return

                else:
                    # Update fields
                    self._read_position()
                    self._read_rotation()
            except Exception as _e:
                # logger.debug(f"BoatManager Reloading {type(_e)}")
                self.__init__()

    def _read_position(self):
        if self.memory.ready_for_updates:
            # (BoatInstance) k__BackingField -> boatController -> currentTargetPosition
            ptr = self.memory.follow_pointer(self.base, [0x40, 0x40, 0x84])
            if ptr:
                x = self.memory.read_float(ptr + 0x0)
                y = self.memory.read_float(ptr + 0x4)
                z = self.memory.read_float(ptr + 0x8)

                self.position = Vec3(x, y, z)
                return

        self.position = Vec3(None, None, None)

    def _read_rotation(self):
        if self.memory.ready_for_updates:
            # (BoatInstance) k__BackingField -> boatSnapRotation -> pitchRollLocalRotation
            ptr = self.memory.follow_pointer(self.base, [0x40, 0x60, 0x0])
            if ptr:
                # not sure what these are called, but the values are here.
                x = self.memory.read_float(ptr + 0x48)
                y = self.memory.read_float(ptr + 0x50)

                self.rotation_x = x
                self.rotation_y = y
                return

        self.rotation_x = None
        self.rotation_y = None


_boat_manager_mem = BoatManager()


def boat_manager_handle() -> BoatManager:
    return _boat_manager_mem
