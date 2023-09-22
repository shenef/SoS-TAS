from typing import Self

from data.enemy.base import BaseEnemy


class CatalystHeal(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "CatalystHeal"
        self.guid = "210da1eb30be5e34bacf6ac5058357e4"
        self.hp = 60
        self.speed = 0
        self.physical_defense = 90
        self.physical_attack = 85
        self.magic_defense = 90
        self.magic_attack = 85
        self.level = 1
        self.fleshmancer_minion = True
