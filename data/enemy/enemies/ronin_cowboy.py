from typing import Self

from data.enemy.base import BaseEnemy


class RoninCowboy(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "RoninCowboy"
        self.guid = "99c8b97ca2edc2644ab9b57832c9984c"
        self.hp = 55
        self.speed = 0
        self.physical_defense = 120
        self.physical_attack = 30
        self.magic_defense = 120
        self.magic_attack = 25
        self.level = 16
        self.fleshmancer_minion = True
