from typing import Self

from data.enemy.base import BaseEnemy


class ElysandArellePhase2(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "ElysandArellePhase2"
        self.guid = "0e5b91e5ad0b2784da76ba6314004370"
        self.hp = 3000
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 110
        self.magic_defense = 50
        self.magic_attack = 155
        self.level = 1
        self.fleshmancer_minion = True
