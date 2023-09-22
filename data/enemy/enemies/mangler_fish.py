from typing import Self

from data.enemy.base import BaseEnemy


class ManglerFish(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "ManglerFish"
        self.guid = "91cece6ac544e8d49809c007d30f73fc"
        self.hp = 75
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 18
        self.magic_defense = 50
        self.magic_attack = 37
        self.level = 7
        self.fleshmancer_minion = True
