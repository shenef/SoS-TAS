import glob
import os
import re
from typing import Self


class EnemyOutput:
    def __init__(self: Self) -> None:
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


def parse_kv(line: str, key: str, field: str, enemy: EnemyOutput) -> None:
    if line.startswith(key):
        regex = r"(.+)(: )(.*)"
        subst = r"\3"
        result = re.sub(regex, subst, line, count=0)
        setattr(enemy, field, result)


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
<<<<<<< HEAD
        if enemy.guid:
            enemies[enemy.guid] = enemy.name

mappings = os.linesep.join(f'"{key}": {value}(),' for key, value in enemies.items())

codegen = f"""# ruff: noqa
from typing import Self
from data.enemy.enemies import *
=======
        # remove non-guid mappings
        if enemy.guid:
            enemies[enemy.guid] = enemy.name
mappings = os.linesep.join(f'"{key}": {value}(),' for key, value in enemies.items())
codegen = f"""from typing import Self

>>>>>>> 0a176d6308d66d1fe3679f89377393c8868cfbbf

class Enemies:
    MAPPINGS = {{
{mappings}
    
    }}

    def get(self: Self, guid: str) -> str:
        return self.MAPPINGS.get(guid)

        """
current_path = os.path.dirname(os.path.abspath(__file__))
path = f"{current_path}/mapper_output/enemies.py"
new_file = open(path, "w")  # noqa: SIM115
new_file.write(codegen)
new_file.close()
