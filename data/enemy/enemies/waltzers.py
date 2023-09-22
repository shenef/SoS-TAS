from typing import Self

from data.enemy.base import BaseEnemy


class Waltzers(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "Waltzers"
        self.guid = "d98c3fb06819d104aa554170cbc05e56"
        self.hp = 99
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 65
        self.magic_defense = 50
        self.magic_attack = 25
        self.level = 8
        self.fleshmancer_minion = True
