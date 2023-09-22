from typing import Self

from data.enemy.base import BaseEnemy


class CukooMonster(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "CukooMonster"
        self.guid = "3e00a15f95b3e1d4cb68e71021579758"
        self.hp = 105
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 60
        self.magic_defense = 50
        self.magic_attack = 0
        self.level = 13
        self.fleshmancer_minion = True
