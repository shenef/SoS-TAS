from typing import Self


class BaseEnemy:
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "UnknownEnemy"
        self.guid = "NONE"
        self.hp = 0
        self.speed = 0
        self.physical_defense = 0
        self.physical_attack = 0
        self.magic_defense = 0
        self.magic_attack = 0
        self.level = 0
        self.fleshmancer_minion = False
