from typing import Self

from data.enemy.base import BaseEnemy


class GunGoddessBullet(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "GunGoddessBullet"
        self.guid = "2b263aee6d5f87e46b1a2ebfbee47c75"
        self.hp = 35
        self.speed = 0
        self.physical_defense = 140
        self.physical_attack = 0
        self.magic_defense = 140
        self.magic_attack = 0
        self.level = 1
        self.fleshmancer_minion = True
