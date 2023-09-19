# Libraries and Core Files
import datetime
import logging
import time
from typing import Self

import imgui

from app import TAS_VERSION_STRING
from control import sos_ctrl
from engine.seq.base import SeqBase
from GUI import Window

logger = logging.getLogger(__name__)


class SequencerEngine:
    """
    Engine for executing sequences of generic TAS events.
    Each event sequence can be nested using SeqList.
    """

    def __init__(self: Self, window: Window, config: dict, root: SeqBase) -> None:
        self.window = window
        self.root = root
        self.done = False
        self.config = config
        self.paused = False
        self.timestamp = time.time()

    def reset(self: Self) -> None:
        self.paused = False
        self.done = False
        self.root.reset()

    def advance_to_checkpoint(self: Self, checkpoint: str) -> bool:
        return self.root.advance_to_checkpoint(checkpoint=checkpoint)

    def pause(self: Self) -> None:
        ctrl = sos_ctrl()
        # Restore controls to neutral state
        ctrl.dpad.none()
        ctrl.set_neutral()
        ctrl.release_buttons()
        self.paused = True
        logger.info("------------------------")
        logger.info("  TAS EXECUTION PAUSED  ")
        logger.info("------------------------")

    def unpause(self: Self) -> None:
        self.paused = False
        self.timestamp = time.time()
        logger.info("------------------------")
        logger.info(" TAS EXECUTION RESUMING ")
        logger.info("------------------------")

    def _get_deltatime(self: Self) -> float:
        now = time.time()
        delta = now - self.timestamp
        self.timestamp = now
        return delta

    def _update(self: Self) -> None:
        # Execute current gamestate logic
        if not self.paused:
            delta = self._get_deltatime()
            self.done = self.root.execute(delta=delta)

    def _print_timer(self: Self) -> None:
        # Timestamp
        start_time = logging._startTime
        now = time.time()
        elapsed = now - start_time
        duration = datetime.datetime.utcfromtimestamp(elapsed)
        timestamp = f"{duration.strftime('%H:%M:%S')}.{int(duration.strftime('%f')) // 1000:03d}"
        pause_str = " == PAUSED ==" if self.paused else ""
        imgui.text_wrapped(f"Time: {timestamp}{pause_str}")

    def _render(self: Self) -> None:
        imgui.text_wrapped(f"TAS version: {TAS_VERSION_STRING} |")
        imgui.same_line()
        # Render timer and gamestate tree
        self._print_timer()
        imgui.text_wrapped(f"Gamestate:\n  {self.root}")

        if imgui.button("Pause"):
            if self.paused:
                self.unpause()
            else:
                self.pause()
        # Render the current gamestate
        self.root.render()

    # Execute and render TAS progress
    def run(self: Self) -> bool:
        self._update()
        self._render()

        return False
