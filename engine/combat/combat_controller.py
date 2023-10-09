import logging
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
    new_dialog_manager_handle,
)

logger = logging.getLogger(__name__)
level_manager = level_manager_handle()
combat_manager = combat_manager_handle()
new_dialog_manager = new_dialog_manager_handle()


class CombatController:
    def __init__(self: Self) -> None:
        self.controller = None

    # returns a bool to feed to the sequencer
    def execute_combat(self: Self, delta: float) -> bool:
        sos_ctrl().set_neutral()

        # Assign a controller, or the correct controller if it changes.
        # This is because sometimes when we check, the controller has not been
        # set by the game yet, or potentially a change in controllers during a fight.
        if (
            self.controller is None
            or self.controller.__class__.__name__
            is not self._encounter_controller_factory().__class__.__name__
        ):
            # TODO(eein): Add a battle controller factory
            logger.debug("Setting New Combat Controller")
            self.controller = self._encounter_controller_factory()
            logger.debug(f"Using: {self.controller.__class__.__name__}")

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
