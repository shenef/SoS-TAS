from typing import Self

from data.enemy.base import BaseEnemy


class WizWanderer(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "WizWanderer"
        self.guid = "42c3cf27ee18164428ad318882f5137e"
        self.hp = 39
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 6
        self.magic_defense = 50
        self.magic_attack = 12
        self.level = 2
        self.fleshmancer_minion = True
