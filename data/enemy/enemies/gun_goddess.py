from typing import Self

from data.enemy.base import BaseEnemy


class GunGoddess(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "GunGoddess"
        self.guid = "5470cc5d33151fc418928aa32cb6876d"
        self.hp = 4700
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 210
        self.magic_defense = 50
        self.magic_attack = 135
        self.level = 1
        self.fleshmancer_minion = True
