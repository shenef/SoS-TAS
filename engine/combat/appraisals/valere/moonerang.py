import logging
from typing import Self

from control import sos_ctrl
from engine.combat.utility.sos_appraisal import (
    SoSAppraisal,
    SoSAppraisalStep,
    SoSBattleCommand,
    SoSTargetType,
    SoSTimingType,
)
from memory.combat_manager import combat_manager_handle

logger = logging.getLogger(__name__)
combat_manager = combat_manager_handle()


class Moonerang(SoSAppraisal):
    HIT_AT_POSITION_VALUE = 0.82

    def __init__(self: Self) -> None:
        super().__init__()
        self.value = 1000
        self.timing_type = SoSTimingType.MultiHit
        self.battle_command = SoSBattleCommand.Skill
        self.target_type = SoSTargetType.Enemy
        # this needs to move to a system that tracks available abilities.
        # May take significant work to determine this unless we do it manually.
        self.skill_command_index = 1

    def execute_timing_sequence(self: Self) -> None:
        if combat_manager.read_back_to_slot() is True:
            self.step = SoSAppraisalStep.ActionComplete

        pos = combat_manager.read_projectile_position()
        is_player = combat_manager.read_projectile_is_current_player()
        if is_player and pos >= self.HIT_AT_POSITION_VALUE:
            sos_ctrl().confirm()
