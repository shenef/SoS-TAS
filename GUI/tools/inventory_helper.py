import logging
from typing import Self

from imgui_bundle import imgui

from engine.inventory import get_inventory_manager
from GUI.GUI import LayoutHelper, Window
from GUI.menu import Menu

logger = logging.getLogger(__name__)

inventory_manager = get_inventory_manager()


class InventoryHelper(Menu):
    def __init__(self: Self, window: Window) -> None:
        super().__init__(window, title="Inventory helper")

    def execute(self: Self, top_level: bool) -> bool:
        self.window.start_window(self.title)

        imgui.set_window_pos(self.title, imgui.ImVec2(5, 110), imgui.Cond_.first_use_ever)
        imgui.set_window_size(imgui.ImVec2(240, 410), cond=imgui.Cond_.first_use_ever)
        imgui.set_window_collapsed(1, cond=imgui.Cond_.once)

        imgui.text(f"Money: {inventory_manager.money}")
        LayoutHelper.add_spacer()

        imgui.text("Items:")
        for item, amount in inventory_manager.items.items():
            imgui.text(f"  {amount}x {item}")

        ret = False
        if not top_level and imgui.button("Back"):
            ret = True
        self.window.end_window()
        return ret
