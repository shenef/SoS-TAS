from typing import Self

from data.enemy.base import BaseEnemy


class Scout(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "Scout"
        self.guid = "5ca276f08b35cd448b7458d85cc8ee5b"
        self.hp = 138
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 105
        self.magic_defense = 75
        self.magic_attack = 105
        self.level = 18
        self.fleshmancer_minion = True
