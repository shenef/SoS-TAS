from typing import Self

from data.enemy.base import BaseEnemy


class Yinke(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "Yinke"
        self.guid = "84a7c81c839bdd949b907f9e7f940c6b"
        self.hp = 210
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 35
        self.magic_defense = 50
        self.magic_attack = 150
        self.level = 21
        self.fleshmancer_minion = True
