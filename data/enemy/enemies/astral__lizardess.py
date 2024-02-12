from typing import Self

from data.enemy.base import BaseEnemy


class Astral_Lizardess(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "Astral_Lizardess"
        self.guid = "f875c492e9ff81d46917be56218ba834"
        self.hp = 310
        self.speed = 45
        self.physical_defense = 75
        self.physical_attack = 41
        self.magic_defense = 50
        self.magic_attack = 30
        self.level = 14
        self.fleshmancer_minion = True
