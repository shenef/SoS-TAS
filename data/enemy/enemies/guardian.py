from typing import Self

from data.enemy.base import BaseEnemy


class Guardian(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "Guardian"
        self.guid = "78457137461e7d345b2287aab380e2e0"
        self.hp = 1333
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 55
        self.magic_defense = 50
        self.magic_attack = 110
        self.level = 1
        self.fleshmancer_minion = True
