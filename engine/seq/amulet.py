import logging
import time
from typing import Self

from control import sos_ctrl
from engine.seq.base import SeqBase

logger = logging.getLogger(__name__)


class SeqAmulet(SeqBase):
    def __init__(
        self: Self,
        name: str,
    ) -> None:
        super().__init__(name)
        self.timer = 0.0
        self.complete = False
        self.steps = ["open_menu", "up_twice", "confirm", "confirm", "cancel", "exit"]
        self.delay = 0.05

    # Override
    def execute(self: Self, delta: float) -> bool:
        step = self.steps.pop(0)
        logger.debug(step)

        match step:
            case "open_menu":
                sos_ctrl().menu()
                time.sleep(0.25)
                return False
            case "up_twice":
                sos_ctrl().dpad.tap_up()
                sos_ctrl().dpad.tap_up()
                return False
            case "confirm":
                sos_ctrl().confirm()
                return False
            case "cancel":
                sos_ctrl().cancel()
                return False
            case "exit":
                sos_ctrl().cancel()
                return True
            case _:
                return False

    def __repr__(self: Self) -> str:
        return f"Amulet sequence ({self.name})."
