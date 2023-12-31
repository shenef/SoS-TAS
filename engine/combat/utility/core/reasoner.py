from typing import Any, Self

from engine.combat.utility.core.consideration import Consideration


class Reasoner:
    def __init__(self: Self) -> None:
        """Initialize a new Reasoner object."""
        self.considerations = []

    def generate_considerations(self: Self, actors: list[Any]) -> list[Consideration]:
        considerations = []
        for actor in actors:
            considerations.append(Consideration(actor))
        return considerations
