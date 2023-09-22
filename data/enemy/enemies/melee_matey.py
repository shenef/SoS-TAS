from typing import Self

from data.enemy.base import BaseEnemy


class MeleeMatey(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "MeleeMatey"
        self.guid = "6081b4ccf00a36343827bc45999f0df2"
        self.hp = 114
        self.speed = 0
        self.physical_defense = 90
        self.physical_attack = 28
        self.magic_defense = 25
        self.magic_attack = 88
        self.level = 9
        self.fleshmancer_minion = True
