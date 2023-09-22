from typing import Self

from data.enemy.base import BaseEnemy


class MeasureChestA(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "MeasureChestA"
        self.guid = "5559dc084cfb23a44b5c5b519196f34d"
        self.hp = 1255
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 0
        self.magic_defense = 50
        self.magic_attack = 225
        self.level = 1
        self.fleshmancer_minion = True
