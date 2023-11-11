"""GUI window for showing shop contents."""

import logging
from typing import Self

from imgui_bundle import imgui

from GUI.GUI import LayoutHelper, Window
from GUI.menu import Menu
from memory import shop_manager_handle

logger = logging.getLogger(__name__)

shop_manager = shop_manager_handle()


class ShopHelper(Menu):
    """GUI window for showing inventory contents."""

    def __init__(self: Self, window: Window) -> None:
        """Initialize an ShopHelper object."""
        super().__init__(window, title="Shop helper")

    def execute(self: Self, top_level: bool) -> bool:
        self.window.start_window(self.title)

        imgui.set_window_pos(self.title, imgui.ImVec2(5, 110), imgui.Cond_.first_use_ever)
        imgui.set_window_size(imgui.ImVec2(240, 410), cond=imgui.Cond_.first_use_ever)
        imgui.set_window_collapsed(1, cond=imgui.Cond_.once)

        for item_ref in shop_manager.items_mapped:
            imgui.text(f"{item_ref.item} [{item_ref.item.order_prio}]")
        LayoutHelper.add_spacer()

        ret = False
        if not top_level and imgui.button("Back"):
            ret = True
        self.window.end_window()
        return ret
