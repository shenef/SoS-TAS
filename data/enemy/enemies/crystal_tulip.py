from typing import Self

from data.enemy.base import BaseEnemy


class CrystalTulip(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "CrystalTulip"
        self.guid = "90c4097a7ecb8d6439bdc8d7a48b8992"
        self.hp = 1
        self.speed = 1
        self.physical_defense = 150
        self.physical_attack = 15
        self.magic_defense = 150
        self.magic_attack = 30
        self.level = 7
        self.fleshmancer_minion = True
