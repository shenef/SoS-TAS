import logging
from typing import Self

from imgui_bundle import imgui

from engine.blackboard import blackboard
from GUI.GUI import Window
from GUI.menu import Menu

logger = logging.getLogger(__name__)


class BlackboardHelper(Menu):
    """Imgui window pane that prints out the blackboard."""

    def __init__(self: Self, window: Window) -> None:
        """Initialize a BlackboardHelper."""
        super().__init__(window, title="Blackboard helper")

    def execute(self: Self, top_level: bool) -> bool:
        self.window.start_window(self.title)

        imgui.set_window_pos(self.title, imgui.ImVec2(5, 110), imgui.Cond_.first_use_ever)
        imgui.set_window_size(imgui.ImVec2(240, 410), cond=imgui.Cond_.first_use_ever)
        imgui.set_window_collapsed(1, cond=imgui.Cond_.once)

        for key, value in blackboard().dict.items():
            imgui.text(f"{key}: {value}")

        ret = False
        if not top_level and imgui.button("Back"):
            ret = True
        self.window.end_window()
        return ret
