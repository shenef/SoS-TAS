import logging
from typing import Self

from engine.combat.utility.sos_appraisal import (
    SoSAppraisal,
    SoSBattleCommand,
    SoSResource,
    SoSTargetType,
    SoSTimingType,
)
from memory.combat_manager import CombatDamageType, CombatEnemyTarget

logger = logging.getLogger(__name__)


class Disorient(SoSAppraisal):
    def __init__(
        self: Self,
        value: float = 0.0,
        timing_type: SoSTimingType = SoSTimingType.OneHit,
        boost: int = 0,
    ) -> None:
        super().__init__(
            name="Disorient",
            boost=boost,
            timing_type=timing_type,
            battle_command=SoSBattleCommand.Skill,
        )
        self.value = value
        self.target_type = SoSTargetType.Enemy
        self.damage_type = [CombatDamageType.Blunt, CombatDamageType.Poison]
        self.battle_command_targeting_type = SoSBattleCommand.Attack
        self.skill_command_index = 1
        self.resource = SoSResource.Mana
        self.cost = 7

    def adjust_value(self: Self, enemy: CombatEnemyTarget) -> None:
        """Heavily reduce utility value if enemy has already taken action."""
        if enemy.turns_to_action == 0:
            self.value *= 0.1
