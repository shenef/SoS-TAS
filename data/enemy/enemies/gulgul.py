from typing import Self

from data.enemy.base import BaseEnemy


class Gulgul(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "Gulgul"
        self.guid = "4cc1949eb31a81a4782b1075c32d268e"
        self.hp = 49
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 49
        self.magic_defense = 50
        self.magic_attack = 15
        self.level = 7
        self.fleshmancer_minion = True
