from typing import Self

from data.enemy.base import BaseEnemy


class StrifeMinion(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "StrifeMinion"
        self.guid = "ffe45f0323cb8924e8296b7cc86d9d1b"
        self.hp = 375
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 36
        self.magic_defense = 50
        self.magic_attack = 33
        self.level = 8
        self.fleshmancer_minion = True
