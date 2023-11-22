from enum import Enum
from typing import Self

from engine.mathlib import Vec3
from memory.core import mem_handle
from memory.mappers.player_party_character import PlayerPartyCharacter


# PlayerDefaultState.EState
class PlayerMovementState(Enum):
    NONE = 0
    Running = 1
    Walking = 2
    Idle = 3


class PlayerPartyManager:
    NULL_POINTER = 0xFFFFFFFF
    PLAYER_OBJECT_OFFSET = 0x8
    PLAYER_INDEX_0_ADDRESS = 0x20

    def __init__(self: Self) -> None:
        """Initialize a new PlayerPartyManager object."""
        self.memory = mem_handle()
        self.base = None
        self.fields_base = None
        self.current_party: list[PlayerPartyCharacter] = []
        self.position: Vec3 = None
        self.gameobject_position: Vec3 = None
        self.leader = None
        self.movement_state = PlayerMovementState.NONE
        self.leader_character = PlayerPartyCharacter.NONE

    def update(self: Self) -> None:
        if self.memory.ready_for_updates:
            try:
                if self.base is None or self.fields_base is None:
                    singleton_ptr = self.memory.get_singleton_by_class_name("PlayerPartyManager")
                    if singleton_ptr is None:
                        return

                    self.base = self.memory.get_class_base(singleton_ptr)
                    if self.base == 0x0:
                        return
                    self.fields_base = self.memory.get_class_fields_base(singleton_ptr)

                else:
                    # Update fields
                    self.leader = self.memory.get_field(self.fields_base, "leader")
                    self._read_position()
                    self._read_gameobject_position()
                    self._read_movement_state()
                    self._read_leader_character()
                    self._read_current_party()

            except Exception as _e:
                # logger.debug(f"PlayerPartyManager Reloading {type(_e)}")
                self.__init__()

    def _read_current_party(self: Self) -> None:
        try:
            current_party_ptr = self.memory.follow_pointer(self.base, [0x98, 0x0])
            # Item is an array of pointers of size 0x08
            # this follows playerPartyManager -> 0x98 (currentParty)

            if current_party_ptr == self.NULL_POINTER:
                self.current_party = []
                return

            combat_players = self.memory.follow_pointer(
                current_party_ptr,
                [0x10, 0x0],
            )
            players = []

            if combat_players:
                address = self.PLAYER_INDEX_0_ADDRESS

                while True:
                    ptr = self.memory.follow_pointer(combat_players, [address, 0x0])

                    if ptr == 0x0 or ptr is self.NULL_POINTER:
                        break

                    definition_id = self.memory.read_string(ptr + 0x14, 8)

                    players.append(PlayerPartyCharacter.parse_definition_id(definition_id))
                    address += self.PLAYER_OBJECT_OFFSET

                self.current_party = players
                return
        except Exception:
            self.current_party = []
            return
        self.current_party = []

    def _read_position(self: Self) -> None:
        if self.memory.ready_for_updates:
            # leader -> controller -> currentTargetPosition
            ptr = self.memory.follow_pointer(self.base, [self.leader, 0x90, 0x84])
            if ptr:
                x = self.memory.read_float(ptr + 0x0)
                y = self.memory.read_float(ptr + 0x4)
                z = self.memory.read_float(ptr + 0x8)

                self.position = Vec3(x, y, z)
                return

        self.position = None

    def _read_gameobject_position(self: Self) -> None:
        if self.memory.ready_for_updates:
            # leader -> controller -> currentTargetPosition
            gameobject_ptr = self.memory.follow_pointer(self.base, [self.leader, 0x30, 0x0])
            if gameobject_ptr == 0x0:
                self.gameobject_position = None
                return

            ptr = self.memory.follow_pointer(gameobject_ptr, [0x48, 0x1C])
            if ptr:
                x = self.memory.read_float(ptr + 0x0)
                y = self.memory.read_float(ptr + 0x4)
                z = self.memory.read_float(ptr + 0x8)

                self.gameobject_position = Vec3(x, y, z)
                return

        self.gameobject_position = None

    def _read_movement_state(self: Self) -> None:
        if self.memory.ready_for_updates:
            # leader -> stateMachine -> currentState
            ptr = self.memory.follow_pointer(self.base, [self.leader, 0x88, 0x50, 0x8C])

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

    def _read_leader_character(self: Self) -> None:
        if self.memory.ready_for_updates:
            # base -> leaderId
            ptr = self.memory.follow_pointer(self.base, [0x88, 0x0])
            definition_id = self.memory.read_string(ptr + 0x14, 8)

            # Definition IDS are stored as some goofy serialized utf encoded string
            # We just do our best with the values that are provided to
            # Determine the character we are looking at

            self.leader_character = PlayerPartyCharacter.parse_definition_id(definition_id)


_player_party_manager_mem = PlayerPartyManager()


def player_party_manager_handle() -> PlayerPartyManager:
    return _player_party_manager_mem
