from control import sos_ctrl
from engine.combat.utility.sos_reasoner import SoSReasoner
from memory.combat_manager import CombatCharacter, combat_manager_handle

combat_manager = combat_manager_handle()


class CombatController:
    def __init__(self):
        self.reasoner = SoSReasoner(combat_manager)
        self.action = None
        self.ctrl = sos_ctrl()

    # returns a bool to feed to the sequencer
    def execute_combat(self) -> bool:
        self.ctrl.set_neutral()

        # if combat is done, just exit
        if combat_manager.encounter_done is True:
          return True

        # if we dont have an action or the current appraisal is complete,
        # we make a new one.
        # we also check if battle command has focus, so it doesn't start executing before
        # we have control
        if (
            (self.action is None or self.action.appraisal.complete)
            and combat_manager.selected_character is not CombatCharacter.NONE
            and combat_manager.battle_command_has_focus
        ):
            # print("No action exists, executing one one")
            self.action = self.reasoner.execute()
            return False

        # For some reason the action isn't set, so bail out.
        if self.action is None:
            # print("baling out because self action is nil")
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
            # print("Consideration is not valid, move cursor")
            self.action.consideration.execute()
            return False

        # do we need to navigate to an action?
        # if we are on the selected character, run the appraisal:
        # print("Try to execute the appraisal")
        self.action.appraisal.execute()
        if self.action.appraisal.complete:
            # print("appraisal is complete, reset action")
            self.action = None

        return False
        # are we waiting for an attack to complete?

        # is an enemy attacking - do we need to defend?

        # execute consideration; it should know what states it expected
        # if consideration not executed, execute it
        #   - considerations must have actions, it will pop an action off the stack
        #     and run it so the ui is not blocked. once the stack is complete it will mark
        #     the consideration as completed and will continue on.
        # if consideration executed

        # Check if we have control
