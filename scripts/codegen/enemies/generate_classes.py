import glob
import os
import re
from re import sub

path = "./files"


class EnemyOutput:
    def __init__(self) -> None:
        self.guid = ""
        self.hp = 0
        self.speed = 0
        self.physical_attack = 0
        self.physical_defense = 0
        self.magic_attack = 0
        self.magic_defense = 0
        # self.damage_type_modifiers = []
        self.name = ""
        self.level = 0
        self.fleshmancer_minion = False
        # self.qualifiers = []


def snake(s):
    return "_".join(
        sub(
            "([A-Z][a-z]+)", r" \1", sub("([A-Z]+)", r" \1", s.replace("-", " "))
        ).split()
    ).lower()


def parse_kv(line, key, field, enemy):
    if line.startswith(key):
        regex = r"(.+)(: )(.*)"
        subst = r"\3"
        result = re.sub(regex, subst, line, count=0)
        setattr(enemy, field, result)


for filename in glob.glob(os.path.join(path, "*.txt")):
    with open(os.path.join(os.getcwd(), filename)) as f:  # open in readonly mode
        lines = f.readlines()
        # Strips the newline character
        enemy = EnemyOutput()

        for line in lines:
            text = line.lstrip().rstrip().strip()
            if text.startswith("--"):
                regex = r"(--\ )(.+)(Data)(\ --)"
                subst = r"\2"
                result = re.sub(regex, subst, line, count=0)
                enemy.name = result.strip()

            parse_kv(text, "guid", "guid", enemy)
            parse_kv(text, "hp", "hp", enemy)
            parse_kv(text, "speed", "speed", enemy)
            parse_kv(text, "basePhysicalDefense", "physical_defense", enemy)
            parse_kv(text, "basePhysicalAttack", "physical_attack", enemy)
            parse_kv(text, "baseMagicDefense", "magic_defense", enemy)
            parse_kv(text, "baseMagicAttack", "magic_attack", enemy)
            parse_kv(text, "enemyLevel", "level", enemy)
            parse_kv(text, "fleshmancerMinion", "fleshmancer_minion", enemy)

        codegen = f"""from typing import Self

from data.enemy.base import BaseEnemy

        
class {enemy.name}(BaseEnemy):
    def __init__(self: Self) -> Self:
        super().__init__()
        self.name = "{enemy.name}"
        self.guid = "{enemy.guid}"
        self.hp = {enemy.hp}
        self.speed = {enemy.speed}
        self.physical_defense = {enemy.physical_defense}
        self.physical_attack = {enemy.physical_attack}
        self.magic_defense = {enemy.magic_defense}
        self.magic_attack = {enemy.magic_attack}
        self.level = {enemy.level}
        self.fleshmancer_minion = {bool(enemy.fleshmancer_minion)}
        """
        current_path = os.path.dirname(os.path.abspath(__file__))
        path = f"{current_path}/output/{snake(enemy.name)}.py"
        new_file = open(path, "w")
        new_file.write(codegen)
        new_file.close()

        # if wyrd, append its custom values
        # weakToSunDamageTypeModifiers: {'keys': [8, 4], 'values': [0.15000000596046448, 1.100000023841858]}
        # weakToMoonDamageTypeModifiers: {'keys': [4, 8], 'values': [0.15000000596046448, 1.100000023841858]}
