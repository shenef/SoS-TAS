import logging
import time
from typing import Self

from imgui_bundle import imgui

from control import sos_ctrl
from engine.mathlib import Quaternion, Vec2, Vec3
from engine.seq.move import move_to
from GUI.GUI import LayoutHelper, Window
from GUI.menu import Menu
from memory import (
    boat_manager_handle,
    player_party_manager_handle,
    title_sequence_manager_handle,
)

logger = logging.getLogger(__name__)

player_party_manager = player_party_manager_handle()
boat_manager = boat_manager_handle()
title_sequence_manager = title_sequence_manager_handle()


class NavHelper(Menu):
    def __init__(self: Self, window: Window) -> None:
        super().__init__(window, title="Navigation helper")
        self.target = Vec3(0, 0, 0)
        self.target_locked = Vec3(0, 0, 0)
        self.moving = False
        self.is_run = True
        self.precision = 0.2
        self.stop = False
        self.stop_time = 0

    _STOP_TIMEOUT = 2

    def execute(self: Self, top_level: bool) -> bool:
        self.window.start_window(self.title)

        imgui.set_window_pos(self.title, imgui.ImVec2(5, 110), imgui.Cond_.first_use_ever)
        imgui.set_window_size(imgui.ImVec2(240, 410), cond=imgui.Cond_.first_use_ever)
        imgui.set_window_collapsed(1, cond=imgui.Cond_.once)

        mstate_v = player_party_manager.movement_state.value
        mstate_m = player_party_manager.movement_state.name

        player_pos = player_party_manager.position or Vec3(0, 0, 0)
        gameobject_pos = player_party_manager.gameobject_position or Vec3(0, 0, 0)

        imgui.text(f"Movement State: {mstate_m} ({mstate_v})")

        LayoutHelper.add_spacer()

        ui_player_coordinates, visible = imgui.collapsing_header(
            "Player Coordinates", True, flags=32
        )
        if ui_player_coordinates and visible:
            imgui.text(f"x: {player_pos.x:.3f}")
            imgui.text(f"y: {player_pos.y:.3f}")
            imgui.text(f"z: {player_pos.z:.3f}")
            if imgui.button("Set as target"):
                self.target = player_pos
            if imgui.button("Copy to clipboard##1"):
                imgui.set_clipboard_text(
                    f"Vec3({player_pos.x:.3f}, {player_pos.y:.3f}, {player_pos.z:.3f}),"
                )
            LayoutHelper.add_spacings(2)

        ui_target_coordinates, visible = imgui.collapsing_header(
            "Target Coordinates", True, flags=32
        )
        if ui_target_coordinates and visible:
            _, self.target.x = imgui.input_float(label="x", v=self.target.x, step=0.001)
            _, self.target.y = imgui.input_float(label="y", v=self.target.y, step=0.001)
            _, self.target.z = imgui.input_float(label="z", v=self.target.z, step=0.001)

            distance = Vec3.dist(self.target, player_pos)
            imgui.text(f"Distance to target: {distance:.3f}\n")

            if imgui.button("Copy to clipboard##2"):
                imgui.set_clipboard_text(
                    f"Vec3({self.target.x:.3f}, {self.target.y:.3f}, {self.target.z:.3f}),"
                )

        LayoutHelper.add_spacer()

        _, self.precision = imgui.slider_float("Precision", self.precision, 0.001, 1.0)
        LayoutHelper.add_tooltip("Set the navigation precision\nCTRL+Click to edit")

        if imgui.button("Navigate to target"):
            self.moving = True
            self.stop = False
            self.target_locked = self.target

        imgui.same_line()
        _, self.is_run = imgui.checkbox("Run", self.is_run)

        if imgui.button("Stop (timed)"):
            self.moving = False
            self.stop = True
            self.stop_time = time.time()

        if self.stop:
            sos_ctrl().set_neutral()
            sos_ctrl().release_buttons()
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

        LayoutHelper.add_spacer()

        ui_gameobject_coordinates, visible = imgui.collapsing_header(
            "GameObject Coordinates", True, flags=32
        )
        if ui_gameobject_coordinates and visible:
            imgui.text(f"x: {gameobject_pos.x:.3f}")
            imgui.text(f"y: {gameobject_pos.y:.3f}")
            imgui.text(f"z: {gameobject_pos.z:.3f}")
            if imgui.button("Copy to clipboard##3"):
                imgui.set_clipboard_text(
                    f"Vec3({gameobject_pos.x:.3f}, {gameobject_pos.y:.3f}, {gameobject_pos.z:.3f}),"
                )
            LayoutHelper.add_spacings(2)

        ui_boat_coordinates, visible = imgui.collapsing_header("Boat Coordinates", True, flags=32)

        boat_pos = boat_manager.position or Vec3(0, 0, 0)
        boat_rotation = boat_manager.rotation or Quaternion(0, 0, 0, 0)

        if ui_boat_coordinates and visible:
            imgui.text(f"x: {boat_pos.x:.3f}")
            imgui.text(f"y: {boat_pos.y:.3f}")
            imgui.text(f"z: {boat_pos.z:.3f}")
            if imgui.button("Copy to clipboard##4"):
                imgui.set_clipboard_text(
                    f"Vec3({boat_pos.x:.3f}, {boat_pos.y:.3f}, {boat_pos.z:.3f}),"
                )
            imgui.text(f"Rot (yaw): {boat_rotation.to_yaw():.3f}")
            imgui.text(f"speed: {boat_manager.speed:.3f}/{boat_manager.max_speed:.3f}")

        ret = False
        if not top_level and imgui.button("Back"):
            ret = True
        self.window.end_window()
        return ret
