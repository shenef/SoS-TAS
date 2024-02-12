from typing import Self

from data.enemy.base import BaseEnemy


class Bushtroo(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "Bushtroo"
        self.guid = "d6d70e14dba609e49888445e42647a8d"
        self.hp = 95
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 0
        self.magic_defense = 50
        self.magic_attack = 20
        self.level = 5
        self.fleshmancer_minion = True
