from typing import Self

from data.enemy.base import BaseEnemy


class SeraiEnemy(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "SeraiEnemy"
        self.guid = "f802ea770f9b9da4c8d95ccb485a79d9"
        self.hp = 100
        self.speed = 0
        self.physical_defense = 0
        self.physical_attack = 0
        self.magic_defense = 0
        self.magic_attack = 0
        self.level = 1
        self.fleshmancer_minion = True
