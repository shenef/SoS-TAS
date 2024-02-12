from typing import Self

from data.enemy.base import BaseEnemy


class WYRD(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "WYRD"
        self.guid = "8beb20a7311444a47b1764ae7ace6658"
        self.hp = 100
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 6
        self.magic_defense = 35
        self.magic_attack = 0
        self.level = 1
        self.fleshmancer_minion = True
