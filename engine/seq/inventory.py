"""Inventory-based sequencer nodes."""

# Libraries and Core Files
import logging
from enum import Enum, auto
from typing import NamedTuple, Self

from control import sos_ctrl
from engine.inventory import EquippableItem, Item, ItemType, get_inventory_manager
from engine.seq.base import SeqBase
from memory import (
    PlayerMovementState,
    PlayerPartyCharacter,
    player_party_manager_handle,
)

logger = logging.getLogger(__name__)

player_party_manager = player_party_manager_handle()
inventory_manager = get_inventory_manager()


class EquipmentCommand(NamedTuple):
    """A command to equip a particular piece of gear on a character."""

    character: PlayerPartyCharacter
    item: EquippableItem
    # 0, 1 (trinket), 2 (gold/group). Only relevant if item.item_type is ItemType.TRINKET
    trinket_slot: int = 0


class SeqEquip(SeqBase):
    """Sequencer node for equipping specific gear."""

    class FSM(Enum):
        """Finite-State-Machine States."""

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
        TRINKET1 = 2
        TRINKET2 = 3
        GROUP_TRINKET = 4

    def __init__(self: Self, name: str, commands: list[EquipmentCommand]) -> None:
        super().__init__(name)
        self.commands = commands
        self.step = 0
        self.selected_char = 0
        self.selected_slot = 0
        self.state = SeqEquip.FSM.OPEN_MENU

    def select_character(self: Self, character: PlayerPartyCharacter) -> bool:
        """Select character with LB/RB in the equip menu."""
        ctrl = sos_ctrl()

        party = player_party_manager.current_party
        if character not in party:
            logger.error(f"SeqEquip: Character {character} is not in party: {party}")
            return False

        while character != party[self.selected_char]:
            # Use LB/RB to swap characters
            # TODO(orkaboy): optimize, go left
            ctrl.shift_right(tapping=True)
            self.selected_char += 1
            if self.selected_char >= len(party):
                self.selected_char = 0
        logger.debug(f"SeqEquip: Character {character} selected")
        return True

    def select_slot(self: Self, item: EquippableItem, trinket_slot: int = 0) -> bool:
        """Select the equipment slot."""
        slot = SeqEquip.EquipSlot.WEAPON
        ctrl = sos_ctrl()
        match item.item_type:
            case ItemType.WEAPON:
                slot = SeqEquip.EquipSlot.WEAPON
            case ItemType.ARMOR:
                slot = SeqEquip.EquipSlot.ARMOR
            case ItemType.TRINKET:
                match trinket_slot:
                    case 0:
                        slot = SeqEquip.EquipSlot.TRINKET1
                    case 1:
                        slot = SeqEquip.EquipSlot.TRINKET2
                    case _:
                        # Can't put accessory in this slot! What are you doing?!
                        logger.error(
                            f"It's not possible to equip {item.name} in slot {trinket_slot}!"
                        )
                        return False
            case ItemType.GROUPTRINKET:
                slot = SeqEquip.EquipSlot.GROUP_TRINKET
            case _:
                # Can't equip this type of item! What are you doing?!
                logger.error(f"It's not possible to equip {item.name}!")
                return False
        logger.debug(f"SeqEquip: Selecting slot {slot}")
        # TODO(orkaboy): Optimize closest up/down depending on current selection
        while self.selected_slot != slot.value:
            ctrl.dpad.tap_down()
            self.selected_slot = self.selected_slot + 1
            if self.selected_slot > SeqEquip.EquipSlot.GROUP_TRINKET.value:
                self.selected_slot = 0
        return True

    def equip_gear(self: Self, item: EquippableItem) -> bool:
        """Iterate the gear selection. Return true if item found."""
        # TODO(orkaboy): Find the correct piece of gear
        # TODO(orkaboy): Find if we don't have the gear and exit

        # TODO(orkaboy): Usually, the best piece of gear is highest in the list,
        # TODO(orkaboy): just after the currently equipped item. Tap down to select it.
        ctrl = sos_ctrl()
        ctrl.dpad.tap_down()

        return True

    def next_command(self: Self) -> bool:
        """Go to next command. Return False if end of list is reached."""
        self.step = self.step + 1
        if self.step >= len(self.commands):
            return False
        return True

    def execute(self: Self, delta: float) -> bool:
        if self.step >= len(self.commands):
            self.state = SeqEquip.FSM.CLOSE_MENU
        else:
            command = self.commands[self.step]
        ctrl = sos_ctrl()
        match self.state:
            case SeqEquip.FSM.OPEN_MENU:
                ctrl.menu(tapping=True)
                self.state = SeqEquip.FSM.ENTER_EQUIP
                logger.debug("SeqEquip: Opened menu")
            case SeqEquip.FSM.ENTER_EQUIP:
                # Select the equip option
                ctrl.confirm(tapping=True)
                # Select the first character
                ctrl.confirm(tapping=True)
                self.selected_char = 0
                self.selected_slot = 0
                self.state = SeqEquip.FSM.SELECT_CHAR
                logger.debug("SeqEquip: Select equip, select first character")
            case SeqEquip.FSM.SELECT_CHAR:
                if self.select_character(command.character):
                    self.state = SeqEquip.FSM.SELECT_SLOT
                else:
                    self.next_command()
            case SeqEquip.FSM.SELECT_SLOT:
                if self.select_slot(command.item, command.trinket_slot):
                    ctrl.confirm(tapping=True)
                    self.state = SeqEquip.FSM.EQUIP_GEAR
                elif self.next_command():
                    self.state = SeqEquip.FSM.SELECT_CHAR
            case SeqEquip.FSM.EQUIP_GEAR:
                # Select the correct piece of gear from the list
                if self.equip_gear(command.item):
                    ctrl.confirm(tapping=True)
                    logger.debug(f"SeqEquip: Equipped item {command.item}")
                else:
                    ctrl.cancel(tapping=True)
                    logger.error(f"SeqEquip: Could not equip item {command.item}")
                # Go to the next command in the list (or end)
                if self.next_command():
                    self.state = SeqEquip.FSM.SELECT_CHAR
            case SeqEquip.FSM.CLOSE_MENU:
                # Exit equip menu to main menu
                ctrl.cancel(tapping=True)
                # Close the menu
                ctrl.cancel()
                logger.debug("SeqEquip: Closing menu")
                return True

        return False


