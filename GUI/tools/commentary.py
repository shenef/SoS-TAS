"""Menu window showing a scrolling log."""

import logging
import random as rnd
import time
from typing import Self

from imgui_bundle import imgui

from GUI.GUI import Window
from GUI.menu import Menu

logger = logging.getLogger(__name__)


class CommentaryAuthor:
    """Author of a commentary entry."""

    def __init__(self: Self, name: str, color: imgui.ImVec4) -> None:
        """Initialize a CommentaryAuthor object."""
        self.name = name
        self.color = color


class AUTHORS:
    """Static namespace of CommentaryAuthors."""

    tas = CommentaryAuthor(
        name="TAS", color=imgui.ImVec4(rnd.random(), rnd.uniform(0.4, 1), rnd.random(), 1.0)
    )
    orkaboy = CommentaryAuthor(name="orkaboy", color=imgui.ImVec4(0.7, 0.1, 0.5, 1.0))
    eein = CommentaryAuthor(name="Eein", color=imgui.ImVec4(1.0, 1.0, 0.0, 1.0))
    shenef = CommentaryAuthor(name="shenef", color=imgui.ImVec4(0.5, 0.0, 1.0, 1.0))


class CommentaryEntry:
    """Internal representation of a comment in the commentary log."""

    def __init__(
        self: Self, author: CommentaryAuthor, text: str, lifetime: float, delay: float
    ) -> None:
        """Initialize a CommentaryEntry object."""
        self.author = author
        self.text = text
        self.timer = 0.0
        self.delay = delay
        self.lifetime = lifetime


class CommentaryLog(Menu):
    """Menu window showing a scrolling log."""

    def __init__(self: Self, window: Window) -> None:
        """Initialize a CommentaryLog object."""
        super().__init__(window, title="Commentary Log")
        self.timestamp = time.time()

    def execute(self: Self, top_level: bool) -> bool:
        self.window.start_window(self.title)

        imgui.set_window_pos(self.title, imgui.ImVec2(5, 110), imgui.Cond_.first_use_ever)
        imgui.set_window_size(imgui.ImVec2(240, 410), cond=imgui.Cond_.first_use_ever)
        imgui.set_window_collapsed(1, cond=imgui.Cond_.once)

        imgui.begin_child("scroll_area")
        now = time.time()
        delta = now - self.timestamp
        self.timestamp = now

        log = get_commentary_log()

        for entry in log:
            entry.timer += delta
            if entry.timer >= entry.delay:
                imgui.text_colored(entry.author.color, entry.author.name)
                imgui.same_line()
                imgui.text_wrapped(entry.text)

        imgui.set_scroll_y(imgui.get_scroll_max_y())

        log[:] = [entry for entry in log if entry.timer < entry.lifetime]

        ret = False
        if not top_level and imgui.button("Back"):
            ret = True
        imgui.end_child()
        self.window.end_window()
        return ret


_commentary_log: list[CommentaryEntry] = []


def get_commentary_log() -> list[CommentaryEntry]:
    """Return a handle to the log."""
    return _commentary_log
