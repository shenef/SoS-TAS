from engine.mathlib import Vec3
from memory.core import mem_handle


class PlayerWorldMapState:
    def __init__(self):
        self.memory = mem_handle()
        self.base = None
        self.fields_base = None
        self.position = Vec3(None, None, None)

    def update(self):
        try:
            self.memory.update()

            if self.memory.ready_for_updates():
                if self.base is None or self.fields_base is None:
                    singleton_ptr = self.memory.get_singleton_by_class_name("PlayerWorldMapState")
                    self.base = self.memory.get_class_base(singleton_ptr)
                    self.fields_base = self.memory.get_class_fields_base(singleton_ptr)
                    self.controller = self.memory.get_field(self.fields_base, "player")

                # Update fields
                self.get_position()
            else:
                self.__init__()
        except Exception:
            return

    def get_position(self):
        if self.memory.ready_for_updates():
            ptr = self.memory.follow_pointer(
                self.base, [self.controller, 0x78, 0x7c, 0x0]
            )
            if ptr:
                x = self.memory.read_float(ptr + 0x1C)
                y = self.memory.read_float(ptr + 0x20)
                z = self.memory.read_float(ptr + 0x24)

                self.position = Vec3(x, y, z)
                return

        self.position = Vec3(None, None, None)
