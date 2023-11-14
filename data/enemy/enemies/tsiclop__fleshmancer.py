from typing import Self

from data.enemy.base import BaseEnemy


class Tsiclop_Fleshmancer(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "Tsiclop_Fleshmancer"
        self.guid = "17869a064ace26541bf54688ee3f7f93"
        self.hp = 499
        self.speed = 150
        self.physical_defense = 90
        self.physical_attack = 95
        self.magic_defense = 50
        self.magic_attack = 0
        self.level = 21
        self.fleshmancer_minion = True
