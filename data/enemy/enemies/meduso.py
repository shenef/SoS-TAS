from typing import Self

from data.enemy.base import BaseEnemy


class Meduso(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "Meduso"
        self.guid = "bb02eb1602e1ec142b85cd6b505ef5b6"
        self.hp = 1666
        self.speed = 10
        self.physical_defense = 75
        self.physical_attack = 0
        self.magic_defense = 50
        self.magic_attack = 0
        self.level = 1
        self.fleshmancer_minion = True
