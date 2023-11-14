from typing import Self

from data.enemy.base import BaseEnemy


class Arentee(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "Arentee"
        self.guid = "30372e1cddf4d8245861bd27363d5f9a"
        self.hp = 110
        self.speed = 0
        self.physical_defense = 90
        self.physical_attack = 35
        self.magic_defense = 50
        self.magic_attack = 0
        self.level = 7
        self.fleshmancer_minion = True
