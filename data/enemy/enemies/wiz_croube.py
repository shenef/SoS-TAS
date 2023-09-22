from typing import Self

from data.enemy.base import BaseEnemy


class WizCroube(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "WizCroube"
        self.guid = "14c5d91be67e5214ba8ce66c21a282e7"
        self.hp = 38
        self.speed = 100
        self.physical_defense = 75
        self.physical_attack = 14
        self.magic_defense = 50
        self.magic_attack = 28
        self.level = 3
        self.fleshmancer_minion = True
