from typing import Self

from data.enemy.base import BaseEnemy


class RockSalamander(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "RockSalamander"
        self.guid = "d0f2cf59f69f42842ac0703193f39c85"
        self.hp = 250
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 25
        self.magic_defense = 50
        self.magic_attack = 45
        self.level = 1
        self.fleshmancer_minion = True
