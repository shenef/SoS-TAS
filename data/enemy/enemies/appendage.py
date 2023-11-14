from typing import Self

from data.enemy.base import BaseEnemy


class Appendage(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "Appendage"
        self.guid = "0763389cb3bdf154ea661ff0ebb6216b"
        self.hp = 1250
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 115
        self.magic_defense = 50
        self.magic_attack = 0
        self.level = 1
        self.fleshmancer_minion = True
