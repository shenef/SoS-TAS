from engine.combat.utility.core.consideration import Consideration
from typing import List

class Reasoner:
    def __init__(self, handle):
        self.handle = None
        self.considerations = []

    def generate_considerations(self, actors: List[any]) -> List[Consideration]:
        considerations = []
        for actor in actors:
            considerations.append(Consideration(actor))
        return considerations
