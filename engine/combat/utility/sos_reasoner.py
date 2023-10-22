import logging
from typing import Self

from engine.combat.contexts.reasoner_execution_context import ReasonerExecutionContext
from engine.combat.utility.core.action import Action
from engine.combat.utility.core.consideration import Consideration
from engine.combat.utility.core.reasoner import Reasoner
from engine.combat.utility.sos_consideration import SoSConsideration
from memory import CombatEnemyTarget, CombatPlayer, combat_manager_handle

logger = logging.getLogger(__name__)
combat_manager = combat_manager_handle()


class SoSReasoner(Reasoner):
    def __init__(self: Self, reasoner_execution_context: ReasonerExecutionContext) -> None:
        """Initialize a new SoSReasoner object."""
        self.reasoner_execution_context = reasoner_execution_context
        self.considerations = []

    def generate_considerations(self: Self, players: list[CombatPlayer]) -> list[Consideration]:
        """Generate considerations for all targets."""
        considerations = []
        for player in players:
            if self._can_generate_consideration_for_player(player):
                considerations.append(SoSConsideration(player))
        return considerations

    def execute(self: Self) -> Action:
        """Generate considerations and select an action off the top of the stack."""
        self.considerations = self.generate_considerations(combat_manager.players)
        return self._select_action()

    def _select_action(self: Self) -> Action:
        """Calculate value for each consideration and return the highest value action."""
        actions = []
        for consideration in self.considerations:
            calculated_actions = consideration.calculate_actions()
            actions.extend(calculated_actions)

        if actions == []:
            return None

        # sort and return the results by their value in desc order
        actions.sort(key=lambda action: action.appraisal.value, reverse=True)

        # filter enemies with no HP (elder mist & botanical horror)
        actions = self._filter_disabled_enemies(actions)

        # if we have priority targets, then filter out any actions that don't target them
        if self.reasoner_execution_context.priority_targets is not []:
            actions = self._filter_priority_targets(actions)

        if len(actions) == 0:
            return None
        return actions[0]

    def _can_generate_consideration_for_player(self: Self, player: CombatPlayer) -> bool:
        """Check if we can generate a consideration for a player."""
        if player.dead or not player.enabled:
            return False
        return True

    def _filter_priority_targets(self: Self, actions: list[Action]) -> list[Action]:
        """Filter out actions that don't target priority targets."""
        for enemy in combat_manager.enemies:
            if (
                self._enemy_is_active(enemy)
                and enemy.guid in self.reasoner_execution_context.priority_targets
            ):
                return list(filter(lambda a: a.appraisal.target == enemy.unique_id, actions))
        return actions

    def _filter_disabled_enemies(self: Self, actions: list[Action]) -> list[Action]:
        """Filter out actions that don't target active targets."""
        for enemy in combat_manager.enemies:
            if not self._enemy_is_active(enemy):
                actions = list(filter(lambda a: a.appraisal.target != enemy.unique_id, actions))
        return actions

    def _enemy_is_active(self: Self, enemy: CombatEnemyTarget) -> bool:
        """Check if an enemy is active."""
        return enemy.current_hp > 0
