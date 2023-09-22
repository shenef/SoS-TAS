from typing import Self

from data.enemy.base import BaseEnemy


class HalfSunken_Gulgul(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "HalfSunken_Gulgul"
        self.guid = "9e34c0f2e5678124f8e503389bd174be"
        self.hp = 222
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 95
        self.magic_defense = 50
        self.magic_attack = 95
        self.level = 20
        self.fleshmancer_minion = True
