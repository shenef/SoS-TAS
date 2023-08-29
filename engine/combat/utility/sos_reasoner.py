from engine.combat.utility.core.reasoner import Reasoner
from engine.combat.utility.core.action import Action
from engine.combat.utility.core.consideration import Consideration
from memory.combat_manager import CombatPlayer
from typing import List

class SoSReasoner(Reasoner):
    def __init__(self, combat_manager_handle):
        self.combat_manager_handle = combat_manager_handle
        self.considerations = []

    def generate_considerations(self, players: List(CombatPlayer)) -> List[Consideration]:
        considerations = []
        for player in players:
            if not player.dead and player.enabled:
                considerations.append(Consideration(player))
        return considerations

    def execute(self) -> Action:
        self.considerations = self.generate_considerations(
            self.combat_manager_handle.players
        )
        return self._select_action()

    def _select_action(self) -> Action:
        # go through each consideration and calculate its value
        # TODO: Optimize, do not calculate values for dead/disabled characters
        actions = []
        for consideration in self.considerations:
            calculated_actions = consideration.calculate_actions()
            actions.extend(calculated_actions)

        if actions == []:
            return None
        # sort and return the results by their value in desc order
        actions.sort(key=lambda action: action.appraisal.value, reverse=True)

        return actions[0]
