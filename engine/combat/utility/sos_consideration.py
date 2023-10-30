import copy
from typing import Self

from control import sos_ctrl
from engine.combat.appraisals.basic_attack import BasicAttack
from engine.combat.appraisals.valere import CrescentArc, Moonerang
from engine.combat.appraisals.zale import Sunball
from engine.combat.utility.core.action import Action
from engine.combat.utility.core.consideration import Consideration
from engine.combat.utility.sos_appraisal import SoSAppraisal
from memory import CombatPlayer, PlayerPartyCharacter, combat_manager_handle
from memory.combat_manager import CombatDamageType

combat_manager = combat_manager_handle()


class SoSConsideration(Consideration):
    def __init__(self: Self, actor: CombatPlayer) -> None:
        self.actor = actor
        super().__init__()

    def generate_appraisals(self: Self) -> list[SoSAppraisal]:
        """Generate a list of appraisals for a character."""
        appraisals = self._default_appraisals() + self._character_appraisals()
        return list(filter(self._has_resources_for_appraisal, appraisals))

    def _has_resources_for_appraisal(self: Self, appraisal: SoSAppraisal) -> bool:
        boosts_available = round(combat_manager.small_live_mana / 5)
        if appraisal.boost > boosts_available:
            return False
        return appraisal.has_resources(self.actor)

    def valid(self: Self, selected_character: PlayerPartyCharacter, action: Action) -> bool:
        """Check if the consideration is valid."""
        return selected_character is PlayerPartyCharacter.NONE or self.on_selected_character(
            selected_character, action
        )

    def on_selected_character(
        self: Self, selected_character: PlayerPartyCharacter, action: Action
    ) -> bool:
        consideration: Self = action.consideration
        return selected_character is consideration.actor.character

    # TODO(eein): Add item appraisals + dont use physical attacks and the appraisal value
    def _default_appraisals(self: Self) -> list[SoSAppraisal]:
        """Generate default appraisals generic to every consideration."""
        match self.actor.character:
            case PlayerPartyCharacter.Zale:
                primary_damage_type = CombatDamageType.Sword
                secondary_damage_type = CombatDamageType.Sun
            case PlayerPartyCharacter.Valere:
                primary_damage_type = CombatDamageType.Blunt
                secondary_damage_type = CombatDamageType.Moon
            case PlayerPartyCharacter.Garl:
                primary_damage_type = CombatDamageType.Blunt
                secondary_damage_type = CombatDamageType.NONE
            case PlayerPartyCharacter.Serai:
                primary_damage_type = CombatDamageType.Sword
                secondary_damage_type = CombatDamageType.Poison
            case PlayerPartyCharacter.Reshan:
                primary_damage_type = CombatDamageType.Poison
                secondary_damage_type = CombatDamageType.Arcane
            case PlayerPartyCharacter.Bst:
                primary_damage_type = CombatDamageType.Blunt
                secondary_damage_type = CombatDamageType.Arcane
        # TODO(orkaboy): Should account for gear too; this should probably be a function?
        basic_attack = BasicAttack(primary_damage_type=primary_damage_type)
        basic_attack.value = self.actor.physical_attack

        attacks = [basic_attack]
        for boost in range(1, 4):  # Generate [1,2,3]
            boosted_attack = BasicAttack(
                boost=boost,
                primary_damage_type=primary_damage_type,
                secondary_damage_type=secondary_damage_type,
            )
            # TODO(orkaboy): Correct damage formula
            boosted_attack.value = (
                self.actor.physical_attack + boost * self.actor.magical_attack / 3
            )
            attacks.append(boosted_attack)

        return attacks

    # TODO(eein): Calculate appraisals based on skill/combo availability
    def _character_appraisals(self: Self) -> list[SoSAppraisal]:
        appraisals: list[SoSAppraisal] = []
        # Generate appraisals based on boost level (0-3)
        for boost in range(0, 4):
            # Create a list of appraisals based on the character acting
            char_appraisals: list[SoSAppraisal] = []
            match self.actor.character:
                case PlayerPartyCharacter.Zale:
                    char_appraisals.append(Sunball(value=100))
                case PlayerPartyCharacter.Valere:
                    # Currently set up to use moonerang if there is only one enemy
                    enemy_count = 0
                    for enemy in combat_manager.enemies:
                        if enemy.current_hp > 0:
                            enemy_count += 1
                    if enemy_count == 1:
                        char_appraisals.append(Moonerang(value=200))
                    char_appraisals.append(CrescentArc(value=100))
                # TODO(orkaboy): Add more skills/characters
            # TODO(orkaboy): For now, multiply utility by boost value
            for appraisal in char_appraisals:
                appraisal.value *= boost + 1
            appraisals.extend(char_appraisals)
        return appraisals

    def calculate_actions(self: Self) -> list[Action]:
        actions = []
        # Takes the appraisals, and creates an action for each enemy.
        for appraisal in self.appraisals:
            for enemy in combat_manager.enemies:
                new_appraisal: SoSAppraisal = copy.copy(appraisal)
                # Adjust value according to if we can break locks
                damage_type: list[CombatDamageType] = copy.copy(new_appraisal.damage_type)
                lock_multiplier = 1.0
                for lock in enemy.spell_locks:
                    if lock in damage_type:
                        damage_type.remove(lock)
                        lock_multiplier += 1.0
                # Make a unique action for each appraisal and enemy combination
                new_appraisal.value *= lock_multiplier
                new_appraisal.target = enemy.unique_id
                actions.append(copy.copy(Action(self, new_appraisal)))
        return actions

    def execute(self: Self) -> None:
        """
        Execute on selecting the consideration to perform the appraisal.

        This should select the character based on the memory. Just pressing left for now.
        """
        sos_ctrl().dpad.tap_left()

    def __repr__(self: Self) -> str:
        return self.actor.character.name
