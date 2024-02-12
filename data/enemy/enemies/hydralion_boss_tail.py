from typing import Self

from data.enemy.base import BaseEnemy


class HydralionBossTail(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "HydralionBossTail"
        self.guid = "5044e84c74fc97343ad3c8bcd3c08fdf"
        self.hp = 210
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 80
        self.magic_defense = 50
        self.magic_attack = 0
        self.level = 1
        self.fleshmancer_minion = True
