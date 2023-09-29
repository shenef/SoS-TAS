"""Time-based sequencer nodes."""

# Libraries and Core Files
from typing import Self

from control import sos_ctrl
from engine.seq.base import SeqBase


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
