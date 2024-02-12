from typing import Self

from data.enemy.base import BaseEnemy


class TwoHeads_Fleshmancer(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "TwoHeads_Fleshmancer"
        self.guid = "d29103a8ea0fec54fac2a092acf1308a"
        self.hp = 255
        self.speed = 45
        self.physical_defense = 150
        self.physical_attack = 158
        self.magic_defense = 100
        self.magic_attack = 38
        self.level = 21
        self.fleshmancer_minion = True
