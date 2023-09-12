import logging

from control import sos_ctrl
from engine.combat.utility.sos_appraisal import SoSAppraisal, SoSAppraisalType
from memory import PlayerPartyCharacter, combat_manager_handle

logger = logging.getLogger(__name__)


class BasicAttack(SoSAppraisal):
    STEP_0 = 0
    STEP_1 = 1
    STEP_2 = 2

    def __init__(self):
        super().__init__()
        self.type = SoSAppraisalType.Basic
        self.complete = False
        self.step = self.STEP_0

    # executes a basic attack with timing
    def execute(self):
        ctrl = sos_ctrl()
        ctrl.delay = 0.1
        combat_manager = combat_manager_handle()
        if (
            self.step == self.STEP_0
            and combat_manager.battle_command_has_focus
            and combat_manager.battle_command_index == 0
        ):
            ctrl.confirm()
            self.step = self.STEP_1
            logger.debug(f"Selected Attack: {combat_manager.selected_character.value}")
            return
        # Just assume we are targeting something
        # TODO: this will be similar to consideration that cycles through targets
        # later until it finds the one where the guid is the same (or the unique id)
        # we should also ensure the target is selected before initiating the action
        if (
            self.step == self.STEP_1
            and self._enemy_targeted(combat_manager)
            and not combat_manager.battle_command_has_focus
            and combat_manager.battle_command_index is None
            and combat_manager.selected_target_guid != ""
            and combat_manager.selected_character != PlayerPartyCharacter.NONE
        ):
            # TODO: Find better timing, or add a delay for this confirm.
            ctrl.confirm()
            self.step = self.STEP_2
            logger.debug(f"Selected Enemy: {combat_manager.selected_character.value}")
            return

        # This step is required because spell lock animations lock the player from selecting a
        # target.
        # TODO: Find a variable we can use to determine if the gamestate is ready to progress.
        if (
            self.step == self.STEP_2
            and combat_manager.selected_character != PlayerPartyCharacter.NONE
        ):
            logger.debug(
                f"Retrying enemy attack confirm - {combat_manager.selected_character.value}"
            )
            ctrl.confirm()
            return

        if (
            self.step == self.STEP_2
            and combat_manager.selected_character == PlayerPartyCharacter.NONE
        ):
            logger.debug(
                f"Basic Attack Complete - {combat_manager.selected_character.value}"
            )
            self.complete = True
            return

    def _enemy_targeted(self, combat_manager) -> bool:
        for enemy in combat_manager.enemies:
            if enemy.unique_id == combat_manager.selected_target_guid:
                return True
        return False
