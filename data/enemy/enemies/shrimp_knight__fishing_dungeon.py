from typing import Self

from data.enemy.base import BaseEnemy


class ShrimpKnight_FishingDungeon(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "ShrimpKnight_FishingDungeon"
        self.guid = "c5fc39dac699f0645a0fa83505b12b2a"
        self.hp = 235
        self.speed = 0
        self.physical_defense = 100
        self.physical_attack = 144
        self.magic_defense = 35
        self.magic_attack = 195
        self.level = 11
        self.fleshmancer_minion = True
