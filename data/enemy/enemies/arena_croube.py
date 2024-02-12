from typing import Self

from data.enemy.base import BaseEnemy


class ArenaCroube(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "ArenaCroube"
        self.guid = "527885ffe2b65d049b17ebbe2d19136d"
        self.hp = 199
        self.speed = 100
        self.physical_defense = 75
        self.physical_attack = 100
        self.magic_defense = 50
        self.magic_attack = 35
        self.level = 6
        self.fleshmancer_minion = True
