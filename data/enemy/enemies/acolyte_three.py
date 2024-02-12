from typing import Self

from data.enemy.base import BaseEnemy


class AcolyteThree(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "AcolyteThree"
        self.guid = "e77c07b22ee83854e8c006101ef5731f"
        self.hp = 390
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 35
        self.magic_defense = 65
        self.magic_attack = 55
        self.level = 1
        self.fleshmancer_minion = True
