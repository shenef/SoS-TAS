from typing import Self

from data.enemy.base import BaseEnemy


class MeasureChestB(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "MeasureChestB"
        self.guid = "3259041d34de847448e496200e994a8a"
        self.hp = 1255
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 0
        self.magic_defense = 50
        self.magic_attack = 80
        self.level = 1
        self.fleshmancer_minion = True
