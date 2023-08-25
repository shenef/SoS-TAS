import logging
import time

import imgui

from control import sos_ctrl
from engine.mathlib import Vec2, Vec3
from engine.seq.move import move_to
from GUI.GUI import GUI_helper, Window
from GUI.menu import Menu
from memory.player_party_manager import player_party_manager_handle
from memory.title_sequence_manager import title_sequence_manager_handle

logger = logging.getLogger(__name__)

player_party_manager = player_party_manager_handle()
title_sequence_manager = title_sequence_manager_handle()


class NavHelper(Menu):
    def __init__(self, window: Window) -> None:
        super().__init__(window, title="Navigation helper")
        self.target = Vec3(0, 0, 0)
        self.target_locked = Vec3(0, 0, 0)
        self.moving = False
        self.is_run = True
        self.precision = 0.3
        self.stop = False
        self.stop_time = 0

    _STOP_TIMEOUT = 2

    def execute(self, top_level: bool) -> bool:
        self.window.start_window(self.title)

        imgui.set_window_size(190, 210, condition=imgui.FIRST_USE_EVER)

        mstate_v = player_party_manager.movement_state.value
        mstate_m = player_party_manager.movement_state.name

        player_pos = Vec3(
            player_party_manager.position.x or 0,
            player_party_manager.position.y or 0,
            player_party_manager.position.z or 0,
        )

        imgui.text(f"Movement State: {mstate_m} ({mstate_v})")

        GUI_helper.add_spacer()

        imgui.text("Player Coordinates")
        imgui.text(f"x: {player_pos.x:.3f}")
        imgui.text(f"y: {player_pos.y:.3f}")
        imgui.text(f"z: {player_pos.z:.3f}")
        if imgui.button("Set as target"):
            self.target = player_pos
        if imgui.button("Copy to clipboard"):
            imgui.core.set_clipboard_text(
                f"Vec3({player_pos.x:.3f}, {player_pos.y:.3f}, {player_pos.z:.3f}),"
            )

        distance = Vec3.dist(self.target, player_pos)
        imgui.text(f"Distance to target: {distance:.3f}\n")

        GUI_helper.add_spacer()

        imgui.text("Target Coordinates:")
        _, self.target.x = imgui.input_float(label="x", value=self.target.x, step=0.001)
        _, self.target.y = imgui.input_float(label="y", value=self.target.y, step=0.001)
        _, self.target.z = imgui.input_float(label="z", value=self.target.z, step=0.001)

        if imgui.button("Copy to clipboard"):
            imgui.core.set_clipboard_text(
                f"Vec3({self.target.x:.3f}, {self.target.y:.3f}, {self.target.z:.3f}),"
            )

        GUI_helper.add_spacer()

        if imgui.button("Navigate to target"):
            self.moving = True
            self.stop = False
            self.target_locked = self.target

        imgui.same_line()
        _, self.is_run = imgui.checkbox("Run", self.is_run)

        _, self.precision = imgui.slider_float("Precision", self.precision, 0.001, 1.0)
        if imgui.is_item_hovered():
            imgui.set_tooltip("Set the navigation precision\nCTRL+Click to edit")

        GUI_helper.add_spacer()

        if imgui.button("Stop (timed)"):
            self.moving = False
            self.stop = True
            self.stop_time = time.time()

        if self.stop:
            sos_ctrl().set_neutral()
            now = time.time()
            difftime = now - self.stop_time
            imgui.same_line()
            imgui.text(f"{self._STOP_TIMEOUT - difftime:.3f}")
            if difftime >= self._STOP_TIMEOUT:
                self.stop = False

        if self.moving:
            move_to(
                player=Vec2(player_pos.x, player_pos.z),
                target=Vec2(self.target_locked.x, self.target_locked.z),
                running=self.is_run,
            )
            if Vec3.is_close(player_pos, self.target_locked, precision=self.precision):
                self.moving = False
                sos_ctrl().set_neutral()

        ret = False
        if not top_level and imgui.button("Back"):
            ret = True
        self.window.end_window()
        return ret
