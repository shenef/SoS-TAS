"""GUI window for showing inventory contents."""

import logging
from typing import Self

from imgui_bundle import imgui

from engine.inventory import ItemType
from GUI.GUI import LayoutHelper, Window
from GUI.menu import Menu
from memory import currency_manager_handle, inventory_manager_handle

logger = logging.getLogger(__name__)

inventory_manager = inventory_manager_handle()
currency_manager = currency_manager_handle()


class InventoryHelper(Menu):
    """GUI window for showing inventory contents."""

    def __init__(self: Self, window: Window) -> None:
        """Initialize an InventoryHelper object."""
        super().__init__(window, title="Inventory helper")

    def execute(self: Self, top_level: bool) -> bool:
        self.window.start_window(self.title)

        imgui.set_window_pos(self.title, imgui.ImVec2(5, 110), imgui.Cond_.first_use_ever)
        imgui.set_window_size(imgui.ImVec2(240, 410), cond=imgui.Cond_.first_use_ever)
        imgui.set_window_collapsed(1, cond=imgui.Cond_.once)

        imgui.text(f"Money: {currency_manager.money}")
        LayoutHelper.add_spacer()

        self.show_inventory()
        self.show_unknown()

        ret = False
        if not top_level and imgui.button("Back"):
            ret = True
        self.window.end_window()
        return ret

    def show_inventory(self: Self) -> None:
        """Show the known item types, in collapsible category tabs."""
        for item_type in [
            ItemType.VALUABLE,
            ItemType.KEY,
            ItemType.WEAPON,
            ItemType.ARMOR,
            ItemType.TRINKET,
            ItemType.GROUPTRINKET,
            ItemType.FOOD,
            ItemType.RECIPE,
            ItemType.INGREDIENT,
            ItemType.RELIC,
        ]:
            items = inventory_manager.get_items_by_type(item_type)
            if len(items):
                header_open, visible = imgui.collapsing_header(item_type.name, True, flags=32)
                if header_open and visible:
                    for item_ref in items:
                        imgui.text(
                            f"{item_ref.quantity}x {item_ref.item} [{item_ref.item.order_prio}]"
                        )

    def show_unknown(self: Self) -> None:
        """Show the list of unknown items."""
        items = inventory_manager.get_items_by_type(ItemType.UNKNOWN)
        if len(items):
            header_open, visible = imgui.collapsing_header("UNKNOWN", True, flags=32)
            if header_open and visible:
                for idx, item_ref in enumerate(items):
                    imgui.text(f"({idx}) guid")
                    imgui.same_line()
                    imgui.input_text(f"##{idx}", item_ref.guid)
                    imgui.same_line()
                    imgui.text(f"x{item_ref.quantity}")
                    LayoutHelper.add_tooltip(
                        "Enter this data in engine > inventory > items > <type>.py"
                    )
