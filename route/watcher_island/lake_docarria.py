"""Routing of Lake Docarria segment of Watcher Island."""

import logging
from typing import Self

from engine.mathlib import Vec2, Vec3
from engine.seq import (
    Graplou,
    HoldDirection,
    InteractMove,
    SeqClimb,
    SeqHoldDirectionUntilLostControl,
    SeqInteract,
    SeqList,
    SeqMove,
    SeqSelectOption,
    SeqSkipUntilIdle,
)

logger = logging.getLogger(__name__)


class LakeDocarria(SeqList):
    """Routing of Lake Docarria segment of Watcher Island."""

    def __init__(self: Self) -> None:
        """Initialize a new LakeDocarria object."""
        super().__init__(
            name="Lake Docarria",
            children=[
                SeqMove(
                    name="Grab wall",
                    coords=[
                        Graplou(40.050, 28.982, 6.530, joy_dir=Vec2(0, 1), hold_timer=0.1),
                    ],
                ),
                SeqClimb(
                    name="Climb wall",
                    coords=[
                        Vec3(41.054, 30.273, 6.530),
                        Vec3(40.817, 34.258, 6.530),
                        Vec3(38.983, 36.445, 6.530),
                    ],
                ),
                SeqMove(
                    name="Move to high ground",
                    coords=[
                        Vec3(38.983, 43.002, 9.076),
                    ],
                ),
                SeqHoldDirectionUntilLostControl("Move to cutscene", joy_dir=Vec2(0, 1)),
                SeqSkipUntilIdle("There's a bell"),
                SeqMove(
                    name="Cross lake",
                    coords=[
                        InteractMove(36.668, 40.803, 36.677),
                        InteractMove(22.753, 43.002, 76.860),
                        Vec3(22.368, 43.002, 79.290),
                    ],
                ),
                SeqSelectOption("Ring bell", skip_dialog_check=True),
                SeqSkipUntilIdle("Stairs rising"),
                SeqMove(
                    name="",
                    coords=[
                        Vec3(24.701, 43.002, 77.896),
                        Vec3(36.297, 48.002, 77.257),
                        Vec3(39.417, 48.002, 77.239),
                    ],
                ),
                SeqHoldDirectionUntilLostControl("Enter hut", joy_dir=Vec2(0, 1)),
                SeqSkipUntilIdle("Selecting seashell"),
                SeqMove(
                    name="Leave Lake Docarria",
                    coords=[
                        Vec3(-15.480, 5.002, 167.735),
                        HoldDirection(40.000, 48.002, 75.566, joy_dir=Vec2(0, -1)),
                        Vec3(48.455, 48.002, 76.542),
                        Vec3(53.653, 48.002, 81.718),
                        Vec3(54.820, 48.002, 86.253),
                        HoldDirection(237.500, 3.002, 71.498, joy_dir=Vec2(0, 1)),
                    ],
                ),
                SeqMove(
                    name="Move to Sacred Grove",
                    coords=[
                        Vec3(237.500, 3.002, 72.500),
                        Vec3(232.500, 3.002, 72.500),
                        Vec3(232.500, 3.002, 74.000),
                        Vec3(231.000, 3.002, 74.000),
                        Vec3(231.000, 3.002, 74.500),
                    ],
                ),
                SeqInteract("Sacred Grove"),
            ],
        )
