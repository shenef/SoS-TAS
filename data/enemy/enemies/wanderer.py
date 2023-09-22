from typing import Self

from data.enemy.base import BaseEnemy


class Wanderer(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "Wanderer"
        self.guid = "c3a2f1d99be4e0c42aca0ae1ff590028"
        self.hp = 39
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 6
        self.magic_defense = 50
        self.magic_attack = 9
        self.level = 2
        self.fleshmancer_minion = True
