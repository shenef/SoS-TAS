"""Routing-related sequencer nodes."""

import logging
from enum import Enum, auto
from typing import Self

from config import get_route_config
from engine.seq import SeqIf
from memory import (
    PlayerPartyCharacter,
    player_party_manager_handle,
)

from .base import SeqBase

logger = logging.getLogger(__name__)


class SeqIfMainCharacterValere(SeqIf):
    """A conditional node that runs different branches depending on the active main character."""

    def condition(self: Self) -> bool:
        """Select `when_true` branch if Valere is main character, and `when_false` for Zale."""
        leader = player_party_manager_handle().leader_character
        if leader == PlayerPartyCharacter.Valere:
            return True
        if leader == PlayerPartyCharacter.Zale:
            return False
        return None


class RouteBranchMode(Enum):
    """Enum for how multiple route conditions interact for `SeqRouteBranch`."""

    OR = auto()
    AND = auto()


class SeqRouteBranch(SeqIf):
    """A conditional node that only runs if a set of route configuration conditions apply."""

    def __init__(
        self: Self,
        name: str,
        when_true: SeqBase,
        when_false: SeqBase,
        route: list[str],
        mode: RouteBranchMode = RouteBranchMode.OR,
    ) -> None:
        super().__init__(name, when_true, when_false)
        self.route = route
        self.mode = mode

    def condition(self: Self) -> bool:
        """Select `when_true` branch when the route conditions are active."""
        route_config = get_route_config()
        match self.mode:
            case RouteBranchMode.OR:
                ret = False
                for route in self.route:
                    if route_config.get(route, False):
                        ret = True
                return ret
            case RouteBranchMode.AND:
                ret = True
                for route in self.route:
                    if route_config.get(route, False) is False:
                        ret = False
                return ret
            case _:
                return False
