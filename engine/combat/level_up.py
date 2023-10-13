"""Code that decides the best level up path."""

import logging

from control import sos_ctrl
from memory import (
    LevelUpUpgradeType,
    level_up_manager_handle,
)

logger = logging.getLogger(__name__)

level_up_manager = level_up_manager_handle()

# Priority of stats (higher up has higher priority)
STAT_PRIORITY = [
    LevelUpUpgradeType.SkillPoint,
    LevelUpUpgradeType.MagicAttack,
    LevelUpUpgradeType.PhysicalAttack,
    LevelUpUpgradeType.HitPoint,
    LevelUpUpgradeType.MagicDefense,
    LevelUpUpgradeType.PhysicalDefense,
]


def handle_level_up() -> None:
    """Handle deciding level-ups."""
    ctrl = sos_ctrl()

    # TODO(orkaboy): Currently uses the same stat priority for all characters
    active_char = level_up_manager.current_character

    # Decide on best option
    best_option: LevelUpUpgradeType = LevelUpUpgradeType.NONE
    best_index = 99  # Not chosen
    for upgrade in level_up_manager.current_upgrades:
        considered_index = STAT_PRIORITY.index(upgrade.upgrade_type)
        if considered_index < best_index:
            best_index = considered_index
            best_option = upgrade.upgrade_type

    # Navigate to the correct option
    # TODO(orkaboy): Change this when active_index works?
    for upgrade in level_up_manager.current_upgrades:
        if upgrade.upgrade_type == best_option and upgrade.active:
            ctrl.confirm(tapping=True)
            # TODO(orkaboy): Spam?
            logger.debug(f"Selecting upgrade {upgrade.upgrade_type.name} for {active_char.name}")
            return
    # Haven't reached the desired option yet, change to next
    ctrl.dpad.tap_right()
