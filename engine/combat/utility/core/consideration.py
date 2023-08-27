from typing import Self


class Consideration:
    def __init__(self, actor):
        self.actor = actor
        self.value = 0
        self.appraisals = self.generate_appraisals()

    # Generates a list of appraisals for a character.
    def generate_appraisals(self):
        return []

    # use to assign a new value based on whatever the current state is
    def calculate(self) -> Self:
        self.value = 0
        return self

    # execute on selecting the consideration to perform the appraisal
    def execute(self):
        pass
