import logging
from typing import Self

from imgui_bundle import imgui

from GUI.GUI import LayoutHelper, Window
from GUI.menu import Menu
from memory import (
    level_manager_handle,
    level_up_manager_handle,
    new_dialog_manager_handle,
    player_party_manager_handle,
    time_of_day_manager_handle,
    title_sequence_manager_handle,
)

logger = logging.getLogger(__name__)

player_party_manager = player_party_manager_handle()
title_sequence_manager = title_sequence_manager_handle()
level_manager = level_manager_handle()
new_dialog_manager = new_dialog_manager_handle()
time_of_day_manager = time_of_day_manager_handle()
level_up_manager = level_up_manager_handle()


class DebugMenu(Menu):
    def __init__(self: Self, window: Window) -> None:
        super().__init__(window, title="Debug menu")
        self.show_metrics_window = False
        self.show_demo_window = False

    def execute(self: Self, top_level: bool) -> bool:
        self.window.start_window(self.title)

        imgui.set_window_collapsed(1, cond=imgui.Cond_.once)
        imgui.set_window_pos(self.title, imgui.ImVec2(185, 30), imgui.Cond_.first_use_ever)

        imgui.text_wrapped("Level Info")
        imgui.text_wrapped(f"Scene Name: {level_manager.scene_name}")
        imgui.text_wrapped(f"Scene GUID: {level_manager.current_level}")
        imgui.text_wrapped(f"Loading: {level_manager.loading}")
        imgui.text_wrapped(f"Time of Day: {time_of_day_manager.current_time}")
        LayoutHelper.add_spacer()
        imgui.text_wrapped("Level Up Info")
        imgui.text_wrapped(f"Level Up Screen Active: {level_up_manager.level_up_screen_active}")
        if level_up_manager.level_up_screen_active:
            imgui.text_wrapped(f"Current Character: {level_up_manager.current_character.value}")
            for option in level_up_manager.current_upgrades:
                imgui.text_wrapped(f"- {option.upgrade_type.name} Selected: {option.active}")

        LayoutHelper.add_spacer()
        imgui.text_wrapped(f"Current Leader: {player_party_manager.leader_character.value}")

        LayoutHelper.add_spacer()

        title_cursor_position = title_sequence_manager.title_cursor_position
        imgui.text_wrapped(
            f"Title Cursor Position: {title_cursor_position.name} ({title_cursor_position.value})"
        )
        left_button = title_sequence_manager.character_select_left_button
        right_button = title_sequence_manager.character_select_right_button
        imgui.text_wrapped(
            f"Left Char.: {left_button.character and left_button.character.value},"
            + f" Selected: {left_button.selected}"
        )
        imgui.text_wrapped(
            f"Right Char.: {right_button.character and right_button.character.value},"
            + f" Selected: {right_button.selected}"
        )

        LayoutHelper.add_spacer()
        imgui.text_wrapped(f"Dialog Open: {new_dialog_manager.dialog_open}")
        LayoutHelper.add_spacer()
        _, self.show_metrics_window = imgui.checkbox(
            "Show performance metrics", self.show_metrics_window
        )
        if self.show_metrics_window:
            imgui.show_metrics_window()

        _, self.show_demo_window = imgui.checkbox("Show UI demo window", self.show_demo_window)
        if self.show_demo_window:
            imgui.show_demo_window()

        imgui.show_style_selector("Default color schemes")

        ret = False
        if not top_level and imgui.button("Back"):
            ret = True
        self.window.end_window()
        return ret
