from typing import Self

from data.enemy.base import BaseEnemy


class PhaseReaper(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "PhaseReaper"
        self.guid = "54abc79fbf9dd2f4a8bd19cab8245391"
        self.hp = 2750
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 110
        self.magic_defense = 50
        self.magic_attack = 110
        self.level = 1
        self.fleshmancer_minion = True
