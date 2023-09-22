from typing import Self

from data.enemy.base import BaseEnemy


class BonePillarPiece(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "BonePillarPiece"
        self.guid = "70523b5040e767e4bb8cb3b7c223e492"
        self.hp = 100
        self.speed = 0
        self.physical_defense = 0
        self.physical_attack = 0
        self.magic_defense = 0
        self.magic_attack = 0
        self.level = 1
        self.fleshmancer_minion = True
