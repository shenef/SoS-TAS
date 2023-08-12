# Libraries and Core Files
import datetime
import logging
import time

import imgui

from app import TAS_VERSION_STRING
from control import sos_ctrl
from engine.seq.base import SeqBase
from GUI import Window
from memory.player_party_manager import PlayerPartyManager

logger = logging.getLogger(__name__)
player_party_manager = PlayerPartyManager()

class SequencerEngine:
    """
    Engine for executing sequences of generic TAS events.
    Each event sequence can be nested using SeqList.
    """

    def __init__(self, window: Window, config, root: SeqBase):
        self.window = window
        self.root = root
        self.done = False
        self.config = config
        self.paused = False
        self.timestamp = time.time()

    def reset(self) -> None:
        self.paused = False
        self.done = False
        self.root.reset()

    def advance_to_checkpoint(self, checkpoint: str) -> bool:
        return self.root.advance_to_checkpoint(checkpoint=checkpoint)

    def pause(self) -> None:
        ctrl = sos_ctrl()
        # Restore controls to neutral state
        ctrl.dpad.none()
        ctrl.set_neutral()
        self.paused = True
        logger.info("------------------------")
        logger.info("  TAS EXECUTION PAUSED  ")
        logger.info("------------------------")

    def unpause(self) -> None:
        self.paused = False
        self.timestamp = time.time()
        logger.info("------------------------")
        logger.info(" TAS EXECUTION RESUMING ")
        logger.info("------------------------")

    def _get_deltatime(self) -> float:
        now = time.time()
        delta = now - self.timestamp
        self.timestamp = now
        return delta

    def _update(self) -> None:
        time.sleep(0.008333333)
        # This should probably be moved somewhere nicer.
        player_party_manager.update()

        # Execute current gamestate logic
        if not self.paused and not self.done:
            delta = self._get_deltatime()
            self.done = self.root.execute(delta=delta)
            

    def _print_timer(self) -> None:
        # Timestamp
        start_time = logging._startTime
        now = time.time()
        elapsed = now - start_time
        duration = datetime.datetime.utcfromtimestamp(elapsed)
        timestamp = f"{duration.strftime('%H:%M:%S')}.{int(duration.strftime('%f')) // 1000:03d}"
        pause_str = " == PAUSED ==" if self.paused else ""
        imgui.text(f"[{timestamp}]{pause_str}")

    def _render(self) -> None:
        # Render timer and gamestate tree
        self._print_timer()
        imgui.text(f"Gamestate:\n  {self.root}")

        position = player_party_manager.position()
        imgui.text(
            f"Coordinates \n x: {position.x} \n y: {position.y} \n z: {position.z}"
        )

        if imgui.button("Pause"):
            if self.paused:
                self.unpause()
            else:
                self.pause()
        # Render the current gamestate
        self.root.render(window=self.window)

    def run_engine(self) -> None:
        self.pause()
        # Run sequence
        # Return current state of sequence engine (False when the game finishes)
        while self.window.is_open():
            self.run()

    # Execute and render TAS progress
    def run(self) -> None:
        self.window.start_frame()
        self.window.start_window(f"Sea of Stars TAS {TAS_VERSION_STRING}")

        if not self.done:
            self._update()
            self._render()
        self.window.end_window()
        self.window.end_frame()
