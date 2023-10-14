"""Routing of Flooded Graveyard and Necromancer's Lair section of Wraith Island."""

import logging
from typing import Self

from engine.combat import SeqCombatAndMove
from engine.mathlib import Vec3
from engine.seq import (
    SeqCheckpoint,
    SeqInteract,
    SeqList,
    SeqMove,
    SeqSkipUntilIdle,
)

logger = logging.getLogger(__name__)


class FloodedGraveyard(SeqList):
    """
    Routing of Flooded Graveyard.

    From arrival at Ferryman's Vigil until entering Necromancer's Lair.
    """

    def __init__(self: Self) -> None:
        """Initialize a new FloodedGraveyard object."""
        super().__init__(
            name="Flooded Graveyard",
            children=[
                SeqCheckpoint("ferrymans_vigil"),
                SeqMove(
                    name="Move to ferryman",
                    coords=[
                        Vec3(23.214, 5.002, 9.606),
                        Vec3(29.489, 5.002, 9.491),
                    ],
                ),
                SeqInteract("Ferryman"),
                SeqSkipUntilIdle("Ferryman"),
                SeqCombatAndMove(
                    name="Navigate Graveyard",
                    coords=[
                        Vec3(21.564, 6.002, 23.199),
                        # TODO(orkaboy): Continue routing
                    ],
                ),
            ],
        )
