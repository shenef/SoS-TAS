"""Routing-related sequencer nodes."""

import logging
from typing import Self

from engine.seq import SeqIf
from memory import (
    PlayerPartyCharacter,
    player_party_manager_handle,
)

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
