"""Code that creates a imgui sub-menu handled by a Menu Manager."""

import logging
from typing import Self

from imgui_bundle import imgui

from GUI.GUI import Window

logger = logging.getLogger(__name__)


class Menu:
    """A sub-menu that can be added to a Menu Manager."""

    def __init__(self: Self, window: Window, title: str, children: list[Self] = None) -> None:
        if children is None:
            children = []
        self.window = window
        self.title = title
        self.children = children
        self.active = None

    # Return True when done
    def execute(self: Self, top_level: bool) -> bool:
        """Render the menu, drawing buttons and handling input."""
        self.window.start_window(self.title)
        imgui.set_window_pos(self.title, imgui.ImVec2(5, 5), imgui.Cond_.once)
        for child in self.children:
            if imgui.button(child.title):
                self.active = child
        ret = False
        if not top_level and imgui.button("Back"):
            ret = True
        self.window.end_window()
        return ret

    def run(self: Self, top_level: bool = False) -> bool:
        """Run main loop of the menu, potentially delegating to a submenu."""
        if self.active is None:
            return self.execute(top_level)
        done = self.active.run()
        if done:
            self.active = None
        return False


class MenuManager:
    """A manager class that is used as a container for multiple Menus."""

    def __init__(self: Self, window: Window, root_menus: list[Menu]) -> None:
        self.window = window
        self.root_menus = root_menus

    def run(self: Self) -> None:
        """Render all root sub-menus."""
        while self.window.is_open():
            self.window.start_frame()
            for menu in self.root_menus:
                menu.run(top_level=True)
            self.window.end_frame()
