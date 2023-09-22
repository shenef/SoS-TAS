from typing import Self

from data.enemy.base import BaseEnemy


class MatsakrunClaw(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "MatsakrunClaw"
        self.guid = "675f39fa7e962f3498552e334e40df9d"
        self.hp = 90
        self.speed = 0
        self.physical_defense = 120
        self.physical_attack = 80
        self.magic_defense = 120
        self.magic_attack = 65
        self.level = 20
        self.fleshmancer_minion = True
