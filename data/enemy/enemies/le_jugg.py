from typing import Self

from data.enemy.base import BaseEnemy


class LeJugg(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "LeJugg"
        self.guid = "7a8be6ca5e9b7bd49ac7d2da414442cc"
        self.hp = 2500
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 65
        self.magic_defense = 50
        self.magic_attack = 95
        self.level = 1
        self.fleshmancer_minion = True
