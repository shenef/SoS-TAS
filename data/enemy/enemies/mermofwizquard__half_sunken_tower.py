from typing import Self

from data.enemy.base import BaseEnemy


class Mermofwizquard_HalfSunkenTower(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "Mermofwizquard_HalfSunkenTower"
        self.guid = "a5a0da6d66767df47b2523b04f14738a"
        self.hp = 266
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 110
        self.magic_defense = 120
        self.magic_attack = 0
        self.level = 20
        self.fleshmancer_minion = True
