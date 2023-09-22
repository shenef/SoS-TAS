from typing import Self

from data.enemy.base import BaseEnemy


class Drone(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "Drone"
        self.guid = "bbaa918249ce3a04883d88eca37cf348"
        self.hp = 132
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 75
        self.magic_defense = 50
        self.magic_attack = 95
        self.level = 15
        self.fleshmancer_minion = True
