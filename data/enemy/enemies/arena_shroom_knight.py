from typing import Self

from data.enemy.base import BaseEnemy


class ArenaShroomKnight(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "ArenaShroomKnight"
        self.guid = "6c2a1e2872a0b5a469d1f9e437f60fb8"
        self.hp = 350
        self.speed = 0
        self.physical_defense = 90
        self.physical_attack = 90
        self.magic_defense = 35
        self.magic_attack = 195
        self.level = 12
        self.fleshmancer_minion = True
