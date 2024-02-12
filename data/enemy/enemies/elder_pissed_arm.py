from typing import Self

from data.enemy.base import BaseEnemy


class ElderPissedArm(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "ElderPissedArm"
        self.guid = "6360b75144ae73845980a1c1e25ccabb"
        self.hp = 100
        self.speed = 0
        self.physical_defense = 0
        self.physical_attack = 5
        self.magic_defense = 0
        self.magic_attack = 0
        self.level = 1
        self.fleshmancer_minion = True
