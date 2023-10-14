"""Routing of Wraith Island Docks."""

import logging
from typing import Self

from engine.combat import SeqCombatAndMove
from engine.mathlib import Vec2, Vec3
from engine.seq import HoldDirection, SeqCheckpoint, SeqInteract, SeqList, SeqMove

logger = logging.getLogger(__name__)


class WraithIslandDocks(SeqList):
    """Routing of Wraith Island Docks, from arrival to entering Lucent."""

    def __init__(self: Self) -> None:
        """Initialize a new WraithIslandDocks object."""
        super().__init__(
            name="Wraith Island Docks",
            children=[
                SeqCheckpoint(
                    "wraith_island_docks",
                    return_path=SeqMove(
                        name="Return to path",
                        coords=[
                            Vec3(15.494, 0.002, -1.225),
                            Vec3(17.039, 1.010, 8.214),
                        ],
                    ),
                ),
                SeqCombatAndMove(
                    name="Navigate forest",
                    coords=[
                        Vec3(23.636, 1.002, 11.523),
                        Vec3(31.083, 1.002, 12.931),
                        Vec3(43.113, 1.002, 12.931),
                        Vec3(45.991, 1.002, 12.173),
                        Vec3(52.290, 1.002, 14.410),
                        Vec3(62.484, 1.002, 14.104),
                        Vec3(65.770, 1.002, 11.840),
                        Vec3(71.065, 0.977, 11.984),
                        Vec3(72.015, 0.977, 10.682),
                        Vec3(72.015, 0.977, 8.030),
                        Vec3(73.663, 0.977, 6.248),
                        Vec3(82.423, 0.977, 6.248),
                        Vec3(84.491, 0.977, 8.285),
                        Vec3(84.491, 1.004, 9.710),
                        Vec3(89.932, 1.002, 11.320),
                        Vec3(102.231, 1.002, 8.682),
                        Vec3(119.794, 1.002, 7.406),
                        Vec3(127.692, 1.002, 10.174),
                        HoldDirection(176.000, 1.002, 104.998, joy_dir=Vec2(1, 0)),
                    ],
                ),
                SeqMove(
                    name="World map",
                    coords=[
                        Vec3(180.500, 1.002, 105.000),
                        Vec3(180.500, 1.002, 106.000),
                        Vec3(188.500, 1.002, 106.000),
                        Vec3(188.500, 1.002, 108.000),
                    ],
                ),
                SeqInteract("Enter Lucent"),
            ],
        )
