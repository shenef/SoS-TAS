from typing import Self

from data.enemy.base import BaseEnemy


class BombThrower(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "BombThrower"
        self.guid = "2a9a0b40f493b11429febb5d927ef84b"
        self.hp = 52
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 17
        self.magic_defense = 50
        self.magic_attack = 20
        self.level = 4
        self.fleshmancer_minion = True
