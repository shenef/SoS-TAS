import logging

import imgui

from GUI.GUI import GUI_helper, Window
from GUI.menu import Menu
from memory.level_manager import level_manager_handle
from memory.player_party_manager import player_party_manager_handle
from memory.title_sequence_manager import title_sequence_manager_handle

logger = logging.getLogger(__name__)

player_party_manager = player_party_manager_handle()
title_sequence_manager = title_sequence_manager_handle()
level_manager = level_manager_handle()


class DebugMenu(Menu):
    def __init__(self, window: Window) -> None:
        super().__init__(window, title="Debug menu")
        self.show_metrics = False
        self.show_test = False

    def execute(self, top_level: bool) -> bool:
        self.window.start_window(self.title)

        imgui.set_window_collapsed(1, condition=imgui.ONCE)

        imgui.text("Level Info")
        imgui.text(f"Scene Name: {level_manager.scene_name}")
        imgui.text(f"Scene GUID: {level_manager.current_level}")
        imgui.text(f"Loading: {level_manager.loading}")

        GUI_helper.add_spacer()

        title_cursor_position = title_sequence_manager.title_cursor_position
        imgui.text(
            f"Title Cursor Position: {title_cursor_position.name} ({title_cursor_position.value})"
        )

        GUI_helper.add_spacer()

        _, self.show_metrics = imgui.checkbox(
            "Show performance metrics", self.show_metrics
        )
        if self.show_metrics:
            imgui.show_metrics_window()

        _, self.show_test = imgui.checkbox("Show UI test window", self.show_test)
        if self.show_test:
            imgui.show_test_window()

        ret = False
        if not top_level and imgui.button("Back"):
            ret = True
        self.window.end_window()
        return ret
