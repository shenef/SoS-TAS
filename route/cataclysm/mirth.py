"""Routing of the founding of Mirth during the Cataclysm."""

import logging
from typing import Self

from engine.mathlib import Vec2, Vec3
from engine.seq import (
    HoldDirection,
    InteractMove,
    SeqBoat,
    SeqHoldDirectionUntilLostControl,
    SeqInteract,
    SeqList,
    SeqMove,
    SeqSelectOption,
    SeqSkipUntilIdle,
)

logger = logging.getLogger(__name__)


class BriskRestored(SeqList):
    """Routing of the restored Brisk, up until arrival at Mirth."""

    def __init__(self: Self) -> None:
        """Initialize a new BriskRestored object."""
        super().__init__(
            name="Brisk restored",
            children=[
                SeqMove(
                    name="Move to Hortence",
                    coords=[
                        Vec3(34.650, 4.002, -19.340),
                        Vec3(32.141, 4.002, -19.161),
                        Vec3(32.323, 4.002, -20.941),
                    ],
                ),
                SeqSelectOption("Board boat", skip_dialog_check=True),
                SeqBoat(
                    name="Cutscene into boat",
                    coords=[
                        Vec3(146.739, 0.500, 150.732),
                    ],
                    hold_skip=True,
                ),
                SeqBoat(
                    name="Cross ocean",
                    coords=[
                        Vec3(217.436, 0.500, 183.592),
                        Vec3(225.185, 0.500, 185.897),
                        Vec3(228.283, 0.500, 189.447),
                        Vec3(228.808, 0.500, 192.250),
                    ],
                ),
                SeqInteract("Disembark"),
            ],
        )


class Mirth(SeqList):
    """Routing of Mirth sequence."""

    def __init__(self: Self) -> None:
        """Initialize a new Mirth object."""
        super().__init__(
            name="Mirth",
            children=[
                SeqMove(
                    name="Move to Settler's Rest",
                    coords=[
                        Vec3(226.500, 1.113, 193.500),
                    ],
                ),
                SeqInteract("Settler's Rest"),
                SeqSkipUntilIdle("Building Mirth"),
                SeqMove(
                    name="Head to Ancient Crypt",
                    coords=[
                        Vec3(-54.014, 12.002, 44.928),
                        Vec3(-64.144, 12.002, 49.157),
                        HoldDirection(224.500, 1.002, 193.998, joy_dir=Vec2(-1, 0)),
                        Vec3(224.500, 1.002, 196.500),
                        Vec3(225.500, 1.002, 196.500),
                        Vec3(225.500, 1.002, 199.000),
                        Vec3(224.500, 1.002, 199.000),
                        Vec3(224.500, 1.002, 200.500),
                        Vec3(223.000, 1.002, 200.500),
                        Vec3(223.000, 1.002, 201.000),
                        Vec3(221.500, 1.002, 201.000),
                        Vec3(221.500, 1.002, 202.500),
                    ],
                ),
                SeqInteract("Ancient Crypt"),
                SeqSkipUntilIdle("Wait for idle"),
                SeqHoldDirectionUntilLostControl("Move into cutscene", joy_dir=Vec2(0, 1)),
                SeqSkipUntilIdle("Cryptwalker"),
                SeqMove(
                    name="Leave Ancient Crypt",
                    coords=[
                        Vec3(328.581, 9.002, 433.494),
                        HoldDirection(330.142, 1.002, 385.055, joy_dir=Vec2(0, -1)),
                        Vec3(330.142, 1.002, 373.517),
                        HoldDirection(221.500, 1.002, 201.998, joy_dir=Vec2(0, -1)),
                    ],
                ),
                SeqMove(
                    name="Move to Mirth",
                    coords=[
                        Vec3(221.500, 1.002, 201.000),
                        Vec3(223.000, 1.002, 201.000),
                        Vec3(223.000, 1.002, 200.500),
                        Vec3(224.500, 1.002, 200.500),
                        Vec3(224.500, 1.002, 199.000),
                        Vec3(225.500, 1.002, 199.000),
                        Vec3(225.500, 1.002, 196.500),
                        Vec3(224.500, 1.002, 196.500),
                        Vec3(224.500, 1.002, 194.000),
                        Vec3(225.000, 1.002, 194.000),
                    ],
                ),
                SeqInteract("Mirth"),
                SeqSkipUntilIdle("Naming Mirth"),
                SeqMove(
                    name="Move to Hortence",
                    coords=[
                        Vec3(5.996, 12.002, 24.565),
                        Vec3(11.939, 8.002, 21.682),
                        Vec3(14.543, 8.002, 18.460),
                        InteractMove(15.461, 4.848, 18.460),
                        Vec3(15.461, 4.010, 17.101),
                        Vec3(8.604, 4.010, 13.455),
                        Vec3(2.235, 4.010, 6.891),
                        Vec3(2.235, 4.010, 2.086),
                        Vec3(12.442, 4.002, 0.562),
                    ],
                ),
                SeqSelectOption("Board boat", skip_dialog_check=True),
            ],
        )
