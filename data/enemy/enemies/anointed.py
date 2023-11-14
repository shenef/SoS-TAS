from typing import Self

from data.enemy.base import BaseEnemy


class Anointed(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "Anointed"
        self.guid = "09b42ce72465d8149997ff1d7bb8708a"
        self.hp = 165
        self.speed = 0
        self.physical_defense = 90
        self.physical_attack = 90
        self.magic_defense = 50
        self.magic_attack = 115
        self.level = 18
        self.fleshmancer_minion = True
