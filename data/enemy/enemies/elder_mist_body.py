from typing import Self

from data.enemy.base import BaseEnemy


class ElderMistBody(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "ElderMistBody"
        self.guid = "962aa552d33fc124782b230fce9185ce"
        self.hp = 350
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 20
        self.magic_defense = 50
        self.magic_attack = 45
        self.level = 1
        self.fleshmancer_minion = True
