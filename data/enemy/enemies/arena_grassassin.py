from typing import Self

from data.enemy.base import BaseEnemy


class ArenaGrassassin(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "ArenaGrassassin"
        self.guid = "470302d28c08352438d633aebb7c0cb5"
        self.hp = 290
        self.speed = 0
        self.physical_defense = 50
        self.physical_attack = 130
        self.magic_defense = 75
        self.magic_attack = 35
        self.level = 12
        self.fleshmancer_minion = True
