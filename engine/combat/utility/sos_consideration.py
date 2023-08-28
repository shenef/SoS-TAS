from control import sos_ctrl
from engine.combat.appraisals.basic_attack import BasicAttack
from engine.combat.utility.core.action import Action
from engine.combat.utility.core.appraisal import Appraisal
from engine.combat.utility.core.consideration import Consideration
from memory.combat_manager import CombatCharacter


class SoSConsideration(Consideration):
    # Generates a list of appraisals for a character.
    def generate_appraisals(self) -> list[Appraisal]:
        return self._default_appraisals() + self._character_appraisals()

    # if the selected character is NONE or we are on the selected character, considered valid'
    # and do nothing else here.
    def valid(self, selected_character: CombatCharacter, action: Action) -> bool:
        return selected_character is CombatCharacter.NONE or self.on_selected_character(
            selected_character, action
        )

    def on_selected_character(self, selected_character, action) -> bool:
        return selected_character is action.consideration.actor.character

    # Generates default appraisals generic to every consideration
    # TODO: Add items?
    def _default_appraisals(self) -> list[Appraisal]:
        basic_attack = BasicAttack()
        # TODO: Dont use this as the value.
        basic_attack.value = self.actor.physical_attack

        return [basic_attack]

    # TODO: Actually make character appraisals. For now we're just doing basic attacks
    def _character_appraisals(self) -> list[Appraisal]:
        match self.actor.character:
            case CombatCharacter.Zale:
                return []
            case CombatCharacter.Valere:
                return []
            case CombatCharacter.Garl:
                return []
            case _:
                return []

    # TODO: Actually calculate appraisals and dont just use
    # physical attack. This will require parsing all of the appraisals
    # for the value and returning an Action
    def calculate_actions(self) -> [Action]:
        # if the actor isn't enabled, return no actions
        actions = []
        for appraisal in self.appraisals:
            # TODO: calculate this for every enemy.
            actions.append(Action(self, appraisal))
        return actions

    # execute on selecting the consideration to perform the appraisal
    def execute(self):
        # This should select the character based on the memory
        # just press left for now
        sos_ctrl().dpad.tap_left()
