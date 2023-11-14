from typing import Self

from data.enemy.base import BaseEnemy


class RangedMatey(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "RangedMatey"
        self.guid = "1b827e3f77cf5e44cbb3c8fbfde8c1df"
        self.hp = 114
        self.speed = 0
        self.physical_defense = 25
        self.physical_attack = 50
        self.magic_defense = 90
        self.magic_attack = 30
        self.level = 9
        self.fleshmancer_minion = True
