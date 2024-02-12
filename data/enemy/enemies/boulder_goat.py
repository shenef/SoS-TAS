from typing import Self

from data.enemy.base import BaseEnemy


class BoulderGoat(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "BoulderGoat"
        self.guid = "fc2736fdbb731394c98da56e8f476d5e"
        self.hp = 65
        self.speed = 100
        self.physical_defense = 75
        self.physical_attack = 18
        self.magic_defense = 50
        self.magic_attack = 15
        self.level = 4
        self.fleshmancer_minion = True
