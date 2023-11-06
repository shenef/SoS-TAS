"""Block puzzle sequencer node."""

import logging
from collections.abc import Callable
from typing import Self

from imgui_bundle import imgui

from control import sos_ctrl
from engine.mathlib import Vec2, Vec3
from engine.seq.base import SeqBase
from engine.seq.move import move_to
from memory import (
    player_party_manager_handle,
)

logger = logging.getLogger(__name__)

player_party_manager = player_party_manager_handle()


class MistralBracelet:
    """Action: Use Mistral Bracelet in a given direction."""

    def __init__(self: Self, joy_dir: Vec2, timeout_s: float = 0.1) -> None:
        self.joy_dir = joy_dir
        self.timeout_s = timeout_s


class SeqBlockPuzzle(SeqBase):
    """Sequence to perform a block puzzle."""

    def __init__(
        self: Self,
        name: str,
        coords: list[Vec3 | MistralBracelet],
        precision: float = 0.2,
        func: Callable = None,
    ) -> None:
        self.step = 0
        self.coords = coords
        # Used for detecting endpoint of Vec3 movement
        self.precision = precision
        # Interact variables
        self.timer = 0
        super().__init__(name, func=func)

    def reset(self: Self) -> None:
        """Reset node."""
        self.step = 0
        self.timer = 0

    def _nav_done(self: Self) -> bool:
        num_coords = len(self.coords)
        # If we are already done with the entire sequence, terminate early
        return self.step >= num_coords

    def _move_function(self: Self, player_pos: Vec3, target_pos: Vec3) -> None:
        move_to(
            player=Vec2(player_pos.x, player_pos.z),
            target=Vec2(target_pos.x, target_pos.z),
            running=True,
            invert=False,
        )

    def _player_position(self: Self) -> Vec3:
        return player_party_manager.position

    def handle_movement(self: Self, player_pos: Vec3, target: Vec3) -> None:
        """Handle movement between block pushes."""
        # If arrived, go to next coordinate in the list
        if Vec3.is_close(player_pos, target, self.precision):
            logger.debug(
                f"Checkpoint {self.step}, "
                + f"Δ: {Vec3.dist(player_pos, target):.3f}, "
                + f"Pos: {player_pos}, "
                + f"{target}"
            )
            self.step = self.step + 1
            # Reset state variables
            self.timer = 0
        else:
            self._move_function(player_pos=player_pos, target_pos=target)

    def navigate_to_checkpoint(self: Self, delta: float) -> None:
        """Handle pushing blocks."""
        # Move towards target
        if self.step >= len(self.coords):
            return
        target = self.coords[self.step]

        player_pos = self._player_position()
        if player_pos.x is None:
            return

        if isinstance(target, MistralBracelet):
            ctrl = sos_ctrl()
            ctrl.set_joystick(target.joy_dir)
            self.timer += delta
            if self.timer >= target.timeout_s:
                self.timer = 0
                ctrl.set_neutral()
                ctrl.bracelet()
                self.step = self.step + 1
        else:
            self.handle_movement(player_pos, target)

    def execute(self: Self, delta: float) -> bool:
        """Top level execution function, called by Sequencer."""
        self.navigate_to_checkpoint(delta)

        done = self._nav_done()

        if done:
            logger.info(f"Finished block puzzle section: {self.name}")
            self._on_done()
        return done

    def _on_done(self: Self) -> None:
        sos_ctrl().set_neutral()

    def __repr__(self: Self) -> str:
        num_coords = len(self.coords)
        if self.step >= num_coords:
            return f"Block Puzzle - {self.name}[{num_coords}/{num_coords}]"
        target = self.coords[self.step]
        step = self.step + 1
        return f"Block Puzzle - {self.name}[{step}/{num_coords}]: {target}"

    def render_tree(self: Self, parent_path: str, selected: bool) -> None:
        """Render imgui tree view."""
        imgui.push_id(parent_path)
        if selected:
            imgui.push_style_color(imgui.Col_.text, imgui.ImVec4(0.1, 0.9, 0.1, 1.0))
        tree_node = imgui.tree_node_ex(
            f"{self.__class__.__name__}({self.name})", imgui.TreeNodeFlags_.span_full_width
        )
        if selected:
            imgui.pop_style_color()
        if tree_node:
            self.render_coords(selected)
            imgui.tree_pop()
        imgui.pop_id()

    def render_coords(self: Self, selected: bool) -> None:
        """Render imgui tree leaf (coords)."""
        for idx, coord in enumerate(self.coords):
            child_selected = selected and idx == self.step
            if child_selected:
                imgui.push_style_color(imgui.Col_.text, imgui.ImVec4(0.1, 0.5, 0.1, 1.0))
            imgui.tree_node_ex(
                f"[{idx}] {coord}",
                imgui.TreeNodeFlags_.no_tree_push_on_open
                | imgui.TreeNodeFlags_.leaf
                | imgui.TreeNodeFlags_.span_full_width,
            )
            if child_selected:
                imgui.pop_style_color()
