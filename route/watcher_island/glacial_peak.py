"""Routing of Glacial Peak segment of Watcher Island."""

import logging
from typing import Self

from engine.mathlib import Vec2, Vec3
from engine.seq import (
    Graplou,
    InteractMove,
    SeqCheckpoint,
    SeqClimb,
    SeqList,
    SeqMove,
)

logger = logging.getLogger(__name__)


class Ascent(SeqList):
    """Routing of Ascent part of Glacial Peak."""

    def __init__(self: Self) -> None:
        """Initialize a new Ascent object."""
        super().__init__(
            name="Ascent",
            children=[
                SeqMove(
                    name="Move to wall",
                    coords=[
                        Vec3(20.914, 9.002, 12.974),
                        Vec3(25.908, 9.002, 17.379),
                    ],
                ),
                SeqClimb(
                    name="Climb wall",
                    coords=[
                        InteractMove(26.632, 10.540, 16.703),
                        Vec3(29.694, 10.993, 15.530),
                    ],
                ),
                SeqMove(
                    name="Move to save branch",
                    coords=[
                        Vec3(29.694, 15.002, 17.367),
                        Vec3(26.308, 15.002, 20.941),
                        Graplou(7.501, 15.010, 21.258, joy_dir=Vec2(-1, 0), hold_timer=0.1),
                        Vec3(-0.726, 15.002, 17.024),
                    ],
                ),
                SeqCheckpoint(
                    "glacial_peak",
                    return_path=SeqMove(
                        name="Return to path",
                        coords=[
                            Vec3(1.281, 15.002, 13.121),
                        ],
                    ),
                ),
                # TODO(orkaboy): Continue routing
            ],
        )


class GlacialPeak(SeqList):
    """Routing of Glacial Peak segment of Watcher Island (technically Mesa)."""

    def __init__(self: Self) -> None:
        """Initialize a new GlacialPeak object."""
        super().__init__(
            name="Glacial Peak",
            children=[
                Ascent(),
                # TODO(orkaboy): Continue routing
            ],
        )
