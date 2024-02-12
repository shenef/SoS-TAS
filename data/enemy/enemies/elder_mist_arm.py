from typing import Self

from data.enemy.base import BaseEnemy


class ElderMistArm(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "ElderMistArm"
        self.guid = "c787becf4fbd0dd4ea2fc6b3bc4ecef2"
        self.hp = 100
        self.speed = 0
        self.physical_defense = 0
        self.physical_attack = 5
        self.magic_defense = 0
        self.magic_attack = 0
        self.level = 1
        self.fleshmancer_minion = True
