import logging
from enum import Enum, auto
from typing import Self

from control import sos_ctrl
from engine.combat.controllers import (
    ElderMistEncounterController,
    EncounterController,
    FirstEncounterController,
    LiveManaTutorialController,
    SecondEncounterController,
)
from engine.combat.level_up import handle_level_up
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
    LEVEL_UP_TIMEOUT = 5.0
    # TODO(eein): Use objects/mappers for these later on.
    ELDER_MIST_ENEMY_GUID = "962aa552d33fc124782b230fce9185ce"
    ELDER_MIST_TRIAL_LEVEL_GUID = "11810c4630980eb43abf7fecebfd5a6b"

    class FSM(Enum):
        """Finite-state machine States."""

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
        return self.state in {CombatController.FSM.IDLE, CombatController.FSM.AFTER_COMBAT}

    def update_state(self: Self, delta: float) -> None:
        """
        Update the FSM. Should be called before execute_combat.

        Assign a controller, or the correct controller if it changes.
        This is because sometimes when we check, the controller has not been
        set by the game yet, or potentially a change in controllers during a fight.
        """
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
            # This is a somewhat janky way of detecting level up,
            # while still allowing for starting movement in SeqMove.
            case CombatController.FSM.AFTER_COMBAT:
                self.timer += delta
                if self.timer >= self.LEVEL_UP_TIMEOUT:
                    self.state = CombatController.FSM.IDLE
                if level_up_manager.level_up_screen_active:
                    self.state = CombatController.FSM.LEVEL_UP_SCREEN
                    logger.debug(f"After combat state -> Level up screen, took {self.timer:.3f}s")
            case CombatController.FSM.LEVEL_UP_SCREEN:
                if level_up_manager.level_up_screen_active is False:
                    self.state = CombatController.FSM.IDLE

    def execute_combat(self: Self, delta: float) -> bool:
        """Return a bool to feed to the sequencer."""
        sos_ctrl().set_neutral()

        if self.state == CombatController.FSM.LEVEL_UP_SCREEN:
            handle_level_up()  # See level_up.py
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
                match map(lambda x: x.guid, combat_manager.enemies):
                    # Handle Enemy Specific Controllers
                    # Elder Mist Fight
                    case _ as enemies if self.ELDER_MIST_ENEMY_GUID in enemies:
                        return ElderMistEncounterController()
                    # Handle level specific controllers or fall back to
                    # standard encounter controller
                    case _:
                        match level_manager.current_level:
                            # Elder Mist Zone
                            case self.ELDER_MIST_TRIAL_LEVEL_GUID:
                                return LiveManaTutorialController()
                            case _:
                                return EncounterController()
