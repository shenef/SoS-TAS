from typing import Self

from data.enemy.base import BaseEnemy


class Sylgain(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "Sylgain"
        self.guid = "4c313193055778746a8caa5a3f51b8c6"
        self.hp = 2999
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 70
        self.magic_defense = 50
        self.magic_attack = 300
        self.level = 1
        self.fleshmancer_minion = True
