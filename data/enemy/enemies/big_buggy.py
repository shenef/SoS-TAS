from typing import Self

from data.enemy.base import BaseEnemy


class BigBuggy(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "BigBuggy"
        self.guid = "eb913e79ba73fd24c809490043822d62"
        self.hp = 225
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 45
        self.magic_defense = 50
        self.magic_attack = 75
        self.level = 14
        self.fleshmancer_minion = True
