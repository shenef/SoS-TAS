from typing import Self

from data.enemy.base import BaseEnemy


class Tsiclop(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "Tsiclop"
        self.guid = "40f05ed0202783449a704978e8670c9b"
        self.hp = 350
        self.speed = 150
        self.physical_defense = 75
        self.physical_attack = 60
        self.magic_defense = 50
        self.magic_attack = 0
        self.level = 11
        self.fleshmancer_minion = True
