from typing import Self

from data.enemy.base import BaseEnemy


class ArenaMermofwizquard(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "ArenaMermofwizquard"
        self.guid = "987f0860e9c1f5a43997e14a219dbe91"
        self.hp = 295
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 125
        self.magic_defense = 120
        self.magic_attack = 0
        self.level = 1
        self.fleshmancer_minion = True
