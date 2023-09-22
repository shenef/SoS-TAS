from typing import Self

from data.enemy.base import BaseEnemy


class Aephorul(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "Aephorul"
        self.guid = "33f520d32c7543a4789622c37138ba87"
        self.hp = 3999
        self.speed = 0
        self.physical_defense = 80
        self.physical_attack = 295
        self.magic_defense = 60
        self.magic_attack = 210
        self.level = 1
        self.fleshmancer_minion = True
