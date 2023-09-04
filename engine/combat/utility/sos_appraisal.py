import logging
from enum import Enum

from engine.combat.utility.core import Appraisal

logger = logging.getLogger(__name__)


# An action that a player can take. See AppraisalType
class SoSAppraisalType(Enum):
    NONE = 0
    Basic = 1
    Skill = 2
    Combo = 3
    Item = 4


class SoSAppraisal(Appraisal):
    def __init__(self):
        super().__init__()
        self.complete = False
        self.type = SoSAppraisalType.NONE
