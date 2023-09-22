from typing import Self

from data.enemy.base import BaseEnemy


class Mermofwizquard(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "Mermofwizquard"
        self.guid = "f8de7842d6be99b40a6d8160044b5f62"
        self.hp = 66
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 35
        self.magic_defense = 50
        self.magic_attack = 0
        self.level = 8
        self.fleshmancer_minion = True
