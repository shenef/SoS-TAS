from typing import Self

from data.enemy.base import BaseEnemy


class Rochecrossidere(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "Rochecrossidere"
        self.guid = "a1a5c1333a1e7fe4f98de4d28b3b9900"
        self.hp = 90
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 50
        self.magic_defense = 50
        self.magic_attack = 85
        self.level = 12
        self.fleshmancer_minion = True
