from typing import Self

from data.enemy.base import BaseEnemy


class ArenaGulgul(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "ArenaGulgul"
        self.guid = "cac4ad5c6feebe443bee7570b8e009b8"
        self.hp = 222
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 100
        self.magic_defense = 50
        self.magic_attack = 35
        self.level = 7
        self.fleshmancer_minion = True
