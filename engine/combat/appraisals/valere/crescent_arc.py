import logging

from engine.combat.utility.sos_appraisal import (
    SoSAppraisal,
    SoSBattleCommand,
    SoSTargetType,
    SoSTimingType,
)

logger = logging.getLogger(__name__)


class CrescentArc(SoSAppraisal):
    def __init__(self):
        super().__init__()
        self.timing_type = SoSTimingType.OneHit
        self.battle_command = SoSBattleCommand.Skill
        self.target_type = SoSTargetType.Enemy
        # this needs to move to a system that tracks available abilities.
        # May take significant work to determine this unless we do it manually.
        self.skill_command_index = 0
