from typing import Self

from data.enemy.base import BaseEnemy


class BoulderDouche(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "BoulderDouche"
        self.guid = "33a6c54c83b68894a93b46c02da7fbc8"
        self.hp = 155
        self.speed = 0
        self.physical_defense = 100
        self.physical_attack = 45
        self.magic_defense = 50
        self.magic_attack = 90
        self.level = 13
        self.fleshmancer_minion = True