class SeqLoot(SeqBase):
    """Pick up an item and track it."""

    class FSM(Enum):
        """Finite-State-Machine States."""

        GRAB = auto()
        CLEAR_TEXT = auto()
        EQUIP = auto()

    def __init__(
        self: Self,
        name: str,
        item: Item = None,
        amount: int = 1,
        equip_node: SeqEquip = None,
        equip_to: PlayerPartyCharacter = None,
        trinket_slot: int = 0,
    ) -> None:
        super().__init__(name)
        self.item = item
        self.amount = amount
        self.state = SeqLoot.FSM.GRAB
        # Optionally, initialize a new SeqEquip node
        self.equip_node: SeqEquip = None
        if equip_node is not None:
            self.equip_node = equip_node
        elif equip_to is not None:
            self.equip_node = SeqEquip(
                name=self.name,
                commands=[
                    EquipmentCommand(character=equip_to, item=self.item, trinket_slot=trinket_slot)
                ],
            )

    def advance_to_checkpoint(self: Self, checkpoint: str) -> bool:
        if self.item is not None:
            inventory_manager.add_item(self.item, self.amount)
        return False

    # Execute pickup logic (interact + skip until idle FSM)
    def execute(self: Self, delta: float) -> bool:
        ctrl = sos_ctrl()
        match self.state:
            case SeqLoot.FSM.GRAB:
                ctrl.confirm()
                if self.item is not None:
                    inventory_manager.add_item(self.item, self.amount)
                self.state = SeqLoot.FSM.CLEAR_TEXT
            case SeqLoot.FSM.CLEAR_TEXT:
                ctrl.toggle_turbo(state=True)
                ctrl.toggle_confirm(state=True)
                if player_party_manager.movement_state == PlayerMovementState.Idle:
                    item = f"{self.amount}x {self.item} " if self.item is not None else ""
                    logger.info(f"Grab loot({self.name}): {item}")
                    ctrl.toggle_turbo(state=False)
                    ctrl.toggle_confirm(state=False)
                    if self.equip_node is None:
                        return True
                    self.state = SeqLoot.FSM.EQUIP
            case SeqLoot.FSM.EQUIP:
                return self.equip_node.execute(delta)
        return False

    def __repr__(self: Self) -> str:
        item = f"{self.amount}x {self.item} " if self.item is not None else ""
        return f"Grab loot({self.name}): {item}[{self.state.name}]"


class ShoppingCommand:
    """A command to buy or sell a particular item, optionally equipping it on a character."""

    def __init__(
        self: Self,
        item: Item,
        sell: bool = False,
        amount: int = 1,
        character: PlayerPartyCharacter = None,
    ) -> None:
        """Initialize a ShoppingCommand object."""
        self.item = item
        self.sell = sell
        self.amount = amount
        # If should equip
        self.character = character


