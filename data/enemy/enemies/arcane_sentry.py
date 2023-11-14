from typing import Self

from data.enemy.base import BaseEnemy


class ArcaneSentry(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "ArcaneSentry"
        self.guid = "013ecd2381fd8574c910cb58203eb2df"
        self.hp = 52
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 30
        self.magic_defense = 120
        self.magic_attack = 0
        self.level = 7
        self.fleshmancer_minion = True
