from typing import Self

from data.enemy.base import BaseEnemy


class SpellBook(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "SpellBook"
        self.guid = "8c69440417c1b28438d94128cd86af6d"
        self.hp = 108
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 22
        self.magic_defense = 75
        self.magic_attack = 25
        self.level = 8
        self.fleshmancer_minion = True
