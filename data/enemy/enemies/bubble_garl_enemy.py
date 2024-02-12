from typing import Self

from data.enemy.base import BaseEnemy


class BubbleGarlEnemy(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "BubbleGarlEnemy"
        self.guid = "1e8082f704ec4d24e9dfc010f00600fb"
        self.hp = 115
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 30
        self.magic_defense = 50
        self.magic_attack = 25
        self.level = 1
        self.fleshmancer_minion = True
