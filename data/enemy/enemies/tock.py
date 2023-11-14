from typing import Self

from data.enemy.base import BaseEnemy


class Tock(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "Tock"
        self.guid = "51b36d4dce9be614f95e77477caecace"
        self.hp = 144
        self.speed = 0
        self.physical_defense = 100
        self.physical_attack = 62
        self.magic_defense = 35
        self.magic_attack = 45
        self.level = 12
        self.fleshmancer_minion = True
