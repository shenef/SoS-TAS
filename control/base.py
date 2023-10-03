# Libraries and Core Files
import logging
from enum import IntEnum, auto
from typing import Self

import vgamepad as vg

logger = logging.getLogger(__name__)


class Buttons(IntEnum):
    DPAD = auto()
    TRIG_L = auto()
    TRIG_R = auto()
    BACK = auto()
    START = auto()
    A = auto()
    B = auto()
    X = auto()
    Y = auto()
    SHOULDER_L = auto()
    SHOULDER_R = auto()


class VgTranslator:
    def __init__(self: Self) -> None:
        logger.info("Setting up emulated Xbox360 controller.")
        self.gamepad = vg.VX360Gamepad()

    def _set_dpad(self: Self, value: int) -> None:
        if value == 1:  # d_pad up
            self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
        elif value == 2:  # d_pad down  # noqa: PLR2004
            self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
        elif value == 4:  # d_pad left  # noqa: PLR2004
            self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
        elif value == 8:  # d_pad right  # noqa: PLR2004
            self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
        elif value == 0:
            self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
            self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
            self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
            self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)

    def set_button(self: Self, x_key: Buttons, value: int | float) -> None:
        match x_key:
            # Dpad movement
            case Buttons.DPAD:
                self._set_dpad(value)
            # Trigger buttons
            case Buttons.TRIG_L:
                self.gamepad.left_trigger_float(value_float=value)
            case Buttons.TRIG_R:
                self.gamepad.right_trigger_float(value_float=value)
            # Buttons
            case Buttons.BACK:
                if value != 0:
                    self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)
                else:
                    self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)
            case Buttons.START:
                if value != 0:
                    self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
                else:
                    self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
            case Buttons.A:
                if value != 0:
                    self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
                else:
                    self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
            case Buttons.B:
                if value != 0:
                    self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
                else:
                    self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
            case Buttons.X:
                if value != 0:
                    self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
                else:
                    self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
            case Buttons.Y:
                if value != 0:
                    self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
                else:
                    self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
            case Buttons.SHOULDER_L:
                if value != 0:
                    self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
                else:
                    self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
            case Buttons.SHOULDER_R:
                if value != 0:
                    self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
                else:
                    self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
        # Update state of gamepad
        self.gamepad.update()
        # For additional details, review this website:
        # https://pypi.org/project/vgamepad/

    def set_joystick(self: Self, x: float, y: float) -> None:
        x = min(x, 1)
        x = max(x, -1)
        y = min(y, 1)
        y = max(y, -1)
        try:
            self.gamepad.left_joystick_float(x_value_float=x, y_value_float=y)
            self.gamepad.update()
        except Exception:
            logger.exception()

    def set_neutral(self: Self) -> None:
        self.gamepad.left_joystick_float(x_value_float=0, y_value_float=0)
        self.gamepad.update()


_controller = VgTranslator()


def handle() -> VgTranslator:
    return _controller
