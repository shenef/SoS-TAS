from typing import Self

from data.enemy.base import BaseEnemy


class ErlinaBoss(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "ErlinaBoss"
        self.guid = "1894c41627be94d408bd64295ab6dd18"
        self.hp = 555
        self.speed = 0
        self.physical_defense = 50
        self.physical_attack = 45
        self.magic_defense = 75
        self.magic_attack = 42
        self.level = 1
        self.fleshmancer_minion = True
