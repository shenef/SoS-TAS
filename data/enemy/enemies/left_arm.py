from typing import Self

from data.enemy.base import BaseEnemy


class LeftArm(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "LeftArm"
        self.guid = ""
        self.hp = 2125
        self.speed = 0
        self.physical_defense = 150
        self.physical_attack = 0
        self.magic_defense = 150
        self.magic_attack = 0
        self.level = 0
        self.fleshmancer_minion = False
