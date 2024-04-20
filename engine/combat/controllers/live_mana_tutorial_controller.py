import logging
from typing import Self

from engine.combat.appraisals.basic_attack import BasicAttack
from engine.combat.controllers.encounter_controller import EncounterController
from engine.combat.utility.core.action import Action
from engine.combat.utility.sos_appraisal import SoSTimingType
from engine.combat.utility.sos_consideration import SoSConsideration
from memory import (
    combat_manager_handle,
    level_manager_handle,
    new_dialog_manager_handle,
)

logger = logging.getLogger(__name__)
level_manager = level_manager_handle()
combat_manager = combat_manager_handle()
new_dialog_manager = new_dialog_manager_handle()


class LiveManaTutorialController(EncounterController):
    MIN_LIVE_MANA = 5

    def generate_action(self: Self) -> bool:
        if self._should_generate_action():
            logger.debug("No action exists, creating one")
            self.action = self._get_action()
            return True
        return False

    def _get_action(self: Self) -> Action:
        for player in combat_manager.players:
            if combat_manager.selected_character == player.character:
                enemy = combat_manager.enemies[0]
                if combat_manager.small_live_mana >= self.MIN_LIVE_MANA:
                    appraisal = BasicAttack(
                        caster=player.character, timing_type=SoSTimingType.NONE, boost=1
                    )
                    appraisal.target = enemy.unique_id
                    combat_manager.current_appraisal = appraisal
                    return Action(SoSConsideration(player), appraisal)

                appraisal = BasicAttack(caster=player.character, timing_type=SoSTimingType.NONE)
                appraisal.target = enemy.unique_id
                combat_manager.current_appraisal = appraisal
                return Action(SoSConsideration(player), appraisal)

        return None
