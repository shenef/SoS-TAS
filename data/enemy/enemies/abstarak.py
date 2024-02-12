from typing import Self

from data.enemy.base import BaseEnemy


class Abstarak(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "Abstarak"
        self.guid = "f4032b2323bc31d4590cf5197db3c3f1"
        self.hp = 920
        self.speed = 0
        self.physical_defense = 90
        self.physical_attack = 95
        self.magic_defense = 50
        self.magic_attack = 110
        self.level = 1
        self.fleshmancer_minion = True
