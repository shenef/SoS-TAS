from typing import Self

from data.enemy.base import BaseEnemy


class DrillBat(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "DrillBat"
        self.guid = "fd131c994e11300458464a864480d743"
        self.hp = 44
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 9
        self.magic_defense = 90
        self.magic_attack = 20
        self.level = 5
        self.fleshmancer_minion = True
