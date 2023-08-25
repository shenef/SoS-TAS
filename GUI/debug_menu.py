import logging

import imgui

from GUI.GUI import Window
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

    def execute(self, top_level: bool) -> bool:
        self.window.start_window(self.title)

        imgui.text("Level Info")
        imgui.text(f"Scene Name: {level_manager.scene_name}")
        imgui.text(f"Scene GUID: {level_manager.current_level}")
        imgui.text(f"Loading: {level_manager.loading}")

        imgui.text("Player Coordinates")
        imgui.text(f"x: {player_party_manager.position.x}")
        imgui.text(f"y: {player_party_manager.position.y}")
        imgui.text(f"z: {player_party_manager.position.z}")

        title_cursor_position = title_sequence_manager.title_cursor_position
        imgui.text(
            f"\nTitle Cursor Position: {title_cursor_position.value} {title_cursor_position.name}"
        )

        mstate_v = player_party_manager.movement_state.value
        mstate_m = player_party_manager.movement_state.name
        imgui.text(f"Movement State: {mstate_v} {mstate_m}")

        ret = False
        if not top_level and imgui.button("Back"):
            ret = True
        self.window.end_window()
        return ret
