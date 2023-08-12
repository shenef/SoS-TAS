from engine.mathlib import Vec3
from memory.core import mem_handle


class PlayerPartyManager:
    def __init__(self):
        self.memory = mem_handle()
        self.base = None

    def update(self):
        self.memory.update()

        if self.memory is not None:
            # fmt: off
            _BASE_PTR = [
                0xB8, 0x10, 0x40, 0x30, 0x10, 0x38, 0xA8, 0x10,
                0xC8, 0x38, 0xE8, 0x20, 0x40, 0xD0, 0x200,
            ]
            # fmt: on

            ptr = self.memory.get_pointer(0x2EAA3D0, _BASE_PTR)
            self.base = ptr

    # def main_character(self):
    #     ptr = self.memory.get_pointer(self.base, [0x70])
    #     return self.memory.pm.read_u8(ptr)

    # def leader_id(self)
    #     ptr = self.memory.get_pointer(self.base, [0x78])
    #     return self.memory.pm.read_u8(ptr)

    def position(self):
        ptr = self.memory.follow_pointer(self.base, [0x98, 0x30, 0x48, 0x0])

        if ptr:
            x = self.memory.read_float(ptr + 0x1C)
            y = self.memory.read_float(ptr + 0x20)
            z = self.memory.read_float(ptr + 0x24)

            return Vec3(x, y, z)
        else:
            return Vec3(None, None, None)
