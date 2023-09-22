from typing import Self

from data.enemy.base import BaseEnemy


class Malkomount(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "Malkomount"
        self.guid = "fc51f181f5f913f4e99195da947b1425"
        self.hp = 310
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 19
        self.magic_defense = 50
        self.magic_attack = 38
        self.level = 1
        self.fleshmancer_minion = True
