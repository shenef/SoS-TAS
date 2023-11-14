from typing import Self

from data.enemy.base import BaseEnemy


class BubbleBstEnemy(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "BubbleBstEnemy"
        self.guid = "135dac78e730914419062e7b27549f39"
        self.hp = 190
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 70
        self.magic_defense = 50
        self.magic_attack = 25
        self.level = 1
        self.fleshmancer_minion = True
