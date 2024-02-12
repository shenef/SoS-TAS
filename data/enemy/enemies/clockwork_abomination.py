from typing import Self

from data.enemy.base import BaseEnemy


class ClockworkAbomination(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "ClockworkAbomination"
        self.guid = "16ffb4ed5f03d5e41b77b93689511c62"
        self.hp = 2666
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 145
        self.magic_defense = 50
        self.magic_attack = 95
        self.level = 1
        self.fleshmancer_minion = True
