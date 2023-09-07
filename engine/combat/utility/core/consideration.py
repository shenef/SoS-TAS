from typing import Self

from engine.combat.utility.core.action import Action
from engine.combat.utility.core.appraisal import Appraisal


class Consideration:
    def __init__(self, actor):
        self.actor = actor
        self.value = 0
        self.appraisals = self.generate_appraisals()

    # Generates a list of appraisals for a character.
    def generate_appraisals(self) -> list[Appraisal]:
        return []

    # use to assign a new value based on whatever the current state is
    def calculate(self) -> Self:
        self.value = 0
        return self

    def calculate_actions(self) -> list[Action]:
        return []

    # execute on selecting the consideration to perform the appraisal
    def execute(self):
        pass
