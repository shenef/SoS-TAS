"""Bracelet puzzle sequencer node."""

import logging
from collections.abc import Callable
from typing import Self

from control import sos_ctrl
from engine.mathlib import Vec3
from engine.seq.move import MistralBracelet, SeqMoveBase
from memory import (
    player_party_manager_handle,
)

logger = logging.getLogger(__name__)

player_party_manager = player_party_manager_handle()


class SeqBraceletPuzzle(SeqMoveBase):
    """Sequence to perform a bracelet puzzle."""

    def __init__(
        self: Self,
        name: str,
        coords: list[Vec3 | MistralBracelet],
        precision: float = 0.2,
        func: Callable = None,
    ) -> None:
        # Interact variables
        super().__init__(name, func=func, coords=coords, precision=precision)

    def handle_movement(self: Self, player_pos: Vec3, target: Vec3) -> None:
        """Handle movement between block pushes."""
        # If arrived, go to next coordinate in the list

        if not self.advance_checkpoint(player_pos, target):
            self.move_function(player_pos=player_pos, target_pos=target)

    def navigate_to_checkpoint(self: Self, delta: float) -> None:
        """Handle pushing blocks."""
        # Move towards target
        target = self.get_target()
        if target is None:
            return

        player_pos = self.player_position()
        if player_pos.x is None:
            return

        if isinstance(target, MistralBracelet):
            ctrl = sos_ctrl()
            ctrl.set_joystick(target.joy_dir)
            if self.update_timer(delta, target.timeout_s):
                ctrl.set_neutral()
                ctrl.bracelet()
                self.next_step()
        else:
            self.handle_movement(player_pos, target)

    def execute(self: Self, delta: float) -> bool:
        """Top level execution function, called by Sequencer."""
        done = super().execute(delta)
        if done:
            logger.info(f"Finished block puzzle section: {self.name}")
        return done
