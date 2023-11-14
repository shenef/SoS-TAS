from typing import Self

from data.enemy.base import BaseEnemy


class CatalystCore(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "CatalystCore"
        self.guid = "b2e5237a9dd152643abaf1fb3e3d7206"
        self.hp = 799
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 0
        self.magic_defense = 50
        self.magic_attack = 0
        self.level = 1
        self.fleshmancer_minion = True
