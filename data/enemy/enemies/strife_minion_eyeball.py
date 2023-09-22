from typing import Self

from data.enemy.base import BaseEnemy


class StrifeMinionEyeball(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "StrifeMinionEyeball"
        self.guid = "22ceeba2aa09ad8499fcade71c0b283d"
        self.hp = 0
        self.speed = 0
        self.physical_defense = 0
        self.physical_attack = 20
        self.magic_defense = 0
        self.magic_attack = 0
        self.level = 1
        self.fleshmancer_minion = True
