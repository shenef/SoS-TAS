from typing import Self

from data.enemy.base import BaseEnemy


class DwellerOfStrife(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "DwellerOfStrife"
        self.guid = "a5d39cc10d1848d478b59c892f636e3b"
        self.hp = 11500
        self.speed = 0
        self.physical_defense = 148
        self.physical_attack = 45
        self.magic_defense = 148
        self.magic_attack = 60
        self.level = 1
        self.fleshmancer_minion = True
