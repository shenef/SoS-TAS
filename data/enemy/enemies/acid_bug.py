from typing import Self

from data.enemy.base import BaseEnemy


class AcidBug(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "AcidBug"
        self.guid = "3c02795df7f5ec647b8ba102263e7574"
        self.hp = 1
        self.speed = 0
        self.physical_defense = 0
        self.physical_attack = 12
        self.magic_defense = 0
        self.magic_attack = 0
        self.level = 1
        self.fleshmancer_minion = True
