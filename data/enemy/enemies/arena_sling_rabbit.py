from typing import Self

from data.enemy.base import BaseEnemy


class ArenaSlingRabbit(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "ArenaSlingRabbit"
        self.guid = "2ef49b6d9ec8fd64f95c49e951c1c8bc"
        self.hp = 311
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 160
        self.magic_defense = 50
        self.magic_attack = 80
        self.level = 14
        self.fleshmancer_minion = True
