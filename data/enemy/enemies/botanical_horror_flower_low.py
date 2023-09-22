from typing import Self

from data.enemy.base import BaseEnemy


class BotanicalHorrorFlowerLow(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "BotanicalHorrorFlowerLow"
        self.guid = "3bbc6ad42918c444c9947d156e7674aa"
        self.hp = 88
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 26
        self.magic_defense = 50
        self.magic_attack = 35
        self.level = 1
        self.fleshmancer_minion = True
