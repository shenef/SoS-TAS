# Libraries and Core Files
import time
from typing import Self

from control import sos_ctrl
from engine.seq.base import SeqBase


def wait_seconds(seconds: float) -> None:
    time.sleep(seconds)


class SeqDelay(SeqBase):
    def __init__(self: Self, name: str, timeout_in_s: float) -> None:
        self.timer = 0.0
        self.timeout = timeout_in_s
        super().__init__(name)

    def reset(self: Self) -> None:
        self.timer = 0.0
        return super().reset()

    def execute(self: Self, delta: float) -> bool:
        self.timer = self.timer + delta
        if self.timer >= self.timeout:
            self.timer = self.timeout
            return True
        return False

    def __repr__(self: Self) -> str:
        return f"Waiting ({self.name}). {self.timer:.2f}/{self.timeout:.2f}"


class SeqHoldConfirm(SeqDelay):
    def execute(self: Self, delta: float) -> bool:
        self.timer += delta
        sos_ctrl().toggle_confirm(state=True)
        # Wait out any cutscene/pickup animation
        done = self.timer >= self.timeout
        if done:
            sos_ctrl().toggle_confirm(state=False)
        return done

    def __repr__(self: Self) -> str:
        return f"Holding confirm while waiting ({self.name}). {self.timer:.2f}/{self.timeout:.2f}"


class SeqMashDelay(SeqDelay):
    def execute(self: Self, delta: float) -> bool:
        self.timer += delta
        sos_ctrl().confirm(tapping=True)
        # Wait out any cutscene/pickup animation
        return self.timer >= self.timeout

    def __repr__(self: Self) -> str:
        return f"Mashing confirm while waiting ({self.name}). {self.timer:.2f}/{self.timeout:.2f}"


class SeqTurboMashDelay(SeqDelay):
    # Mash through cutscene while holding the turbo button
    def execute(self: Self, delta: float) -> bool:
        self.timer += delta
        sos_ctrl().toggle_turbo(state=True)
        sos_ctrl().confirm(tapping=True)
        done = self.timer >= self.timeout
        if done:
            sos_ctrl().toggle_turbo(state=False)
        return done

    def __repr__(self: Self) -> str:
        return f"Mashing confirm while waiting ({self.name}). {self.timer:.2f}/{self.timeout:.2f}"