class SeqShop(SeqBase):
    """Shopping node."""

    SKIP_TIMEOUT = 1.0

    class FSM(Enum):
        """Finite-State-Machine States."""

        OPEN_SHOP = auto()
        SKIP_DIALOG = auto()
        SELECT_MODE = auto()
        SELECT_ITEM = auto()
        SELECT_AMOUNT = auto()
        STORE_OR_EQUIP = auto()
        EQUIP_GEAR = auto()
        NEXT_ITEM = auto()
        CLOSE_SHOP = auto()

    def __init__(self: Self, name: str, commands: list[ShoppingCommand]) -> None:
        """Initialize a SeqShop node."""
        super().__init__(name)
        self.timer = 0.0
        self.step = 0
        self.commands = commands
        self.state = SeqShop.FSM.OPEN_SHOP
        self.sell_mode = False

    def advance_to_checkpoint(self: Self, checkpoint: str) -> bool:
        for command in self.commands:
            if command.sell:
                inventory_manager.sell_item(command.item)
            else:
                inventory_manager.buy_item(command.item)
        return False

    def next_command(self: Self) -> bool:
        self.step += 1
        return self.step < len(self.commands)

    def execute(self: Self, delta: float) -> bool:
        ctrl = sos_ctrl()

        if self.step < len(self.commands):
            command = self.commands[self.step]
        # Empty command list guard
        elif self.step == 0:
            return True

        match self.state:
            case SeqShop.FSM.OPEN_SHOP:
                logger.debug("SeqShop: Entering shop")
                ctrl.toggle_confirm(state=True)
                ctrl.toggle_turbo(state=True)
                self.state = SeqShop.FSM.SKIP_DIALOG
            case SeqShop.FSM.SKIP_DIALOG:
                self.timer += delta
                if self.timer >= SeqShop.SKIP_TIMEOUT:
                    ctrl.toggle_turbo(state=False)
                    ctrl.toggle_confirm(state=False)
                    self.state = SeqShop.FSM.SELECT_MODE
            case SeqShop.FSM.SELECT_MODE:
                if command.sell != self.sell_mode:
                    self.sell_mode = command.sell
                    ctrl.dpad.tap_down()
                    ctrl.confirm(tapping=True)
                logger.debug(f"SeqShop: Mode = {"Sell" if self.sell_mode else "Buy"}")
                self.state = SeqShop.FSM.SELECT_ITEM
            case SeqShop.FSM.SELECT_ITEM:
                # TODO(orkaboy): Need to know which slot the item we want is in, from memory?

                # TODO(orkaboy): In sell mode, we need to be in the correct cathegory (LB/RB)

                # TODO(orkaboy): For now, select whatever's first in the list (not correct!)
                logger.debug(f"SeqShop:   Item = {command.item}")
                ctrl.confirm(tapping=True)
                # TODO(orkaboy): Need to handle logic for Relics?
                if command.sell or not isinstance(command.item, EquippableItem):
                    self.state = SeqShop.FSM.SELECT_AMOUNT
                else:
                    self.state = SeqShop.FSM.STORE_OR_EQUIP
            case SeqShop.FSM.SELECT_AMOUNT:
                # Select the amount to buy/sell (starts at 1)
                # TODO(orkaboy): Currently doesn't check for if we CAN buy this amount of items
                # TODO(orkaboy): Could optimize this with up/down for amounts > 10
                for _ in range(command.amount - 1):
                    ctrl.dpad.tap_right()

                # Actually buy/sell the item
                ctrl.confirm(tapping=True)
                if command.sell:
                    inventory_manager.sell_item(command.item, command.amount)
                else:
                    inventory_manager.buy_item(command.item, command.amount)

                self.state = SeqShop.FSM.NEXT_ITEM
            case SeqShop.FSM.STORE_OR_EQUIP:
                # Equip is selected by default
                if command.character is None:
                    # Select "Store"
                    ctrl.dpad.tap_left()
                    # Actually buy the item
                    ctrl.confirm(tapping=True)
                    inventory_manager.buy_item(command.item)
                    self.state = SeqShop.FSM.NEXT_ITEM
                else:
                    ctrl.confirm(tapping=True)
                    self.state = SeqShop.FSM.EQUIP_GEAR
            case SeqShop.FSM.EQUIP_GEAR:
                item: EquippableItem = command.item
                party = player_party_manager.current_party
                if item.equippable_by is not None:
                    party = list(filter(lambda character: character in item.equippable_by, party))

                try:
                    # Tap down in the list to target character
                    index = party.index(command.character)
                    for _ in range(index):
                        ctrl.dpad.tap_down()
                    logger.debug(f"SeqShop:    Equipping {item} on {command.character.name}")
                    # Actually buy + equip the item
                    ctrl.confirm(tapping=True)
                    inventory_manager.buy_item(command.item)
                except ValueError:
                    logger.warning(
                        f"SeqShop:    Can't equip {item} to any character in current party!"
                    )
                    ctrl.cancel(tapping=True)
                    ctrl.cancel(tapping=True)

                self.state = SeqShop.FSM.NEXT_ITEM
            case SeqShop.FSM.NEXT_ITEM:
                if self.next_command():
                    command = self.commands[self.step]
                    if command.sell != self.sell_mode:
                        ctrl.cancel(tapping=True)
                        self.state = SeqShop.FSM.SELECT_MODE
                    else:
                        self.state = SeqShop.FSM.SELECT_ITEM
                else:
                    self.state = SeqShop.FSM.CLOSE_SHOP
            case SeqShop.FSM.CLOSE_SHOP:
                logger.debug("SeqShop: Closing shop")
                ctrl.cancel(tapping=True)
                ctrl.cancel()
                logger.info("SeqShop: Finished shopping segment")
                return True

        return False
