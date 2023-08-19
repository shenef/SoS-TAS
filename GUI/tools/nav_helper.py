import logging

import imgui

from engine.mathlib import Vec3
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
            pass
        if imgui.button("Cancel navigation"):
            pass

        imgui.set_window_size(190, 210, condition=imgui.FIRST_USE_EVER)

        ret = False
        if not top_level and imgui.button("Back"):
            ret = True
        self.window.end_window()
        return ret
