from typing import Self

from data.enemy.base import BaseEnemy


class HalfSunkenBonePile(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "HalfSunkenBonePile"
        self.guid = "d0a6e3e6b8288bf4bb7abd1cedb38ca3"
        self.hp = 2000
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 0
        self.magic_defense = 50
        self.magic_attack = 0
        self.level = 1
        self.fleshmancer_minion = True
