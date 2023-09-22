from typing import Self

from data.enemy.base import BaseEnemy


class BubbleSunboyEnemy(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "BubbleSunboyEnemy"
        self.guid = "667e9f6f8bb894f4dafcbc412dfdc293"
        self.hp = 95
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 32
        self.magic_defense = 50
        self.magic_attack = 25
        self.level = 1
        self.fleshmancer_minion = True
