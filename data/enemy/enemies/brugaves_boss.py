from typing import Self

from data.enemy.base import BaseEnemy


class BrugavesBoss(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "BrugavesBoss"
        self.guid = "cc767e360aab54d4ca314a206e32ffee"
        self.hp = 555
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 18
        self.magic_defense = 50
        self.magic_attack = 25
        self.level = 1
        self.fleshmancer_minion = True
