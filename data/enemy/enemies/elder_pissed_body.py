from typing import Self

from data.enemy.base import BaseEnemy


class ElderPissedBody(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "ElderPissedBody"
        self.guid = "6b3a54899475c384385fdcee4fa1fe26"
        self.hp = 3995
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 160
        self.magic_defense = 50
        self.magic_attack = 200
        self.level = 1
        self.fleshmancer_minion = True
