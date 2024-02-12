from typing import Self

from data.enemy.base import BaseEnemy


class Sharksenal(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "Sharksenal"
        self.guid = "2ac7d969f7f6fb74a9c8322db76bf9b6"
        self.hp = 165
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 65
        self.magic_defense = 50
        self.magic_attack = 35
        self.level = 11
        self.fleshmancer_minion = True
