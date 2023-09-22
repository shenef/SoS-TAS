from typing import Self

from data.enemy.base import BaseEnemy


class ArenaMeleeMatey(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "ArenaMeleeMatey"
        self.guid = "980a2ead2b197f947aa5199927376dbb"
        self.hp = 205
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 111
        self.magic_defense = 50
        self.magic_attack = 210
        self.level = 9
        self.fleshmancer_minion = True
