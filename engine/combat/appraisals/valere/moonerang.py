import logging
from typing import Self

from control import sos_ctrl
from engine.combat.utility.sos_appraisal import (
    SoSAppraisal,
    SoSAppraisalStep,
    SoSBattleCommand,
    SoSResource,
    SoSTargetType,
    SoSTimingType,
)
from memory.combat_manager import combat_manager_handle

logger = logging.getLogger(__name__)
combat_manager = combat_manager_handle()


class Moonerang(SoSAppraisal):
    HIT_AT_POSITION_VALUE = 0.82

    def __init__(
        self: Self,
        value: int = 0,
        timing_type: SoSTimingType = SoSTimingType.MultiHit,
        boost: int = 0,
    ) -> None:
        super().__init__(
            boost=boost, timing_type=timing_type, battle_command=SoSBattleCommand.Skill
        )
        self.value = value
        self.battle_command_targeting_type = SoSBattleCommand.Attack
        self.target_type = SoSTargetType.Enemy
        # this needs to move to a system that tracks available abilities.
        # May take significant work to determine this unless we do it manually.
        self.skill_command_index = 1
        self.instruction_done = False
        self.resource = SoSResource.Mana
        self.cost = 7

    def execute_timing_sequence(self: Self) -> None:
        if self.instruction_done is False:
            sos_ctrl().confirm()
            if combat_manager.read_projectile_hit_count() > 0:
                self.instruction_done = True
                return

        if (
            # if we jump back after a failure
            combat_manager.read_back_to_slot() is True
            # or if we kill the boss/enemy
            or combat_manager.encounter_done is True
        ):
            self.step = SoSAppraisalStep.ActionComplete

        pos = combat_manager.read_projectile_position()
        is_player = combat_manager.read_projectile_is_current_player()
        if is_player and pos >= self.HIT_AT_POSITION_VALUE:
            sos_ctrl().confirm()
