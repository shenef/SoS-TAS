import unittest
from typing import Self

from engine.combat.utility.sos_reasoner import SoSReasoner
from memory.combat_manager import CombatManager, CombatPlayer
from memory.mappers.player_party_character import PlayerPartyCharacter

# This test file is simply for testing Utility AI outside of the game
# so time isn't wasted restarting the game on guesses
# Below it mocks some information for use in test

combat_manager = CombatManager()

zale = CombatPlayer()
zale.current_mp = 6
zale.physical_attack = 9
zale.magical_attack = 13  # TODO(orkaboy): Maybe not correct
zale.selected = False
zale.character = PlayerPartyCharacter.Zale
zale.definition_id = "zale"
zale.enabled = True

valere = CombatPlayer()
valere.current_mp = 6
valere.physical_attack = 10
valere.magical_attack = 11  # TODO(orkaboy): Maybe not correct
valere.selected = False
valere.character = PlayerPartyCharacter.Valere
valere.definition_id = "valere"
valere.enabled = True

garl = CombatPlayer()
garl.current_mp = 6
garl.physical_attack = 12
garl.magical_attack = 9  # TODO(orkaboy): Maybe not correct
garl.selected = False
garl.character = PlayerPartyCharacter.Garl
garl.definition_id = "garl"
garl.enabled = True

combat_manager.players = [zale, valere, garl]


# This is a sanity class for testing the combat controller and the
class TestCombatUtility(unittest.TestCase):
    def test_create(self: Self) -> None:
        reasoner = SoSReasoner(combat_manager)
        # Ensure considerations are generated
        self.assertEqual(len(reasoner.considerations), 3)
        for consideration in reasoner.considerations:
            self.assertTrue(len(consideration.appraisals) > 0)

    # Because Basic Attack is the only appraisal, we expect
    # The selection process to pick Garl.
    # This will have to be optimized to calculate damage to enemies and
    # make a distinction later, but for now, it will just pick whoever
    # has the highest physical attack.

    def test_consideration_selection(self: Self) -> None:
        reasoner = SoSReasoner(combat_manager)
        action = reasoner._select_action()
        self.assertEqual(action.consideration.actor.character, PlayerPartyCharacter.Garl)

        # With garl disabled, it should always pick valere
        garl.enabled = False
        action = reasoner._select_action()
        self.assertEqual(action.consideration.actor.character, PlayerPartyCharacter.Valere)

        # With valere disabled as well, it will pick zale
        valere.enabled = False
        action = reasoner._select_action()
        self.assertEqual(action.consideration.actor.character, PlayerPartyCharacter.Zale)
