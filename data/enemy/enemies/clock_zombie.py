from typing import Self

from data.enemy.base import BaseEnemy


class ClockZombie(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "ClockZombie"
        self.guid = "090c2ec246656b643a5d1e5b0bb3db28"
        self.hp = 155
        self.speed = 0
        self.physical_defense = 90
        self.physical_attack = 77
        self.magic_defense = 50
        self.magic_attack = 0
        self.level = 13
        self.fleshmancer_minion = True
