from typing import Self

from data.enemy.base import BaseEnemy


class PraPra(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "PraPra"
        self.guid = "fb69218273345394baef9abf6fa9a345"
        self.hp = 140
        self.speed = 0
        self.physical_defense = 15
        self.physical_attack = 55
        self.magic_defense = 50
        self.magic_attack = 28
        self.level = 10
        self.fleshmancer_minion = True
