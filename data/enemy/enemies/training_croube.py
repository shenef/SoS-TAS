from typing import Self

from data.enemy.base import BaseEnemy


class TrainingCroube(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "TrainingCroube"
        self.guid = "a9b692dccd6e2a748abe6f848cff857e"
        self.hp = 13
        self.speed = 100
        self.physical_defense = 75
        self.physical_attack = 9
        self.magic_defense = 75
        self.magic_attack = 0
        self.level = 1
        self.fleshmancer_minion = True
