import logging
from typing import Self

from control import sos_ctrl
from engine.combat.appraisals.valere.crescent_arc import CrescentArc
from engine.combat.appraisals.zale.sunball import Sunball
from engine.combat.utility.core.action import Action
from engine.combat.utility.sos_appraisal import SoSTimingType
from engine.combat.utility.sos_consideration import SoSConsideration
from engine.combat.utility.sos_reasoner import SoSReasoner
from memory import (
    CombatTutorialState,
    NextCombatAction,
    PlayerPartyCharacter,
    combat_manager_handle,
    level_manager_handle,
    new_dialog_manager_handle,
)

logger = logging.getLogger(__name__)
level_manager = level_manager_handle()
combat_manager = combat_manager_handle()
new_dialog_manager = new_dialog_manager_handle()


class CombatController:
    SLUG_TIMING = 0.35

    def __init__(self: Self, delta: float = 0.0) -> None:
        self.reasoner = SoSReasoner(combat_manager)
        self.action = None
        self.ctrl = sos_ctrl()
        self.block_timing = 0.0
        self.delta = delta

    # returns a bool to feed to the sequencer
    def execute_combat(self: Self) -> bool:
        self.ctrl.set_neutral()

        # if combat is done, just exit
        if combat_manager.encounter_done is True:
            return True

        # if some dialog is on the screen - make it go away
        if new_dialog_manager.dialog_open:
            self.ctrl.confirm()
            self._handle_alternate_encounters()
            return False

        # We need to decide how to handle these specific scenarios; via profile
        # or whatever else, but this is good for now.
        # Note: It can't be stopped or tested mid encounter.

        # if we dont have an action or the current appraisal is complete,
        # we make a new one.
        # we also check if battle command has focus, so it doesn't start executing before
        # we have control
        if (
            (self.action is None or self.action.appraisal.complete)
            and combat_manager.selected_character is not PlayerPartyCharacter.NONE
            and combat_manager.battle_command_has_focus
        ):
            logger.debug("No action exists, executing one one")
            self.action = self.reasoner.execute()
            return False

        # Defending an ability
        # TODO(eein): Move this to a new method
        if (
            self.action is None or self.action.appraisal.complete
        ) and combat_manager.selected_character is PlayerPartyCharacter.NONE:
            combat_manager.read_next_combat_enemy()
            next_combat_enemy = combat_manager.next_combat_enemy
            if (
                next_combat_enemy
                and next_combat_enemy.state_type is NextCombatAction.Attacking
                and next_combat_enemy.movement_done is True
            ):
                # accumalates the delta time until it's greater than the block timing
                if self.block_timing >= self.SLUG_TIMING:
                    logger.debug(f"Hitting Block for {next_combat_enemy.move_name}")
                    sos_ctrl().confirm()
                    self.block_timing = 0.0
                elif next_combat_enemy.movement_done is True:
                    self.block_timing += self.delta

            elif (
                next_combat_enemy
                and next_combat_enemy.state_type is NextCombatAction.Casting
            ):
                logger.debug(f"Spam Block for {next_combat_enemy.move_name} Casting")
                sos_ctrl().confirm()

            else:
                self.block_timing = 0.0
            return False
        # For some reason the action isn't set, so bail out.
        if self.action is None:
            # logger.debug("baling out because self action is nil")
            return False

        # if the consideration doesn't believe the situation is valid, execute it.
        # This will put the cursor on the character it should be on.
        # internally it checks to see if the character is not NONE and if the selected
        # character is the one it wants and return true if so.
        # if the character is None, it knows it can't move things.
        consideration_valid = self.action.consideration.valid(
            combat_manager.selected_character, self.action
        )
        if not consideration_valid:
            logger.debug("Consideration is not valid, move cursor")
            self.action.consideration.execute()
            return False

        # do we need to navigate to an action?
        # if we are on the selected character, run the appraisal:
        # logger.debug("Try to execute the appraisal")
        self.action.appraisal.execute()
        if self.action.appraisal.complete:
            logger.debug("appraisal is complete, reset action")
            self.action = None

        # are we waiting for an attack to complete?

        # is an enemy attacking - do we need to defend?

        # execute consideration; it should know what states it expected
        # if consideration not executed, execute it
        #   - considerations must have actions, it will pop an action off the stack
        #     and run it so the ui is not blocked. once the stack is complete it will mark
        #     the consideration as completed and will continue on.
        # if consideration executed

        # Check if we have control
        return False

    def _handle_alternate_encounters(self: Self) -> None:
        # checks if we are in the second encounter zone and if we are in the tutorial
        if (
            not self.action
            and level_manager.current_level == "72e9f2699f7c8394b93afa1d273ce67a"
            and combat_manager.tutorial_state is CombatTutorialState.SecondEncounter
        ):
            # if we're in the "second encounter" combat tutorial after the dialog state
            # just add an action for using the correct move
            for player in combat_manager.players:
                if player.character == PlayerPartyCharacter.Valere:
                    self.action = Action(
                        SoSConsideration(player),
                        CrescentArc(timing_type=SoSTimingType.NONE),
                    )
                if player.character == PlayerPartyCharacter.Zale:
                    self.action = Action(
                        SoSConsideration(player), Sunball(hold_time=2.0)
                    )
