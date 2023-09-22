from typing import Self

from data.enemy.base import BaseEnemy


class ArenaLonzon(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "ArenaLonzon"
        self.guid = "1e62e41d77ce0f344bb884ffb4d92ebf"
        self.hp = 244
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 75
        self.magic_defense = 50
        self.magic_attack = 185
        self.level = 8
        self.fleshmancer_minion = True
