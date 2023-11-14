from typing import Self

from data.enemy.base import BaseEnemy


class Malkomud(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "Malkomud"
        self.guid = "810980f005079324fb9fb643243eccee"
        self.hp = 180
        self.speed = 0
        self.physical_defense = 33
        self.physical_attack = 25
        self.magic_defense = 130
        self.magic_attack = 13
        self.level = 1
        self.fleshmancer_minion = True
