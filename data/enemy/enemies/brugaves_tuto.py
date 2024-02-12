from typing import Self

from data.enemy.base import BaseEnemy


class BrugavesTuto(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "BrugavesTuto"
        self.guid = "96a30eb1f53ec1c4ebe90da25545b1ac"
        self.hp = 1000
        self.speed = 0
        self.physical_defense = 0
        self.physical_attack = 0
        self.magic_defense = 0
        self.magic_attack = 0
        self.level = 1
        self.fleshmancer_minion = True
