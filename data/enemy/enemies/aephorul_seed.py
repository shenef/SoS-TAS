from typing import Self

from data.enemy.base import BaseEnemy


class AephorulSeed(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "AephorulSeed"
        self.guid = "94dd0e887519ebd4ca13aa0d7fdb1da7"
        self.hp = 250
        self.speed = 0
        self.physical_defense = 100
        self.physical_attack = 0
        self.magic_defense = 100
        self.magic_attack = 0
        self.level = 1
        self.fleshmancer_minion = True
