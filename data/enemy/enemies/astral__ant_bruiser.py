from typing import Self

from data.enemy.base import BaseEnemy


class Astral_AntBruiser(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "Astral_AntBruiser"
        self.guid = "6db3b04b05f18ae48a952691c0edc99f"
        self.hp = 90
        self.speed = 0
        self.physical_defense = 120
        self.physical_attack = 46
        self.magic_defense = 0
        self.magic_attack = 0
        self.level = 14
        self.fleshmancer_minion = True
