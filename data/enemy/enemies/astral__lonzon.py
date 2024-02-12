from typing import Self

from data.enemy.base import BaseEnemy


class Astral_Lonzon(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "Astral_Lonzon"
        self.guid = "d7cdfe62090e94047991a1b9ca612a6d"
        self.hp = 95
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 35
        self.magic_defense = 50
        self.magic_attack = 90
        self.level = 14
        self.fleshmancer_minion = True
