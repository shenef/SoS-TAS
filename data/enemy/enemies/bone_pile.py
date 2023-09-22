from typing import Self

from data.enemy.base import BaseEnemy


class BonePile(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "BonePile"
        self.guid = "30bd6b9747d75724496a60116d875f96"
        self.hp = 300
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 0
        self.magic_defense = 50
        self.magic_attack = 0
        self.level = 1
        self.fleshmancer_minion = True
