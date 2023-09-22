import glob
import os
import re
from re import sub


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


path = "./files"


def parse_kv(line, key, field, enemy):
    if line.startswith(key):
        regex = r"(.+)(: )(.*)"
        subst = r"\3"
        result = re.sub(regex, subst, line, count=0)
        setattr(enemy, field, result)


def snake(s):
    return "_".join(
        sub(
            "([A-Z][a-z]+)", r" \1", sub("([A-Z]+)", r" \1", s.replace("-", " "))
        ).split()
    ).lower()


enemies = {}

for filename in glob.glob(os.path.join(path, "*.txt")):
    with open(os.path.join(os.getcwd(), filename)) as f:  # open in readonly mode
        lines = f.readlines()
        enemy = EnemyOutput()

        for line in lines:
            text = line.strip()
            if text.startswith("--"):
                regex = r"(--\ )(.+)(Data)(\ --)"
                subst = r"\2"
                result = re.sub(regex, subst, line, count=0)
                enemy.name = result.strip()

            parse_kv(text, "guid", "guid", enemy)
        # remove non-guid mappings
        if enemy.guid:
            enemies[enemy.guid] = enemy.name
imports = os.linesep.join(
    f"from data.enemy.enemies.{snake(value)} import {value}"
    for _key, value in enemies.items()
)
names = os.linesep.join(f'"{value}",' for key, value in enemies.items())
codegen = f"""{imports}

__all__ = [
   {names}
]

        """
current_path = os.path.dirname(os.path.abspath(__file__))
path = f"{current_path}/mapper_output/__init__.py"
new_file = open(path, "w")
new_file.write(codegen)
new_file.close()
