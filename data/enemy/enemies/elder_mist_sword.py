from typing import Self

from data.enemy.base import BaseEnemy


class ElderMistSword(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "ElderMistSword"
        self.guid = "ddc4a3bbf0edb9945ba4b06f96f9c20e"
        self.hp = 90
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 25
        self.magic_defense = 50
        self.magic_attack = 0
        self.level = 1
        self.fleshmancer_minion = True
