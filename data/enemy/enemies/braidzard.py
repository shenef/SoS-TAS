from typing import Self

from data.enemy.base import BaseEnemy


class Braidzard(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "Braidzard"
        self.guid = "9cbcb4063d9b8d8448cf96a2c14a6826"
        self.hp = 135
        self.speed = 0
        self.physical_defense = 50
        self.physical_attack = 50
        self.magic_defense = 75
        self.magic_attack = 55
        self.level = 14
        self.fleshmancer_minion = True
