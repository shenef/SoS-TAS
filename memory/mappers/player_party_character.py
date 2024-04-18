from enum import Enum
from typing import Self


class PlayerPartyCharacter(Enum):
    """Definitions for a character that can be in your party."""

    NONE = "None"
    Zale = "Zale"
    Valere = "Valere"
    Garl = "Garl"
    Serai = "Seraï"
    Reshan = "Resh'an"
    Bst = "B'st"
    Moraine = "Moraine"

    def parse_definition_id(definition_id: str) -> Self:
        ascii_data = definition_id.encode("ascii", "ignore")

        if ascii_data == b"ZALE":
            return PlayerPartyCharacter.Zale
        if ascii_data == b"VALE":
            return PlayerPartyCharacter.Valere
        if ascii_data == b"GARL":
            return PlayerPartyCharacter.Garl
        if ascii_data == b"SERA":
            return PlayerPartyCharacter.Serai
        if ascii_data == b"RESH":
            return PlayerPartyCharacter.Reshan
        if ascii_data == b"BST":
            return PlayerPartyCharacter.Bst
        if ascii_data == b"MAST":
            return PlayerPartyCharacter.Moraine
        return PlayerPartyCharacter.NONE
