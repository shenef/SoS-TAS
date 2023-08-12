from engine.mathlib import Vec3
from memory.core import mem_handle


class PlayerPartyManager:
    def __init__(self):
        self.memory = mem_handle()
        self.base = None
        self.position = Vec3(None, None, None)

    def update(self):
        self.memory.update()

        if self.base is None:
            local_class = self.memory.get_class("PlayerPartyManager")
            parent = self.memory.get_parent(local_class)
            instance_ptr = self.memory.get_field(parent, "instance")
            static_table = self.memory.get_static_table(parent) 
            singleton_ptr = static_table + instance_ptr
            self.base = self.memory.get_class_root(singleton_ptr)
        
        if self.memory is not None:
            self.controller = self.memory.get_field(self.base, "leader")
            
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
