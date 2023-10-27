import logging
from enum import Enum, auto
from typing import Self

from control import sos_ctrl
from engine.inventory.items import KEY
from engine.seq.base import SeqBase
from engine.seq.inventory import Item, ItemType
from memory.inventory_manager import ItemReference, inventory_manager_handle

logger = logging.getLogger(__name__)

inventory_manager = inventory_manager_handle()


class SeqToggleRelic(SeqBase):
    class FSM(Enum):
        """Finite-State-Machine States."""

        OPEN_MENU = auto()
        ENTER_RELIC = auto()
        FIND_NEXT_RELIC = auto()
        SELECT_RELIC = auto()
        CLOSE_MENU = auto()

    def __init__(
        self: Self,
        name: str,
        relics: list[Item],
    ) -> None:
        super().__init__(name)
        self.relics = relics
        # State variables
        self.current_index = 0
        self.target_index = 0
        self.step = 0
        self.state = SeqToggleRelic.FSM.OPEN_MENU
        self.held_relics: list[ItemReference] = None

    # Override
    def execute(self: Self, delta: float) -> bool:
        if self.step < len(self.relics):
            relic = self.relics[self.step]
        else:
            self.state = SeqToggleRelic.FSM.CLOSE_MENU

        ctrl = sos_ctrl()
        match self.state:
            case SeqToggleRelic.FSM.OPEN_MENU:
                ctrl.menu(tapping=True)
                self.state = SeqToggleRelic.FSM.ENTER_RELIC
                self.held_relics = inventory_manager.get_items_by_type(item_type=ItemType.RELIC)
                logger.debug("SeqToggleRelic: Opened menu")
            case SeqToggleRelic.FSM.ENTER_RELIC:
                # Tap up twice
                ctrl.dpad.tap_up()
                ctrl.dpad.tap_up()
                # If we are carrying the map, need to press up a third time
                if KEY.Map in map(lambda item_ref: item_ref.item, inventory_manager.items_mapped):
                    ctrl.dpad.tap_up()
                # Select the relic option
                ctrl.confirm(tapping=True)
                self.state = SeqToggleRelic.FSM.FIND_NEXT_RELIC
                logger.debug("SeqToggleRelic: Select relic")
            case SeqToggleRelic.FSM.FIND_NEXT_RELIC:
                self.target_index = -1
                for idx, held_relic in enumerate(self.held_relics):
                    if held_relic.item == relic:
                        self.target_index = idx
                        break
                # Warn if relic not found
                if self.target_index == -1:
                    logger.error(
                        f"SeqToggleRelic: Error in step {self.step}, could not find {relic}! Skipping."  # noqa: E501
                    )
                    self.step += 1
                else:  # Ok
                    self.state = SeqToggleRelic.FSM.SELECT_RELIC
            case SeqToggleRelic.FSM.SELECT_RELIC:
                if self.target_index > self.current_index:
                    self.current_index += 1
                    ctrl.dpad.tap_down()
                elif self.target_index < self.current_index:
                    self.current_index -= 1
                    ctrl.dpad.tap_up()
                else:
                    # Toggle state of the relic
                    ctrl.confirm(tapping=True)
                    logger.debug(f"SeqToggleRelic: Toggled state of {relic}")
                    self.step += 1
                    self.state = SeqToggleRelic.FSM.FIND_NEXT_RELIC
            case SeqToggleRelic.FSM.CLOSE_MENU:
                # Exit equip menu to main menu
                ctrl.cancel(tapping=True)
                # Close the menu
                ctrl.cancel()
                logger.debug("SeqToggleRelic: Closing menu")
                logger.info(f"Done toggling relics ({self.name})")
                return True

        return False

    def __repr__(self: Self) -> str:
        return f"Toggle relic sequence ({self.name}): {self.state.name}."
