from typing import Self

from data.enemy.base import BaseEnemy


class Croustalion(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "Croustalion"
        self.guid = "23cf24f17aff1674786c7fc3086dc388"
        self.hp = 5225
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 135
        self.magic_defense = 50
        self.magic_attack = 150
        self.level = 1
        self.fleshmancer_minion = True
