import logging
from typing import Self

from engine.combat.utility.sos_appraisal import (
    SoSAppraisal,
    SoSBattleCommand,
    SoSTargetType,
    SoSTimingType,
)

logger = logging.getLogger(__name__)


class BasicAttack(SoSAppraisal):
    def __init__(
        self: Self, timing_type: SoSTimingType = SoSTimingType.OneHit, boost: int = 0
    ) -> None:
        super().__init__(
            name="Attack",
            boost=boost,
            timing_type=timing_type,
            battle_command=SoSBattleCommand.Attack,
        )
        self.target_type = SoSTargetType.Enemy
