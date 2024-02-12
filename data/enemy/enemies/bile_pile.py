from typing import Self

from data.enemy.base import BaseEnemy


class BilePile(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "BilePile"
        self.guid = "e79eceacb415fd04f84e6da6f9b23d3d"
        self.hp = 499
        self.speed = 20
        self.physical_defense = 90
        self.physical_attack = 75
        self.magic_defense = 50
        self.magic_attack = 40
        self.level = 13
        self.fleshmancer_minion = True
