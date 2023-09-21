# Libraries and Core Files
from collections.abc import Callable
from typing import Any, Self

from control import sos_ctrl
from engine.mathlib import Vec3
from engine.seq.base import SeqBase
from memory import (
    PlayerMovementState,
    combat_manager_handle,
    player_party_manager_handle,
)

player_party_manager = player_party_manager_handle()
combat_manager = combat_manager_handle()


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


class SeqTapDown(SeqBase):
    def __init__(self: Self, name: str = "Tap down") -> None:
        super().__init__(name)

    def execute(self: Self, delta: float) -> bool:
        sos_ctrl().dpad.tap_down()
        return True


class SeqSkipUntilIdle(SeqBase):
    def __init__(
        self: Self,
        name: str,
        hold_cancel: bool = False,
        func: Callable[..., Any] = None,
    ) -> None:
        super().__init__(name, func)
        self.hold_cancel = hold_cancel

    # Hold confirm through cutscene while holding the turbo button
    def execute(self: Self, delta: float) -> bool:
        ctrl = sos_ctrl()
        ctrl.toggle_turbo(state=True)
        ctrl.toggle_confirm(state=True)
        if self.hold_cancel:
            ctrl.toggle_cancel(state=True)

        # Check if we have control
        done = self.is_done()
        if done:
            ctrl.toggle_confirm(state=False)
            ctrl.toggle_turbo(state=False)
            if self.hold_cancel:
                ctrl.toggle_cancel(state=False)
        return done

    def is_done(self: Self) -> bool:
        return player_party_manager.movement_state == PlayerMovementState.Idle

    def __repr__(self: Self) -> str:
        return f"Holding turbo/confirm/cancel while waiting for control ({self.name})."


class SeqSkipUntilClose(SeqSkipUntilIdle):
    def __init__(
        self: Self,
        name: str,
        coord: Vec3,
        precision: float = 1.0,
        hold_cancel: bool = False,
        func: Callable[..., Any] = None,
    ) -> None:
        super().__init__(name, hold_cancel, func)
        self.coord = coord
        self.precision = precision

    def is_done(self: Self) -> bool:
        player_pos = player_party_manager.position
        return Vec3.is_close(player_pos, self.coord, precision=self.precision)

    def __repr__(self: Self) -> str:
        return f"Holding turbo/confirm/cancel while waiting to arrive at {self.coord} ({self.name})."  # noqa: E501


class SeqSkipUntilCombat(SeqSkipUntilIdle):
    def is_done(self: Self) -> bool:
        return combat_manager.encounter_done is False

    def __repr__(self: Self) -> str:
        return f"Holding turbo/confirm/cancel while waiting for combat ({self.name})."


class SeqMashUntilIdle(SeqBase):
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
            sos_ctrl().toggle_confirm(state=False)
        return done

    def __repr__(self: Self) -> str:
        return f"Mashing confirm while waiting for control ({self.name})."
