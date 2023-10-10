"""Inventory-based sequencer nodes."""

# Libraries and Core Files
import logging
from enum import Enum, auto
from typing import Self

from control import sos_ctrl
from engine.inventory import Item, get_inventory_manager
from engine.seq.base import SeqBase
from memory import (
    PlayerMovementState,
    player_party_manager_handle,
)

logger = logging.getLogger(__name__)

player_party_manager = player_party_manager_handle()
inventory_manager = get_inventory_manager()


class SeqLoot(SeqBase):
    """Pick up an item and track it."""

    class FSM(Enum):
        """FSM States."""

        GRAB = auto()
        CLEAR_TEXT = auto()

    def __init__(self: Self, name: str, item: Item, amount: int = 1) -> None:
        self.item = item
        self.amount = amount
        self.state = SeqLoot.FSM.GRAB
        super().__init__(name)

    def advance_to_checkpoint(self: Self, checkpoint: str) -> bool:
        inventory_manager.add_item(self.item, self.amount)
        return False

    # Execute pickup logic (interact + skip until idle FSM)
    def execute(self: Self, delta: float) -> bool:
        ctrl = sos_ctrl()
        match self.state:
            case SeqLoot.FSM.GRAB:
                ctrl.confirm()
                inventory_manager.add_item(self.item, self.amount)
                self.state = SeqLoot.FSM.CLEAR_TEXT
            case SeqLoot.FSM.CLEAR_TEXT:
                ctrl.toggle_turbo(state=True)
                ctrl.toggle_confirm(state=True)
                if player_party_manager.movement_state == PlayerMovementState.Idle:
                    ctrl.toggle_turbo(state=False)
                    ctrl.toggle_confirm(state=False)
                    return True
        return False

    def __repr__(self: Self) -> str:
        return f"Grab loot({self.name}): {self.amount}x {self.item} [{self.state.name}]"


# TODO(orkaboy): Implement state object with a player character and an item? Tuple?
# TODO(orkaboy): Implement logic for menuing to equip one or more items.
class SeqEquip(SeqBase):
    """."""
