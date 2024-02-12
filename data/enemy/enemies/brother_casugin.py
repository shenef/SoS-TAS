from typing import Self

from data.enemy.base import BaseEnemy


class BrotherCasugin(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "BrotherCasugin"
        self.guid = "bdff582229a41f3438d4c4faac714255"
        self.hp = 655
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 42
        self.magic_defense = 120
        self.magic_attack = 110
        self.level = 1
        self.fleshmancer_minion = True
