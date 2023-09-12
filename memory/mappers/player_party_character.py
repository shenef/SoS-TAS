from enum import Enum


class PlayerPartyCharacter(Enum):
    NONE = "None"
    Zale = "Zale"
    Valere = "Valere"
    Garl = "Garl"
    Serai = "Seraï"
    Reshan = "Resh'an"

    def parse_definition_id(definition_id):
        asciidata = definition_id.encode("ascii", "ignore")

        if asciidata == b"Z\x00A\x00L\x00E\x00":
            return PlayerPartyCharacter.Zale
        if asciidata == b"V\x00A\x00L\x00E\x00":
            return PlayerPartyCharacter.Valere
        if asciidata == b"G\x00A\x00R\x00L\x00":
            return PlayerPartyCharacter.Garl
        if asciidata == b"S\x00E\x00R\x00A\x00":
            return PlayerPartyCharacter.Serai
        if asciidata == b"R\x00E\x00S\x00H\x00":
            return PlayerPartyCharacter.Reshan
        return PlayerPartyCharacter.NONE
