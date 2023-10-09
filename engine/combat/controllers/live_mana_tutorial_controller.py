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
    level_manager_handle,
    new_dialog_manager_handle,
)

logger = logging.getLogger(__name__)
level_manager = level_manager_handle()
combat_manager = combat_manager_handle()
new_dialog_manager = new_dialog_manager_handle()


# The classes in encounter controllers are intended to return True if they
# should short circuit the root combat controller.
class LiveManaTutorialController(EncounterController):
    MIN_LIVE_MANA = 5

    def generate_action(self: Self) -> bool:
        if (
            (self.action is None or self.action.appraisal.complete)
            and combat_manager.selected_character is not PlayerPartyCharacter.NONE
            and combat_manager.battle_command_has_focus
        ):
            logger.debug("No action exists, executing one one")
            self.action = self._get_action()
            return True
        return False

    def _get_action(self: Self) -> Action:
        for player in combat_manager.players:
            if combat_manager.selected_character == player.character:
                if combat_manager.small_live_mana >= self.MIN_LIVE_MANA:
                    return Action(
                        SoSConsideration(player),
                        BasicAttack(timing_type=SoSTimingType.NONE, boost=1),
                    )
                return Action(
                    SoSConsideration(player),
                    BasicAttack(timing_type=SoSTimingType.NONE),
                )

        return None
