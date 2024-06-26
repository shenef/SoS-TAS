import logging
import random
import time
from enum import Enum, auto
from typing import Self

from control import sos_ctrl
from engine.combat.utility.core import Appraisal
from memory.combat_manager import (
    CombatDamageType,
    CombatEnemyTarget,
    CombatPlayer,
    combat_manager_handle,
)
from memory.mappers.player_party_character import PlayerPartyCharacter

combat_manager = combat_manager_handle()
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
    SelectingCombo = auto()
    ConfirmCombo = auto()
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
    MAX_ENEMY_TARGETING_FAILURES = 15
    CONFIRM_DELAY_IN_SECONDS = 0.1

    def __init__(
        self: Self,
        name: str,
        timing_type: SoSTimingType = SoSTimingType.NONE,
        internal_name: str = "",
        boost: int = 0,
        battle_command: SoSBattleCommand = SoSBattleCommand.Attack,
        battle_command_targeting_type: SoSBattleCommand = None,
    ) -> None:
        super().__init__(name=name)

        self.internal_name = internal_name
        self.complete = False
        self.battle_command: SoSBattleCommand = battle_command
        self.skill_command_index = 0
        self.target_type = SoSTargetType.Enemy
        self.damage_type: list[CombatDamageType] = []
        # the following provides an alternative targeting type for moves that break out of
        # the normal controller types. Moonerang is an example of this, which acts like a
        # basic attack when it targets, but is a skill when it is selected
        self.battle_command_targeting_type: SoSBattleCommand = (
            battle_command_targeting_type or self.battle_command
        )

        self.timing_type: SoSTimingType = timing_type
        self.step = SoSAppraisalStep.SelectingCommand
        self.character = PlayerPartyCharacter.NONE
        self.resource = SoSResource.NONE
        self.cost: int = 0
        self.combo_cost: int = None
        self.ultimate: float = False
        self.boost: int = boost
        self.enemy_targeting_failures: int = 0

    def __repr__(self: Self) -> str:
        name = f"[{self.name}]" if self.battle_command != SoSBattleCommand.Attack else ""
        target = ""
        boost = ""
        if self.boost > 0:
            boost = f" boost={self.boost}"
        if self.target is not None:
            enemy_name = ""
            enemy_idx = 0
            for idx, enemy in enumerate(combat_manager.enemies):
                if self.target == enemy.unique_id:
                    enemy_idx = idx
                    enemy_name = enemy.name
            if enemy_name is not None and enemy_name != "":
                target = f" (target = {enemy_name} [{enemy_idx}])"
            else:
                target = f" (target = {self.target})"
        return f"{self.battle_command.name}{name}{target}{boost}"

    def execute(self: Self) -> None:
        """Select the step to perform based on the current step."""
        # Fallback for missing action complete step after timing sequence
        # This can happen if the boss overrides the timing attack to do something.
        self._fallback_for_missing_action_complete()

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
            case SoSAppraisalStep.SelectingCombo:
                self.execute_select_combo()
            case SoSAppraisalStep.ConfirmCombo:
                self.execute_confirm_combo()
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
            combat_manager.battle_command_has_focus
            and combat_manager.battle_command_index != self.battle_command.value
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
            combat_manager.battle_command_has_focus
            and combat_manager.battle_command_index == self.battle_command.value
        ):
            time.sleep(self.CONFIRM_DELAY_IN_SECONDS)
            sos_ctrl().confirm()

            # If we dont see an enemy targeted, then just go back to confirm command.
            # This prevents a race where jumping in place to combat area can sometimes
            # jump too far forward in state.
            # TODO(eein): add player_targeted here too

            # Attack skips to selecting enemy sequence
            match self.battle_command:
                case SoSBattleCommand.Attack:
                    self.step = SoSAppraisalStep.SelectingEnemySequence
                case SoSBattleCommand.Skill:
                    self.step = SoSAppraisalStep.SelectingSkill
                case SoSBattleCommand.Combo:
                    self.step = SoSAppraisalStep.SelectingCombo
                case SoSBattleCommand.Item:
                    self.step = SoSAppraisalStep.SelectingSkill
                case _:
                    logger.error(f"Invalid Battle Command: {self.battle_command}")

            # set the character here for use later - since it drops from memory
            self.character = combat_manager.selected_character
            logger.debug(f"Confirmed Battle Command: {self.battle_command.name}")
            # logger.debug(f"Entering step: {self.step.name}")

    def execute_selecting_skill(self: Self) -> None:
        if (
            combat_manager.battle_command_has_focus is False
            and combat_manager.skill_command_has_focus is True
            and combat_manager.skill_command_index != self.skill_command_index
        ):
            sos_ctrl().dpad.tap_down()
        else:
            self.step = SoSAppraisalStep.ConfirmSkill
            # logger.debug(f"Selecting Battle Skill: {self.name}")

    def execute_confirm_skill(self: Self) -> None:
        if (
            combat_manager.battle_command_has_focus is False
            and combat_manager.skill_command_has_focus
            and combat_manager.skill_command_index == self.skill_command_index
        ):
            time.sleep(self.CONFIRM_DELAY_IN_SECONDS)
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

    def execute_select_combo(self: Self) -> None:
        if (
            combat_manager.battle_command_has_focus is True
            and combat_manager.battle_command_index != self.skill_command_index
        ):
            sos_ctrl().dpad.tap_down()
        else:
            self.step = SoSAppraisalStep.ConfirmCombo
            logger.debug(f"Selecting Battle Combo: {self.name}")

    def execute_confirm_combo(self: Self) -> None:
        if (
            combat_manager.battle_command_has_focus is True
            and combat_manager.battle_command_index == self.skill_command_index
        ):
            time.sleep(self.CONFIRM_DELAY_IN_SECONDS)
            sos_ctrl().confirm()
            # TODO(orkaboy): Check targeting type
            match self.target_type:
                case SoSTargetType.Enemy:
                    self.step = SoSAppraisalStep.SelectingEnemySequence
                case SoSTargetType.Player:
                    self.step = SoSAppraisalStep.SelectingPlayerSequence
                case _:
                    logger.error(f"Unimplemented Combo Target type {self.target_type}")

            logger.debug(f"Confirmed Combo Command: {self.name}")

    def execute_selecting_enemy_sequence(self: Self) -> None:
        if (
            self._enemy_targeted()
            and not combat_manager.battle_command_has_focus
            and combat_manager.battle_command_index is None
            and combat_manager.selected_character != PlayerPartyCharacter.NONE
        ):
            self.step = SoSAppraisalStep.ConfirmEnemySequence
            logger.debug(f"Selected Target {self.target}")
            return

        # if we shouldn't be here, go back a step
        if combat_manager.battle_command_index is not None:
            self.step = SoSAppraisalStep.ConfirmCommand
            return

        logger.warn("Enemy Target Not Valid, moving cursor")
        # Use a randomly selected directional input to find enemies that are otherwise not reachable
        direction = random.randint(0, 3)
        match direction:
            case 0:
                sos_ctrl().dpad.tap_left()
            case 1:
                sos_ctrl().dpad.tap_right()
            case 2:
                sos_ctrl().dpad.tap_up()
            case 3:
                sos_ctrl().dpad.tap_down()
        # TODO(eein): This will be improved when we have a better way to
        # detect who we are targeting. For now we just fail after a set amount of
        # failures to avoid getting stuck in a loop.
        self.enemy_targeting_failures += 1
        if self.enemy_targeting_failures >= self.MAX_ENEMY_TARGETING_FAILURES:
            self.step = SoSAppraisalStep.ConfirmEnemySequence
            logger.warn("Max Targeting Failures Reached, Confirming Target")

    def execute_confirm_enemy_sequence(self: Self) -> None:
        if combat_manager.selected_character != PlayerPartyCharacter.NONE:
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

    def _fallback_for_missing_action_complete(self: Self) -> None:
        """
        Handle falling back when a timing attack sequence isn't finished by the appraisal.

        The default state for coming back to command selection from doing an attack is
        Battle Command Has Focus: True and Skill Command Has Focus: True.

        So we check:
        - We are on the command selection step
        - The current Character is not NONE,
        - and the current appraisal step is in the timing sequence (to isolate it for this bug)

        If we know we are in the above state, we should be selecting an action, not waiting on
        timing, so complete the action so a new one can be generated.
        """
        if (
            combat_manager.battle_command_has_focus
            and combat_manager.skill_command_has_focus
            and combat_manager.selected_character is not PlayerPartyCharacter.NONE
            and self.step is SoSAppraisalStep.TimingSequence
        ):
            logger.warn("Missing Action Complete, Fallback")
            self.step = SoSAppraisalStep.ActionComplete

    def _enemy_targeted(self: Self) -> bool:
        for enemy in combat_manager.enemies:
            if enemy.unique_id == self.target:
                match self.battle_command_targeting_type:
                    case SoSBattleCommand.Attack:
                        if enemy.unique_id == combat_manager.selected_attack_target_guid:
                            return True

                    case SoSBattleCommand.Skill | SoSBattleCommand.Combo:
                        if enemy.unique_id == combat_manager.selected_skill_target_guid:
                            return True
        return False

    def has_resources(self: Self, actor: CombatPlayer) -> bool:
        match self.resource:
            case SoSResource.Mana:
                return actor.current_mp >= self.cost
            case SoSResource.ComboPoints:
                return actor.combo_points >= self.combo_cost
            case SoSResource.UltimateGauge:
                return actor.ultimate_gauge >= 1
            case _:
                return True

    def is_player_timed_attack_ready(self: Self) -> bool:
        for player in combat_manager.players:
            if player.character == self.character:
                return player.timed_attack_ready
        return False

    def adjust_value(self: Self, enemy: CombatEnemyTarget) -> None:
        """Can be overridden to adjust value against specific enemy."""
        return


class UtilityEntry:
    """Internal representation of a comment in the utility log."""

    def __init__(self: Self, character: PlayerPartyCharacter, appraisal: SoSAppraisal) -> None:
        """Initialize a UtilityEntry object."""
        self.character = character
        self.appraisal = appraisal

    def __repr__(self: Self) -> str:
        return f"[{self.appraisal.value}] {self.character.name}: {self.appraisal}"


_utility_log: list[UtilityEntry] = []


def get_utility_log() -> list[UtilityEntry]:
    """Return a handle to the log."""
    return _utility_log
