from typing import Self

from data.enemy.base import BaseEnemy


class ManglerFish_FishingDungeon(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "ManglerFish_FishingDungeon"
        self.guid = "ae0a040c2cb657d4b9d10aaa9603ac15"
        self.hp = 255
        self.speed = 0
        self.physical_defense = 75
        self.physical_attack = 165
        self.magic_defense = 50
        self.magic_attack = 195
        self.level = 21
        self.fleshmancer_minion = True
