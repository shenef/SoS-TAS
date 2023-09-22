from typing import Self

from data.enemy.base import BaseEnemy


class CrystalPrison(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "CrystalPrison"
        self.guid = "dcbec33a2784ace4ab16ded6d8ec0ae0"
        self.hp = 999
        self.speed = 1
        self.physical_defense = 75
        self.physical_attack = 15
        self.magic_defense = 50
        self.magic_attack = 30
        self.level = 7
        self.fleshmancer_minion = True
