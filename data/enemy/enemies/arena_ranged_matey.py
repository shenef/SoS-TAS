from typing import Self

from data.enemy.base import BaseEnemy


class ArenaRangedMatey(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "ArenaRangedMatey"
        self.guid = "b10c6cc7a49f77246848a74cae5ea119"
        self.hp = 190
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 125
        self.magic_defense = 50
        self.magic_attack = 80
        self.level = 9
        self.fleshmancer_minion = True
