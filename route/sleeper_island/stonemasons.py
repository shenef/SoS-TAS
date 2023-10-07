"""Routing of Stonemason's Outpost section of Sleeper Island."""

import logging
from typing import Self

from engine.mathlib import Vec2, Vec3
from engine.seq import (
    HoldDirection,
    InteractMove,
    SeqAwaitLostControl,
    SeqCheckpoint,
    SeqClimb,
    SeqHoldDirectionUntilClose,
    SeqHoldDirectionUntilLostControl,
    SeqInteract,
    SeqList,
    SeqMove,
    SeqSkipUntilIdle,
)

logger = logging.getLogger(__name__)


class MoveToMines(SeqList):
    """Route from arrival at Stonemason's Outpost into the mines."""

    def __init__(self: Self) -> None:
        super().__init__(
            name="Navigate to mines",
            children=[
                SeqSkipUntilIdle("Await control"),
                SeqHoldDirectionUntilLostControl(
                    name="Enter outpost",
                    joy_dir=Vec2(1, 0),
                ),
                SeqSkipUntilIdle("Panicking Molekin"),
                SeqMove(
                    name="Move into mines",
                    coords=[
                        Vec3(15.428, 11.002, 23.590),
                        Vec3(21.657, 16.002, 23.590),
                        Vec3(22.453, 16.002, 29.540),
                        InteractMove(22.454, 21.002, 32.976),
                        Vec3(25.246, 26.002, 44.388),
                        HoldDirection(-16.500, 8.002, 68.000, joy_dir=Vec2(0, 1)),
                        Vec3(-16.500, 8.002, 76.540),
                    ],
                ),
                SeqInteract("Jump into pit"),
                SeqAwaitLostControl("Wait for cutscene"),
                SeqSkipUntilIdle("Screen transition"),
                SeqAwaitLostControl("Wait for cutscene"),
                SeqSkipUntilIdle("Elder"),
                SeqMove(
                    name="Leave elevator",
                    coords=[
                        Vec3(18.521, 1.002, 12.012),
                        Vec3(19.863, 1.002, 12.012),
                    ],
                ),
            ],
        )


class WindTunnelMines(SeqList):
    """Route through the Wind Tunnel Mines."""

    def __init__(self: Self) -> None:
        super().__init__(
            name="WindTunnelMines",
            children=[
                SeqMove(
                    name="Move into cave",
                    coords=[
                        Vec3(27.406, 1.002, 16.253),
                        InteractMove(27.500, 14.002, 20.634),
                        Vec3(26.299, 14.002, 20.634),
                        HoldDirection(33.500, 1.002, 76.500, joy_dir=Vec2(0, 1)),
                        Vec3(33.500, 1.002, 93.857),
                        Vec3(36.303, 1.002, 99.433),
                        Vec3(36.072, 1.002, 115.042),
                    ],
                ),
                SeqInteract("Lever"),
                SeqMove(
                    name="Move to wall",
                    coords=[
                        Vec3(36.407, 1.002, 101.482),
                        Vec3(44.240, 1.002, 101.419),
                        InteractMove(46.270, 3.002, 103.390),
                        Vec3(46.549, 3.002, 104.743),
                    ],
                ),
                SeqClimb(
                    name="Climb wall",
                    coords=[
                        InteractMove(46.712, 11.294, 104.623),
                        Vec3(44.463, 10.010, 106.873),
                    ],
                ),
                SeqMove(
                    name="Jump onto pillar",
                    coords=[
                        InteractMove(43.688, 10.002, 106.959),
                        Vec3(37.118, 10.002, 112.922),
                        InteractMove(31.539, 10.002, 112.922),
                    ],
                ),
                SeqHoldDirectionUntilClose(
                    name="Wait for pillar to depress",
                    target=Vec3(31.539, 3.020, 112.922),
                    joy_dir=Vec2(1, 0),
                    precision=0.2,
                ),
                # TODO(orkaboy): Continue routing
            ],
        )


class StonemasonsOutpost(SeqList):
    """Route from arrival at Stonemason's Outpost until leaving."""

    def __init__(self: Self) -> None:
        super().__init__(
            name="Stonemason's Outpost",
            children=[
                MoveToMines(),
                SeqCheckpoint("wind_tunnel_mines"),
                WindTunnelMines(),
            ],
        )
