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


class SolsticeStrike(ComboSkill):
    """Solstice Strike appraisal."""

    def __init__(
        self: Self,
        main_caster: PlayerPartyCharacter,
        value: float = 0.0,
        boost: int = 0,
    ) -> None:
        super().__init__(
            name="Solstice Strike",
            timing_type=SoSTimingType.OneHit,
            boost=boost,
            casters=[PlayerPartyCharacter.Valere, PlayerPartyCharacter.Zale],
            combo_cost=1,
        )
        self.damage_type = [
            CombatDamageType.Blunt,
            CombatDamageType.Blunt,
            CombatDamageType.Sword,
            CombatDamageType.Sword,
        ]
        if self.boost >= 1:
            match main_caster:
                case PlayerPartyCharacter.Valere:
                    self.damage_type.append(CombatDamageType.Moon)
                case PlayerPartyCharacter.Zale:
                    self.damage_type.append(CombatDamageType.Sun)
        self.skill_command_index = 0
        self.target_type = SoSTargetType.Enemy
        self.value = value
        self.battle_command_targeting_type = SoSBattleCommand.Attack
