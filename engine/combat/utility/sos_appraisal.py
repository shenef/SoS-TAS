import logging
import time
from enum import Enum, auto
from typing import Self

from control import sos_ctrl
from engine.combat.utility.core import Appraisal
from memory.combat_manager import CombatDamageType, CombatPlayer, combat_manager_handle
from memory.mappers.player_party_character import PlayerPartyCharacter

logger = logging.getLogger(__name__)


class SoSBattleCommand(Enum):
    """Actions that a player can take. See `AppraisalType`."""

    Attack = 0
    Skill = 1
    Combo = 2
    Item = 3


class SoSTimingType(Enum):
    NONE = auto()
    OneHit = auto()
    Charge = auto()
    MultiHit = auto()


class SoSAppraisalStep(Enum):
    SelectingCommand = auto()
    Boost = auto()
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


class SoSResource(Enum):
    NONE = auto()
    Mana = auto()
    ComboPoints = auto()
    UltimateGauge = auto()


class SoSAppraisal(Appraisal):
    MAX_ENEMY_TARGETING_FAILURES = 6

    def __init__(
        self: Self,
        name: str,
        timing_type: SoSTimingType = SoSTimingType.NONE,
        boost: int = 0,
        battle_command: SoSBattleCommand = SoSBattleCommand.Attack,
    ) -> None:
        super().__init__(name=name)

        self.combat_manager = combat_manager_handle()
        self.complete = False
        self.battle_command: SoSBattleCommand = battle_command
        self.skill_command_index = 0
        self.target_type = SoSTargetType.Enemy
        self.damage_type: list[CombatDamageType] = []
        # the following provides an alternative targeting type for moves that break out of
        # the normal controller types. Moonerang is an example of this, which acts like a
        # basic attack when it targets, but is a skill when it is selected
        self.battle_command_targeting_type: SoSBattleCommand = self.battle_command
        self.timing_type = timing_type
        self.step = SoSAppraisalStep.SelectingCommand
        self.character = PlayerPartyCharacter.NONE
        self.resource = SoSResource.NONE
        self.cost = 0
        self.boost = boost
        self.enemy_targeting_failures = 0

    def __repr__(self: Self) -> str:
        name = f"[{self.name}]" if self.battle_command != SoSBattleCommand.Attack else ""
        target = ""
        if self.target is not None:
            enemy_name = ""
            enemy_idx = 0
            for idx, enemy in enumerate(self.combat_manager.enemies):
                if self.target is enemy.unique_id:
                    enemy_idx = idx
                    enemy_name = enemy.name
            if not enemy_name:
                target = f" (target = {enemy_name}[{enemy_idx}])"
            else:
                target = f" (target = {self.target})"
        return f"{self.battle_command.name}{name}{target}"

    def execute(self: Self) -> None:
        """Select the step to perform based on the current step."""
        match self.step:
            case SoSAppraisalStep.SelectingCommand:
                self.execute_selecting_command()
            case SoSAppraisalStep.Boost:
                self.execute_boost()
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
                logger.error(f"Appraisal Step {self.step} OUT OF BOUNDS")

    def execute_selecting_command(self: Self) -> None:
        """
        Execute battle command selection.

        Attempt to select the battle command set to `self.battle_command` if the battle command
        is already selected, set the appraisal step and confirm if it is not selected,
        tap down until it is selected
        """
        if (
            self.combat_manager.battle_command_has_focus
            and self.combat_manager.battle_command_index != self.battle_command.value
        ):
            sos_ctrl().dpad.tap_down()
        else:
            self.step = SoSAppraisalStep.Boost
            # logger.debug(f"Selecting Battle Command: {self.battle_command.name}")

    def execute_boost(self: Self) -> None:
        # TODO(eein): Check if theres a flag that shows when live mana is available and use
        # that to guard this function as well
        if self.boost > 0:
            logger.debug(f"Boosting: {self.name} {self.boost} times")
            sos_ctrl().toggle_boost(True)
            time.sleep(0.5)

            for boost in range(self.boost):
                logger.debug(f"  Triggering Boost: {boost + 1}")
                sos_ctrl().confirm(tapping=True)

            sos_ctrl().toggle_boost(False)
        self.step = SoSAppraisalStep.ConfirmCommand

    def execute_confirm_command(self: Self) -> None:
        if (
            self.combat_manager.battle_command_has_focus
            and self.combat_manager.battle_command_index == self.battle_command.value
        ):
            sos_ctrl().confirm()
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
                    logger.error(f"Invalid Battle Command: {self.battle_command}")

            # set the character here for use later - since it drops from memory
            self.character = self.combat_manager.selected_character
            logger.debug(f"Confirmed Battle Command: {self.battle_command.name}")
            # logger.debug(f"Entering step: {self.step.name}")

    def execute_selecting_skill(self: Self) -> None:
        if (
            self.combat_manager.battle_command_has_focus is False
            and self.combat_manager.skill_command_has_focus is True
            and self.combat_manager.skill_command_index != self.skill_command_index
        ):
            sos_ctrl().dpad.tap_down()
        else:
            self.step = SoSAppraisalStep.ConfirmSkill
            # logger.debug(f"Selecting Battle Skill: {self.name}")

    def execute_confirm_skill(self: Self) -> None:
        if (
            self.combat_manager.battle_command_has_focus is False
            and self.combat_manager.skill_command_has_focus
            and self.combat_manager.skill_command_index == self.skill_command_index
        ):
            sos_ctrl().confirm()
            # Attack skips to selecting enemy sequence
            match self.battle_command:
                # TODO(orkaboy): This is technically wrong; healing combos and skills like
                # TODO(orkaboy): Zale's heal would target a player character
                case SoSBattleCommand.Skill | SoSBattleCommand.Combo:
                    self.step = SoSAppraisalStep.SelectingEnemySequence
                case SoSBattleCommand.Item:
                    self.step = SoSAppraisalStep.SelectingPlayerSequence
                case _:
                    logger.error("Invalid Skill Command")

            # set the character here for use later - since it drops from memory

            logger.debug(f"Confirmed Skill Command: {self.name}")
            # logger.debug(f"Entering step: {self.step.name}")

    def execute_selecting_enemy_sequence(self: Self) -> None:
        if (
            self._enemy_targeted()
            and not self.combat_manager.battle_command_has_focus
            and self.combat_manager.battle_command_index is None
            and self.combat_manager.selected_character != PlayerPartyCharacter.NONE
        ):
            self.step = SoSAppraisalStep.ConfirmEnemySequence
            # logger.debug(f"Selected Target {self.target}")
            return
        # logger.warn("Enemy Target Not Valid, moving cursor")
        sos_ctrl().dpad.tap_right()
        # TODO(eein): This will be improved when we have a better way to
        # detect who we are targeting. For now we just fail after 6 failures
        # to avoid getting stuck in a loop
        self.enemy_targeting_failures += 1
        if self.enemy_targeting_failures >= self.MAX_ENEMY_TARGETING_FAILURES:
            self.step = SoSAppraisalStep.ConfirmEnemySequence
            logger.warn("Max Targeting Failures Reached, Confirming Target")

    def execute_confirm_enemy_sequence(self: Self) -> None:
        if self.combat_manager.selected_character != PlayerPartyCharacter.NONE:
            logger.debug(f"Confirming Enemy {self.target}")
            sos_ctrl().confirm()
        else:
            self.step = SoSAppraisalStep.TimingSequence
            # logger.debug(f"Confirmed Target {self.target}")

    def execute_timing_sequence(self: Self) -> None:
        match self.timing_type:
            case SoSTimingType.OneHit:
                # wait for timing and press button
                # need a way to bail out if missed timing
                if self.is_player_timed_attack_ready():
                    logger.debug(f"Executing Timing Attack, Tap ({self.name})")
                    sos_ctrl().confirm()
                    self.step = SoSAppraisalStep.ActionComplete
            case SoSTimingType.Charge:
                # Hold Button until timing ready
                # need a way to bail out if missed timing
                sos_ctrl().toggle_confirm(True)
                if self.is_player_timed_attack_ready():
                    sos_ctrl().toggle_confirm(False)
                    logger.debug(f"Executing Timing Attack, Charge ({self.name})")
                    self.step = SoSAppraisalStep.ActionComplete
            case _:
                self.step = SoSAppraisalStep.ActionComplete

    def execute_action_complete(self: Self) -> None:
        self.complete = True
        logger.debug("Action Complete")

    def _enemy_targeted(self: Self) -> bool:
        # If we are doing some custom controller stuff that doesn't need a target, just return True
        if self.target is None:
            return True

        for enemy in self.combat_manager.enemies:
            if enemy.unique_id == self.target:
                match self.battle_command_targeting_type:
                    case SoSBattleCommand.Attack:
                        if enemy.unique_id == self.combat_manager.selected_attack_target_guid:
                            return True

                    case SoSBattleCommand.Skill | SoSBattleCommand.Combo:
                        if enemy.unique_id == self.combat_manager.selected_skill_target_guid:
                            return True
        return False

    def has_resources(self: Self, actor: CombatPlayer) -> bool:
        match self.resource:
            case SoSResource.Mana:
                return actor.current_mp >= self.cost
            # TODO(eein): Not yet implemented
            # case SoSResource.ComboPoints:
            #     return actor.combo_points >= self.cost
            # case SoSResource.UltimateGauge:
            #     return actor.ultimate_gauge >= self.cost
            case _:
                return True

    def is_player_timed_attack_ready(self: Self) -> bool:
        for player in self.combat_manager.players:
            if player.character == self.character:
                return player.timed_attack_ready
        return False
