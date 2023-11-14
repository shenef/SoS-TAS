from typing import Self

from data.enemy.base import BaseEnemy


class SoulCurator(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "SoulCurator"
        self.guid = "baf4bd47c31e1954099f3a466a43059e"
        self.hp = 455
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 110
        self.magic_defense = 50
        self.magic_attack = 0
        self.level = 1
        self.fleshmancer_minion = True
