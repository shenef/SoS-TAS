from typing import Self

from data.enemy.base import BaseEnemy


class Rachater(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "Rachater"
        self.guid = "c4480713abcb0d04f8a21a702987e6e1"
        self.hp = 799
        self.speed = 0
        self.physical_defense = 95
        self.physical_attack = 75
        self.magic_defense = 50
        self.magic_attack = 110
        self.level = 1
        self.fleshmancer_minion = True
