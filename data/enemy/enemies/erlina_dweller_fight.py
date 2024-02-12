from typing import Self

from data.enemy.base import BaseEnemy


class ErlinaDwellerFight(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "ErlinaDwellerFight"
        self.guid = "1dc70fb2d0f1b374cbecf052b953824b"
        self.hp = 255
        self.speed = 0
        self.physical_defense = 80
        self.physical_attack = 40
        self.magic_defense = 55
        self.magic_attack = 35
        self.level = 1
        self.fleshmancer_minion = True
