from typing import Self

from data.enemy.base import BaseEnemy


class StormCaller(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "StormCaller"
        self.guid = "b4e6c3b0168970144a55f4d41fe344c4"
        self.hp = 1200
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 30
        self.magic_defense = 50
        self.magic_attack = 30
        self.level = 1
        self.fleshmancer_minion = True
