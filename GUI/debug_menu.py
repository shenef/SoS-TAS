import logging

import imgui

from GUI.GUI import Window
from GUI.menu import Menu
from memory.player_party_manager import PlayerPartyManager
from memory.title_sequence_manager import TitleSequenceManager

logger = logging.getLogger(__name__)

player_party_manager = PlayerPartyManager()
title_sequence_manager = TitleSequenceManager()


class DebugMenu(Menu):
    def __init__(self, window: Window) -> None:
        super().__init__(window, title="Debug menu")

    def execute(self, top_level: bool) -> bool:
        self.window.start_window(self.title)

        imgui.set_window_collapsed(1, condition=imgui.ONCE)

        player_party_manager.update()
        title_sequence_manager.update()

        title_cursor_position = title_sequence_manager._read_title_cursor_position()
        imgui.text(
            f"\nTitle Cursor Position: {title_cursor_position.value} {title_cursor_position.name}"
        )

        ret = False
        if not top_level and imgui.button("Back"):
            ret = True
        self.window.end_window()
        return ret
