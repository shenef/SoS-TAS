from typing import Self

from data.enemy.base import BaseEnemy


class DwellerOfTorment(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "DwellerOfTorment"
        self.guid = "94680e3651254c54ca6030f9461b3ed7"
        self.hp = 4999
        self.speed = 0
        self.physical_defense = 150
        self.physical_attack = 50
        self.magic_defense = 150
        self.magic_attack = 15
        self.level = 1
        self.fleshmancer_minion = True
