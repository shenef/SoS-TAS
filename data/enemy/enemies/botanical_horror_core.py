from typing import Self

from data.enemy.base import BaseEnemy


class BotanicalHorrorCore(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "BotanicalHorrorCore"
        self.guid = "64246a3a9059257409ea628466ced26e"
        self.hp = 599
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 0
        self.magic_defense = 50
        self.magic_attack = 0
        self.level = 1
        self.fleshmancer_minion = True
