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

    def generate_appraisals(self: Self) -> list[Appraisal]:
        """Generate a list of appraisals for a character."""
        appraisals = self._default_appraisals() + self._character_appraisals()
        return list(filter(self._has_resources_for_appraisal, appraisals))

    def _has_resources_for_appraisal(self: Self, appraisal: Appraisal) -> bool:
        return appraisal.has_resources(self.actor)

    def valid(self: Self, selected_character: PlayerPartyCharacter, action: Action) -> bool:
        """Check if the consideration is valid."""
        return selected_character is PlayerPartyCharacter.NONE or self.on_selected_character(
            selected_character, action
        )

    def on_selected_character(
        self: Self, selected_character: PlayerPartyCharacter, action: Action
    ) -> bool:
        actor: CombatPlayer = action.consideration.actor
        return selected_character is actor.character

    # TODO(eein): Add item appraisals + dont use physical attacks and the appraisal value
    def _default_appraisals(self: Self) -> list[Appraisal]:
        """Generate default appraisals generic to every consideration."""
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
                enemy_count = 0
                for enemy in combat_manager.enemies:
                    if enemy.current_hp > 0:
                        enemy_count += 1
                if enemy_count == 1:
                    return [Moonerang(value=200)]
                return [CrescentArc(value=100)]
            case PlayerPartyCharacter.Garl:
                return []
            case _:
                return []

    def calculate_actions(self: Self) -> list[Action]:
        actions = []
        # TODO(eein): To give value to boosted appraisals we will just multiply the value by
        # the boost for now, we can modify this when we work further on utility.
        boosted_appraisals = []
        for appraisal in self.appraisals:
            boosts_available = round(combat_manager.small_live_mana / 5)
            if boosts_available == 0:
                boosted_appraisals.append(appraisal)
                continue

            for boost in range(0, boosts_available + 1):
                new_appraisal = copy.copy(appraisal)
                new_appraisal.boost = boost
                new_appraisal.value = new_appraisal.value * (boost + 1)
                boosted_appraisals.append(new_appraisal)

        # Takes the boosted appraisals, and creates an action for each enemy.
        for appraisal in boosted_appraisals:
            for enemy in combat_manager.enemies:
                new_appraisal = copy.copy(appraisal)
                new_appraisal.target = enemy.unique_id
                actions.append(copy.copy(Action(self, new_appraisal)))
        return actions

    def execute(self: Self) -> None:
        """
        Execute on selecting the consideration to perform the appraisal.

        This should select the character based on the memory. Just pressing left for now.
        """
        sos_ctrl().dpad.tap_left()
