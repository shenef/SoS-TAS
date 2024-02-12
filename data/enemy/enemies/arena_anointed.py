from typing import Self

from data.enemy.base import BaseEnemy


class ArenaAnointed(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "ArenaAnointed"
        self.guid = "09ab35a6a52c0c74f836febf7d6e7a2e"
        self.hp = 325
        self.speed = 0
        self.physical_defense = 90
        self.physical_attack = 135
        self.magic_defense = 35
        self.magic_attack = 210
        self.level = 18
        self.fleshmancer_minion = True
