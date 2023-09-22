from typing import Self

from data.enemy.base import BaseEnemy


class Luslug(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "Luslug"
        self.guid = "f526fdd8553bd7344a34243f16f8fc96"
        self.hp = 16
        self.speed = 100
        self.physical_defense = 75
        self.physical_attack = 10
        self.magic_defense = 50
        self.magic_attack = 0
        self.level = 1
        self.fleshmancer_minion = True
