from typing import Self

from data.enemy.base import BaseEnemy


class CatalystWeapon_SingleTargetRepeat(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "CatalystWeapon_SingleTargetRepeat"
        self.guid = "19255ab0a339bd44a8873944c866afc9"
        self.hp = 110
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 33
        self.magic_defense = 50
        self.magic_attack = 0
        self.level = 1
        self.fleshmancer_minion = True
