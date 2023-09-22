from typing import Self

from data.enemy.base import BaseEnemy


class ArenaRevenant(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "ArenaRevenant"
        self.guid = "eef757b01f5cd80459e634f109a1e69c"
        self.hp = 409
        self.speed = 0
        self.physical_defense = 90
        self.physical_attack = 95
        self.magic_defense = 35
        self.magic_attack = 0
        self.level = 8
        self.fleshmancer_minion = True
