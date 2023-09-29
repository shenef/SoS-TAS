"""
TAS execution engine.

This code is the core of the TAS run, and executes a tree of
sequencer nodes (`SeqBase` and classes that inherit from it).

Each node is some kind of action for the TAS to take, and can
have varying complexity:

Some examples:

    `SeqInteract`, presses the confirm button once.
    `SeqMove`, navigates a list of game coordinates.
    `SeqList`, iterate over a list of other sequencer nodes.

`SeqList` in particular can be used to create a hierarchical tree of nodes.
"""

# Libraries and Core Files
import datetime
import logging
import time
from typing import Self

from imgui_bundle import imgui

from app import TAS_VERSION_STRING
from control import sos_ctrl
from engine.seq.base import SeqBase
from GUI import Window

logger = logging.getLogger(__name__)


class SequencerEngine:
    """
    Engine for executing sequences of generic TAS events.

    Each event sequence can be nested using `SeqList`.
    """

    def __init__(self: Self, window: Window, config: dict, root: SeqBase) -> None:
        self.window = window
        self.root = root
        self.done = False
        self.config = config
        self.paused = False
        self.timestamp = time.time()

    # TODO(orkaboy): Not really used at this point (we just create a new sequencer instead).
    def reset(self: Self) -> None:
        """Reset the sequencer."""
        self.paused = False
        self.done = False
        self.root.reset()

    def advance_to_checkpoint(self: Self, checkpoint: str) -> bool:
        """
        Advance the sequencer to a particular SeqCheckpoint in the tree.

        Can be used to load game into a particular segment of the route.
        """
        return self.root.advance_to_checkpoint(checkpoint=checkpoint)

    def pause(self: Self) -> None:
        """Pause the execution of the TAS, releasing all gamepad buttons."""
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
        """Resume execution of the TAS when paused."""
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
        """Execute current gamestate logic."""
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
        """Render the state of the sequencer in an imgui window."""
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

    def run(self: Self) -> bool:
        """Execute and render TAS progress."""
        self._update()
        self._render()

        return False
