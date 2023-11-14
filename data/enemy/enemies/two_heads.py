from typing import Self

from data.enemy.base import BaseEnemy


class TwoHeads(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "TwoHeads"
        self.guid = "c6f57cbee5d9cff4a82778ce36f94fdf"
        self.hp = 75
        self.speed = 45
        self.physical_defense = 150
        self.physical_attack = 70
        self.magic_defense = 100
        self.magic_attack = 38
        self.level = 12
        self.fleshmancer_minion = True
