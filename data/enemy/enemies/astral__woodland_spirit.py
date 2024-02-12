from typing import Self

from data.enemy.base import BaseEnemy


class Astral_WoodlandSpirit(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "Astral_WoodlandSpirit"
        self.guid = "5e1fb9276fd3e714d8fe1a4cfa8681af"
        self.hp = 88
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 42
        self.magic_defense = 50
        self.magic_attack = 65
        self.level = 14
        self.fleshmancer_minion = True
