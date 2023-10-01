"""Time-based sequencer nodes."""

# Libraries and Core Files
import logging
from math import fabs
from typing import Self

from control import sos_ctrl
from engine.seq.base import SeqBase
from memory import time_of_day_manager_handle

logger = logging.getLogger(__name__)

time_of_day_manager = time_of_day_manager_handle()


class SeqChangeTimeOfDay(SeqBase):
    TIME_EPSILON = 0.3
    FULLDAY = 24.0
    MIDDAY = 12.0

    def __init__(self: Self, name: str, time_target: float) -> None:
        super().__init__(name)
        self.time_target = time_target

    def execute(self: Self, delta: float) -> bool:
        cur_time = time_of_day_manager.current_time
        ctrl = sos_ctrl()

        # Change time
        diff_time = self.time_target - cur_time
        # Get the difference in time in 0-24 range
        adjusted_diff = diff_time if diff_time >= 0 else diff_time + self.FULLDAY
        # If diff is in range 0-12, hold RT
        if adjusted_diff < self.MIDDAY:
            ctrl.toggle_time_inc(state=True)
            ctrl.toggle_time_dec(state=False)
        # Else (diff is in range 12-24), hold LT
        else:
            ctrl.toggle_time_inc(state=False)
            ctrl.toggle_time_dec(state=True)

        # Check if done
        done = fabs(diff_time) < self.TIME_EPSILON
        if done:
            ctrl.toggle_time_inc(state=False)
            ctrl.toggle_time_dec(state=False)
            logger.info(f"Changed time of day to {self.time_target:.2f} ({self.name})")
        return done

    def __repr__(self: Self) -> str:
        cur_time = time_of_day_manager.current_time
        return f"Change Time ({self.name}). Cur: {cur_time:.2f}, Target: {self.time_target:.2f}"


class SeqDelay(SeqBase):
    """Wait for a fixed amount of time."""

    def __init__(self: Self, name: str, timeout_in_s: float) -> None:
        self.timer = 0.0
        self.timeout = timeout_in_s
        super().__init__(name)

    def reset(self: Self) -> None:
        """Reset the clock."""
        self.timer = 0.0
        return super().reset()

    def execute(self: Self, delta: float) -> bool:
        """Track timer until it expires."""
        self.timer = self.timer + delta
        if self.timer >= self.timeout:
            self.timer = self.timeout
            return True
        return False

    def __repr__(self: Self) -> str:
        return f"Waiting ({self.name}). {self.timer:.2f}/{self.timeout:.2f}"


class SeqHoldConfirm(SeqDelay):
    """Hold confirm button for a fixed period of time."""

    def execute(self: Self, delta: float) -> bool:
        self.timer += delta
        ctrl = sos_ctrl()
        ctrl.toggle_confirm(state=True)
        # Wait out any cutscene/pickup animation
        done = self.timer >= self.timeout
        if done:
            ctrl.toggle_confirm(state=False)
        return done

    def __repr__(self: Self) -> str:
        return f"Holding confirm while waiting ({self.name}). {self.timer:.2f}/{self.timeout:.2f}"


class SeqTurboMashDelay(SeqDelay):
    """Mash while holding the turbo button for a fixed period of time."""

    def execute(self: Self, delta: float) -> bool:
        self.timer += delta
        ctrl = sos_ctrl()
        ctrl.toggle_turbo(state=True)
        ctrl.confirm(tapping=True)
        done = self.timer >= self.timeout
        if done:
            ctrl.toggle_turbo(state=False)
            ctrl.toggle_confirm(state=False)
        return done

    def __repr__(self: Self) -> str:
        return f"Mashing confirm while waiting ({self.name}). {self.timer:.2f}/{self.timeout:.2f}"
