from typing import Self

from data.enemy.base import BaseEnemy


class GenericEnemy(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "GenericEnemy"
        self.guid = "78623dd6db7791841a9bd48adfb65ba6"
        self.hp = 100
        self.speed = 0
        self.physical_defense = 0
        self.physical_attack = 0
        self.magic_defense = 0
        self.magic_attack = 0
        self.level = 1
        self.fleshmancer_minion = True
