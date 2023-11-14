from typing import Self

from data.enemy.base import BaseEnemy


class AntBruiser(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "AntBruiser"
        self.guid = "e6ac627711e4ee44da103c47d1cd5736"
        self.hp = 35
        self.speed = 0
        self.physical_defense = 120
        self.physical_attack = 23
        self.magic_defense = 0
        self.magic_attack = 0
        self.level = 4
        self.fleshmancer_minion = True
