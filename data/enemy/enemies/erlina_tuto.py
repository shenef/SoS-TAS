from typing import Self

from data.enemy.base import BaseEnemy


class ErlinaTuto(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "ErlinaTuto"
        self.guid = "f71d669f95fdec7498d0ec4e4bab0e81"
        self.hp = 1000
        self.speed = 0
        self.physical_defense = 0
        self.physical_attack = 0
        self.magic_defense = 0
        self.magic_attack = 0
        self.level = 1
        self.fleshmancer_minion = True
