"""Routing of Mesa Hike."""

import logging
from typing import Self

from engine.mathlib import Vec2, Vec3
from engine.seq import (
    Graplou,
    HoldDirection,
    InteractMove,
    SeqHoldDirectionUntilLostControl,
    SeqInteract,
    SeqList,
    SeqMove,
    SeqSkipUntilIdle,
)

logger = logging.getLogger(__name__)


class MesaHike(SeqList):
    """Mesa Hike part of Mesa Island segment."""

    def __init__(self: Self) -> None:
        """Initialize a new MesaHike object."""
        super().__init__(
            name="Mesa Hike",
            children=[
                SeqMove(
                    name="Move to Mesa Hike",
                    coords=[
                        Vec3(246.500, 1.002, 160.500),
                    ],
                ),
                SeqInteract("Mesa Hike"),
                SeqMove(
                    name="Move to Khukharr",
                    coords=[
                        Vec3(10.349, 1.002, 11.055),
                    ],
                ),
                SeqHoldDirectionUntilLostControl("Move to Khukharr", joy_dir=Vec2(0, 1)),
                SeqSkipUntilIdle("Khukharr's task"),
                SeqMove(
                    name="Ascend to Mesa Island",
                    coords=[
                        Vec3(10.345, 1.002, 16.692),
                        Vec3(10.345, 1.002, 13.391),
                        Vec3(13.836, 1.002, 10.053),
                        Vec3(22.648, 1.002, 10.053),
                        InteractMove(22.648, 3.002, 11.467),
                        Graplou(22.597, 3.550, 14.530, joy_dir=Vec2(0, 1), hold_timer=0.1),
                        Vec3(22.597, 34.002, 16.809),
                        Vec3(27.034, 34.002, 20.003),
                        HoldDirection(245.500, 7.002, 162.998, joy_dir=Vec2(1, 0)),
                    ],
                ),
                SeqMove(
                    name="Move to Autumn Hills",
                    coords=[
                        Vec3(246.000, 7.002, 165.500),
                        Vec3(248.000, 7.002, 165.500),
                    ],
                ),
                # TODO(orkaboy): Equip Resh'an?
                SeqInteract("Autumn Hills"),
            ],
        )
