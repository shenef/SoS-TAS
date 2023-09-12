import logging
from enum import Enum, auto

from control import sos_ctrl
from engine.combat.utility.core import Appraisal
from memory.combat_manager import combat_manager_handle
from memory.mappers.player_party_character import PlayerPartyCharacter

logger = logging.getLogger(__name__)


# An action that a player can take. See AppraisalType
class SoSBattleCommand(Enum):
    Attack = 0
    Skill = 1
    Combo = 2
    Item = 3


class SoSTimingType(Enum):
    NONE = auto()
    OneHit = auto()
    Charge = auto()


class SoSAppraisalStep(Enum):
    SelectingCommand = auto()
    ConfirmCommand = auto()
    SelectingSkill = auto()
    ConfirmSkill = auto()
    SelectingAction = auto()
    SelectingEnemySequence = auto()
    ConfirmEnemySequence = auto()
    SelectingPlayerSequence = auto()
    TimingSequence = auto()
    ActionComplete = auto()


class SoSTargetType(Enum):
    NONE = auto()
    Player = auto()
    Enemy = auto()


class SoSAppraisal(Appraisal):
    def __init__(self):
        super().__init__()

        self.combat_manager = combat_manager_handle()
        self.ctrl = sos_ctrl()
        self.ctrl.delay = 0.1
        self.complete = False
        self.battle_command = SoSBattleCommand.Attack
        self.skill_command_index = 0
        self.target_type = SoSTargetType.Enemy
        self.timing_type = SoSTimingType.NONE
        self.step = SoSAppraisalStep.SelectingCommand
        self.character = PlayerPartyCharacter.NONE

    # selects the step to perform based on the current step
    def execute(self):
        match self.step:
            case SoSAppraisalStep.SelectingCommand:
                self.execute_selecting_command()
            case SoSAppraisalStep.ConfirmCommand:
                self.execute_confirm_command()
            case SoSAppraisalStep.SelectingSkill:
                self.execute_selecting_skill()
            case SoSAppraisalStep.ConfirmSkill:
                self.execute_confirm_skill()
            case SoSAppraisalStep.SelectingEnemySequence:
                self.execute_selecting_enemy_sequence()
            case SoSAppraisalStep.ConfirmEnemySequence:
                self.execute_confirm_enemy_sequence()
            case SoSAppraisalStep.SelectingPlayerSequence:
                pass
            case SoSAppraisalStep.TimingSequence:
                self.execute_timing_sequence()
            case SoSAppraisalStep.ActionComplete:
                self.execute_action_complete()
            case _:
                logger.debug("Appraisal Step OUT OF BOUNDS")

    # attempt to select the battle command set to self.battle_command
    # if the battle command is already selected, set the appraisal step and
    # confirm
    # if it is not selected, tap down until it is selected
    def execute_selecting_command(self):
        if (
            self.combat_manager.battle_command_has_focus
            and self.combat_manager.battle_command_index != self.battle_command.value
        ):
            sos_ctrl().dpad.tap_down()
        else:
            self.step = SoSAppraisalStep.ConfirmCommand
            logger.debug(f"Selecting Battle Command: {self.battle_command.name}")
            return

    def execute_confirm_command(self):
        if (
            self.combat_manager.battle_command_has_focus
            and self.combat_manager.battle_command_index == self.battle_command.value
        ):
            self.ctrl.confirm()
            # TODO: Add items and whatever else here.
            # Attack skips to selecting enemy sequence
            match self.battle_command:
                case SoSBattleCommand.Attack:
                    self.step = SoSAppraisalStep.SelectingEnemySequence
                case SoSBattleCommand.Skill:
                    self.step = SoSAppraisalStep.SelectingSkill
                case SoSBattleCommand.Combo:
                    # combos reflect as skills in the menu
                    self.step = SoSAppraisalStep.SelectingSkill
                case SoSBattleCommand.Item:
                    self.step = SoSAppraisalStep.SelectingSkill
                case _:
                    logger.debug("Invalid Battle Command")

            # set the character here for use later - since it drops from memory
            self.character = self.combat_manager.selected_character
            logger.debug(f"Confirmed Battle Command: {self.battle_command.name}")
            logger.debug(f"Entering step: {self.step.name}")
            return

    def execute_selecting_skill(self):
        if (
            self.combat_manager.skill_command_has_focus
            and self.combat_manager.skill_command_index != self.skill_command_index
        ):
            sos_ctrl().dpad.tap_down()
        else:
            self.step = SoSAppraisalStep.ConfirmSkill
            logger.debug(f"Selecting Battle Command: {self.battle_command.name}")
            return

    def execute_confirm_skill(self):
        if (
            self.combat_manager.skill_command_has_focus
            and self.combat_manager.skill_command_index == self.skill_command_index
        ):
            self.ctrl.confirm()
            # TODO: Add items and whatever else here.
            # Attack skips to selecting enemy sequence
            match self.battle_command:
                case SoSBattleCommand.Skill | SoSBattleCommand.Combo:
                    self.step = SoSAppraisalStep.SelectingEnemySequence
                case SoSBattleCommand.Item:
                    self.step = SoSAppraisalStep.SelectingPlayerSequence
                case _:
                    logger.debug("Invalid Skill Command")

            # set the character here for use later - since it drops from memory

            logger.debug(f"Confirmed Skill Command: {self.battle_command.name}")
            logger.debug(f"Entering step: {self.step.name}")
            return

    def execute_selecting_enemy_sequence(self):
        # Just assume we are targeting something for now
        # TODO: this will be similar to consideration that cycles through targets
        # later until it finds the one where the guid is the same (or the unique id)
        # we should also ensure the target is selected before initiating the action
        # This is simply hovering the target and ensures we can move to the next state

        match self.battle_command:
            case SoSBattleCommand.Attack:
                selected_target = self.combat_manager.selected_attack_target_guid
            case SoSBattleCommand.Skill | SoSBattleCommand.Combo:
                selected_target = self.combat_manager.selected_skill_target_guid
            case _:
                selected_target = ""
        if (
            self._enemy_targeted()
            and not self.combat_manager.battle_command_has_focus
            and self.combat_manager.battle_command_index is None
            and selected_target != ""
            and self.combat_manager.selected_character != PlayerPartyCharacter.NONE
        ):
            self.step = SoSAppraisalStep.ConfirmEnemySequence
            logger.debug("Selected Target")
            return
        sos_ctrl().dpad.tap_right()
        return

    def execute_confirm_enemy_sequence(self):
        # TODO: Find better timing, or add a delay for this confirm.
        if self.combat_manager.selected_character != PlayerPartyCharacter.NONE:
            logger.debug("Confirming Enemy")
            self.ctrl.confirm()
        else:
            self.step = SoSAppraisalStep.TimingSequence
            logger.debug("Confirmed Target")

    def execute_timing_sequence(self):
        match self.timing_type:
            case SoSTimingType.OneHit:
                # wait for timing and press button
                # need a way to bail out if missed timing
                if self.is_player_timed_attack_ready():
                    logger.debug("Executing Timing Attack")
                    self.ctrl.confirm()
                    self.step = SoSAppraisalStep.ActionComplete
            case SoSTimingType.Charge:
                # Hold Button until timing ready
                # need a way to bail out if missed timing
                sos_ctrl().toggle_confirm(True)
                if self.is_player_timed_attack_ready():
                    sos_ctrl().toggle_confirm(False)
                    logger.debug("Executing Timing Attack")
                    self.step = SoSAppraisalStep.ActionComplete
            case _:
                self.step = SoSAppraisalStep.ActionComplete

    def execute_action_complete(self):
        self.complete = True
        logger.debug("Action Complete")

    def _enemy_targeted(self) -> bool:
        return True
        # for enemy in self.combat_manager.enemies:
        #     match self.battle_command:
        #         case SoSBattleCommand.Attack:
        #             return (
        #                 enemy.unique_id
        #                 == self.combat_manager.selected_attack_target_guid
        #             )
        #         case SoSBattleCommand.Skill | SoSBattleCommand.Combo:
        #             return (
        #                 enemy.unique_id
        #                 == self.combat_manager.selected_skill_target_guid
        #             )
        # return False

    def is_player_timed_attack_ready(self) -> bool:
        for player in self.combat_manager.players:
            if player.character == self.character:
                return player.timed_attack_ready
        return False
