from typing import Self

from data.enemy.base import BaseEnemy


class BilePile_Fleshmancer(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "BilePile_Fleshmancer"
        self.guid = "4578c77a3346d0845bae8eb8f4bb1cd1"
        self.hp = 666
        self.speed = 20
        self.physical_defense = 90
        self.physical_attack = 125
        self.magic_defense = 50
        self.magic_attack = 70
        self.level = 22
        self.fleshmancer_minion = True
