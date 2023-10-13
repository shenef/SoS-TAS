import logging
from typing import Self

from engine.combat.utility.sos_appraisal import (
    SoSAppraisal,
    SoSBattleCommand,
    SoSResource,
    SoSTargetType,
    SoSTimingType,
)

logger = logging.getLogger(__name__)


class CrescentArc(SoSAppraisal):
    def __init__(
        self: Self,
        value: int = 0,
        timing_type: SoSTimingType = SoSTimingType.OneHit,
        boost: int = 0,
    ) -> None:
        super().__init__(boost=boost, timing_type=timing_type, battle_command=SoSBattleCommand.Skill)
        self.value = value
        self.target_type = SoSTargetType.Enemy
        # this needs to move to a system that tracks available abilities.
        # May take significant work to determine this unless we do it manually.
        self.skill_command_index = 0
        self.resource = SoSResource.Mana
        self.cost = 6
