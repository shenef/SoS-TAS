from typing import Self

from data.enemy.base import BaseEnemy


class ElderPissedSword(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "ElderPissedSword"
        self.guid = "7b27481afea42bb479dc3f81032a16d9"
        self.hp = 800
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 0
        self.magic_defense = 50
        self.magic_attack = 0
        self.level = 1
        self.fleshmancer_minion = True
