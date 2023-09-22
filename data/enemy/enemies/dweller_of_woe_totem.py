from typing import Self

from data.enemy.base import BaseEnemy


class DwellerOfWoeTotem(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "DwellerOfWoeTotem"
        self.guid = "bcde1eb0ea076f846a0ee20287d88204"
        self.hp = 3600
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 50
        self.magic_defense = 50
        self.magic_attack = 95
        self.level = 1
        self.fleshmancer_minion = True
