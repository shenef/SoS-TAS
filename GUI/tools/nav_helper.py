import logging
import time

import imgui

from control import sos_ctrl
from engine.mathlib import Quaternion, Vec2, Vec3
from engine.seq.move import move_to
from GUI.GUI import GUI_helper, Window
from GUI.menu import Menu
from memory.boat_manager import boat_manager_handle
from memory.player_party_manager import player_party_manager_handle
from memory.title_sequence_manager import title_sequence_manager_handle

logger = logging.getLogger(__name__)

player_party_manager = player_party_manager_handle()
boat_manager = boat_manager_handle()
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

        imgui.set_window_position(0, 80, condition=imgui.FIRST_USE_EVER)
        imgui.set_window_size(240, 410, condition=imgui.FIRST_USE_EVER)
        imgui.set_window_collapsed(1, condition=imgui.ONCE)

        mstate_v = player_party_manager.movement_state.value
        mstate_m = player_party_manager.movement_state.name

        player_pos = Vec3(
            player_party_manager.position.x or 0,
            player_party_manager.position.y or 0,
            player_party_manager.position.z or 0,
        )

        gameobject_pos = Vec3(
            player_party_manager.gameobject_position.x or 0,
            player_party_manager.gameobject_position.y or 0,
            player_party_manager.gameobject_position.z or 0,
        )

        imgui.text(f"Movement State: {mstate_m} ({mstate_v})")

        GUI_helper.add_spacer()

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
                imgui.core.set_clipboard_text(
                    f"Vec3({player_pos.x:.3f}, {player_pos.y:.3f}, {player_pos.z:.3f}),"
                )
            GUI_helper.add_spacings(2)

        ui_target_coordinates, visible = imgui.collapsing_header(
            "Target Coordinates", True, flags=32
        )
        if ui_target_coordinates and visible:
            _, self.target.x = imgui.input_float(
                label="x", value=self.target.x, step=0.001
            )
            _, self.target.y = imgui.input_float(
                label="y", value=self.target.y, step=0.001
            )
            _, self.target.z = imgui.input_float(
                label="z", value=self.target.z, step=0.001
            )

            distance = Vec3.dist(self.target, player_pos)
            imgui.text(f"Distance to target: {distance:.3f}\n")

            if imgui.button("Copy to clipboard##2"):
                imgui.core.set_clipboard_text(
                    f"Vec3({self.target.x:.3f}, {self.target.y:.3f}, {self.target.z:.3f}),"
                )

        GUI_helper.add_spacer()

        _, self.precision = imgui.slider_float("Precision", self.precision, 0.001, 1.0)
        if imgui.is_item_hovered():
            imgui.set_tooltip("Set the navigation precision\nCTRL+Click to edit")

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

        GUI_helper.add_spacer()

        ui_gameobject_coordinates, visible = imgui.collapsing_header(
            "GameObject Coordinates", True
        )
        if ui_gameobject_coordinates and visible:
            imgui.text(f"x: {gameobject_pos.x:.3f}")
            imgui.text(f"y: {gameobject_pos.y:.3f}")
            imgui.text(f"z: {gameobject_pos.z:.3f}")
            GUI_helper.add_spacings(2)

        ui_boat_coordinates, visible = imgui.collapsing_header("Boat Coordinates", True)
        boat_pos = Vec3(
            boat_manager.position.x or 0,
            boat_manager.position.y or 0,
            boat_manager.position.z or 0,
        )
        boat_rotation = Quaternion(
            boat_manager.rotation.x or 0,
            boat_manager.rotation.y or 0,
            boat_manager.rotation.z or 0,
            boat_manager.rotation.w or 0,
        )
        if ui_boat_coordinates and visible:
            imgui.text(f"x: {boat_pos.x:.3f}")
            imgui.text(f"y: {boat_pos.y:.3f}")
            imgui.text(f"z: {boat_pos.z:.3f}")
            imgui.text(f"Rot x: {boat_rotation.x:.3f}")
            imgui.text(f"Rot y: {boat_rotation.y:.3f}")
            imgui.text(f"Rot z: {boat_rotation.z:.3f}")
            imgui.text(f"Rot w: {boat_rotation.w:.3f}")
            imgui.text(f"speed: {boat_manager.speed:.3f}/{boat_manager.max_speed:.3f}")

        ret = False
        if not top_level and imgui.button("Back"):
            ret = True
        self.window.end_window()
        return ret
