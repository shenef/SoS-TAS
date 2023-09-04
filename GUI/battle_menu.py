import logging

import imgui

from GUI.GUI import Window
from GUI.menu import Menu
from memory.combat_manager import combat_manager_handle

logger = logging.getLogger(__name__)

combat_manager = combat_manager_handle()


class BattleMenu(Menu):
    # Determines the amount of columns, 4 is enough for most scenarios.
    # If there are more than 4 enemies, it'll just flow over into the player columns.
    COLUMN_MAX = 4

    def __init__(self, window: Window) -> None:
        super().__init__(window, title="Battle menu")

    def execute(self, top_level: bool) -> bool:
        self.window.start_window(self.title)

        imgui.set_window_collapsed(1, condition=imgui.ONCE)
        imgui.set_window_position(0, 420, condition=imgui.FIRST_USE_EVER)
        imgui.set_window_size(600, 300, condition=imgui.FIRST_USE_EVER)

        imgui.text(f"Encounter done: {combat_manager.encounter_done}")
        if not combat_manager.encounter_done:
            imgui.text(
                f"Battle Command has focus: {combat_manager.battle_command_has_focus}"
            )
            imgui.text(f"Battle Command Index: {combat_manager.battle_command_index}")
            imgui.text(
                f"Skill Command has focus: {combat_manager.skill_command_has_focus}"
            )
            imgui.text(f"Skill Command Index: {combat_manager.skill_command_index}")
            imgui.text(f"Small Live Mana: {combat_manager.small_live_mana}")
            imgui.text(f"Big Live Mana: {combat_manager.big_live_mana}")
            imgui.text(f"Selected Character: {combat_manager.selected_character.value}")
            imgui.separator()

            imgui.columns(self.COLUMN_MAX)

            if combat_manager.enemies is not []:
                for idx, enemy in enumerate(combat_manager.enemies):
                    imgui.text(f"Enemy {idx}:")
                    imgui.text(f"HP: {enemy.current_hp}")
                    imgui.text(f"Next action: {enemy.turns_to_action}")
                    targeted = enemy.unique_id == combat_manager.selected_target_guid
                    imgui.text(f"Targeted: {targeted}")
                    imgui.text(f"Locks: {enemy.total_spell_locks}")

                    for lock in enemy.spell_locks:
                        imgui.bullet_text(f"{lock.name}")
                    imgui.next_column()

                columns_remaining = self.COLUMN_MAX - len(combat_manager.enemies)
                for _column in range(columns_remaining):
                    imgui.next_column()
                imgui.separator()

            if combat_manager.players is not []:
                for player in combat_manager.players:
                    imgui.text(f"{player.character.value}:")
                    imgui.text(f"HP: {player.current_hp}")
                    imgui.text(f"MP: {player.current_mp}")
                    imgui.text(f"Selected: {player.selected}")
                    imgui.text(f"Enabled: {player.enabled}")
                    imgui.text(f"Mana Charge: {player.mana_charge_count}")

                    imgui.next_column()

                columns_remaining = self.COLUMN_MAX - len(combat_manager.players)
                for _column in range(columns_remaining):
                    imgui.next_column()
        ret = False
        if not top_level and imgui.button("Back"):
            ret = True
        self.window.end_window()
        return ret
