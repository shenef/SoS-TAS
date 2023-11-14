from typing import Self

from data.enemy.base import BaseEnemy


class ArenaScout(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "ArenaScout"
        self.guid = "9b7d5ffcd415b664abdc0987f7776524"
        self.hp = 344
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 95
        self.magic_defense = 35
        self.magic_attack = 210
        self.level = 18
        self.fleshmancer_minion = True
