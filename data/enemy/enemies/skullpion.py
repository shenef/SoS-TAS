from typing import Self

from data.enemy.base import BaseEnemy


class Skullpion(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "Skullpion"
        self.guid = "d34eee0d16a720248a3ce2e6ce2b108b"
        self.hp = 80
        self.speed = 10
        self.physical_defense = 75
        self.physical_attack = 45
        self.magic_defense = 50
        self.magic_attack = 21
        self.level = 10
        self.fleshmancer_minion = True
