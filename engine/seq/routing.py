import logging
from typing import Self

from engine.seq import SeqIf
from memory import (
    PlayerPartyCharacter,
    player_party_manager_handle,
)

logger = logging.getLogger(__name__)


class SeqIfMainCharacterValere(SeqIf):
    def condition(self: Self) -> bool:
        leader = player_party_manager_handle().leader_character
        if leader == PlayerPartyCharacter.Valere:
            return True
        if leader == PlayerPartyCharacter.Zale:
            return False
        return None
