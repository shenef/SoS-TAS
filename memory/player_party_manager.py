from enum import Enum

from engine.mathlib import Vec3
from memory.core import mem_handle


# PlayerDefaultState.EState
class PlayerMovementState(Enum):
    NONE = 0
    Running = 1
    Walking = 2
    Idle = 3


class PlayerPartyManager:
    def __init__(self):
        self.memory = mem_handle()
        self.base = None
        self.fields_base = None
        self.position = Vec3(None, None, None)
        self.leader = None
        self.movement_state = PlayerMovementState.NONE

    def update(self):
        try:
            self.memory.update()

            if self.memory.ready_for_updates():
                if self.base is None or self.fields_base is None:
                    singleton_ptr = self.memory.get_singleton_by_class_name(
                        "PlayerPartyManager"
                    )
                    self.base = self.memory.get_class_base(singleton_ptr)
                    self.fields_base = self.memory.get_class_fields_base(singleton_ptr)
                    self.leader = self.memory.get_field(self.fields_base, "leader")

                # Update fields
                self.get_position()
                self.get_movement_state()
            else:
                self.__init__()
        except Exception:
            return

    def get_position(self):
        if self.memory.ready_for_updates():
            # leader -> controller -> currentTargetPosition
            ptr = self.memory.follow_pointer(self.base, [self.leader, 0x78, 0x7C])
            if ptr:
                x = self.memory.read_float(ptr + 0x0)
                y = self.memory.read_float(ptr + 0x4)
                z = self.memory.read_float(ptr + 0x8)

                self.position = Vec3(x, y, z)
                return

        self.position = Vec3(None, None, None)

    def get_movement_state(self):
        if self.memory.ready_for_updates():
            ptr = self.memory.follow_pointer(self.base, [self.leader, 0x70, 0x50, 0x84])

            match self.memory.read_int(ptr):
                case 0:
                    self.movement_state = PlayerMovementState.NONE
                case 1:
                    self.movement_state = PlayerMovementState.Running
                case 2:
                    self.movement_state = PlayerMovementState.Walking
                case 3:
                    self.movement_state = PlayerMovementState.Idle
                case _:
                    self.movement_state = PlayerMovementState.NONE
