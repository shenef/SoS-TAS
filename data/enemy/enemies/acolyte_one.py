from typing import Self

from data.enemy.base import BaseEnemy


class AcolyteOne(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "AcolyteOne"
        self.guid = "76c4290aa2a896b4cb405e5a2d29b3a0"
        self.hp = 415
        self.speed = 0
        self.physical_defense = 90
        self.physical_attack = 35
        self.magic_defense = 35
        self.magic_attack = 55
        self.level = 1
        self.fleshmancer_minion = True
