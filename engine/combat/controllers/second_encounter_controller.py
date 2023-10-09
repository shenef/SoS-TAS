import logging
from typing import Self

from control import sos_ctrl
from engine.combat.appraisals.basic_attack import BasicAttack
from engine.combat.appraisals.valere import CrescentArc
from engine.combat.appraisals.zale import Sunball
from engine.combat.controllers.encounter_controller import EncounterController
from engine.combat.utility.core.action import Action
from engine.combat.utility.sos_appraisal import SoSTimingType
from engine.combat.utility.sos_consideration import SoSConsideration
from memory import (
    PlayerPartyCharacter,
    combat_manager_handle,
    new_dialog_manager_handle,
)

logger = logging.getLogger(__name__)
combat_manager = combat_manager_handle()
new_dialog_manager = new_dialog_manager_handle()


class SecondEncounterController(EncounterController):
    def __init__(self: Self) -> None:
        super().__init__()
        self.second_attack = False

    def execute_dialog(self: Self) -> bool:
        if new_dialog_manager.dialog_open:
            sos_ctrl().toggle_turbo(True)
            sos_ctrl().confirm()
            sos_ctrl().toggle_turbo(False)
            self.action = None
            self.second_attack = True
            return True
        return False

    def generate_action(self: Self) -> bool:
        if self._should_generate_action():
            logger.debug("No action exists, executing one one")
            self.action = self._get_action()
            return True
        return False

    def _get_action(self: Self) -> Action:
        for player in combat_manager.players:
            if combat_manager.selected_character == player.character:
                match player.character:
                    case PlayerPartyCharacter.Valere:
                        if self.second_attack is True:
                            return Action(
                                SoSConsideration(player),
                                CrescentArc(timing_type=SoSTimingType.NONE),
                            )
                        return Action(
                            SoSConsideration(player),
                            BasicAttack(timing_type=SoSTimingType.NONE),
                        )
                    case PlayerPartyCharacter.Zale:
                        if self.second_attack is True:
                            return Action(
                                SoSConsideration(player),
                                Sunball(value=1000, hold_time=2.0),
                            )
                        return Action(
                            SoSConsideration(player),
                            BasicAttack(timing_type=SoSTimingType.NONE),
                        )

        return None
