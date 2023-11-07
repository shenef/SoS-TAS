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


class VenomFlurry(SoSAppraisal):
    def __init__(
        self: Self,
        value: int = 0,
        timing_type: SoSTimingType = SoSTimingType.MultiHit,
        boost: int = 0,
    ) -> None:
        super().__init__(
            name="Venom Flurry",
            boost=boost,
            timing_type=timing_type,
            battle_command=SoSBattleCommand.Skill,
        )
        self.value = value
        self.target_type = SoSTargetType.Enemy
        self.damage_type = [CombatDamageType.Poison] * 10
        self.battle_command_targeting_type = SoSBattleCommand.Attack
        self.skill_command_index = 0
        self.resource = SoSResource.Mana
        self.cost = 6

    # TODO(orkaboy): Implement timing
