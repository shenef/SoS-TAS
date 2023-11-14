from typing import Self

from data.enemy.base import BaseEnemy


class DwellerOfWoeMirrorImage(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "DwellerOfWoeMirrorImage"
        self.guid = "e1685476dd793e44c9c8909fe0b3622f"
        self.hp = 525
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 35
        self.magic_defense = 50
        self.magic_attack = 25
        self.level = 1
        self.fleshmancer_minion = True
