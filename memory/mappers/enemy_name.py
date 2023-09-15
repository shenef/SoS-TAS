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
        # Mesa Island: Glacial Peak
        "a1a5c1333a1e7fe4f98de4d28b3b9900": "Rochecrossidere",
        "33a6c54c83b68894a93b46c02da7fbc8": "Boulder Douche",
        # Mesa Island: Autumn Hills
        "51b36d4dce9be614f95e77477caecace": "Tock",
        "2c78ebcab00eb2c4daef5082c88503cc": "Grassassin",
        "c99b902697c6f734f9fc64b421c06728": "Leaf Monster",
        # Mesa Island: Songshroom Marsh
        "0af340a99d84e2f4a98c5d9b617fe0ea": "Fungtoise",
        "acf70102f6cc47e41b953fc2c44ad802": "Shroomy Shroomy Knight",
        # Mesa Island: Clockwork Castle
        "3e00a15f95b3e1d4cb68e71021579758": "Cukoo Monster",
        "090c2ec246656b643a5d1e5b0bb3db28": "Clock Zombie",
        "ffe45f0323cb8924e8296b7cc86d9d1b": "Strife Minion",
        "a5d39cc10d1848d478b59c892f636e3b": "Dweller of Strife",
        # The Acolytes
        "76c4290aa2a896b4cb405e5a2d29b3a0": "One",
        "73c4c0922e5ae274eb759f86702353a8": "Two",
        "e77c07b22ee83854e8c006101ef5731f": "Three",
        "0c831eb6bc1c0c648828b405cb8c0667": "Four",
        # Skylands
        "4e00be6b55350d64090bff46533eb2aa": "SlingRabbit",
        "9cbcb4063d9b8d8448cf96a2c14a6826": "Braidzard",
    }

    def get(self: Self, guid: str) -> str:
        return self.NAMES.get(guid)
