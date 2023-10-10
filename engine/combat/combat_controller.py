import logging
from enum import Enum, auto
from typing import Self

from control import sos_ctrl
from engine.combat.controllers import (
    EncounterController,
    FirstEncounterController,
    LiveManaTutorialController,
    SecondEncounterController,
)
from memory import (
    CombatEncounter,
    combat_manager_handle,
    level_manager_handle,
    level_up_manager_handle,
    new_dialog_manager_handle,
)

logger = logging.getLogger(__name__)
level_manager = level_manager_handle()
level_up_manager = level_up_manager_handle()
combat_manager = combat_manager_handle()
new_dialog_manager = new_dialog_manager_handle()


class CombatController:
    LEVEL_UP_TIMEOUT = 10.0

    class FSM(Enum):
        """FSM States."""

        IDLE = auto()
        COMBAT = auto()
        AFTER_COMBAT = auto()
        LEVEL_UP_SCREEN = auto()

    def __init__(self: Self) -> None:
        """Initialize a new CombatController object."""
        self.controller = None
        self.state = CombatController.FSM.IDLE
        self.timer = 0

    def is_done(self: Self) -> bool:
        return self.state in [CombatController.FSM.IDLE, CombatController.FSM.AFTER_COMBAT]

    def update_state(self: Self, delta: float) -> None:
        """Update the FSM. Should be called before execute_combat."""
        # Assign a controller, or the correct controller if it changes.
        # This is because sometimes when we check, the controller has not been
        # set by the game yet, or potentially a change in controllers during a fight.
        if (
            self.controller is None
            or self.controller.__class__.__name__
            is not self._encounter_controller_factory().__class__.__name__
        ):
            logger.debug("Setting New Combat Controller")
            self.controller = self._encounter_controller_factory()
            logger.debug(f"Using: {self.controller.__class__.__name__}")

        if self.controller.encounter_done() is False:
            self.state = CombatController.FSM.COMBAT

        match self.state:
            case CombatController.FSM.IDLE:
                pass
            case CombatController.FSM.COMBAT:
                if self.controller.encounter_done():
                    self.timer = 0
                    self.state = CombatController.FSM.AFTER_COMBAT
            case CombatController.FSM.AFTER_COMBAT:
                self.timer += delta
                if self.timer >= self.LEVEL_UP_TIMEOUT:
                    self.state = CombatController.FSM.IDLE
                if level_up_manager.level_up_screen_active:
                    self.state = CombatController.FSM.LEVEL_UP_SCREEN
            case CombatController.FSM.LEVEL_UP_SCREEN:
                if level_up_manager.level_up_screen_active is False:
                    self.state = CombatController.FSM.IDLE

    # returns a bool to feed to the sequencer
    def execute_combat(self: Self, delta: float) -> bool:
        sos_ctrl().set_neutral()

        if self.state == CombatController.FSM.LEVEL_UP_SCREEN:
            # TODO(orkaboy): Very temporary code to mash past level up screen
            sos_ctrl().confirm(tapping=True)
            return False

        if self.controller.encounter_done():
            self.controller = None
            return True

        if self.controller.execute_dialog():
            return False

        if self.controller.generate_action():
            return False

        if self.controller.execute_block():
            return False

        if not self.controller.has_action():
            return False

        if self.controller.execute_consideration():
            return False

        if self.controller.action.appraisal.execute():
            return False

        return False

    def _encounter_controller_factory(self: Self) -> EncounterController:
        match combat_manager.combat_controller:
            case CombatEncounter.FirstEncounter:
                return FirstEncounterController()
            case CombatEncounter.SecondEncounter:
                return SecondEncounterController()
            case CombatEncounter.LiveManaTutorial:
                return LiveManaTutorialController()
            case _:
                return EncounterController()
