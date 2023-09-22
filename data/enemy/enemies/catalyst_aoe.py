from typing import Self

from data.enemy.base import BaseEnemy


class CatalystAOE(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "CatalystAOE"
        self.guid = "502a27a3594091742b14552afd49fa0a"
        self.hp = 95
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 75
        self.magic_defense = 50
        self.magic_attack = 75
        self.level = 1
        self.fleshmancer_minion = True
