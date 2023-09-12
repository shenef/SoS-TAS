# Libraries and Core Files
from collections.abc import Callable
from typing import Self

from control import sos_ctrl
from engine.seq.base import SeqBase
from memory import PlayerMovementState, player_party_manager_handle

player_party_manager = player_party_manager_handle()


class SeqInteract(SeqBase):
    def __init__(self: Self, name: str = "Interact") -> None:
        super().__init__(name)

    def execute(self: Self, delta: float) -> bool:
        sos_ctrl().confirm()
        return True


class SeqBracelet(SeqBase):
    def __init__(self: Self, name: str = "Bracelet") -> None:
        super().__init__(name)

    def execute(self: Self, delta: float) -> bool:
        sos_ctrl().bracelet()
        return True


class SeqTurboMashUntilIdle(SeqBase):
    _TOGGLE_TIME = 0.05

    def __init__(self: Self, name: str = "", func: Callable = None) -> None:
        super().__init__(name, func)
        self.state = False
        self.timer = 0.0

    # Mash through cutscene while holding the turbo button
    def execute(self: Self, delta: float) -> bool:
        self.timer = self.timer + delta

        sos_ctrl().toggle_turbo(state=True)
        if self.timer > self._TOGGLE_TIME:
            self.timer = 0
            self.state = not self.state
            sos_ctrl().toggle_confirm(self.state)

        # Check if we have control
        done = player_party_manager.movement_state == PlayerMovementState.Idle
        if done:
            sos_ctrl().toggle_turbo(state=False)
        return done

    def __repr__(self: Self) -> str:
        return f"Mashing confirm while waiting for control ({self.name})."


class SeqTurboMashSkipCutsceneUntilIdle(SeqTurboMashUntilIdle):
    # Mash through cutscene while holding the turbo button
    def execute(self: Self, delta: float) -> bool:
        ctrl = sos_ctrl()
        ctrl.toggle_cancel(state=True)
        if super().execute(delta):
            ctrl.toggle_cancel(state=False)
            return True
        return False

    def __repr__(self: Self) -> str:
        return f"Mashing confirm and holding cancel while waiting for control ({self.name})."
