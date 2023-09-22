from typing import Self

from data.enemy.base import BaseEnemy


class Croube(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "Croube"
        self.guid = "50229dee567088647809e9b737b397b7"
        self.hp = 38
        self.speed = 100
        self.physical_defense = 75
        self.physical_attack = 14
        self.magic_defense = 50
        self.magic_attack = 28
        self.level = 6
        self.fleshmancer_minion = True
