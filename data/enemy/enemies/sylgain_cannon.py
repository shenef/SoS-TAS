from typing import Self

from data.enemy.base import BaseEnemy


class SylgainCannon(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "SylgainCannon"
        self.guid = "4ed3837bcd9bb1d4f84fbe0681af90bc"
        self.hp = 100
        self.speed = 0
        self.physical_defense = 0
        self.physical_attack = 0
        self.magic_defense = 0
        self.magic_attack = 0
        self.level = 1
        self.fleshmancer_minion = True
