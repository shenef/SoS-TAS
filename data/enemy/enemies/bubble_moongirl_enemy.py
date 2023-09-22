from typing import Self

from data.enemy.base import BaseEnemy


class BubbleMoongirlEnemy(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "BubbleMoongirlEnemy"
        self.guid = "6df65b41a30cde44a967d340ec7666d3"
        self.hp = 95
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 40
        self.magic_defense = 50
        self.magic_attack = 25
        self.level = 1
        self.fleshmancer_minion = True
