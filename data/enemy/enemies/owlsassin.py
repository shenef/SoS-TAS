from typing import Self

from data.enemy.base import BaseEnemy


class Owlsassin(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "Owlsassin"
        self.guid = "a071d2cccf4848746bbc63e27a0af3b9"
        self.hp = 133
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 60
        self.magic_defense = 90
        self.magic_attack = 135
        self.level = 19
        self.fleshmancer_minion = True
