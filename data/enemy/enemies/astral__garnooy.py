from typing import Self

from data.enemy.base import BaseEnemy


class Astral_Garnooy(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "Astral_Garnooy"
        self.guid = "7181b3e6a1edf44409d05e9b51b86f02"
        self.hp = 225
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 70
        self.magic_defense = 50
        self.magic_attack = 55
        self.level = 14
        self.fleshmancer_minion = True
