from typing import Self

from data.enemy.base import BaseEnemy


class BoneCage(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "BoneCage"
        self.guid = "2219ed20bdc00cc4fbc2b854954dbc4d"
        self.hp = 195
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 0
        self.magic_defense = 50
        self.magic_attack = 0
        self.level = 1
        self.fleshmancer_minion = True
