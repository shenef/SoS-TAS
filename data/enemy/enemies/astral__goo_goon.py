from typing import Self

from data.enemy.base import BaseEnemy


class Astral_GooGoon(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "Astral_GooGoon"
        self.guid = "e0e39853cf0aedc4a87abc25605ea4a6"
        self.hp = 12
        self.speed = 0
        self.physical_defense = 140
        self.physical_attack = 32
        self.magic_defense = 150
        self.magic_attack = 95
        self.level = 14
        self.fleshmancer_minion = True
