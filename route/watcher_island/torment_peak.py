"""Routing of Torment Peak segment of Watcher Island."""

import logging
from typing import Self

from engine.mathlib import Vec2, Vec3
from engine.seq import (
    HoldDirection,
    InteractMove,
    MistralBracelet,
    SeqAwaitLostControl,
    SeqBraceletPuzzle,
    SeqChangeTimeOfDay,
    SeqCheckpoint,
    SeqDelay,
    SeqHoldDirectionUntilLostControl,
    SeqInteract,
    SeqList,
    SeqMove,
    SeqSkipUntilIdle,
)

logger = logging.getLogger(__name__)


class OnToTormentPeak(SeqList):
    """Routing from Lake Docarria to Torment Peak."""

    def __init__(self: Self) -> None:
        """Initialize a new OnToTormentPeak object."""
        super().__init__(
            name="On to Torment Peak",
            children=[
                SeqMove(
                    name="Navigate Lake Docarria",
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
                SeqChangeTimeOfDay("Right rune", time_target=16.0),
                SeqMove(
                    name="Move close to pedestal",
                    coords=[
                        Vec3(26.130, 5.002, -43.551),
                    ],
                ),
                SeqDelay("Wait for rune to fill", timeout_in_s=3.0),
                SeqChangeTimeOfDay("Left rune", time_target=8.0),
                SeqMove(
                    name="Move close to left rune",
                    coords=[
                        Vec3(19.323, 5.002, -40.471),
                    ],
                ),
                SeqSkipUntilIdle("Wait for idle"),
                SeqAwaitLostControl("Wait for cutscene"),
                SeqBraceletPuzzle(
                    name="Push blocks",
                    coords=[
                        Vec3(14.345, 5.002, -38.635),
                        Vec3(14.345, 5.002, -37.384),
                        MistralBracelet(joy_dir=Vec2(1, 0)),
                        Vec3(19.535, 5.002, -38.687),
                        Vec3(21.650, 5.002, -38.738),
                        MistralBracelet(joy_dir=Vec2(0, 1)),
                        Vec3(38.709, 5.002, -38.753),
                        Vec3(38.709, 5.002, -37.319),
                        MistralBracelet(joy_dir=Vec2(-1, 0)),
                        Vec3(33.369, 5.002, -38.883),
                        Vec3(32.552, 5.002, -38.883),
                        MistralBracelet(joy_dir=Vec2(0, 1)),
                    ],
                ),
                # Cutscene is a little finicky
                SeqSkipUntilIdle("Wait for control"),
                SeqHoldDirectionUntilLostControl("Move to cutscene", joy_dir=Vec2(-1, 1)),
                SeqSkipUntilIdle("No turning back now"),
                # Enter Torment Peak
                SeqMove(
                    name="Move to save branch",
                    coords=[
                        Vec3(26.280, 5.002, -30.670),
                        HoldDirection(27.500, 5.002, 4.301, joy_dir=Vec2(0, 1)),
                        Vec3(27.500, 5.002, 34.756),
                    ],
                ),
            ],
        )


class Dungeon(SeqList):
    """Routing of Dungeon segment of Torment Peak."""

    def __init__(self: Self) -> None:
        """Initialize a new Dungeon object."""
        super().__init__(
            name="Dungeon",
            children=[
                SeqMove(
                    name="",  # TODO(orkaboy): name
                    coords=[
                        Vec3(26.728, 5.002, 36.403),
                        # TODO(orkaboy): Continue routing
                    ],
                ),
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
                SeqCheckpoint("torment_peak"),
                Dungeon(),
                # TODO(orkaboy): Continue routing
            ],
        )
