import logging
import time

import imgui

from GUI.GUI import Window

logger = logging.getLogger(__name__)


class Menu:
    def __init__(self, window: Window, title: str, children: list = None) -> None:
        if children is None:
            children = []
        self.window = window
        self.title = title
        self.children = children
        self.active = None

    # Return True when done
    def execute(self, top_level: bool) -> bool:
        self.window.start_window(self.title)
        for child in self.children:
            if imgui.button(child.title):
                self.active = child
        ret = False
        if not top_level:
            if imgui.button("Back"):
                ret = True
        self.window.end_window()
        return ret

    def run(self, top_level: bool = False) -> bool:
        if self.active is None:
            return self.execute(top_level)
        else:
            done = self.active.run()
            if done:
                self.active = None
        return False


class MenuManager:
    def __init__(self, window: Window, root_menues: list[Menu]) -> None:
        self.window = window
        self.root_menues = root_menues

    def run(self) -> None:
        while self.window.is_open():
            self.window.start_frame()
            for menu in self.root_menues:
                menu.run(top_level=True)
            self.window.end_frame()
            time.sleep(0.008333333)