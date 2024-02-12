from typing import Self

from data.enemy.base import BaseEnemy


class Boulbe(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "Boulbe"
        self.guid = "6dd1189ece4445c48a7fb978f16eb797"
        self.hp = 99
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 39
        self.magic_defense = 50
        self.magic_attack = 0
        self.level = 7
        self.fleshmancer_minion = True
