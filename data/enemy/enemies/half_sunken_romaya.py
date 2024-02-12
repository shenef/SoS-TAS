from typing import Self

from data.enemy.base import BaseEnemy


class HalfSunkenRomaya(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "HalfSunkenRomaya"
        self.guid = "ce1df87d1facdf2469716190f2d6ad51"
        self.hp = 3450
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 170
        self.magic_defense = 50
        self.magic_attack = 195
        self.level = 1
        self.fleshmancer_minion = True
