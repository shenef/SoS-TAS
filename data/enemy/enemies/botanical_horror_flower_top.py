from typing import Self

from data.enemy.base import BaseEnemy


class BotanicalHorrorFlowerTop(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "BotanicalHorrorFlowerTop"
        self.guid = "621eeda6cacd76740b9b24518c3d211b"
        self.hp = 105
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 20
        self.magic_defense = 50
        self.magic_attack = 36
        self.level = 1
        self.fleshmancer_minion = True
