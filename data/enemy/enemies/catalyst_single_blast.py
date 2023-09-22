from typing import Self

from data.enemy.base import BaseEnemy


class CatalystSingleBlast(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "CatalystSingleBlast"
        self.guid = "34e76b8dc018975409a6a84332a5124f"
        self.hp = 175
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 105
        self.magic_defense = 50
        self.magic_attack = 105
        self.level = 1
        self.fleshmancer_minion = True
