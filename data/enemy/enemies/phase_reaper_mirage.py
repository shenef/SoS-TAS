from typing import Self

from data.enemy.base import BaseEnemy


class PhaseReaperMirage(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "PhaseReaperMirage"
        self.guid = "fdffd9c935c80c44bb937f761764f245"
        self.hp = 688
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 110
        self.magic_defense = 50
        self.magic_attack = 110
        self.level = 1
        self.fleshmancer_minion = True
