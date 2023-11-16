"""Routing of Torment Peak segment of Watcher Island."""

import logging
from typing import Self

from engine.mathlib import Vec2, Vec3
from engine.seq import (
    HoldDirection,
    InteractMove,
    SeqInteract,
    SeqList,
    SeqMove,
)

logger = logging.getLogger(__name__)


class OnToTormentPeak(SeqList):
    """Routing from Lake Doccaria to Torment Peak."""

    def __init__(self: Self) -> None:
        """Initialize a new OnToTormentPeak object."""
        super().__init__(
            name="On to Torment Peak",
            children=[
                SeqMove(
                    name="Navigate Lake Doccaria",
                    coords=[
                        Vec3(63.480, 43.002, 64.460),
                        InteractMove(63.459, 40.803, 63.540),
                        Vec3(50.394, 40.803, 62.848),
                        Vec3(28.628, 40.803, 65.011),
                        Vec3(24.992, 40.803, 74.351),
                        InteractMove(24.148, 43.002, 75.156),
                        Vec3(24.148, 43.002, 77.281),
                        Vec3(39.631, 48.002, 76.688),
                        Vec3(41.845, 48.002, 75.835),
                        Vec3(47.688, 48.002, 75.835),
                        Vec3(53.691, 48.002, 82.063),
                        Vec3(54.618, 48.002, 86.572),
                        HoldDirection(237.500, 3.002, 71.498, joy_dir=Vec2(0, 1)),
                    ],
                ),
                SeqMove(
                    name="Navigate overworld",
                    coords=[
                        Vec3(237.500, 3.002, 73.000),
                        Vec3(238.000, 3.002, 73.000),
                        Vec3(238.000, 3.002, 77.000),
                        Vec3(237.500, 3.002, 77.000),
                        Vec3(237.500, 3.002, 77.500),
                    ],
                ),
                SeqInteract("Torment Peak"),
                # TODO(orkaboy): Continue routing
            ],
        )


class TormentPeak(SeqList):
    """Routing of Torment Peak segment of Watcher Island."""

    def __init__(self: Self) -> None:
        """Initialize a new TormentPeak object."""
        super().__init__(
            name="Torment Peak",
            children=[
                OnToTormentPeak(),
                # TODO(orkaboy): Continue routing
            ],
        )
