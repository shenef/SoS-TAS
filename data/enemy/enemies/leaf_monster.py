from typing import Self

from data.enemy.base import BaseEnemy


class LeafMonster(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "LeafMonster"
        self.guid = "c99b902697c6f734f9fc64b421c06728"
        self.hp = 755
        self.speed = 0
        self.physical_defense = 25
        self.physical_attack = 55
        self.magic_defense = 25
        self.magic_attack = 50
        self.level = 1
        self.fleshmancer_minion = True
