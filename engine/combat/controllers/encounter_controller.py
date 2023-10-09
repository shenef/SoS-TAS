import logging
from typing import Self

from control import sos_ctrl
from engine.combat.utility.core.action import Action
from engine.combat.utility.sos_reasoner import SoSReasoner
from memory import (
    NextCombatAction,
    NextCombatEnemy,
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
class EncounterController:
    def __init__(self: Self) -> None:
        self.reasoner = SoSReasoner()
        self.action: Action = None
        self.block_timing = 0.0

    # if combat is done, just exit
    def encounter_done(self: Self) -> bool:
        if combat_manager.encounter_done is True:
            return True
        return False

    # If some dialog is on the screen - make it go away by mashing confirm
    # There are some fights with dialog mid-fight and this will get us through it
    # until we regain control
    def execute_dialog(self: Self) -> bool:
        if new_dialog_manager.dialog_open:
            sos_ctrl().toggle_turbo(True)
            sos_ctrl().confirm()
            sos_ctrl().toggle_turbo(False)
            return True
        return False

    # If we dont have an action or the current appraisal is complete,
    # we make a new one.
    # we also check if battle command has focus, so it doesn't start executing before
    # we have control
    def generate_action(self: Self) -> bool:
        if self._should_generate_action():
            logger.debug("No action exists, executing one one")
            self.action = self.reasoner.execute()
            return True
        return False

    # Handles block execution - code is commented out until we have a better
    # solution for blocking.
    # Currently it will spam confirm to block.
    def execute_block(self: Self) -> bool:
        if self._should_block():
            combat_manager.read_next_combat_enemy()
            next_combat_enemy = combat_manager.next_combat_enemy

            if self._is_blocking_attack(next_combat_enemy):
                logger.debug(f"Spam Block for {next_combat_enemy.move_name} Attack")
                sos_ctrl().confirm()
            elif self._is_blocking_spell(next_combat_enemy):
                logger.debug(f"Spam Block for {next_combat_enemy.move_name} Casting")
                sos_ctrl().confirm()

                return True
        return False

    # If the consideration doesn't believe the situation is valid, execute changing
    # the selected consideration (character). This will rotate the cursor to the next
    # available consideration until it finds the one it expects.
    # TODO(eein): This should also take into considerations swapping characters into
    # the game field.
    def execute_consideration(self: Self) -> bool:
        if not self._consideration_valid():
            logger.debug("Consideration is not valid, move cursor")
            self.action.consideration.execute()
            return True
        return False

    # Executes the appraisal of the action. If the appraisal completes its lifecycle
    # it will set self.action to None so that a new action can be generated.
    def execute_appraisal(self: Self) -> bool:
        self.action.appraisal.execute()
        if self.action.appraisal.complete:
            # logger.debug("Appraisal is complete, reset action")
            self.action = None
            return True
        return False

    # Checks if an action has been assigned by utility and returns true if so
    # If there is no action to act on, it should be unable to continue with
    # attempting to take control and attack an enemy.
    def has_action(self: Self) -> bool:
        return self.action is not None

    def _should_generate_action(self: Self) -> bool:
        return (
            (self.action is None or self.action.appraisal.complete)
            and combat_manager.selected_character is not PlayerPartyCharacter.NONE
            and combat_manager.battle_command_has_focus
        )

    # Check if we should block. This is used to determine if we should be blocking
    def _should_block(self: Self) -> bool:
        return (
            self.action is None or self.action.appraisal.complete
        ) and combat_manager.selected_character is PlayerPartyCharacter.NONE

    # Determine if we are blocking an attack
    def _is_blocking_attack(self: Self, next_combat_enemy: NextCombatEnemy) -> bool:
        return (
            next_combat_enemy
            and next_combat_enemy.movement_done is True
            and next_combat_enemy.state_type is NextCombatAction.Attacking
        )

    def _is_blocking_spell(self: Self, next_combat_enemy: NextCombatEnemy) -> bool:
        return (
            next_combat_enemy
            and next_combat_enemy.state_type is NextCombatAction.Casting
        )

    # Check the consideration to see if it's valid and return true if so.
    def _consideration_valid(self: Self) -> bool:
        return self.action.consideration.valid(
            combat_manager.selected_character, self.action
        )
