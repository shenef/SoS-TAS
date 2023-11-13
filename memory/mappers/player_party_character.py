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

        if ascii_data == b"Z\x00A\x00L\x00E\x00":
            return PlayerPartyCharacter.Zale
        if ascii_data == b"V\x00A\x00L\x00E\x00":
            return PlayerPartyCharacter.Valere
        if ascii_data == b"G\x00A\x00R\x00L\x00":
            return PlayerPartyCharacter.Garl
        if ascii_data == b"S\x00E\x00R\x00A\x00":
            return PlayerPartyCharacter.Serai
        if ascii_data == b"R\x00E\x00S\x00H\x00":
            return PlayerPartyCharacter.Reshan
        if ascii_data == b"B\x00S\x00T\x00\x00\x00":
            return PlayerPartyCharacter.Bst
        if ascii_data == b"M\x00A\x00S\x00T\x00":
            return PlayerPartyCharacter.Moraine
        return PlayerPartyCharacter.NONE
