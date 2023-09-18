from collections.abc import Callable
from typing import Self

from control import sos_ctrl
from engine.mathlib import Vec3
from engine.seq.move import HoldDirection, InteractMove, SeqMove
from memory import combat_manager_handle

combat_manager = combat_manager_handle()


# TODO(orkaboy): Temporary code, moves along path, pausing while combat is active
class SeqCombatManual(SeqMove):
    def __init__(
        self: Self,
        name: str,
        coords: list[Vec3 | InteractMove | HoldDirection],
        precision: float = 0.2,
        precision2: float = 1.0,
        tap_rate: float = 0.1,
        running: bool = True,
        func: Callable = None,
        emergency_skip: Callable[[], bool] | None = None,
        invert: bool = False,
    ) -> None:
        super().__init__(
            name,
            coords,
            precision,
            precision2,
            tap_rate,
            running,
            func,
            emergency_skip,
            invert,
        )
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
            # Manual control, do nothing
            pass
        self.encounter_done = combat_manager.encounter_done
