from typing import Self

from data.enemy.base import BaseEnemy


class Revenant(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "Revenant"
        self.guid = "a5d5e39e2ca42bb43b343c4cde2ec1e7"
        self.hp = 225
        self.speed = 0
        self.physical_defense = 90
        self.physical_attack = 25
        self.magic_defense = 35
        self.magic_attack = 0
        self.level = 8
        self.fleshmancer_minion = True
