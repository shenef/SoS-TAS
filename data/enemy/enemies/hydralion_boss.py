from typing import Self

from data.enemy.base import BaseEnemy


class HydralionBoss(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "HydralionBoss"
        self.guid = "7e2e026eb3354c74685427b26cf9acb8"
        self.hp = 1150
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 44
        self.magic_defense = 50
        self.magic_attack = 65
        self.level = 1
        self.fleshmancer_minion = True
