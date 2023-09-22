from typing import Self

from data.enemy.base import BaseEnemy


class Stitcher(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "Stitcher"
        self.guid = "f91e5e3a6e4c9934db9f0f799f727499"
        self.hp = 195
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 55
        self.magic_defense = 50
        self.magic_attack = 0
        self.level = 22
        self.fleshmancer_minion = True
