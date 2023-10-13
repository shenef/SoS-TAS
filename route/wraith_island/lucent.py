"""Routing of Lucent section of Wraith Island."""

import logging
from typing import Self

from engine.mathlib import Vec2, Vec3
from engine.seq import (
    HoldDirection,
    SeqHoldDirectionUntilLostControl,
    SeqInteract,
    SeqList,
    SeqMove,
    SeqSelectOption,
    SeqSkipUntilIdle,
)

logger = logging.getLogger(__name__)


class LucentArrival(SeqList):
    """Routing of Lucent, from arrival from docks to leaving for Cursed Woods."""

    def __init__(self: Self) -> None:
        """Initialize a new LucentArrival object."""
        super().__init__(
            name="Lucent",
            children=[
                SeqMove(
                    name="Move to fountain",
                    coords=[
                        Vec3(26.333, 1.002, 19.224),
                        Vec3(22.102, 1.002, 26.034),
                        Vec3(22.102, 1.002, 29.360),
                    ],
                ),
                # TODO(orkaboy): Shopping in building to the left
                SeqMove(
                    name="Move to inn",
                    coords=[
                        Vec3(25.577, 1.002, 32.925),
                    ],
                ),
                SeqHoldDirectionUntilLostControl("Enter First Stage of Grief", joy_dir=Vec2(0, 1)),
                SeqSkipUntilIdle("The First Stage of Grief"),
                SeqMove(
                    name="Approach Edgar",
                    coords=[
                        Vec3(38.710, 1.002, 114.708),
                    ],
                ),
                SeqSelectOption("Rest"),
                SeqSkipUntilIdle("Call of the cursed voice"),
                SeqMove(
                    name="Leave for world map",
                    coords=[
                        Vec3(27.586, 1.002, 32.619),
                        Vec3(67.814, 1.002, 32.619),
                        HoldDirection(191.500, 1.002, 109.998, joy_dir=Vec2(1, 0)),
                    ],
                ),
                SeqMove(
                    name="Move to Cursed Woods",
                    coords=[
                        Vec3(193.500, 1.002, 110.000),
                        Vec3(193.500, 1.002, 111.000),
                        Vec3(194.500, 1.002, 111.000),
                        Vec3(194.500, 1.002, 115.000),
                        Vec3(191.000, 1.002, 115.000),
                        Vec3(191.000, 1.002, 116.500),
                        Vec3(187.500, 1.002, 116.500),
                        Vec3(187.500, 1.002, 117.500),
                    ],
                ),
                SeqInteract("Cursed Woods"),
            ],
        )
