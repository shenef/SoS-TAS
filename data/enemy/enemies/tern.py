from typing import Self

from data.enemy.base import BaseEnemy


class Tern(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "Tern"
        self.guid = "72351ffc3ecd46d46bf11cec4eee353a"
        self.hp = 5
        self.speed = 0
        self.physical_defense = 150
        self.physical_attack = 22
        self.magic_defense = 0
        self.magic_attack = 0
        self.level = 3
        self.fleshmancer_minion = True
