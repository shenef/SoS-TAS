from typing import Self

from data.enemy.base import BaseEnemy


class SlingRabbit(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "SlingRabbit"
        self.guid = "4e00be6b55350d64090bff46533eb2aa"
        self.hp = 145
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 60
        self.magic_defense = 50
        self.magic_attack = 39
        self.level = 14
        self.fleshmancer_minion = True
