import logging
from typing import Self

from engine.combat.utility.sos_appraisal import (
    SoSAppraisal,
    SoSBattleCommand,
    SoSTargetType,
    SoSTimingType,
)
from memory.combat_manager import CombatDamageType
from memory.player_party_manager import PlayerPartyCharacter

logger = logging.getLogger(__name__)


class BasicAttack(SoSAppraisal):
    def __init__(
        self: Self,
        caster: PlayerPartyCharacter,
        timing_type: SoSTimingType = SoSTimingType.OneHit,
        boost: int = 0,
    ) -> None:
        super().__init__(
            name="Attack",
            boost=boost,
            timing_type=timing_type,
            battle_command=SoSBattleCommand.Attack,
        )
        self.target_type = SoSTargetType.Enemy

        primary_damage_type: CombatDamageType = CombatDamageType.NONE
        secondary_damage_type: CombatDamageType = CombatDamageType.NONE
        match caster:
            case PlayerPartyCharacter.Zale:
                primary_damage_type = CombatDamageType.Sword
                secondary_damage_type = CombatDamageType.Sun
            case PlayerPartyCharacter.Valere:
                primary_damage_type = CombatDamageType.Blunt
                secondary_damage_type = CombatDamageType.Moon
            case PlayerPartyCharacter.Garl:
                primary_damage_type = CombatDamageType.Blunt
                secondary_damage_type = CombatDamageType.NONE
            case PlayerPartyCharacter.Serai:
                primary_damage_type = CombatDamageType.Sword
                secondary_damage_type = CombatDamageType.Poison
            case PlayerPartyCharacter.Reshan:
                primary_damage_type = CombatDamageType.Poison
                secondary_damage_type = CombatDamageType.Arcane
            case PlayerPartyCharacter.Bst:
                primary_damage_type = CombatDamageType.Blunt
                secondary_damage_type = CombatDamageType.Arcane

        self.damage_type = [
            primary_damage_type,
            primary_damage_type,
        ]
        if boost >= 1:
            self.damage_type.append(secondary_damage_type)
