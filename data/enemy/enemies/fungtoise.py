from typing import Self

from data.enemy.base import BaseEnemy


class Fungtoise(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "Fungtoise"
        self.guid = "0af340a99d84e2f4a98c5d9b617fe0ea"
        self.hp = 188
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 70
        self.magic_defense = 50
        self.magic_attack = 95
        self.level = 12
        self.fleshmancer_minion = True
