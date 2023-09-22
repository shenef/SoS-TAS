from typing import Self

from data.enemy.base import BaseEnemy


class Bosslug(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "Bosslug"
        self.guid = "5750f181921e1f349b595e8e47760d33"
        self.hp = 290
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 7
        self.magic_defense = 50
        self.magic_attack = 0
        self.level = 1
        self.fleshmancer_minion = True
