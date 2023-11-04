"""Routing of Haunted Mansion and Dweller of Woe section of Wraith Island."""

import logging
from typing import Self

from engine.combat import SeqCombat
from engine.mathlib import Vec2, Vec3
from engine.seq import (
    HoldDirection,
    SeqCheckpoint,
    SeqInteract,
    SeqList,
    SeqMashUntilCombat,
    SeqMove,
    SeqSkipUntilIdle,
)

logger = logging.getLogger(__name__)


class BriskDestroyed(SeqList):
    """Routing of the destroyed Brisk."""

    def __init__(self: Self) -> None:
        """Initialize a new BriskDestroyed object."""
        super().__init__(
            name="Brisk destroyed",
            children=[
                SeqMove(
                    name="Go to Yolande",
                    coords=[
                        Vec3(31.780, 1.002, 180.300),
                        Vec3(32.349, 1.002, 182.460),
                        Vec3(44.461, 1.002, 182.460),
                        Vec3(45.978, 1.002, 170.457),
                        HoldDirection(46.000, 9.034, 123.145, joy_dir=Vec2(0, -1)),
                        Vec3(44.741, 1.002, 113.578),
                        Vec3(39.638, 1.002, 113.466),
                        Vec3(32.341, 1.002, 118.699),
                        Vec3(26.524, 1.002, 118.721),
                    ],
                ),
                SeqInteract("Yolande"),
                # Somewhat suboptimal time-wise
                SeqMashUntilCombat("Heading to Brisk"),
                SeqCombat("Dweller minions"),
                SeqSkipUntilIdle("Seraï returns"),
                SeqCheckpoint("brisk3"),
                # TODO(orkaboy): Continue routing
            ],
        )
