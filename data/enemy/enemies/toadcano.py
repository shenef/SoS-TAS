from typing import Self

from data.enemy.base import BaseEnemy


class Toadcano(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "Toadcano"
        self.guid = "816de006c125b9b4eaa7139bac5c6b77"
        self.hp = 1100
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 55
        self.magic_defense = 50
        self.magic_attack = 5
        self.level = 1
        self.fleshmancer_minion = True
