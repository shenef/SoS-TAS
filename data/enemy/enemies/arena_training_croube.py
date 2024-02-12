from typing import Self

from data.enemy.base import BaseEnemy


class ArenaTrainingCroube(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "ArenaTrainingCroube"
        self.guid = "e126c542eee0aa7468e3f62ad953ca4d"
        self.hp = 199
        self.speed = 100
        self.physical_defense = 75
        self.physical_attack = 100
        self.magic_defense = 50
        self.magic_attack = 85
        self.level = 1
        self.fleshmancer_minion = True
