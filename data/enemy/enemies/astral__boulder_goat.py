from typing import Self

from data.enemy.base import BaseEnemy


class Astral_BoulderGoat(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "Astral_BoulderGoat"
        self.guid = "d788814517a8e1549b0253e534126938"
        self.hp = 110
        self.speed = 100
        self.physical_defense = 75
        self.physical_attack = 36
        self.magic_defense = 50
        self.magic_attack = 45
        self.level = 14
        self.fleshmancer_minion = True
