"""Base class for Combo Skill appraisals."""

import logging
from typing import Self

from engine.combat.utility.sos_appraisal import (
    SoSAppraisal,
    SoSBattleCommand,
    SoSTargetType,
    SoSTimingType,
)
from memory import PlayerPartyCharacter, combat_manager_handle

logger = logging.getLogger(__name__)
combat_manager = combat_manager_handle()


class ComboSkill(SoSAppraisal):
    """A Combo Skill appraisal."""

    def __init__(
        self: Self,
        name: str,
        timing_type: SoSTimingType = SoSTimingType.OneHit,
        boost: int = 0,
        casters: list[PlayerPartyCharacter] = None,
        combo_cost: int = 1,
    ) -> None:
        """Initialize a ComboSkill object."""
        super().__init__(
            name=name,
            boost=boost,
            timing_type=timing_type,
            battle_command=SoSBattleCommand.Combo,
        )
        self.target_type = SoSTargetType.Enemy
        self.casters = casters
        self.combo_cost = combo_cost

    def can_use(self: Self) -> bool:
        """Check if the combo skill can be used right now."""
        for caster in self.casters:
            found = False
            for player in combat_manager.players:
                if caster == player.character and not player.dead:
                    found = True
                    break
            if not found:
                return False
        return True
