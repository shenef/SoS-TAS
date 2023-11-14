from typing import Self

from data.enemy.base import BaseEnemy


class DwellerOfDread(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "DwellerOfDread"
        self.guid = "a1c7a4d91b5c8c54b96c3a159ad3a1b5"
        self.hp = 11990
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 110
        self.magic_defense = 50
        self.magic_attack = 75
        self.level = 1
        self.fleshmancer_minion = True
