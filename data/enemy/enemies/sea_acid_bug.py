from typing import Self

from data.enemy.base import BaseEnemy


class SeaAcidBug(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "SeaAcidBug"
        self.guid = "d5f7b3f22f54712468481c6a987ddb85"
        self.hp = 45
        self.speed = 0
        self.physical_defense = 140
        self.physical_attack = 0
        self.magic_defense = 140
        self.magic_attack = 0
        self.level = 1
        self.fleshmancer_minion = True
