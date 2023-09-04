from enum import Enum


class PlayerPartyCharacter(Enum):
    NONE = "None"
    Zale = "Zale"
    Valere = "Valere"
    Garl = "Garl"
    _SPOILERS = "_SPOILERS"

    def parse_definition_id(definition_id):
        match definition_id:
            case str(x) if "Z" in x:
                return PlayerPartyCharacter.Zale
            case str(x) if "V" in x:
                return PlayerPartyCharacter.Valere
            case str(x) if "G" in x:
                return PlayerPartyCharacter.Garl
            case str(x) if "S" in x:
                return PlayerPartyCharacter._SPOILERS
            case str(x) if "R" in x:
                return PlayerPartyCharacter._SPOILERS
