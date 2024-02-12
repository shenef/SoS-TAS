from typing import Self

from data.enemy.base import BaseEnemy


class WoodlandSpirit(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "WoodlandSpirit"
        self.guid = "01101b1b5a47ca14b8979f4597514a59"
        self.hp = 63
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 26
        self.magic_defense = 50
        self.magic_attack = 30
        self.level = 6
        self.fleshmancer_minion = True
