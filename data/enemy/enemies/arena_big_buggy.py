from typing import Self

from data.enemy.base import BaseEnemy


class ArenaBigBuggy(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "ArenaBigBuggy"
        self.guid = "4608a56ce03fa8f42a467a917c438bcc"
        self.hp = 345
        self.speed = 0
        self.physical_defense = 90
        self.physical_attack = 90
        self.magic_defense = 50
        self.magic_attack = 150
        self.level = 14
        self.fleshmancer_minion = True
