from typing import Self

from data.enemy.base import BaseEnemy


class MoongirlEnemy(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "MoongirlEnemy"
        self.guid = "3ac5141f57d77c642948246353f8b5b4"
        self.hp = 210
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 55
        self.magic_defense = 50
        self.magic_attack = 55
        self.level = 1
        self.fleshmancer_minion = True
