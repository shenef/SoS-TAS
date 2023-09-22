from typing import Self

from data.enemy.base import BaseEnemy


class HorseMech(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "HorseMech"
        self.guid = "68f9357277cff414eb0bf287dabd1cb0"
        self.hp = 155
        self.speed = 0
        self.physical_defense = 90
        self.physical_attack = 85
        self.magic_defense = 25
        self.magic_attack = 45
        self.level = 16
        self.fleshmancer_minion = True
