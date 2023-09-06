from collections.abc import Callable

from control.sos import sos_ctrl
from engine.combat.combat_controller import CombatController
from engine.mathlib import Vec3
from engine.seq.move import HoldDirection, InteractMove, SeqMove
from memory.combat_manager import combat_manager_handle

combat_manager = combat_manager_handle()


# TODO: Temporary code, moves along path, pausing while combat is active
class SeqCombatAndMove(SeqMove):
    _TOGGLE_TIME = 0.05

    def __init__(
        self,
        name: str,
        coords: list[Vec3 | InteractMove | HoldDirection],
        precision: float = 0.2,
        tap_rate: float = 0.1,
        running: bool = True,
        func=None,
        emergency_skip: Callable[[], bool] | None = None,
        invert: bool = False,
    ):
        super().__init__(
            name, coords, precision, tap_rate, running, func, emergency_skip, invert
        )
        self.timer = 0.0
        self.combat_controller = CombatController()
        self.encounter_done = True

    # Override
    def navigate_to_checkpoint(self, delta: float) -> None:
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

    def __repr__(self) -> str:
        return f"Executing Combat Sequence ({self.name})."
