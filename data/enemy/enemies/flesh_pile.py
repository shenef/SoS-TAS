from typing import Self

from data.enemy.base import BaseEnemy


class FleshPile(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "FleshPile"
        self.guid = "ebf760c7aea1c1d46b18e9db92c5af76"
        self.hp = 300
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 0
        self.magic_defense = 50
        self.magic_attack = 0
        self.level = 1
        self.fleshmancer_minion = True
