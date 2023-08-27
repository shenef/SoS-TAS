from engine.combat.utility.sos_reasoner import SoSReasoner
from engine.mathlib import Vec3
from engine.seq.move import InteractMove, SeqMove
from memory.combat_manager import CombatCharacter, combat_manager_handle

combat_manager = combat_manager_handle()


# TODO: Temporary code, moves along path, pausing while combat is active
class SeqCombatAndMove(SeqMove):
    _TOGGLE_TIME = 0.05

    def __init__(
        self,
        name: str,
        coords: list[Vec3 | InteractMove],
    ):
        super().__init__(name, coords)
        self.timer = 0.0
        self.reasoner = None
        self.action = None

    # Override
    def navigate_to_checkpoint(self, delta: float) -> None:
        if combat_manager.encounter_done:
            # If there is no active fight, move along the designated path
            super().navigate_to_checkpoint(delta)
        else:
            # Manual control, do nothing
            self.execute_combat(delta)

    # Mash through cutscene while holding the turbo button
    def execute_combat(self, delta: float) -> bool:
        self.timer = self.timer + delta
        # if combat is done, just exit
        if combat_manager.encounter_done is True:
            return True

        # if reasoner doesn't exist, add it.
        if combat_manager.encounter_done is False and self.reasoner is None:
            self.reasoner = SoSReasoner(combat_manager)

        if (
            self.action is None or self.appraisal.complete
        ) and combat_manager.selected_character is not CombatCharacter.NONE:
            print("No action exists, executing one one")
            self.action = self.reasoner.execute()

        # For some reason the action isn't set, so bail out.
        if self.action is None:
            return True

        # do we need to navigate to an action?
        # if we are on the selected character, run the appraisal:
        if self.action.consideration.on_selected_character(
            combat_manager.selected_character, self.action
        ):
            # print("We're on our character, execute the appraisal")
            self.action.appraisal.execute()
            if self.action.appraisal.complete:
                # print("appraisal is complete, reset action")
                self.action = None
                return True

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

        # are we waiting for an attack to complete?

        # is an enemy attacking - do we need to defend?

        # execute consideration; it should know what states it expected
        # if consideration not executed, execute it
        #   - considerations must have actions, it will pop an action off the stack
        #     and run it so the ui is not blocked. once the stack is complete it will mark
        #     the consideration as completed and will continue on.
        # if consideration executed

        # Check if we have control
        return combat_manager.encounter_done is True

    def __repr__(self) -> str:
        return f"Mashing confirm while waiting for encounter ({self.name})..."
