from typing import Self

from data.enemy.base import BaseEnemy


class BrugavesDwellerFight(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "BrugavesDwellerFight"
        self.guid = "ec0b935c78a26044f89a236921671642"
        self.hp = 275
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 20
        self.magic_defense = 50
        self.magic_attack = 25
        self.level = 1
        self.fleshmancer_minion = True
