from typing import Self

from data.enemy.base import BaseEnemy


class Firecracker(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "Firecracker"
        self.guid = "f08a6f708a24d87499439e14326c7a59"
        self.hp = 115
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 35
        self.magic_defense = 120
        self.magic_attack = 55
        self.level = 14
        self.fleshmancer_minion = True
