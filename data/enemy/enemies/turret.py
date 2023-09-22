from typing import Self

from data.enemy.base import BaseEnemy


class Turret(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "Turret"
        self.guid = "fbf61f8475d74b64e800e19dacb061a0"
        self.hp = 129
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 60
        self.magic_defense = 50
        self.magic_attack = 45
        self.level = 16
        self.fleshmancer_minion = True
