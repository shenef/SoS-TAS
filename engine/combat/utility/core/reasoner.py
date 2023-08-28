from engine.combat.utility.core.consideration import Consideration


class Reasoner:
    def __init__(self, handle):
        self.handle = None
        self.considerations = []

    def generate_considerations(self, actors: list[any]) -> list[Consideration]:
        considerations = []
        for actor in actors:
            considerations.append(Consideration(actor))
        return considerations
