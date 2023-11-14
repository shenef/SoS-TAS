from typing import Self

from data.enemy.base import BaseEnemy


class BubbleReshanEnemy(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "BubbleReshanEnemy"
        self.guid = "525744509ae9e144fb7f7435acf69e00"
        self.hp = 90
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 35
        self.magic_defense = 50
        self.magic_attack = 25
        self.level = 1
        self.fleshmancer_minion = True
