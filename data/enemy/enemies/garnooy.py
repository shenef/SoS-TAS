from typing import Self

from data.enemy.base import BaseEnemy


class Garnooy(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "Garnooy"
        self.guid = "ea0a539bb73e45a42ae867fce0822b92"
        self.hp = 225
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 40
        self.magic_defense = 50
        self.magic_attack = 33
        self.level = 10
        self.fleshmancer_minion = True
