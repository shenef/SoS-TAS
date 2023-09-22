from typing import Self

from data.enemy.base import BaseEnemy


class BabyPraPra(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "BabyPraPra"
        self.guid = "2ab124591b5a20840856ba5c79425a56"
        self.hp = 100
        self.speed = 0
        self.physical_defense = 0
        self.physical_attack = 0
        self.magic_defense = 0
        self.magic_attack = 0
        self.level = 1
        self.fleshmancer_minion = True
