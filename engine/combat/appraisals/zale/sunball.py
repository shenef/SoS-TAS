import logging
from datetime import datetime, timedelta
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
from memory.combat_manager import CombatDamageType

logger = logging.getLogger(__name__)


class Sunball(SoSAppraisal):
    def __init__(
        self: Self,
        value: float = 0.0,
        hold_time: float = 4.0,
        timing_type: SoSTimingType = SoSTimingType.Charge,
        boost: int = 0,
        skill_command_index: int = 1,
    ) -> None:
        super().__init__(
            name="Sunball",
            internal_name="Sunball",
            boost=boost,
            timing_type=timing_type,
            battle_command=SoSBattleCommand.Skill,
        )
        self.value = value
        self.target_type = SoSTargetType.Enemy
        self.damage_type = [CombatDamageType.Sun]
        # this needs to move to a system that tracks available abilities.
        # May take significant work to determine this unless we do it manually.
        # This ability is 2nd index until you learn dash strike.. then it's 3rd.
        self.skill_command_index = skill_command_index
        self.ability_time: datetime = None
        self.resource = SoSResource.Mana
        self.hold_time = hold_time
        self.cost = 8  # add modifier for mana cost reduction?

    def execute_timing_sequence(self: Self) -> None:
        if self.ability_time is None:
            ability_timing = timedelta(seconds=self.hold_time)
            self.ability_time = datetime.utcnow() + ability_timing
        else:
            sos_ctrl().toggle_confirm(True)
            if self.ability_time <= datetime.utcnow():
                sos_ctrl().toggle_confirm(False)
                logger.debug(f"Executing Timing Attack, Charge ({self.name})")
                self.step = SoSAppraisalStep.ActionComplete
