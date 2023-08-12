<<<<<<< HEAD
from engine.mathlib import Vec3
from memory.core import mem_handle


class PlayerPartyManager:
    def __init__(self):
        self.memory = mem_handle()
=======
import memory.core as Memory
from helpers.vec import Vec

class PlayerPartyManager():
    def __init__(self):
        self.memory = Memory.mem_handle()
>>>>>>> 621c191 (Adds initial memory reads and some performance fixes)
        self.base = None

    def update(self):
        self.memory.update()

        if self.memory is not None:
<<<<<<< HEAD
            # fmt: off
            _BASE_PTR = [
                0xB8, 0x10, 0x40, 0x30, 0x10, 0x38, 0xA8, 0x10,
                0xC8, 0x38, 0xE8, 0x20, 0x40, 0xD0, 0x200,
            ]
            # fmt: on

            ptr = self.memory.get_pointer(0x2EAA3D0, _BASE_PTR)
=======
            offset = [
                0xB8, 0x10, 0x40, 0x30, 0x10, 0x38, 0xA8, 0x10, 
                0xC8, 0x38, 0xE8, 0x20, 0x40, 0xD0, 0x200
            ] 
            ptr = self.memory.get_pointer(0x2EAA3D0, offset)
>>>>>>> 621c191 (Adds initial memory reads and some performance fixes)
            self.base = ptr

    # def main_character(self):
    #     ptr = self.memory.get_pointer(self.base, [0x70])
    #     return self.memory.pm.read_u8(ptr)
<<<<<<< HEAD

=======
    
>>>>>>> 621c191 (Adds initial memory reads and some performance fixes)
    # def leader_id(self)
    #     ptr = self.memory.get_pointer(self.base, [0x78])
    #     return self.memory.pm.read_u8(ptr)

    def position(self):
        ptr = self.memory.follow_pointer(self.base, [0x98, 0x30, 0x48, 0x0])

        if ptr:
<<<<<<< HEAD
            x = self.memory.read_float(ptr + 0x1C)
            y = self.memory.read_float(ptr + 0x20)
            z = self.memory.read_float(ptr + 0x24)

            return Vec3(x, y, z)
        else:
            return Vec3(None, None, None)
=======
            x = self.memory.read_float(ptr + 0x1c)
            y = self.memory.read_float(ptr + 0x20)
            z = self.memory.read_float(ptr + 0x24)

            return Vec(x,y,z)
        else:
            return Vec(None, None, None)

>>>>>>> 621c191 (Adds initial memory reads and some performance fixes)
