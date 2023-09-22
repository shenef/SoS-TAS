from typing import Self

from data.enemy.base import BaseEnemy


class ArenaOwlsassin(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "ArenaOwlsassin"
        self.guid = "5064bcbd33aceb1418e0ef6b4ed40515"
        self.hp = 325
        self.speed = 0
        self.physical_defense = 90
        self.physical_attack = 75
        self.magic_defense = 35
        self.magic_attack = 225
        self.level = 19
        self.fleshmancer_minion = True
