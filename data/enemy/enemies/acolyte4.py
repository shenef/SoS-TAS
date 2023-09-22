from typing import Self

from data.enemy.base import BaseEnemy


class Acolyte4(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "Acolyte4"
        self.guid = "0c831eb6bc1c0c648828b405cb8c0667"
        self.hp = 488
        self.speed = 0
        self.physical_defense = 90
        self.physical_attack = 80
        self.magic_defense = 35
        self.magic_attack = 0
        self.level = 1
        self.fleshmancer_minion = True
