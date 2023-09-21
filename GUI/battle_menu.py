import logging
from typing import Self

import imgui

from GUI.GUI import LayoutHelper, Window
from GUI.menu import Menu
from memory import combat_manager_handle

logger = logging.getLogger(__name__)

combat_manager = combat_manager_handle()


class BattleMenu(Menu):
    # Determines the amount of columns, 4 is enough for most scenarios.
    # If there are more than 4 enemies, it'll just flow over into the player columns.
    COLUMN_MAX = 3

    def __init__(self: Self, window: Window) -> None:
        super().__init__(window, title="Battle menu")

    def execute(self: Self, top_level: bool) -> bool:
        self.window.start_window(self.title)

        imgui.set_window_collapsed(1, condition=imgui.ONCE)
        imgui.set_window_position(5, 210, condition=imgui.FIRST_USE_EVER)
        imgui.set_window_size(470, 585, condition=imgui.FIRST_USE_EVER)

        imgui.text_wrapped(f"Encounter done: {combat_manager.encounter_done} |")
        imgui.same_line()
        imgui.text_wrapped(f"Tutorial State: {combat_manager.tutorial_state.name}")
        if not combat_manager.encounter_done:
            imgui.text_wrapped(
                f"Battle Command has focus: {combat_manager.battle_command_has_focus} |"
            )
            imgui.same_line()
            imgui.text_wrapped(f"Index: {combat_manager.battle_command_index}")
            imgui.text_wrapped(
                f"Skill Command has focus: {combat_manager.skill_command_has_focus} |"
            )
            imgui.same_line()
            imgui.text_wrapped(f"Index: {combat_manager.skill_command_index}")
            imgui.text_wrapped(f"Live Mana Small: {combat_manager.small_live_mana} |")
            imgui.same_line()
            imgui.text_wrapped(f"Big: {combat_manager.big_live_mana}")
            imgui.text_wrapped(
                f"Selected Character: {combat_manager.selected_character.value}"
            )
            att_target = (
                combat_manager.selected_attack_target_guid.replace("\x00", "")
                if combat_manager.selected_attack_target_guid
                else "None"
            )
            imgui.text_wrapped(f"Attack target: {att_target}")
            skill_target = (
                combat_manager.selected_skill_target_guid.replace("\x00", "")
                if combat_manager.selected_skill_target_guid
                else "None"
            )
            imgui.text_wrapped(f"Skill target: {skill_target}")
            imgui.separator()
            imgui.text_wrapped(
                f"Moonerang Bounces: {combat_manager.projectile_hit_count} |"
            )
            imgui.same_line()
            imgui.text_wrapped(
                f"Moonerang Travel Speed: {combat_manager.projectile_speed:.0f}/75"
            )
            imgui.separator()
            imgui.columns(self.COLUMN_MAX)

            if combat_manager.enemies is not []:
                for idx, enemy in enumerate(combat_manager.enemies):
                    if not enemy.name:
                        imgui.text(f"({idx}) guid")
                        imgui.same_line()
                        imgui.input_text(f"##{idx}", value=enemy.guid)
                        LayoutHelper.add_tooltip(
                            "Enter this data in memory > mappers > enemy_name.py"
                        )
                    else:
                        imgui.text(f"{enemy.name} ({idx}):")
                    imgui.text(f"HP: {enemy.current_hp}/{enemy.max_hp}")
                    attack_targeted = (
                        enemy.unique_id == combat_manager.selected_attack_target_guid
                    )
                    skill_targeted = (
                        enemy.unique_id == combat_manager.selected_skill_target_guid
                    )

                    imgui.text_wrapped(f"pATK: {enemy.physical_attack} |")
                    imgui.same_line()
                    imgui.text_wrapped(f"mATK: {enemy.magic_attack}")
                    imgui.text_wrapped(f"pDEF: {enemy.physical_defense} |")
                    imgui.same_line()
                    imgui.text_wrapped(f"mDEF: {enemy.magic_defense}")
                    imgui.text_wrapped(f"Speed: {enemy.speed}")
                    imgui.text_wrapped(f"Attack Targeted: {attack_targeted}")
                    imgui.text_wrapped(f"Skill Targeted: {skill_targeted}")
                    imgui.text_wrapped(f"Next action: {enemy.turns_to_action}")
                    imgui.text_wrapped(f"Locks: {enemy.total_spell_locks}")

                    for lock in enemy.spell_locks:
                        imgui.bullet_text(f"{lock.name}")
                    imgui.next_column()

                columns_remaining = self.COLUMN_MAX - len(combat_manager.enemies)
                for _column in range(columns_remaining):
                    imgui.next_column()
                imgui.separator()

            if combat_manager.players is not []:
                for player in combat_manager.players:
                    imgui.text_wrapped(f"{player.character.value}:")
                    imgui.text_wrapped(f"HP: {player.current_hp} |")
                    imgui.same_line()
                    imgui.text_wrapped(f"MP: {player.current_mp}")
                    imgui.text_wrapped(f"Dead: {player.dead}")
                    imgui.text_wrapped(f"Selected: {player.selected}")
                    imgui.text_wrapped(f"Enabled: {player.enabled}")
                    imgui.text_wrapped(f"Mana Charge: {player.mana_charge_count}")

                    imgui.next_column()

                columns_remaining = self.COLUMN_MAX - len(combat_manager.players)
                for _column in range(columns_remaining):
                    imgui.next_column()
        ret = False
        if not top_level and imgui.button("Back"):
            ret = True
        self.window.end_window()
        return ret
