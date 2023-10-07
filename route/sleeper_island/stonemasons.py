"""Routing of Stonemason's Outpost section of Sleeper Island."""

import logging
from typing import Self

from engine.combat import SeqCombat, SeqCombatAndMove
from engine.mathlib import Vec2, Vec3
from engine.seq import (
    HoldDirection,
    InteractMove,
    MoveToward,
    SeqAwaitLostControl,
    SeqCheckpoint,
    SeqCliffMove,
    SeqClimb,
    SeqHoldDirectionUntilClose,
    SeqHoldDirectionUntilCombat,
    SeqHoldDirectionUntilLostControl,
    SeqInteract,
    SeqList,
    SeqMove,
    SeqRouteBranch,
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
                SeqCombatAndMove(
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
                SeqCombatAndMove(
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
                        InteractMove(43.915, 10.002, 106.732),
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
                SeqMove(
                    name="Move to lever",
                    coords=[
                        InteractMove(34.057, 1.002, 112.459),
                        Vec3(34.947, 1.002, 114.740),
                    ],
                ),
                SeqInteract("Lever"),
                SeqMove(
                    name="Move to ledge",
                    coords=[
                        Vec3(37.867, 1.002, 111.028),
                        Vec3(40.346, 1.002, 110.650),
                    ],
                ),
                SeqCliffMove(
                    name="Move along ledge",
                    coords=[
                        HoldDirection(42.452, 1.000, 111.000, joy_dir=Vec2(1, 0)),
                        Vec3(50.870, 1.000, 112.000),
                    ],
                ),
                SeqMove(
                    name="Move to branch",
                    coords=[
                        HoldDirection(52.839, 1.002, 111.242, joy_dir=Vec2(1, 0)),
                        Vec3(80.900, 1.002, 110.469),
                        Vec3(81.042, 1.002, 109.688),
                    ],
                ),
                # Optionally, grab Green Leaf
                SeqRouteBranch(
                    name="Green Leaf",
                    route=["wtm_green_leaf"],
                    when_true=SeqList(
                        name="Upper route",
                        children=[
                            SeqMove(
                                name="Move to chest",
                                coords=[
                                    Vec3(83.398, 1.002, 109.710),
                                    InteractMove(85.980, 8.002, 112.680),
                                    Vec3(90.894, 8.002, 113.510),
                                    Vec3(92.588, 8.002, 113.237),
                                    InteractMove(93.237, 5.002, 112.588),
                                    Vec3(97.205, 5.002, 112.148),
                                    InteractMove(97.875, 8.002, 112.789),
                                    Vec3(101.648, 8.002, 113.502),
                                    Vec3(105.640, 8.002, 113.502),
                                ],
                            ),
                            SeqInteract("Green Leaf"),
                            SeqSkipUntilIdle("Green Leaf"),
                            # TODO(orkaboy): Equip?
                            SeqMove(
                                name="Return to route",
                                coords=[
                                    Vec3(105.640, 8.002, 111.460),
                                    InteractMove(105.640, 1.002, 110.542),
                                ],
                            ),
                        ],
                    ),
                    when_false=SeqMove(
                        name="Lower route",
                        coords=[
                            Vec3(85.592, 1.002, 107.717),
                            Vec3(92.530, 1.002, 107.454),
                            InteractMove(98.481, 1.002, 107.454),
                            Vec3(107.310, 1.002, 107.454),
                        ],
                    ),
                ),
                SeqMove(
                    name="Move to ledge",
                    coords=[
                        Vec3(113.758, 1.002, 109.424),
                        Vec3(137.455, 1.002, 109.272),
                        Vec3(139.931, 1.002, 111.479),
                    ],
                ),
                SeqCliffMove(
                    name="Move along ledge",
                    coords=[
                        HoldDirection(142.999, 1.000, 112.000, joy_dir=Vec2(1, 1)),
                        Vec3(145.728, 1.000, 111.713),
                        HoldDirection(148.451, 1.002, 109.216, joy_dir=Vec2(1, -1)),
                    ],
                ),
                SeqMove(
                    name="Move to chest",
                    coords=[
                        Vec3(150.365, 1.002, 109.476),
                        InteractMove(150.365, 7.002, 112.467),
                        Vec3(152.540, 7.002, 112.467),
                        InteractMove(153.875, 8.002, 112.467),
                        Vec3(153.875, 8.002, 106.727),
                        Vec3(151.974, 8.002, 104.677),
                        InteractMove(150.335, 8.002, 102.985),
                        Vec3(149.458, 8.002, 102.355),
                        Vec3(149.458, 8.002, 100.405),
                        Vec3(148.881, 8.002, 99.770),
                        InteractMove(147.215, 8.002, 98.104),
                        Vec3(146.284, 8.002, 97.115),
                        Vec3(146.284, 8.002, 93.630),
                        Vec3(147.940, 8.002, 91.943),
                        InteractMove(149.781, 8.002, 90.101),
                        Vec3(151.085, 8.002, 89.095),
                        Vec3(151.085, 8.002, 87.762),
                        Vec3(152.793, 8.002, 86.565),
                        Vec3(154.415, 8.002, 86.548),
                        InteractMove(161.614, 8.002, 86.548),
                        Vec3(164.040, 8.002, 86.548),
                    ],
                ),
                SeqInteract("Teal Amber Ore"),
                SeqSkipUntilIdle("Teal Amber Ore"),
                SeqMove(
                    name="Move to fight",
                    coords=[
                        Vec3(164.040, 8.002, 88.082),
                        Vec3(165.186, 8.002, 89.165),
                        InteractMove(167.186, 8.002, 90.886),
                        Vec3(168.119, 8.002, 93.508),
                        InteractMove(168.119, 8.002, 96.939),
                        Vec3(167.221, 8.002, 100.701),
                        Vec3(164.649, 8.002, 102.998),
                        InteractMove(162.979, 8.002, 104.947),
                        Vec3(161.252, 8.002, 106.732),
                        Vec3(161.252, 8.002, 110.576),
                        Vec3(166.582, 8.002, 116.006),
                        Vec3(175.703, 8.002, 116.006),
                        Vec3(180.724, 8.002, 111.408),
                        HoldDirection(240.500, 1.002, 113.500, joy_dir=Vec2(1, 1)),
                        Vec3(243.178, 1.002, 115.641),
                        Vec3(249.894, 1.002, 115.619),
                        Vec3(252.783, 1.002, 111.985),
                        Vec3(252.783, 1.002, 105.423),
                        HoldDirection(114.500, 12.002, 27.733, joy_dir=Vec2(0, -1)),
                        Vec3(114.500, 12.002, 26.166),
                        Vec3(112.567, 12.002, 24.084),
                    ],
                ),
                SeqInteract("Jump into pit"),
                SeqHoldDirectionUntilCombat(
                    name="Start fight",
                    joy_dir=Vec2(-1, 0.5),
                    mash_confirm=True,
                ),
                SeqCombat("Fight Bushtroo"),
                SeqMove(
                    name="Move into tunnel mouth",
                    coords=[
                        Vec3(99.725, 2.002, 28.737),
                        InteractMove(98.564, 3.002, 29.228),
                    ],
                ),
                SeqHoldDirectionUntilLostControl(
                    name="Go into tunnel",
                    joy_dir=Vec2(-1, 1),
                ),
                SeqSkipUntilIdle("Wind tunnel"),
                SeqAwaitLostControl("Screen transition"),
                SeqSkipUntilIdle("Elder cutscene"),
                SeqCheckpoint("wind_tunnel_mines2"),
                SeqMove(
                    name="Move to elevator shaft",
                    coords=[
                        Vec3(21.364, 1.002, 12.669),
                        Vec3(17.251, 1.002, 11.549),
                        MoveToward(-69.250, 0.002, 15.500, anchor=Vec3(15, 1.002, 13), mash=True),
                    ],
                ),
                # TODO(orkaboy): Continue routing (second floor)
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
