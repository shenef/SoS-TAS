"""Routing of Flooded Graveyard and Necromancer's Lair section of Wraith Island."""

import logging
from typing import Self

from engine.mathlib import Vec2, Vec3
from engine.seq import (
    HoldDirection,
    InteractMove,
    SeqCheckpoint,
    SeqClimb,
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
                SeqMove(
                    name="Move to ferryman",
                    coords=[
                        Vec3(23.214, 5.002, 9.606),
                        Vec3(29.489, 5.002, 9.491),
                    ],
                ),
                SeqInteract("Ferryman"),
                SeqSkipUntilIdle("Ferryman"),
                SeqCheckpoint("flooded_graveyard"),
                SeqMove(
                    name="Move to Solstice Door",
                    coords=[
                        Vec3(25.952, 6.002, 23.202),
                        Vec3(14.912, 4.002, 26.811),
                        Vec3(9.879, 4.002, 32.508),
                        Vec3(-7.284, 4.002, 33.666),
                        InteractMove(-11.113, 5.002, 37.315),
                        Vec3(-12.947, 5.002, 39.915),
                        Vec3(-12.947, 5.002, 48.040),
                    ],
                ),
                SeqInteract("Door"),
                SeqMove(
                    name="Move to wall",
                    coords=[
                        HoldDirection(72.000, 1.002, 205.968, joy_dir=Vec2(0, 1)),
                        Vec3(67.982, 1.002, 210.076),
                        Vec3(65.735, 1.002, 210.010),
                        Vec3(64.058, 1.002, 213.063),
                        Vec3(64.344, 1.002, 217.946),
                        Vec3(65.215, 1.002, 219.546),
                    ],
                ),
                SeqClimb(
                    name="Climb wall",
                    coords=[
                        InteractMove(65.215, 4.540, 219.540),
                        Vec3(67.701, 5.343, 219.530),
                        Vec3(69.491, 10.947, 219.530),
                        Vec3(70.752, 10.947, 219.530),
                    ],
                ),
                SeqMove(
                    name="Move to chest",
                    coords=[
                        InteractMove(70.752, 6.002, 217.542),
                        Vec3(71.857, 6.002, 217.437),
                    ],
                ),
                SeqInteract("Shimmering Daggers"),
                SeqSkipUntilIdle("Shimmering Daggers"),
                SeqMove(
                    name="Move to crypt",
                    coords=[
                        InteractMove(71.857, 1.002, 207.191),
                        HoldDirection(-13.107, 5.002, 47.962, joy_dir=Vec2(0, -1)),
                        Vec3(-16.711, 5.002, 34.460),
                        InteractMove(-16.711, 4.002, 30.092),
                        Vec3(-25.252, 4.002, 20.940),
                        Vec3(-36.434, 4.002, 20.122),
                        Vec3(-47.895, 4.191, 15.422),
                        HoldDirection(-126.500, 1.002, 14.500, joy_dir=Vec2(-1, 1)),
                        # TODO(orkaboy): Continue routing
                    ],
                ),
            ],
        )
