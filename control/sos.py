# Libraries and Core Files
import logging
import time
from enum import IntEnum
from typing import Self

from control.base import Buttons as VgButtons, VgTranslator, handle as ctrl_handle
from engine.mathlib import Vec2

logger = logging.getLogger(__name__)


# Game functions
class Buttons(IntEnum):
    CONFIRM = VgButtons.A
    BRACELET = VgButtons.X
    CANCEL = VgButtons.B
    MENU = VgButtons.Y
    PAUSE = VgButtons.START
    TURBO = VgButtons.SHOULDER_R
    BOOST = VgButtons.TRIG_R
    SHIFT_LEFT = VgButtons.SHOULDER_L
    SHIFT_RIGHT = VgButtons.SHOULDER_R


class SoSController:
    def __init__(self: Self, delay: float) -> None:
        self.ctrl = ctrl_handle()
        self.delay = delay  # In seconds
        self.dpad = self.DPad(ctrl=self.ctrl, delay=self.delay)

    # Wrappers
    def set_button(self: Self, x_key: Buttons, value: int | float) -> None:
        self.ctrl.set_button(x_key, value)

    def set_joystick(self: Self, direction: Vec2) -> None:
        self.ctrl.set_joystick(direction.x, direction.y)

    def set_neutral(self: Self) -> None:
        self.ctrl.set_neutral()

    def release_buttons(self: Self) -> None:
        self.ctrl.set_button(x_key=VgButtons.A, value=0)
        self.ctrl.set_button(x_key=VgButtons.B, value=0)
        self.ctrl.set_button(x_key=VgButtons.X, value=0)
        self.ctrl.set_button(x_key=VgButtons.Y, value=0)
        self.ctrl.set_button(x_key=VgButtons.SHOULDER_L, value=0)
        self.ctrl.set_button(x_key=VgButtons.SHOULDER_R, value=0)
        self.ctrl.set_button(x_key=VgButtons.START, value=0)
        self.ctrl.set_button(x_key=VgButtons.TRIG_L, value=0)
        self.ctrl.set_button(x_key=VgButtons.TRIG_R, value=0)

    class DPad:
        def __init__(self: Self, ctrl: VgTranslator, delay: float) -> None:
            self.ctrl = ctrl
            self.delay = delay

        def up(self: Self) -> None:
            self.ctrl.set_button(x_key=VgButtons.DPAD, value=1)

        def down(self: Self) -> None:
            self.ctrl.set_button(x_key=VgButtons.DPAD, value=2)

        def left(self: Self) -> None:
            self.ctrl.set_button(x_key=VgButtons.DPAD, value=4)

        def right(self: Self) -> None:
            self.ctrl.set_button(x_key=VgButtons.DPAD, value=8)

        def none(self: Self) -> None:
            self.ctrl.set_button(x_key=VgButtons.DPAD, value=0)

        def tap_up(self: Self) -> None:
            self.up()
            time.sleep(self.delay)
            self.none()
            time.sleep(self.delay)

        def tap_down(self: Self) -> None:
            self.down()
            time.sleep(self.delay)
            self.none()
            time.sleep(self.delay)

        def tap_left(self: Self) -> None:
            self.left()
            time.sleep(self.delay)
            self.none()
            time.sleep(self.delay)

        def tap_right(self: Self) -> None:
            self.right()
            time.sleep(self.delay)
            self.none()
            time.sleep(self.delay)

    def toggle_cancel(self: Self, state: bool) -> None:
        self.set_button(x_key=Buttons.CANCEL, value=1 if state else 0)

    def toggle_confirm(self: Self, state: bool) -> None:
        self.set_button(x_key=Buttons.CONFIRM, value=1 if state else 0)

    def toggle_bracelet(self: Self, state: bool) -> None:
        self.set_button(x_key=Buttons.BRACELET, value=1 if state else 0)

    def toggle_turbo(self: Self, state: bool) -> None:
        self.set_button(x_key=Buttons.TURBO, value=1 if state else 0)

    def confirm(self: Self, tapping: bool = False) -> None:
        self.set_button(x_key=Buttons.CONFIRM, value=1)
        time.sleep(self.delay)
        self.set_button(x_key=Buttons.CONFIRM, value=0)
        if tapping:
            time.sleep(self.delay)

    def cancel(self: Self, tapping: bool = False) -> None:
        self.set_button(x_key=Buttons.CANCEL, value=1)
        time.sleep(self.delay)
        self.set_button(x_key=Buttons.CANCEL, value=0)
        if tapping:
            time.sleep(self.delay)

    def bracelet(self: Self, tapping: bool = False) -> None:
        self.set_button(x_key=Buttons.BRACELET, value=1)
        time.sleep(self.delay)
        self.set_button(x_key=Buttons.BRACELET, value=0)
        if tapping:
            time.sleep(self.delay)

    def menu(self: Self, tapping: bool = False) -> None:
        self.set_button(x_key=Buttons.MENU, value=1)
        time.sleep(self.delay)
        self.set_button(x_key=Buttons.MENU, value=0)
        if tapping:
            time.sleep(self.delay)

    def start(self: Self, tapping: bool = False) -> None:
        self.set_button(x_key=Buttons.PAUSE, value=1)
        time.sleep(self.delay)
        self.set_button(x_key=Buttons.PAUSE, value=0)
        if tapping:
            time.sleep(self.delay)

    def shift_left(self: Self, tapping: bool = False) -> None:
        self.set_button(x_key=Buttons.SHIFT_LEFT, value=1)
        time.sleep(self.delay)
        self.set_button(x_key=Buttons.SHIFT_LEFT, value=0)
        if tapping:
            time.sleep(self.delay)

    def shift_right(self: Self, tapping: bool = False) -> None:
        self.set_button(x_key=Buttons.SHIFT_RIGHT, value=1)
        time.sleep(self.delay)
        self.set_button(x_key=Buttons.SHIFT_RIGHT, value=0)
        if tapping:
            time.sleep(self.delay)


_controller = SoSController(delay=0.1)


def sos_ctrl() -> SoSController:
    return _controller
