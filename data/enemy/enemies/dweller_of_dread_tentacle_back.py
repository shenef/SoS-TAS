from typing import Self

from data.enemy.base import BaseEnemy


class DwellerOfDreadTentacleBack(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "DwellerOfDreadTentacleBack"
        self.guid = "c109e23c16e478b4e992161662fa81c0"
        self.hp = 1100
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 150
        self.magic_defense = 50
        self.magic_attack = 200
        self.level = 1
        self.fleshmancer_minion = True
