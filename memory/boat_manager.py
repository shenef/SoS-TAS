from typing import Self

from engine.mathlib import Quaternion, Vec3
from memory.core import mem_handle


class BoatManager:
    def __init__(self: Self) -> None:
        """Initialize a new BoatManager object."""
        self.memory = mem_handle()
        self.base = None
        self.position = Vec3(None, None, None)
        self.rotation = Quaternion(None, None, None, None)
        self.speed = 0
        self.max_speed = 0

    def update(self: Self) -> None:
        if self.memory.ready_for_updates:
            try:
                if self.base is None:
                    singleton_ptr = self.memory.get_singleton_by_class_name("BoatManager")
                    if singleton_ptr is None:
                        return

                    self.base = self.memory.get_class_base(singleton_ptr)
                    if self.base == 0x0:
                        return

                else:
                    # Update fields
                    self._read_position()
                    self._read_rotation()
                    self._read_speed()
            except Exception as _e:
                # logger.debug(f"BoatManager Reloading {type(_e)}")
                self.__init__()

    def _read_position(self: Self) -> None:
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

    def _read_rotation(self: Self) -> None:
        if self.memory.ready_for_updates:
            # (BoatInstance) k__BackingField -> boatSnapRotation -> pitchRollLocalRotation
            ptr = self.memory.follow_pointer(self.base, [0x40, 0x60, 0x0])
            if ptr:
                # not sure what these are called, but the values are here.
                x = self.memory.read_float(ptr + 0x44)
                y = self.memory.read_float(ptr + 0x48)
                z = self.memory.read_float(ptr + 0x4C)
                w = self.memory.read_float(ptr + 0x50)

                self.rotation = Quaternion(x, y, z, w)
                return

        self.rotation = Quaternion(None, None, None, None)

    def _read_speed(self: Self) -> None:
        if self.memory.ready_for_updates:
            # (BoatInstance) k__BackingField -> boatSnapRotation -> pitchRollLocalRotation
            ptr = self.memory.follow_pointer(self.base, [0x40, 0x0])
            if ptr:
                #
                max_speed = self.memory.read_float(ptr + 0x78)
                speed = self.memory.read_float(ptr + 0x134)

                self.max_speed = max_speed
                self.speed = speed
                return

        self.speed = 0


_boat_manager_mem = BoatManager()


def boat_manager_handle() -> BoatManager:
    return _boat_manager_mem
