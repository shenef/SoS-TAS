from engine.combat.appraisals.basic_attack import BasicAttack
from engine.combat.utility.core.action import Action
from engine.combat.utility.core.consideration import Consideration
from memory.combat_manager import CombatCharacter


class SoSConsideration(Consideration):
    # Generates a list of appraisals for a character.
    def generate_appraisals(self):
        return self._default_appraisals() + self._character_appraisals()

    # Generates default appraisals generic to every consideration
    # TODO: Add items?
    def _default_appraisals(self):
        basic_attack = BasicAttack()
        # TODO: Dont use this as the value.
        basic_attack.value = self.actor.physical_attack

        return [basic_attack]

    # TODO: Actually make character appraisals. For now we're just doing basic attacks
    def _character_appraisals(self):
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
    def calculate_actions(self):
        # if the actor isn't enabled, return no actions
        if not self.actor.enabled:
            return []

        actions = []
        for appraisal in self.appraisals:
            # TODO: calculate this for every enemy.
            actions.append(Action(self, appraisal))
        return actions

    # execute on selecting the consideration to perform the appraisal
    def execute(self, _handle):
        # This should select the character based on the memory
        pass
