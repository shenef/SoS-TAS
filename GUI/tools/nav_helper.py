import logging
import time

import imgui

from control import sos_ctrl
from engine.mathlib import Vec2, Vec3
from engine.seq.move import move_to
from GUI.GUI import Window
from GUI.menu import Menu
from memory.player_party_manager import PlayerPartyManager
from memory.title_sequence_manager import TitleSequenceManager

logger = logging.getLogger(__name__)

player_party_manager = PlayerPartyManager()
title_sequence_manager = TitleSequenceManager()


class NavHelper(Menu):
    def __init__(self, window: Window) -> None:
        super().__init__(window, title="(WIP)Navigation helper")
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

        player_party_manager.update()

        imgui.text("Target Coordinates:")
        _, self.target.x = imgui.input_float(label="x", value=self.target.x, step=0.001)
        _, self.target.y = imgui.input_float(label="y", value=self.target.y, step=0.001)
        _, self.target.z = imgui.input_float(label="z", value=self.target.z, step=0.001)
        player_pos = Vec3(
            player_party_manager.position.x or 0,
            player_party_manager.position.y or 0,
            player_party_manager.position.z or 0,
        )
        distance = Vec3.dist(self.target, player_pos)
        imgui.text(f"Distance: {distance:.3f}\n")

        # TODO: Implement buttons
        if imgui.button("Set current as target"):
            self.target = player_pos

        _, self.precision = imgui.slider_float("Precision", self.precision, 0.0, 1.0)

        if imgui.button("Navigate to target"):
            self.moving = True
            self.stop = False
            self.target_locked = self.target

        imgui.same_line()
        _, self.is_run = imgui.checkbox("Run", self.is_run)
        move_speed = 1.0 if self.is_run else 0.5

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
                speed=move_speed,
            )
            if Vec3.is_close(player_pos, self.target_locked, precision=self.precision):
                self.moving = False
                sos_ctrl().set_neutral()

        imgui.set_window_size(190, 210, condition=imgui.FIRST_USE_EVER)

        if imgui.button("Copy target to clipboard"):
            imgui.core.set_clipboard_text(
                f"Vec3({self.target.x:.3f}, {self.target.y:.3f}, {self.target.z:.3f})"
            )

        ret = False
        if not top_level and imgui.button("Back"):
            ret = True
        self.window.end_window()
        return ret
