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


class SolarRain(ComboSkill):
    """Solar Rain appraisal."""

    def __init__(
        self: Self,
        value: int,
        boost: int = 0,
    ) -> None:
        super().__init__(
            name="Solar Rain",
            timing_type=SoSTimingType.Charge,
            boost=boost,
            casters=[PlayerPartyCharacter.Zale, PlayerPartyCharacter.Garl],
            combo_cost=2,
        )
        self.damage_type = [
            CombatDamageType.Sun,
        ]
        # TODO(orkaboy): Depends on what is learned/who's in party, but 2 is minimum
        self.skill_command_index = 2
        # TODO(orkaboy): All enemies
        self.target_type = SoSTargetType.Enemy
        self.value = value
        self.battle_command_targeting_type = SoSBattleCommand.Attack
