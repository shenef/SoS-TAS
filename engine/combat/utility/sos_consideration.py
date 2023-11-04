import copy
from typing import Self

from control import sos_ctrl
from engine.blackboard import blackboard
from engine.combat.appraisals.basic_attack import BasicAttack
from engine.combat.appraisals.combos import SolarRain, SolsticeStrike, XStrike
from engine.combat.appraisals.serai import Disorient, PhaseShiv, VenomFlurry
from engine.combat.appraisals.valere import CrescentArc, Moonerang
from engine.combat.appraisals.zale import DashStrike, Sunball
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
        attacks: list[BasicAttack] = []
        for boost in range(0, 4):  # Generate [0,1,2,3]
            basic_attack = BasicAttack(
                caster=self.actor.character,
                boost=boost,
            )
            # TODO(orkaboy): Should account for gear too; this should probably be a function?
            # TODO(orkaboy): Correct damage formula
            if boost == 0:
                basic_attack.value = self.actor.physical_attack
            else:
                basic_attack.value = (
                    self.actor.physical_attack + boost * self.actor.magical_attack / 3
                )
            attacks.append(basic_attack)

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
                    # Logic for handling learning Dash Strike
                    has_dash_strike = blackboard().get_dict(key="dash_strike", default=False)
                    sunball_index = 1
                    if has_dash_strike:
                        sunball_index = 2
                    char_appraisals.append(
                        Sunball(value=100, boost=boost, skill_command_index=sunball_index)
                    )
                    if has_dash_strike:
                        char_appraisals.append(DashStrike(value=50, boost=boost))
                    # Combos
                    solstice_strike = SolsticeStrike(
                        main_caster=self.actor.character, value=100, boost=boost
                    )
                    if solstice_strike.can_use():
                        char_appraisals.append(solstice_strike)
                    # Logic for handling learning Combos
                    # TODO(orkaboy): Activate these. Need to be able to swap characters
                    if False:
                        has_solar_rain = blackboard().get_dict(key="solar_rain", default=False)
                        has_x_strike = blackboard().get_dict(key="x_strike", default=False)
                        x_strike_index = 2
                        if has_solar_rain:
                            x_strike_index += 1
                            char_appraisals.append(
                                SolarRain(value=200, boost=boost, skill_command_index=2)
                            )
                        if has_x_strike:
                            char_appraisals.append(
                                XStrike(value=150, boost=boost, skill_command_index=x_strike_index)
                            )
                case PlayerPartyCharacter.Valere:
                    # Currently set up to use moonerang if there is only one enemy
                    enemy_count = 0
                    for enemy in combat_manager.enemies:
                        if enemy.current_hp > 0:
                            enemy_count += 1
                    if enemy_count == 1:
                        char_appraisals.append(Moonerang(value=200, boost=boost))
                    char_appraisals.append(CrescentArc(value=100, boost=boost))
                    # Combos
                    solstice_strike = SolsticeStrike(
                        main_caster=self.actor.character, value=100, boost=boost
                    )
                    if solstice_strike.can_use():
                        char_appraisals.append(solstice_strike)
                case PlayerPartyCharacter.Garl:
                    # Logic for handling learning Solar Rain
                    has_solar_rain = blackboard().get_dict(key="solar_rain", default=False)
                    if has_solar_rain:
                        char_appraisals.append(
                            SolarRain(value=200, boost=boost, skill_command_index=0)
                        )
                case PlayerPartyCharacter.Serai:
                    # TODO(orkaboy): Activate these. Need to be able to swap characters
                    # TODO(orkaboy): Need to increase value on Disorient based on locks/turns
                    # TODO(orkaboy): Balance value
                    if False:
                        char_appraisals.extend(
                            (
                                Disorient(value=100, boost=boost),
                                VenomFlurry(value=100, boost=boost),
                                PhaseShiv(value=150, boost=boost),
                            )
                        )
                        has_x_strike = blackboard().get_dict(key="x_strike", default=False)
                        if has_x_strike:
                            char_appraisals.append(
                                XStrike(value=150, boost=boost, skill_command_index=0)
                            )
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
                lock_multiplier = 1.0
                num_enemy_locks = len(enemy.spell_locks)
                # Sometimes locks remain after action has been taken, so check first.
                if num_enemy_locks > 0 and enemy.turns_to_action > 0:
                    damage_type: list[CombatDamageType] = copy.copy(new_appraisal.damage_type)
                    for lock in enemy.spell_locks:
                        if lock in damage_type:
                            damage_type.remove(lock)
                            lock_multiplier += 1.0
                            num_enemy_locks -= 1
                    # Further reward clearing all locks on an enemy.
                    if num_enemy_locks == 0:
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
