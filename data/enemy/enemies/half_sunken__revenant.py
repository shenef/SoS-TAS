from typing import Self

from data.enemy.base import BaseEnemy


class HalfSunken_Revenant(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "HalfSunken_Revenant"
        self.guid = "4d5fce1b06b687c4fbf91daa5b2b1d67"
        self.hp = 225
        self.speed = 0
        self.physical_defense = 90
        self.physical_attack = 115
        self.magic_defense = 35
        self.magic_attack = 0
        self.level = 8
        self.fleshmancer_minion = True
