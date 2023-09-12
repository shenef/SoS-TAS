from typing import Self


class EnemyName:
    NAMES = {
        # Evermist Island: Mountain Trail
        "c3a2f1d99be4e0c42aca0ae1ff590028": "Wanderer",
        "fc2736fdbb731394c98da56e8f476d5e": "Rochèvre",
        # Sleeper Island: Moorlands
        "e6ac627711e4ee44da103c47d1cd5736": "Ant Bruiser",
        "2a9a0b40f493b11429febb5d927ef84b": "Srower",
        "d0f2cf59f69f42842ac0703193f39c85": "Salamander",
        "810980f005079324fb9fb643243eccee": "Malkomud",
        "fc51f181f5f913f4e99195da947b1425": "Malkomount",
        # Wraith Island: Haunted Mansion
        "64246a3a9059257409ea628466ced26e": "Botanical Horror",
        "3bbc6ad42918c444c9947d156e7674aa": "Bottom Flower",
        "621eeda6cacd76740b9b24518c3d211b": "Top Flower",
        "807fd9a36ea523f4aa7d532ddc565a69": "Dweller of Woe",
        "e1685476dd793e44c9c8909fe0b3622f": "DoW Clone",
        "bcde1eb0ea076f846a0ee20287d88204": "DoW Phase 2",
        "ec0b935c78a26044f89a236921671642": "Brugraves?",
        "1dc70fb2d0f1b374cbecf052b953824b": "Erlina?",
        # Watcher Island: Jungle Path
        "d34eee0d16a720248a3ce2e6ce2b108b": "Skullpion",
        "fb69218273345394baef9abf6fa9a345": "Prapra",
        "50229dee567088647809e9b737b397b7": "Croube",
        # Watcher Island: Torment Peak
        "40f05ed0202783449a704978e8670c9b": "Tsiclop",
        "c6f57cbee5d9cff4a82778ce36f94fdf": "Sleuth",
        "e79eceacb415fd04f84e6da6f9b23d3d": "BilePile",
    }

    def get(self: Self, guid: str) -> str:
        return self.NAMES.get(guid)
