"""GUI window for showing utility decisions."""

import logging
from typing import Self

from imgui_bundle import imgui

from engine.combat.utility.sos_appraisal import get_utility_log
from GUI.GUI import Window
from GUI.menu import Menu

logger = logging.getLogger(__name__)


class UtilityHelper(Menu):
    """GUI window for showing utility decisions."""

    def __init__(self: Self, window: Window) -> None:
        """Initialize an UtilityHelper object."""
        super().__init__(window, title="Utility helper")

    def execute(self: Self, top_level: bool) -> bool:
        self.window.start_window(self.title)

        imgui.set_window_pos(self.title, imgui.ImVec2(5, 110), imgui.Cond_.first_use_ever)
        imgui.set_window_size(imgui.ImVec2(240, 410), cond=imgui.Cond_.first_use_ever)
        imgui.set_window_collapsed(1, cond=imgui.Cond_.once)

        imgui.begin_child("scroll_area")

        for entry in get_utility_log():
            imgui.text(f"[{entry.appraisal.value}] {entry.character.name}: {entry.appraisal}")

        ret = False
        if not top_level and imgui.button("Back"):
            ret = True
        imgui.end_child()

        self.window.end_window()
        return ret
