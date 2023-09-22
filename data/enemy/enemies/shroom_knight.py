from typing import Self

from data.enemy.base import BaseEnemy


class ShroomKnight(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "ShroomKnight"
        self.guid = "acf70102f6cc47e41b953fc2c44ad802"
        self.hp = 122
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 52
        self.magic_defense = 100
        self.magic_attack = 75
        self.level = 12
        self.fleshmancer_minion = True
