from typing import Self

from data.enemy.base import BaseEnemy


class SunboyEnemy(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "SunboyEnemy"
        self.guid = "f0a9344cdf22e654c9e3c6ef7b1508d6"
        self.hp = 210
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 55
        self.magic_defense = 50
        self.magic_attack = 55
        self.level = 1
        self.fleshmancer_minion = True
