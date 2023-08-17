import logging

import imgui

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

    def execute(self, top_level: bool) -> bool:
        self.window.start_window(self.title)

        player_party_manager.update()

        imgui.text("Target Coordinates:")
        imgui.text("x:")
        imgui.same_line()
        imgui.input_text("", "0.000")

        imgui.text("y:")
        imgui.same_line()
        imgui.input_text("", "0.000")

        imgui.text("z:")
        imgui.same_line()
        imgui.input_text("", "0.000")

        imgui.text("\n")

        imgui.button("Set current as target")
        imgui.button("Navigate to target")
        imgui.button("Cancel navigation")

        imgui.set_window_size(190, 210)

        ret = False
        if not top_level:
            if imgui.button("Back"):
                ret = True
        self.window.end_window()
        return ret
