from typing import Self

from data.enemy.base import BaseEnemy


class SeaBossSlug(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "SeaBossSlug"
        self.guid = "1b8297af091713d47ba1bfec1cc53d75"
        self.hp = 4200
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 0
        self.magic_defense = 50
        self.magic_attack = 0
        self.level = 1
        self.fleshmancer_minion = True
