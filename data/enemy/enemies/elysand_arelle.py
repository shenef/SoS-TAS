from typing import Self

from data.enemy.base import BaseEnemy


class ElysandArelle(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "ElysandArelle"
        self.guid = "0c24f27ebab6b854ba75700be2df5b21"
        self.hp = 2700
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 200
        self.magic_defense = 50
        self.magic_attack = 125
        self.level = 1
        self.fleshmancer_minion = True
