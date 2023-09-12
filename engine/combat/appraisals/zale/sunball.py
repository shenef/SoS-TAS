import logging
from datetime import datetime, timedelta

from control import sos_ctrl
from engine.combat.utility.sos_appraisal import (
    SoSAppraisal,
    SoSAppraisalStep,
    SoSBattleCommand,
    SoSTargetType,
    SoSTimingType,
)

logger = logging.getLogger(__name__)


class Sunball(SoSAppraisal):
    def __init__(self, value: int = 0):
        super().__init__()
        self.value = value
        self.timing_type = SoSTimingType.Charge
        self.battle_command = SoSBattleCommand.Skill
        self.target_type = SoSTargetType.Enemy
        # this needs to move to a system that tracks available abilities.
        # May take significant work to determine this unless we do it manually.
        # This ability is 2nd index until you learn dash strike.. then it's 3rd.
        self.skill_command_index = 2
        self.ability_time = None

    def execute_timing_sequence(self):
        if self.ability_time is None:
            # set current time + 3.6 seconds
            ability_timing = timedelta(seconds=3.8)
            self.ability_time = datetime.utcnow() + ability_timing

        else:
            sos_ctrl().toggle_confirm(True)
            if self.ability_time <= datetime.utcnow():
                sos_ctrl().toggle_confirm(False)
                logger.debug("Executing Timing Attack")
                self.step = SoSAppraisalStep.ActionComplete
