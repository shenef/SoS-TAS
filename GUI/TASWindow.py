from typing import Self

from GUI.GUI import Window
from memory import (
    boat_manager_handle,
    combat_manager_handle,
    currency_manager_handle,
    inventory_manager_handle,
    level_manager_handle,
    level_up_manager_handle,
    mem_handle,
    new_dialog_manager_handle,
    player_party_manager_handle,
    shop_manager_handle,
    time_of_day_manager_handle,
    title_sequence_manager_handle,
)


class TASWindow(Window):
    """SoS TAS specific implementation."""

    INVENTORY_UPDATE_TIME = 0.5

    def __init__(self: Self, config: dict) -> None:
        super().__init__(config)
        self.timer = 0.0

    def update(self: Self, delta: float) -> None:
        """Update all game memory modules."""
        self.timer += delta
        mem_handle().update()
        if mem_handle().ready_for_updates:
            level_manager_handle().update()
            scene_name = level_manager_handle().scene_name
            loading = level_manager_handle().loading

            if scene_name == "TitleScreen":
                title_sequence_manager_handle().update()
            elif scene_name is not None and loading is False:
                player_party_manager_handle().update()
                time_of_day_manager_handle().update()
                level_up_manager_handle().update()
                combat_manager_handle().update()
                shop_manager_handle().update()
                new_dialog_manager_handle().update()
                # These don't need to be updated all the time
                if self.timer >= TASWindow.INVENTORY_UPDATE_TIME:
                    self.timer = 0.0
                    inventory_manager_handle().update()
                    currency_manager_handle().update()
                if "WorldMap" in scene_name:
                    boat_manager_handle().update()
