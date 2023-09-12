import logging

from engine.combat.utility.sos_appraisal import (
    SoSAppraisal,
    SoSBattleCommand,
    SoSTargetType,
    SoSTimingType,
)

logger = logging.getLogger(__name__)


class BasicAttack(SoSAppraisal):
    def __init__(self):
        super().__init__()
        self.timing_type = SoSTimingType.OneHit
        self.battle_command = SoSBattleCommand.Attack
        self.target_type = SoSTargetType.Enemy
