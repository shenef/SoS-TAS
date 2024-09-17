"""GUI window for showing relics."""

import logging
from typing import Self

from imgui_bundle import imgui

from GUI.GUI import Window
from GUI.menu import Menu
from memory import title_sequence_manager_handle

logger = logging.getLogger(__name__)

title_sequence_manager = title_sequence_manager_handle()


class RelicHelper(Menu):
    """GUI window for showing relics."""

    def __init__(self: Self, window: Window) -> None:
        """Initialize an RelicHelper object."""
        super().__init__(window, title="Relic helper")

    def execute(self: Self, top_level: bool) -> bool:
        self.window.start_window(self.title)

        imgui.set_window_pos(self.title, imgui.ImVec2(5, 110), imgui.Cond_.first_use_ever)
        imgui.set_window_size(imgui.ImVec2(240, 410), cond=imgui.Cond_.first_use_ever)
        imgui.set_window_collapsed(1, cond=imgui.Cond_.once)

        imgui.begin_child("scroll_area")

        for entry in title_sequence_manager.relics:
            enabled = "[ ]"
            if entry.enabled:
                enabled = "[x]"
            imgui.text(f"{enabled} {entry.name}")

        ret = False
        if not top_level and imgui.button("Back"):
            ret = True
        imgui.end_child()

        self.window.end_window()
        return ret
