"""Inventory-based sequencer nodes."""

# Libraries and Core Files
import logging
from enum import Enum, auto
from typing import NamedTuple, Self

from control import sos_ctrl
from engine.inventory import Item, ItemType, get_inventory_manager
from engine.seq.base import SeqBase
from memory import (
    PlayerMovementState,
    PlayerPartyCharacter,
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


class EquipmentCommand(NamedTuple):
    """A command to equip a particular piece of gear on a character."""

    character: PlayerPartyCharacter
    item: Item
    # 0, 1, 2 (gold). Only relevant if item.item_type is ItemType.ACCESSORY
    accessory_slot: int = 0


class SeqEquip(SeqBase):
    """Sequencer node for equipping specific gear."""

    class FSM(Enum):
        """FSM States."""

        OPEN_MENU = auto()
        ENTER_EQUIP = auto()
        SELECT_CHAR = auto()
        SELECT_SLOT = auto()
        EQUIP_GEAR = auto()
        CLOSE_MENU = auto()

    class EquipSlot(Enum):
        """Menu index for different equipment slots."""

        WEAPON = 0
        ARMOR = 1
        ACC1 = 2
        ACC2 = 3
        ACC3 = 4

    def __init__(self: Self, name: str, commands: list[EquipmentCommand]) -> None:
        super().__init__(name)
        self.commands = commands
        self.step = 0
        self.selected_char = 0
        self.selected_slot = 0
        self.state = SeqEquip.FSM.OPEN_MENU

    def select_character(self: Self, character: PlayerPartyCharacter) -> bool:
        """Select character with LB/RB in the equip menu."""
        # ctrl = sos_ctrl()
        # TODO(orkaboy): Need to read which character is currently selected
        # if command.character in party:
        # if command.character == current_char:
        # Use LB/RB to swap characters
        # ctrl.shift_left(tapping=True)
        # ctrl.shift_right(tapping=True)
        # return True
        # else:
        # logger.error(f"Character {character.name} is not in party!")
        # return False

        # TODO(orkaboy): Temp, select first char
        return True

    def select_slot(self: Self, item: Item, accessory_slot: int = 0) -> bool:
        """Select the equipment slot."""
        slot = SeqEquip.EquipSlot.WEAPON
        ctrl = sos_ctrl()
        match item.item_type:
            case ItemType.WEAPON:
                slot = SeqEquip.EquipSlot.WEAPON
            case ItemType.ARMOR:
                slot = SeqEquip.EquipSlot.ARMOR
            case ItemType.ACCESSORY:
                match accessory_slot:
                    case 0:
                        slot = SeqEquip.EquipSlot.ACC1
                    case 1:
                        slot = SeqEquip.EquipSlot.ACC2
                    case 2:
                        slot = SeqEquip.EquipSlot.ACC3
                    case _:
                        # Can't put accessory in this slot! What are you doing?!
                        logger.error(
                            f"It's not possible to equip {item.name} in slot {accessory_slot}!"
                        )
                        return False
            case _:
                # Can't equip this type of item! What are you doing?!
                logger.error(f"It's not possible to equip {item.name}!")
                return False
        # TODO(orkaboy): Optimize closest up/down depending on current selection
        while self.selected_slot != slot:
            ctrl.dpad.tap_down()
            self.selected_slot = self.selected_slot + 1
        return True

    def equip_gear(self: Self, item: Item) -> bool:
        """Iterate the gear selection. Return true if item found."""
        # TODO(orkaboy): Find the correct piece of gear
        # TODO(orkaboy): Find if we don't have the gear and exit

        return True

    def next_command(self: Self) -> bool:
        """Go to next command. Return False if end of list is reached."""
        self.step = self.step + 1
        if self.step >= len(self.commands):
            self.state = SeqEquip.FSM.CLOSE_MENU
            return False
        return True

    def execute(self: Self, delta: float) -> bool:
        command = self.commands[self.step]
        ctrl = sos_ctrl()
        match self.state:
            case SeqEquip.FSM.OPEN_MENU:
                ctrl.menu(tapping=True)
                self.state = SeqEquip.FSM.ENTER_EQUIP
            case SeqEquip.FSM.ENTER_EQUIP:
                # Select the equip option
                ctrl.confirm(tapping=True)
                # Select the first character
                ctrl.confirm(tapping=True)
                self.selected_char = 0
                self.selected_slot = 0
                self.state = SeqEquip.FSM.SELECT_CHAR
            case SeqEquip.FSM.SELECT_CHAR:
                if self.select_character(command.character):
                    self.state = SeqEquip.FSM.SELECT_SLOT
                else:
                    self.next_command()
            case SeqEquip.FSM.SELECT_SLOT:
                if self.select_slot(command.item, command.accessory_slot):
                    ctrl.confirm(tapping=True)
                    self.state = SeqEquip.FSM.EQUIP_GEAR
                elif self.next_command():
                    self.state = SeqEquip.FSM.SELECT_CHAR
            case SeqEquip.FSM.EQUIP_GEAR:
                # Select the correct piece of gear from the list
                if self.equip_gear(command.item):
                    ctrl.confirm(tapping=True)
                else:
                    ctrl.cancel(tapping=True)
                # Go to the next command in the list (or end)
                if self.next_command():
                    self.state = SeqEquip.FSM.SELECT_CHAR
            case SeqEquip.FSM.CLOSE_MENU:
                # Exit equip menu to main menu
                ctrl.cancel(tapping=True)
                # Close the menu
                ctrl.cancel()
                return True

        return False
