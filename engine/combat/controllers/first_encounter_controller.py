import logging
from typing import Self

from engine.combat.appraisals.basic_attack import BasicAttack
from engine.combat.controllers.encounter_controller import EncounterController
from engine.combat.utility.core.action import Action
from engine.combat.utility.sos_appraisal import SoSTimingType
from engine.combat.utility.sos_consideration import SoSConsideration
from memory import (
    PlayerPartyCharacter,
    combat_manager_handle,
)

logger = logging.getLogger(__name__)
combat_manager = combat_manager_handle()


class FirstEncounterController(EncounterController):
    def generate_action(self: Self) -> bool:
        if self._should_generate_action():
            logger.debug("No action exists, creating one")
            self.action = self._get_action()
            return True
        return False

    def _get_action(self: Self) -> Action:
        for player in combat_manager.players:
            if combat_manager.selected_character == player.character:
                match player.character:
                    case PlayerPartyCharacter.Valere:
                        return Action(
                            SoSConsideration(player),
                            BasicAttack(caster=player.character, timing_type=SoSTimingType.NONE),
                        )
                    case PlayerPartyCharacter.Zale:
                        return Action(
                            SoSConsideration(player),
                            BasicAttack(caster=player.character, timing_type=SoSTimingType.NONE),
                        )
        return None
