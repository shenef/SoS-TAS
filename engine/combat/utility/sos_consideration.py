from typing import Self

from control import sos_ctrl
from engine.combat.appraisals.basic_attack import BasicAttack
from engine.combat.appraisals.valere.moonerang import Moonerang
from engine.combat.appraisals.zale.sunball import Sunball
from engine.combat.utility.core.action import Action
from engine.combat.utility.core.appraisal import Appraisal
from engine.combat.utility.core.consideration import Consideration
from memory import CombatPlayer, PlayerPartyCharacter


class SoSConsideration(Consideration):
    def __init__(self: Self, actor: CombatPlayer) -> None:
        self.actor = actor
        super().__init__()

    # Generates a list of appraisals for a character.
    def generate_appraisals(self: Self) -> list[Appraisal]:
        appraisals = self._default_appraisals() + self._character_appraisals()
        return list(filter(self._has_resources_for_appraisal, appraisals))

    def _has_resources_for_appraisal(self: Self, appraisal: Appraisal) -> bool:
        return appraisal.has_resources(self.actor)

    # if the selected character is NONE or we are on the selected character, considered valid'
    # and do nothing else here.
    def valid(
        self: Self, selected_character: PlayerPartyCharacter, action: Action
    ) -> bool:
        return (
            selected_character is PlayerPartyCharacter.NONE
            or self.on_selected_character(selected_character, action)
        )

    def on_selected_character(
        self: Self, selected_character: PlayerPartyCharacter, action: Action
    ) -> bool:
        actor: CombatPlayer = action.consideration.actor
        return selected_character is actor.character

    # Generates default appraisals generic to every consideration
    # TODO(eein): Add item appraisals + dont use physical attacks and the appraisal value
    def _default_appraisals(self: Self) -> list[Appraisal]:
        basic_attack = BasicAttack()
        basic_attack.value = self.actor.physical_attack

        return [basic_attack]

    def _character_appraisals(self: Self) -> list[Appraisal]:
        match self.actor.character:
            case PlayerPartyCharacter.Zale:
                return [Sunball()]
            case PlayerPartyCharacter.Valere:
                return [Moonerang()]
            case PlayerPartyCharacter.Garl:
                return []
            case _:
                return []

    def calculate_actions(self: Self) -> list[Action]:
        # if the actor isn't enabled, return no actions
        actions = []
        for appraisal in self.appraisals:
            # TODO(eein): calculate this for every enemy.
            actions.append(Action(self, appraisal))
        return actions

    # execute on selecting the consideration to perform the appraisal
    def execute(self: Self) -> None:
        # This should select the character based on the memory
        # just press left for now
        sos_ctrl().dpad.tap_left()
