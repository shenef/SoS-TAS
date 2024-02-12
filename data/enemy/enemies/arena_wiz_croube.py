from typing import Self

from data.enemy.base import BaseEnemy


class ArenaWizCroube(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "ArenaWizCroube"
        self.guid = "e92dfcf5e74aeb34f98f32b8cd563ebf"
        self.hp = 199
        self.speed = 100
        self.physical_defense = 75
        self.physical_attack = 100
        self.magic_defense = 50
        self.magic_attack = 35
        self.level = 3
        self.fleshmancer_minion = True
