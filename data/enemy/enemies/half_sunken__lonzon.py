from typing import Self

from data.enemy.base import BaseEnemy


class HalfSunken_Lonzon(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "HalfSunken_Lonzon"
        self.guid = "2167ae398eb2ca3409431e9c3e48e7bc"
        self.hp = 288
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 70
        self.magic_defense = 50
        self.magic_attack = 125
        self.level = 20
        self.fleshmancer_minion = True
