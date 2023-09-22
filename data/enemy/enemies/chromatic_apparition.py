from typing import Self

from data.enemy.base import BaseEnemy


class ChromaticApparition(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "ChromaticApparition"
        self.guid = "a3b51cc4bda782c41a9ada029c202824"
        self.hp = 700
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 35
        self.magic_defense = 50
        self.magic_attack = 9
        self.level = 1
        self.fleshmancer_minion = True
