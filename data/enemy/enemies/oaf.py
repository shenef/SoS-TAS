from typing import Self

from data.enemy.base import BaseEnemy


class OAF(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "OAF"
        self.guid = "8011d343c45597d40b59678731a6782d"
        self.hp = 775
        self.speed = 0
        self.physical_defense = 90
        self.physical_attack = 75
        self.magic_defense = 75
        self.magic_attack = 0
        self.level = 23
        self.fleshmancer_minion = True
