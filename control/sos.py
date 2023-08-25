# Libraries and Core Files
import logging
import time
from enum import IntEnum

from control.base import Buttons as VgButtons
from control.base import VgTranslator
from control.base import handle as ctrl_handle
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
    def __init__(self, delay: float):
        self.ctrl = ctrl_handle()
        self.delay = delay  # In seconds
        self.dpad = self.DPad(ctrl=self.ctrl, delay=self.delay)

    # Wrappers
    def set_button(self, x_key: Buttons, value):
        self.ctrl.set_button(x_key, value)

    def set_joystick(self, direction: Vec2):
        self.ctrl.set_joystick(direction.x, direction.y)

    def set_neutral(self):
        self.ctrl.set_neutral()

    class DPad:
        def __init__(self, ctrl: VgTranslator, delay: float):
            self.ctrl = ctrl
            self.delay = delay

        def up(self):
            self.ctrl.set_button(x_key=VgButtons.DPAD, value=1)

        def down(self):
            self.ctrl.set_button(x_key=VgButtons.DPAD, value=2)

        def left(self):
            self.ctrl.set_button(x_key=VgButtons.DPAD, value=4)

        def right(self):
            self.ctrl.set_button(x_key=VgButtons.DPAD, value=8)

        def none(self):
            self.ctrl.set_button(x_key=VgButtons.DPAD, value=0)

        def tap_up(self):
            self.up()
            time.sleep(self.delay)
            self.none()
            time.sleep(self.delay)

        def tap_down(self):
            self.down()
            time.sleep(self.delay)
            self.none()
            time.sleep(self.delay)

        def tap_left(self):
            self.left()
            time.sleep(self.delay)
            self.none()
            time.sleep(self.delay)

        def tap_right(self):
            self.right()
            time.sleep(self.delay)
            self.none()
            time.sleep(self.delay)

    def toggle_cancel(self, state: bool):
        self.set_button(x_key=Buttons.CANCEL, value=1 if state else 0)

    def toggle_confirm(self, state: bool):
        self.set_button(x_key=Buttons.CONFIRM, value=1 if state else 0)

    def toggle_bracelet(self, state: bool):
        self.set_button(x_key=Buttons.BRACELET, value=1 if state else 0)

    def toggle_turbo(self, state: bool):
        self.set_button(x_key=Buttons.TURBO, value=1 if state else 0)

    def confirm(self, tapping=False):
        self.set_button(x_key=Buttons.CONFIRM, value=1)
        time.sleep(self.delay)
        self.set_button(x_key=Buttons.CONFIRM, value=0)
        if tapping:
            time.sleep(self.delay)

    def cancel(self, tapping=False):
        self.set_button(x_key=Buttons.CANCEL, value=1)
        time.sleep(self.delay)
        self.set_button(x_key=Buttons.CANCEL, value=0)
        if tapping:
            time.sleep(self.delay)

    def bracelet(self, tapping=False):
        self.set_button(x_key=Buttons.BRACELET, value=1)
        time.sleep(self.delay)
        self.set_button(x_key=Buttons.BRACELET, value=0)
        if tapping:
            time.sleep(self.delay)

    def menu(self, tapping=False):
        self.set_button(x_key=Buttons.MENU, value=1)
        time.sleep(self.delay)
        self.set_button(x_key=Buttons.MENU, value=0)
        if tapping:
            time.sleep(self.delay)

    def start(self, tapping=False):
        self.set_button(x_key=Buttons.PAUSE, value=1)
        time.sleep(self.delay)
        self.set_button(x_key=Buttons.PAUSE, value=0)
        if tapping:
            time.sleep(self.delay)

    def shift_left(self, tapping=False):
        self.set_button(x_key=Buttons.SHIFT_LEFT, value=1)
        time.sleep(self.delay)
        self.set_button(x_key=Buttons.SHIFT_LEFT, value=0)
        if tapping:
            time.sleep(self.delay)

    def shift_right(self, tapping=False):
        self.set_button(x_key=Buttons.SHIFT_RIGHT, value=1)
        time.sleep(self.delay)
        self.set_button(x_key=Buttons.SHIFT_RIGHT, value=0)
        if tapping:
            time.sleep(self.delay)


_controller = SoSController(delay=0.1)


def sos_ctrl():
    return _controller
