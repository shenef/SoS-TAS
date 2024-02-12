from typing import Self

from data.enemy.base import BaseEnemy


class DwellerOfWoeBanshee(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "DwellerOfWoeBanshee"
        self.guid = "807fd9a36ea523f4aa7d532ddc565a69"
        self.hp = 1999
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 56
        self.magic_defense = 50
        self.magic_attack = 50
        self.level = 1
        self.fleshmancer_minion = True
