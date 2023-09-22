from typing import Self

from data.enemy.base import BaseEnemy


class BubbleSeraiEnemy(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "BubbleSeraiEnemy"
        self.guid = "aaf855be11272ed4da5687c47da27579"
        self.hp = 85
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 38
        self.magic_defense = 50
        self.magic_attack = 25
        self.level = 1
        self.fleshmancer_minion = True
