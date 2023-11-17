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


class VespertineCannons(SoSAppraisal):
    def __init__(
        self: Self,
        value: float = 0.0,
        boost: int = 0,
    ) -> None:
        super().__init__(
            name="Vespertine Cannons",
            boost=boost,
            timing_type=SoSTimingType.OneHit,
            battle_command=SoSBattleCommand.Skill,
        )
        self.value = value
        self.target_type = SoSTargetType.Enemy
        self.damage_type = [CombatDamageType.Blunt, CombatDamageType.Sword]
        self.skill_command_index = 3
        self.resource = SoSResource.UltimateGauge
