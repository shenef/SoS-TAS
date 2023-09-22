from typing import Self

from data.enemy.base import BaseEnemy


class MedusoClaw(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "MedusoClaw"
        self.guid = "79150c51ef673bd49a3e5b83af4c5f8c"
        self.hp = 100
        self.speed = 0
        self.physical_defense = 150
        self.physical_attack = 0
        self.magic_defense = 150
        self.magic_attack = 20
        self.level = 1
        self.fleshmancer_minion = True
