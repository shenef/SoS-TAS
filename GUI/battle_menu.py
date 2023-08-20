import logging

import imgui

from GUI.GUI import Window
from GUI.menu import Menu
from memory.combat_manager import CombatManager

logger = logging.getLogger(__name__)

combat_manager = CombatManager()


class BattleMenu(Menu):
    COLUMN_MAX = 4

    def __init__(self, window: Window) -> None:
        super().__init__(window, title="Battle menu")

    def execute(self, top_level: bool) -> bool:
        self.window.start_window(self.title)
        combat_manager.update()
        imgui.text(f"Encounter Done: {combat_manager.encounter_done}")
        if not combat_manager.encounter_done:
            imgui.text(f"Small Live Mana: {combat_manager.small_live_mana}")
            imgui.text(f"Big Live Mana: {combat_manager.big_live_mana}")
            # 4 seems to be the max enemies and players on screen
            # This may change outside the demo
            imgui.columns(self.COLUMN_MAX)

            if len(combat_manager.enemies):
                for idx, e in enumerate(combat_manager.enemies):
                    imgui.text(f"Enemy {idx}:")
                    imgui.text(f"hp: {e.current_hp}")
                    imgui.text(f"next action: {e.turns_to_action}")
                    imgui.text(f"LOCKS: {e.total_spell_locks}")
                    for lock in e.spell_locks:
                        imgui.text(f"{lock.name}")
                    imgui.next_column()

                columns_remaining = self.COLUMN_MAX - len(combat_manager.enemies)
                for _r in range(columns_remaining):
                    imgui.next_column()
                imgui.separator()

            if len(combat_manager.players):
                for e in combat_manager.players:
                    imgui.text(f"{e.definition_id}")
                    imgui.text(f"hp: {e.current_hp}")
                    imgui.text(f"mp: {e.current_mp}")
                    imgui.text(f"selected: {e.selected}")
                    imgui.text(f"enabled: {e.enabled}")
                    imgui.text(f"mana charge: {e.mana_charge_count}")

                    imgui.next_column()

                columns_remaining = self.COLUMN_MAX - len(combat_manager.players)
                for _r in range(columns_remaining):
                    imgui.next_column()
        ret = False
        if not top_level and imgui.button("Back"):
            ret = True
        self.window.end_window()
        return ret
