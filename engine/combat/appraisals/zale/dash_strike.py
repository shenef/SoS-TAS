import logging
from typing import Self

from engine.combat.utility.sos_appraisal import (
    SoSAppraisal,
    SoSBattleCommand,
    SoSResource,
    SoSTargetType,
    SoSTimingType,
)
from memory.combat_manager import CombatDamageType

logger = logging.getLogger(__name__)


class DashStrike(SoSAppraisal):
    def __init__(
        self: Self,
        value: int = 0,
        timing_type: SoSTimingType = SoSTimingType.OneHit,
        boost: int = 0,
    ) -> None:
        super().__init__(
            name="Dash Strike",
            boost=boost,
            timing_type=timing_type,
            battle_command=SoSBattleCommand.Skill,
        )
        self.value = value
        # TODO(orkaboy): SoSTargetType.AllEnemies
        # no such target type exists but there are a couple cases where something like
        # `AllEnemies`, `AllPlayers` and just `All` could be useful
        self.target_type = SoSTargetType.Enemy
        self.damage_type = [CombatDamageType.Sword, CombatDamageType.Sun]
        self.skill_command_index = 1
        self.resource = SoSResource.Mana
        self.cost = 8
