# Libraries and Core Files
from collections.abc import Callable
from enum import Enum, auto
from math import fabs
from typing import Any, Self

from control import sos_ctrl
from engine.mathlib import Vec3
from engine.seq.base import SeqBase
from memory import (
    PlayerMovementState,
    combat_manager_handle,
    new_dialog_manager_handle,
    player_party_manager_handle,
    time_of_day_manager_handle,
)

player_party_manager = player_party_manager_handle()
combat_manager = combat_manager_handle()
new_dialog_manager = new_dialog_manager_handle()
time_of_day_manager = time_of_day_manager_handle()


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


class SeqGraplou(SeqBase):
    def __init__(self: Self, name: str = "Graplou", until_combat: bool = False) -> None:
        super().__init__(name)
        self.until_combat = until_combat

    def execute(self: Self, delta: float) -> bool:
        if self.until_combat:
            sos_ctrl().graplou(tapping=True)
            return combat_manager.encounter_done is False

        sos_ctrl().graplou()
        return True


class SeqTapDown(SeqBase):
    def __init__(self: Self, name: str = "Tap down") -> None:
        super().__init__(name)

    def execute(self: Self, delta: float) -> bool:
        sos_ctrl().dpad.tap_down()
        return True


class SeqSkipUntilIdle(SeqBase):
    TIME_EPSILON = 0.3

    def __init__(
        self: Self,
        name: str,
        hold_cancel: bool = False,
        time_target: float = None,
        func: Callable[..., Any] = None,
    ) -> None:
        super().__init__(name, func)
        self.hold_cancel = hold_cancel
        self.time_target = time_target

    # Hold confirm through cutscene while holding the turbo button
    def execute(self: Self, delta: float) -> bool:
        ctrl = sos_ctrl()
        ctrl.toggle_turbo(state=True)
        ctrl.toggle_confirm(state=True)
        if self.hold_cancel:
            ctrl.toggle_cancel(state=True)
        # Used specifically for the Elder Mist time tutorial
        if self.time_target is not None:
            ctrl.toggle_time_inc(state=True)

        # Check if we have control
        done = self.is_done()
        if done:
            ctrl.toggle_confirm(state=False)
            ctrl.toggle_turbo(state=False)
            if self.hold_cancel:
                ctrl.toggle_cancel(state=False)
            if self.time_target is not None:
                ctrl.toggle_time_inc(state=False)
        return done

    def is_done(self: Self) -> bool:
        if (
            self.time_target is not None
            and fabs(time_of_day_manager.current_time - self.time_target) < self.TIME_EPSILON
        ):
            return True
        return player_party_manager.movement_state == PlayerMovementState.Idle

    def __repr__(self: Self) -> str:
        return f"Holding turbo + confirm while waiting for control ({self.name})."


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
        return f"Holding turbo + confirm while waiting to arrive at {self.coord} ({self.name})."


class SeqSkipUntilCombat(SeqSkipUntilIdle):
    def is_done(self: Self) -> bool:
        return combat_manager.encounter_done is False

    def __repr__(self: Self) -> str:
        return f"Holding turbo + confirm while waiting for combat ({self.name})."


class SeqMashUntilIdle(SeqBase):
    _TOGGLE_TIME = 0.05

    def __init__(self: Self, name: str = "", func: Callable = None) -> None:
        super().__init__(name, func)
        self.state = False
        self.timer = 0.0

    def is_done(self: Self) -> bool:
        return player_party_manager.movement_state == PlayerMovementState.Idle

    # Mash through cutscene while holding the turbo button
    def execute(self: Self, delta: float) -> bool:
        self.timer = self.timer + delta

        ctrl = sos_ctrl()
        ctrl.toggle_turbo(state=True)
        if self.timer > self._TOGGLE_TIME:
            self.timer = 0
            self.state = not self.state
            ctrl.toggle_confirm(self.state)

        # Check if we have control
        done = self.is_done()
        if done:
            ctrl.toggle_turbo(state=False)
            ctrl.toggle_confirm(state=False)
        return done

    def __repr__(self: Self) -> str:
        return f"Mashing confirm while waiting for control ({self.name})."


class SeqMashUntilCombat(SeqSkipUntilIdle):
    def is_done(self: Self) -> bool:
        return combat_manager.encounter_done is False

    def __repr__(self: Self) -> str:
        return f"Holding turbo + mash confirm while waiting for combat ({self.name})."


class SeqSelectOption(SeqBase):
    class State(Enum):
        Approach = auto()
        WaitForDialog = auto()
        ClearPrompt = auto()
        Answer = auto()

    TIMEOUT = 0.3

    def __init__(self: Self, name: str, option: int = 0, skip_dialog_check: bool = False) -> None:
        super().__init__(name)
        self.timer = 0
        self.option = option
        self.state = self.State.Approach
        self.skip_dialog_check = skip_dialog_check

    def execute(self: Self, delta: float) -> bool:
        ctrl = sos_ctrl()
        match self.state:
            case self.State.Approach:
                ctrl.confirm()
                self.state = self.State.WaitForDialog
            case self.State.WaitForDialog:
                if new_dialog_manager.dialog_open or self.skip_dialog_check:
                    ctrl.toggle_turbo(state=True)
                    ctrl.toggle_confirm(state=True)
                    self.state = self.State.ClearPrompt
            case self.State.ClearPrompt:
                self.timer += delta
                if self.timer >= self.TIMEOUT:
                    self.state = self.State.Answer
                    ctrl.toggle_turbo(state=False)
                    ctrl.toggle_confirm(state=False)
            case self.State.Answer:
                for _ in range(self.option):
                    ctrl.dpad.tap_down()
                ctrl.confirm()
                return True
        return False

    def __repr__(self: Self) -> str:
        return f"{self.state} ({self.state})"
