from typing import Self

from data.enemy.base import BaseEnemy


class ShrimpKnight(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "ShrimpKnight"
        self.guid = "6fd00c7bd71304e41aacabb2c6f401c7"
        self.hp = 132
        self.speed = 0
        self.physical_defense = 100
        self.physical_attack = 60
        self.magic_defense = 35
        self.magic_attack = 35
        self.level = 11
        self.fleshmancer_minion = True
