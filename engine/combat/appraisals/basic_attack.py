import logging
from typing import Self

from engine.combat.utility.sos_appraisal import (
    SoSAppraisal,
    SoSBattleCommand,
    SoSTargetType,
    SoSTimingType,
)
from memory.combat_manager import CombatDamageType

logger = logging.getLogger(__name__)


class BasicAttack(SoSAppraisal):
    def __init__(
        self: Self,
        timing_type: SoSTimingType = SoSTimingType.OneHit,
        boost: int = 0,
        primary_damage_type: CombatDamageType = CombatDamageType.NONE,
        secondary_damage_type: CombatDamageType = CombatDamageType.NONE,
    ) -> None:
        super().__init__(
            name="Attack",
            boost=boost,
            timing_type=timing_type,
            battle_command=SoSBattleCommand.Attack,
        )
        self.target_type = SoSTargetType.Enemy
        self.damage_type = [
            primary_damage_type,
            primary_damage_type,
        ]
        if secondary_damage_type != CombatDamageType.NONE:
            self.damage_type.append(secondary_damage_type)
