"""Routing of Docarri Village segment of Watcher Island."""

import logging
from typing import Self

from engine.mathlib import Vec2, Vec3
from engine.seq import (
    HoldDirection,
    InteractMove,
    SeqCheckpoint,
    SeqHoldDirectionUntilLostControl,
    SeqInteract,
    SeqList,
    SeqMove,
    SeqSkipUntilIdle,
)

logger = logging.getLogger(__name__)


class DocarriVillage(SeqList):
    """Routing of Docarri Village segment of Watcher Island."""

    def __init__(self: Self) -> None:
        """Initialize a new DocarriVillage object."""
        super().__init__(
            name="Docarri Village",
            children=[
                SeqMove(
                    name="Overworld movement",
                    coords=[
                        Vec3(232.500, 3.002, 73.500),
                        Vec3(232.500, 3.002, 72.500),
                        Vec3(237.500, 3.002, 72.500),
                        Vec3(237.500, 3.002, 71.000),
                    ],
                ),
                SeqInteract("Lake Docarria"),
                SeqMove(
                    name="Swim to whirlpool",
                    coords=[
                        Vec3(53.433, 48.002, 81.845),
                        Vec3(47.994, 48.002, 76.294),
                        Vec3(43.052, 48.002, 74.917),
                        Vec3(40.816, 48.002, 73.454),
                        InteractMove(40.366, 40.803, 54.949),
                        Vec3(40.366, 40.803, 51.447),
                    ],
                ),
                SeqInteract("Whirlpool"),
                SeqCheckpoint("docarri_village"),
                SeqMove(
                    name="Move to shop branch",
                    coords=[
                        Vec3(40.200, 37.002, -207.552),
                        Vec3(36.805, 37.002, -206.892),
                        Vec3(34.379, 37.002, -199.543),
                    ],
                ),
                # TODO(orkaboy): Branch for shopping
                SeqMove(
                    name="Move to temple",
                    coords=[
                        Vec3(34.599, 37.002, -195.838),
                        Vec3(41.077, 37.002, -187.870),
                    ],
                ),
                SeqHoldDirectionUntilLostControl("Enter temple", joy_dir=Vec2(0, 1)),
                SeqSkipUntilIdle("Oracle of Tides"),
                SeqMove(
                    name="Move to Antsudlo",
                    coords=[
                        Vec3(-80.397, 3.002, 185.573),
                        HoldDirection(471.500, 1.002, 505.998, joy_dir=Vec2(0, 1)),
                        Vec3(471.500, 1.002, 513.000),
                    ],
                ),
                SeqInteract("Tower of Antsudlo"),
            ],
        )
