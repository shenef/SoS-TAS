from typing import Self

from data.enemy.base import BaseEnemy


class Lonzon(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "Lonzon"
        self.guid = "f93fa5cbb04648047902c7c612f418ee"
        self.hp = 75
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 19
        self.magic_defense = 50
        self.magic_attack = 50
        self.level = 8
        self.fleshmancer_minion = True
