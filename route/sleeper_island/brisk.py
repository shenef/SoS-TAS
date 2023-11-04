"""Routing of Brisk section of Sleeper Island."""

import logging
from typing import Self

from engine.mathlib import Vec2, Vec3
from engine.seq import (
    HoldDirection,
    SeqCheckpoint,
    SeqHoldDirectionUntilLostControl,
    SeqInteract,
    SeqList,
    SeqMashUntilIdle,
    SeqMove,
    SeqSkipUntilIdle,
)

logger = logging.getLogger(__name__)


class Brisk(SeqList):
    """Route from arrival at Brisk until leaving."""

    def __init__(self: Self) -> None:
        """Initialize a new Brisk object."""
        super().__init__(
            name="Brisk",
            children=[
                SeqSkipUntilIdle("Cutscene", hold_cancel=True),
                SeqMove(
                    name="Move to pirates",
                    coords=[
                        Vec3(3.097, 4.002, 48.114),
                        Vec3(4.627, 4.002, 27.412),
                        Vec3(11.467, 4.002, 20.297),
                        Vec3(11.467, 4.002, 9.450),
                        Vec3(25.520, 4.002, 2.325),
                        Vec3(33.536, 4.002, -5.871),
                    ],
                ),
                SeqHoldDirectionUntilLostControl("Pirates", joy_dir=Vec2(0, -1)),
                SeqSkipUntilIdle("Pirates"),
                SeqMove(
                    name="Move down",
                    coords=[
                        Vec3(44.195, 4.002, -18.460),
                    ],
                ),
                SeqCheckpoint("brisk"),
                # TODO(orkaboy): Can optionally buy stuff here
                SeqMove(
                    name="Move to Humble Boast",
                    coords=[
                        Vec3(54.043, 4.002, -18.460),
                        Vec3(73.276, 4.002, -19.657),
                        Vec3(84.918, 4.002, -17.815),
                        Vec3(89.295, 4.002, -17.815),
                        Vec3(100.957, 3.002, -28.523),
                        Vec3(104.318, 3.002, -28.523),
                        Vec3(109.050, 3.002, -23.832),
                        HoldDirection(237.875, 1.002, -12.278, joy_dir=Vec2(1, 1)),
                        Vec3(245.042, 1.002, -9.262),
                        Vec3(251.600, 1.002, -4.355),
                    ],
                ),
                SeqHoldDirectionUntilLostControl("Garl cooking", joy_dir=Vec2(0, 1)),
                SeqSkipUntilIdle("Garl cooking"),
                SeqMove(
                    name="Move to pirates",
                    coords=[
                        Vec3(251.458, 1.002, -3.882),
                        Vec3(247.337, 1.002, -8.228),
                        Vec3(234.289, 1.002, 5.248),
                        Vec3(230.417, 1.002, 5.226),
                    ],
                ),
                SeqHoldDirectionUntilLostControl("Pirates", joy_dir=Vec2(-1, 1)),
                SeqMashUntilIdle("Arm wrestling"),
                SeqMove(
                    name="Move to exit",
                    coords=[
                        Vec3(227.700, 3.002, 12.295),
                        Vec3(227.700, 3.002, 8.836),
                        Vec3(233.083, 1.010, 3.805),
                        Vec3(235.154, 1.002, 3.783),
                        Vec3(242.085, 1.002, -2.910),
                        Vec3(242.085, 1.002, -8.163),
                    ],
                ),
                SeqHoldDirectionUntilLostControl("Move to exit", joy_dir=Vec2(-1, -1)),
                SeqSkipUntilIdle("Wheels"),
                SeqMove(
                    name="Leave town",
                    coords=[
                        HoldDirection(110.333, 3.002, -22.722, joy_dir=Vec2(-1, -1)),
                        Vec3(103.540, 3.002, -29.663),
                        Vec3(88.638, 4.002, -17.359),
                        Vec3(77.999, 4.002, -17.359),
                        Vec3(74.805, 4.002, -19.942),
                        Vec3(43.898, 4.002, -19.942),
                        Vec3(18.201, 4.002, 5.593),
                        Vec3(11.795, 4.002, 9.151),
                        Vec3(11.795, 4.002, 20.242),
                        Vec3(3.581, 4.002, 28.249),
                        Vec3(3.581, 4.002, 49.682),
                        Vec3(-1.717, 4.002, 55.070),
                        Vec3(-7.326, 4.002, 60.114),
                        HoldDirection(134.500, 1.002, 151.498, joy_dir=Vec2(-1, 0.5)),
                    ],
                ),
            ],
        )


class BriskToWizardLab(SeqList):
    def __init__(self: Self) -> None:
        """Initialize a new BriskToWizardLab object."""
        super().__init__(
            name="World map",
            children=[
                SeqMove(
                    name="Move to wizard lab",
                    coords=[
                        Vec3(134.000, 1.002, 151.500),
                        Vec3(134.000, 1.002, 160.000),
                        Vec3(144.000, 1.002, 160.000),
                        Vec3(144.000, 1.002, 161.000),
                    ],
                ),
                SeqInteract("Enter wizard lab"),
            ],
        )
