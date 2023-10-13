"""Routing of Cursed Woods section of Wraith Island."""

import logging
from typing import Self

from engine.combat import SeqCombatAndMove
from engine.mathlib import Vec3
from engine.seq import SeqCheckpoint, SeqList

logger = logging.getLogger(__name__)


class CursedWoods(SeqList):
    """Routing of Cursed Woods, from arrival until leaving for Ferryman's Vigil."""

    def __init__(self: Self) -> None:
        """Initialize a new CursedWoods object."""
        super().__init__(
            name="Cursed Woods",
            children=[
                SeqCombatAndMove(
                    name="Move to save point",
                    coords=[
                        Vec3(13.792, 3.002, -4.069),
                        Vec3(22.023, 3.002, 5.332),
                        Vec3(22.042, 3.002, 11.359),
                        Vec3(16.289, 3.002, 14.189),
                        Vec3(16.289, 2.998, 18.318),
                        Vec3(13.945, 2.998, 20.659),
                        Vec3(13.945, 2.997, 24.292),
                        Vec3(12.358, 2.993, 26.526),
                        Vec3(15.350, 3.001, 33.157),
                    ],
                ),
                SeqCheckpoint("cursed_woods"),
                SeqCombatAndMove(
                    name="Navigate woods",
                    coords=[
                        Vec3(15.350, 3.001, 33.157),
                        # TODO(orkaboy): Continue routing
                    ],
                ),
            ],
        )
