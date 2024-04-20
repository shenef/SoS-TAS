"""Base class for Combo Skill appraisals."""

import logging
from typing import Self

from engine.combat.appraisals.combos.base import ComboSkill
from engine.combat.utility.sos_appraisal import (
    SoSBattleCommand,
    SoSTargetType,
    SoSTimingType,
)
from memory.combat_manager import CombatDamageType, PlayerPartyCharacter

logger = logging.getLogger(__name__)


class XStrike(ComboSkill):
    """X-Strike appraisal."""

    def __init__(
        self: Self,
        skill_command_index: int,
        value: float = 0.0,
        boost: int = 0,
    ) -> None:
        super().__init__(
            name="X-Strike",
            internal_name="XStrike",
            timing_type=SoSTimingType.OneHit,
            boost=boost,
            casters=[PlayerPartyCharacter.Zale, PlayerPartyCharacter.Serai],
            combo_cost=2,
        )
        self.damage_type = [
            CombatDamageType.Sword,
            CombatDamageType.Poison,
            CombatDamageType.Sun,
        ]
        self.skill_command_index = skill_command_index
        # TODO(orkaboy): All enemies
        self.target_type = SoSTargetType.Enemy
        self.value = value
        self.battle_command_targeting_type = SoSBattleCommand.Attack
