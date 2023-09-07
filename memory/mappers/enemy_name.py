class EnemyName:
    NAMES = {
        # Mountain Trail
        "c3a2f1d99be4e0c42aca0ae1ff590028": "Wanderer",
        "fc2736fdbb731394c98da56e8f476d5e": "Rochèvre",
        # Moorlands
        "e6ac627711e4ee44da103c47d1cd5736": "Ant Bruiser",
        "2a9a0b40f493b11429febb5d927ef84b": "Srower",
    }

    def get(self, guid: str) -> str:
        return self.NAMES.get(guid)
