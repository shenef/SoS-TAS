from typing import Self

from data.enemy.base import BaseEnemy


class Grassassin(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "Grassassin"
        self.guid = "2c78ebcab00eb2c4daef5082c88503cc"
        self.hp = 122
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 55
        self.magic_defense = 50
        self.magic_attack = 55
        self.level = 12
        self.fleshmancer_minion = True
