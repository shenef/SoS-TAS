from typing import Self

from data.enemy.base import BaseEnemy


class DukeAventry(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "DukeAventry"
        self.guid = "028beee8dff72234a9ad3d8578f6e588"
        self.hp = 475
        self.speed = 0
        self.physical_defense = 90
        self.physical_attack = 70
        self.magic_defense = 50
        self.magic_attack = 44
        self.level = 1
        self.fleshmancer_minion = True
