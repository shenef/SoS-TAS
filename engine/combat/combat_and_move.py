from collections.abc import Callable
from enum import Enum, auto
from typing import Any, Self

from control.sos import sos_ctrl
from engine.combat.combat_controller import CombatController
from engine.mathlib import Vec3
from engine.seq import HoldDirection, InteractMove, SeqBase, SeqMove
from memory import combat_manager_handle

combat_manager = combat_manager_handle()


class EncounterState(Enum):
    BEFORE_COMBAT = auto()
    COMBAT = auto()
    POST_COMBAT = auto()


class SeqCombat(SeqBase):
    def __init__(self: Self, name: str, func: Callable[..., Any] = None) -> None:
        super().__init__(name, func)
        self.state = EncounterState.BEFORE_COMBAT
        self.combat_controller = CombatController()

    def execute(self: Self, delta: float) -> bool:
        match self.state:
            case EncounterState.BEFORE_COMBAT:
                if combat_manager.encounter_done is False:
                    self.state = EncounterState.COMBAT
            case EncounterState.COMBAT:
                if combat_manager.encounter_done is True:
                    self.state = EncounterState.POST_COMBAT
                else:
                    self.combat_controller.execute_combat()
            case EncounterState.POST_COMBAT:
                ctrl = sos_ctrl()
                ctrl.set_neutral()
                ctrl.toggle_confirm(False)
                return True

        return False

    def __repr__(self: Self) -> str:
        return f"Executing single Combat Sequence ({self.name})."


class SeqCombatAndMove(SeqMove):
    _TOGGLE_TIME = 0.05

    def __init__(
        self: Self,
        name: str,
        coords: list[Vec3 | InteractMove | HoldDirection],
        precision: float = 0.2,
        tap_rate: float = 0.1,
        running: bool = True,
        func: Callable = None,
        emergency_skip: Callable[[], bool] | None = None,
        invert: bool = False,
    ) -> None:
        super().__init__(
            name, coords, precision, tap_rate, running, func, emergency_skip, invert
        )
        self.combat_controller = CombatController()
        self.encounter_done = True

    # Override
    def navigate_to_checkpoint(self: Self, delta: float) -> None:
        if combat_manager.encounter_done:
            # If there is no active fight, move along the designated path
            super().navigate_to_checkpoint(delta)
        elif self.encounter_done:
            ctrl = sos_ctrl()
            ctrl.set_neutral()
            ctrl.toggle_confirm(False)
        else:
            self.combat_controller.execute_combat()
        self.encounter_done = combat_manager.encounter_done

    def __repr__(self: Self) -> str:
        if combat_manager.encounter_done:
            return super().__repr__()
        return f"Executing Combat Sequence ({self.name})."
