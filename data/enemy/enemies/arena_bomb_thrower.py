from typing import Self

from data.enemy.base import BaseEnemy


class ArenaBombThrower(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "ArenaBombThrower"
        self.guid = "ca5e21141b95aad49bc08403f495b38d"
        self.hp = 211
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 95
        self.magic_defense = 50
        self.magic_attack = 80
        self.level = 4
        self.fleshmancer_minion = True
