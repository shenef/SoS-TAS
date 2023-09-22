from typing import Self

from data.enemy.base import BaseEnemy


class GooGoon(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "GooGoon"
        self.guid = "0fdc3ecd763b6244eb8c172a11cd661a"
        self.hp = 12
        self.speed = 0
        self.physical_defense = 140
        self.physical_attack = 20
        self.magic_defense = 150
        self.magic_attack = 70
        self.level = 12
        self.fleshmancer_minion = True
