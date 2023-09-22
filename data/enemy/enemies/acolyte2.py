from typing import Self

from data.enemy.base import BaseEnemy


class Acolyte2(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "Acolyte2"
        self.guid = "73c4c0922e5ae274eb759f86702353a8"
        self.hp = 395
        self.speed = 0
        self.physical_defense = 60
        self.physical_attack = 25
        self.magic_defense = 65
        self.magic_attack = 25
        self.level = 1
        self.fleshmancer_minion = True
