from engine.combat.utility.core.consideration import Consideration


class Reasoner:
    def __init__(self, handle):
        self.handle = None
        self.considerations = []

    def generate_considerations(self, players):
        considerations = []
        for player in players:
            considerations.append(Consideration(player))
        return considerations
