class EnemyName:
    NAMES = {
        # Moorlands
        "e6ac627711e4ee44da103c47d1cd5736": "Ant Bruiser",
        "2a9a0b40f493b11429febb5d927ef84b": "Srower",
    }

    def get(self, guid: str) -> str:
        return self.NAMES.get(guid)
