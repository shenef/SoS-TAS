from typing import Self

from data.enemy.base import BaseEnemy


class Romaya(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "Romaya"
        self.guid = "5cdedb65d17f3b24c8b7ad5bcbe1bea6"
        self.hp = 888
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 40
        self.magic_defense = 50
        self.magic_attack = 35
        self.level = 1
        self.fleshmancer_minion = True
