import glob
import os
import re


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
mappings = os.linesep.join(f'"{key}": {value}(),' for key, value in enemies.items())
print(mappings)
codegen = f"""from typing import Self


class Enemies:
    MAPPINGS = {{
{mappings}
    
    }}

    def get(self: Self, guid: str) -> str:
        return self.MAPPINGS.get(guid)

        """
current_path = os.path.dirname(os.path.abspath(__file__))
path = f"{current_path}/mapper_output/enemies.py"
new_file = open(path, "w")
new_file.write(codegen)
new_file.close()
