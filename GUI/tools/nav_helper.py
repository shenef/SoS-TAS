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
        self.stop = False
        self.stop_time = 0

    _PRECISION = 0.3
    _STOP_TIMEOUT = 2

    def execute(self, top_level: bool) -> bool:
        self.window.start_window(self.title)

        player_party_manager.update()

        imgui.text("Target Coordinates:")
        _, self.target.x = imgui.input_float(label="x", value=self.target.x, step=0.001)
        _, self.target.y = imgui.input_float(label="y", value=self.target.y, step=0.001)
        _, self.target.z = imgui.input_float(label="z", value=self.target.z, step=0.001)
        imgui.text("\n")

        # TODO: Implement buttons
        if imgui.button("Set current as target"):
            self.target.x = player_party_manager.position.x or 0
            self.target.y = player_party_manager.position.y or 0
            self.target.z = player_party_manager.position.z or 0
        if imgui.button("Navigate to target"):
            self.moving = True
            self.stop = False
            self.target_locked = Vec3(self.target.x, self.target.y, self.target.z)
        if imgui.button("Stop (timed)"):
            self.moving = False
            self.stop = True
            self.stop_time = time.time()

        if self.stop:
            sos_ctrl().set_neutral()
            now = time.time()
            difftime = now - self.stop_time
            imgui.same_line()
            imgui.text(f"{self._STOP_TIMEOUT - difftime:.3}")
            if difftime >= self._STOP_TIMEOUT:
                self.stop = False

        if self.moving:
            player_pos = player_party_manager.position
            move_to(
                player=Vec2(player_pos.x, player_pos.z),
                target=Vec2(self.target_locked.x, self.target_locked.z),
                precision=self._PRECISION,
            )
            if Vec3.is_close(player_pos, self.target_locked, precision=self._PRECISION):
                self.moving = False
                sos_ctrl().set_neutral()

        imgui.set_window_size(190, 210, condition=imgui.FIRST_USE_EVER)

        ret = False
        if not top_level and imgui.button("Back"):
            ret = True
        self.window.end_window()
        return ret
