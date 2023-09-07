class EnemyName:
    NAMES = {
        # Evermist Island: Mountain Trail
        "c3a2f1d99be4e0c42aca0ae1ff590028": "Wanderer",
        "fc2736fdbb731394c98da56e8f476d5e": "Rochèvre",
        # Sleeper Island: Moorlands
        "e6ac627711e4ee44da103c47d1cd5736": "Ant Bruiser",
        "2a9a0b40f493b11429febb5d927ef84b": "Srower",
        # Watcher Island: Jungle Path
        "d34eee0d16a720248a3ce2e6ce2b108b": "Skullpion",
        "fb69218273345394baef9abf6fa9a345": "Prapra",
        "50229dee567088647809e9b737b397b7": "Croube",
        # Watcher Island: Torment Peak
        "40f05ed0202783449a704978e8670c9b": "Tsiclop",
        "c6f57cbee5d9cff4a82778ce36f94fdf": "Sleuth",
        "e79eceacb415fd04f84e6da6f9b23d3d": "BilePile",
    }

    def get(self, guid: str) -> str:
        return self.NAMES.get(guid)
