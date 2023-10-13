import copy
from typing import Self

from control import sos_ctrl
from engine.combat.appraisals.basic_attack import BasicAttack
from engine.combat.appraisals.valere import CrescentArc, Moonerang
from engine.combat.appraisals.zale import Sunball
from engine.combat.utility.core.action import Action
from engine.combat.utility.core.appraisal import Appraisal
from engine.combat.utility.core.consideration import Consideration
from memory import CombatPlayer, PlayerPartyCharacter, combat_manager_handle

combat_manager = combat_manager_handle()


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
    def valid(self: Self, selected_character: PlayerPartyCharacter, action: Action) -> bool:
        return selected_character is PlayerPartyCharacter.NONE or self.on_selected_character(
            selected_character, action
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
    
    # TODO(eein): Calculate appraisals based on skill/combo availability
    def _character_appraisals(self: Self) -> list[Appraisal]:
        match self.actor.character:
            case PlayerPartyCharacter.Zale:
                return [Sunball(value=100)]
            case PlayerPartyCharacter.Valere:
                # Currently set up to use moonerang if there is only one enemy
                if len(combat_manager.enemies) == 1:
                    return [Moonerang(value=200)]
                return [CrescentArc(value=100)]
            case PlayerPartyCharacter.Garl:
                return []
            case _:
                return []

    def calculate_actions(self: Self) -> list[Action]:
        # if the actor isn't enabled, return no actions
        actions = []

        for appraisal in self.appraisals:
            for enemy in combat_manager.enemies:
                new_appraisal = copy.copy(appraisal)
                new_appraisal.target = enemy.unique_id
                actions.append(copy.copy(Action(self, new_appraisal)))
        return actions

    # execute on selecting the consideration to perform the appraisal
    def execute(self: Self) -> None:
        # This should select the character based on the memory
        # just press left for now
        sos_ctrl().dpad.tap_left()
