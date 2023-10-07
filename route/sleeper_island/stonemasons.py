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
    SeqBracelet,
    SeqCheckpoint,
    SeqCliffMove,
    SeqClimb,
    SeqDelay,
    SeqHoldDirectionDelay,
    SeqHoldDirectionUntilClose,
    SeqHoldDirectionUntilCombat,
    SeqHoldDirectionUntilLostControl,
    SeqInteract,
    SeqList,
    SeqMove,
    SeqRouteBranch,
    SeqSkipUntilCombat,
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


class WindTunnelMinesFirstFloor(SeqList):
    """Route through the First Floor of Wind Tunnel Mines."""

    def __init__(self: Self) -> None:
        super().__init__(
            name="Wind Tunnel Mines First Floor",
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
            ],
        )


class WindTunnelMinesLowerFloorBlockPuzzle1(SeqList):
    """First block puzzle sequence."""

    def __init__(self: Self) -> None:
        super().__init__(
            name="Block Puzzle #1",
            children=[
                SeqMove(
                    name="Move south of block",
                    coords=[
                        Vec3(146.307, 1.002, -92.047),
                        InteractMove(135.818, 1.002, -92.047),
                        Vec3(124.043, 1.002, -92.614),
                        Vec3(124.043, 1.002, -91.460),
                    ],
                ),
                SeqBracelet("Push block"),
                SeqMove(
                    name="Move left of block",
                    coords=[
                        Vec3(122.067, 1.002, -90.512),
                        Vec3(122.067, 1.002, -88.945),
                    ],
                ),
                SeqHoldDirectionDelay(name="Block", joy_dir=Vec2(1, 0), timeout_s=0.2),
                SeqBracelet("Push block"),
                SeqMove(
                    name="Move north of block",
                    coords=[
                        Vec3(125.220, 1.002, -86.541),
                        Vec3(128.214, 1.002, -86.659),
                    ],
                ),
                SeqHoldDirectionDelay(name="Block", joy_dir=Vec2(0, -1), timeout_s=0.2),
                SeqBracelet("Push block"),
                SeqMove(
                    name="Move right of block",
                    coords=[
                        Vec3(129.907, 1.002, -93.817),
                        Vec3(129.929, 1.002, -95.855),
                    ],
                ),
                SeqHoldDirectionDelay(name="Block", joy_dir=Vec2(-1, 0), timeout_s=0.2),
                SeqBracelet("Push block"),
                SeqMove(
                    name="Move south of block",
                    coords=[
                        Vec3(124.476, 1.002, -97.991),
                        Vec3(119.140, 1.002, -97.991),
                    ],
                ),
                SeqHoldDirectionDelay(name="Block", joy_dir=Vec2(0, 1), timeout_s=0.2),
                SeqBracelet("Push block"),
                SeqMove(
                    name="Move to right of block",
                    coords=[
                        Vec3(120.715, 1.002, -93.769),
                        Vec3(120.715, 1.002, -91.819),
                    ],
                ),
                SeqHoldDirectionDelay(name="Block", joy_dir=Vec2(-1, 0), timeout_s=0.2),
                SeqBracelet("Push block"),
                # Block puzzle done
            ],
        )


class WindTunnelMinesLowerFloorBlockPuzzle2(SeqList):
    """Second block puzzle sequence."""

    def __init__(self: Self) -> None:
        super().__init__(
            name="Block Puzzle #2",
            children=[
                SeqHoldDirectionDelay(name="Block", joy_dir=Vec2(1, 0), timeout_s=0.2),
                SeqBracelet("Push block"),
                SeqMove(
                    name="Move north of block",
                    coords=[
                        Vec3(-56.904, 1.010, 9.713),
                        Vec3(-53.961, 1.002, 9.713),
                    ],
                ),
                SeqHoldDirectionDelay(name="Block", joy_dir=Vec2(0, -1), timeout_s=0.2),
                SeqBracelet("Push block"),
                SeqMove(
                    name="Move right of block",
                    coords=[
                        Vec3(-52.402, 1.010, 5.533),
                        Vec3(-52.402, 1.010, 0.896),
                    ],
                ),
                SeqHoldDirectionDelay(name="Block", joy_dir=Vec2(-1, 0), timeout_s=0.2),
                SeqBracelet("Push block"),
                SeqMove(
                    name="Move south of block",
                    coords=[
                        Vec3(-57.365, 1.002, -0.616),
                        Vec3(-63.142, 1.002, -0.616),
                    ],
                ),
                SeqHoldDirectionDelay(name="Block", joy_dir=Vec2(0, 1), timeout_s=0.2),
                SeqBracelet("Push block"),
                SeqMove(
                    name="Move north of block",
                    coords=[
                        Vec3(-71.421, 1.010, 7.773),
                        Vec3(-75.965, 1.002, 7.773),
                    ],
                ),
                SeqDelay("Wait", timeout_in_s=6.0),
                SeqHoldDirectionDelay(name="Block", joy_dir=Vec2(0, -1), timeout_s=0.2),
                SeqBracelet("Push block"),
                SeqMove(
                    name="Move right of block",
                    coords=[
                        Vec3(-74.251, 1.002, 5.236),
                        Vec3(-74.251, 1.002, 2.102),
                    ],
                ),
                SeqHoldDirectionDelay(name="Block", joy_dir=Vec2(-1, 0), timeout_s=0.2),
                SeqBracelet("Push block"),
                SeqMove(
                    name="Move south of block",
                    coords=[
                        Vec3(-86.716, 1.002, 0.232),
                        Vec3(-91.953, 1.002, 0.232),
                    ],
                ),
                SeqHoldDirectionDelay(name="Block", joy_dir=Vec2(0, 1), timeout_s=0.2),
                SeqBracelet("Push block"),
                # Block puzzle done
            ],
        )


class WindTunnelMinesLowerFloor(SeqList):
    """Route through the lower floor Wind Tunnel Mines."""

    def __init__(self: Self) -> None:
        super().__init__(
            name="Wind Tunnel Mines Lower Floor",
            children=[
                SeqMove(
                    name="Jump into elevator shaft",
                    coords=[
                        Vec3(21.364, 1.002, 12.669),
                        Vec3(17.251, 1.002, 11.549),
                        MoveToward(-69.250, 0.002, 15.500, anchor=Vec3(15, 1.002, 13), mash=True),
                        Vec3(-71.005, 0.002, 13.243),
                        InteractMove(-71.005, 1.002, 11.266),
                    ],
                ),
                SeqHoldDirectionUntilCombat(
                    name="Attack!", joy_dir=Vec2(-1, -1), mash_confirm=True
                ),
                SeqCombat("Bats and ant"),
                SeqMove(
                    name="Move to ladder",
                    coords=[
                        Vec3(-85.505, 1.002, 16.540),
                    ],
                ),
                SeqClimb(
                    name="Climb ladder",
                    coords=[
                        InteractMove(-85.500, 5.112, 16.530),
                    ],
                ),
                SeqMove(
                    name="Head outside",
                    coords=[
                        HoldDirection(-85.490, 9.002, 17.998, joy_dir=Vec2(0, 1)),
                        Vec3(-83.156, 9.002, 17.998),
                        Vec3(-80.520, 9.002, 14.775),
                        Vec3(-80.520, 9.002, 8.498),
                        Vec3(-80.291, 9.002, 8.238),
                        InteractMove(-70.930, 9.004, -1.070),
                        Vec3(-70.096, 9.002, -7.515),
                        HoldDirection(-15.000, -2.998, -77.067, joy_dir=Vec2(0, -1)),
                        Vec3(-11.032, -2.998, -77.067),
                        InteractMove(-6.393, -2.998, -77.067),
                        Vec3(3.460, -0.998, -77.108),
                    ],
                ),
                SeqClimb(
                    name="Climb ladder",
                    coords=[
                        InteractMove(3.500, 3.090, -76.470),
                        Vec3(3.500, 9.002, -75.533),
                    ],
                ),
                SeqMove(
                    name="Head back inside",
                    coords=[
                        Vec3(1.550, 9.002, -75.533),
                        Vec3(0.407, 9.002, -76.765),
                        Vec3(-5.228, 12.002, -76.765),
                        InteractMove(-6.458, 6.002, -76.765),
                        HoldDirection(95.000, 1.002, -98.500, joy_dir=Vec2(0, 1)),
                        Vec3(95.000, 1.002, -96.724),
                        Vec3(101.511, 1.002, -91.928),
                        Vec3(101.511, 1.002, -89.460),
                        InteractMove(101.500, 8.002, -88.125),
                        Vec3(110.148, 8.002, -80.457),
                    ],
                ),
                SeqClimb(
                    name="Climb wall",
                    coords=[
                        InteractMove(110.219, 11.540, -80.470),
                        Vec3(119.796, 11.540, -80.470),
                    ],
                ),
                SeqMove(
                    name="Cross rope",
                    coords=[
                        Vec3(119.796, 9.002, -81.962),
                        InteractMove(124.083, 9.002, -82.500),
                        InteractMove(132.250, 9.002, -82.500),
                        Vec3(136.540, 9.002, -80.454),
                    ],
                ),
                SeqClimb(
                    name="Climb wall",
                    coords=[
                        InteractMove(136.540, 11.248, -80.470),
                        Vec3(140.079, 11.230, -80.470),
                        Vec3(142.141, 9.165, -80.470),
                        Vec3(144.887, 9.036, -80.470),
                        Vec3(147.224, 11.259, -80.470),
                        Vec3(149.308, 11.259, -80.470),
                    ],
                ),
                SeqMove(
                    name="Get off wall",
                    coords=[
                        Vec3(149.983, 8.002, -81.687),
                    ],
                ),
                SeqCheckpoint("wind_tunnel_mines3"),
                SeqMove(
                    name="Move to wall",
                    coords=[
                        Vec3(153.858, 8.002, -85.539),
                        Vec3(155.540, 8.002, -85.539),
                        InteractMove(156.458, 2.002, -85.539),
                        Vec3(158.683, 2.002, -83.457),
                    ],
                ),
                SeqClimb(
                    name="Climb wall",
                    coords=[
                        InteractMove(158.500, 4.276, -83.470),
                    ],
                ),
                SeqMove(
                    name="Move to chest",
                    coords=[
                        Vec3(158.500, 7.002, -82.533),
                        HoldDirection(233.500, 1.002, -94.891, joy_dir=Vec2(0, 1)),
                        Vec3(233.500, 1.002, -75.200),
                    ],
                ),
                SeqInteract("Mistral Bracelet"),
                SeqSkipUntilIdle("Mistral Bracelet"),
                SeqMove(
                    name="Move to block",
                    coords=[
                        Vec3(233.500, 1.002, -93.340),
                        HoldDirection(158.500, 7.002, -80.500, joy_dir=Vec2(0, -1)),
                        InteractMove(158.500, 2.002, -85.846),
                        Vec3(158.500, 2.002, -87.540),
                    ],
                ),
                SeqBracelet("Push block"),
                SeqMove(
                    name="Move right of block",
                    coords=[
                        Vec3(159.541, 2.002, -89.799),
                        InteractMove(160.852, 1.002, -91.332),
                        Vec3(159.642, 1.002, -91.784),
                    ],
                ),
                SeqBracelet("Push block"),
                SeqAwaitLostControl("Wait for cutscene"),
                SeqSkipUntilCombat("Rockie"),
                SeqCombat("Rockie"),
                SeqSkipUntilIdle("Cutscene"),
                # Block puzzle with Mistral Bracelet
                WindTunnelMinesLowerFloorBlockPuzzle1(),
                SeqMove(
                    name="Move outside",
                    coords=[
                        Vec3(116.460, 1.002, -92.099),
                        InteractMove(110.840, 7.002, -92.099),
                        Vec3(108.830, 7.002, -92.099),
                        InteractMove(107.006, 1.002, -93.956),
                        Vec3(95.013, 1.002, -96.624),
                        HoldDirection(-7.000, 6.002, -77.225, joy_dir=Vec2(0, -1)),
                        Vec3(-6.137, 6.002, -78.540),
                        InteractMove(-6.137, -2.998, -79.458),
                        Vec3(1.216, -0.998, -77.205),
                        Vec3(5.540, -0.998, -77.205),
                    ],
                ),
                SeqBracelet("Push block"),
                SeqMove(
                    name="Move to cavern",
                    coords=[
                        Vec3(8.577, -1.003, -77.183),
                        InteractMove(12.481, -0.998, -77.183),
                        Vec3(31.736, 7.002, -77.183),
                        InteractMove(36.015, 7.002, -77.183),
                        Vec3(40.845, 7.002, -72.911),
                        InteractMove(43.708, -0.998, -72.440),
                        Vec3(48.914, -0.998, -67.407),
                        Vec3(48.936, -0.998, -64.985),
                        HoldDirection(109.246, 1.002, -42.246, joy_dir=Vec2(-1, 1)),
                    ],
                ),
                SeqHoldDirectionUntilCombat(
                    name="Start fight",
                    joy_dir=Vec2(-1, 1),
                    mash_confirm=True,
                ),
                SeqCombat("Fight Bushtroo"),
                SeqMove(
                    name="Move to tunnel mouth",
                    coords=[
                        Vec3(93.373, 1.002, -33.274),
                        InteractMove(92.663, 2.002, -32.462),
                    ],
                ),
                SeqHoldDirectionUntilLostControl(
                    name="Go into tunnel",
                    joy_dir=Vec2(-1, 1),
                ),
                SeqMove(
                    name="Move to windtrap",
                    coords=[
                        Vec3(-76.669, 1.002, 11.049),
                        Vec3(-85.591, 1.002, 15.799),
                        InteractMove(-85.500, 9.002, 17.467),
                        Vec3(-82.983, 9.002, 17.467),
                        Vec3(-79.696, 9.002, 15.027),
                        Vec3(-76.522, 11.002, 15.027),
                        Vec3(-72.927, 11.002, 11.594),
                        Vec3(-65.879, 11.002, 11.543),
                        Vec3(-61.856, 10.986, 15.195),
                        Vec3(-58.469, 9.002, 16.319),
                        Vec3(-57.958, 9.056, 19.568),
                    ],
                ),
                SeqBracelet("Windtrap"),
                SeqMove(
                    name="Move to box puzzle",
                    coords=[
                        Vec3(-57.958, 9.010, 14.462),
                        InteractMove(-57.958, 1.002, 13.192),
                        Vec3(-59.908, 1.002, 9.577),
                        Vec3(-59.908, 1.002, 7.960),
                    ],
                ),
                # Second block puzzle
                WindTunnelMinesLowerFloorBlockPuzzle2(),
                SeqCombatAndMove(
                    name="Move into tunnel",
                    coords=[
                        Vec3(-91.953, 1.002, 8.952),
                        InteractMove(-91.953, 6.002, 12.467),
                        HoldDirection(-122.377, 1.002, 25.377, joy_dir=Vec2(-1, 1)),
                        Vec3(-125.833, 1.002, 28.126),
                        Vec3(-160.126, 1.002, 28.126),
                        Vec3(-167.717, 1.002, 35.383),
                        InteractMove(-169.604, 2.002, 36.931),
                        Vec3(-173.062, 2.002, 37.733),
                        Vec3(-183.568, 2.002, 37.733),
                        Vec3(-185.861, 2.002, 40.026),
                        InteractMove(-187.274, 3.002, 41.601),
                        Vec3(-188.470, 3.002, 43.519),
                        InteractMove(-188.500, 9.002, 45.025),
                        Vec3(-188.581, 9.002, 47.934),
                        InteractMove(-186.444, 14.002, 50.105),
                        Vec3(-170.711, 14.002, 51.173),
                    ],
                ),
                # TODO(orkaboy): Can grab food here
                SeqMove(
                    name="Move to fight",
                    coords=[
                        Vec3(-125.541, 13.002, 51.899),
                        HoldDirection(-143.000, 1.002, 84.000, joy_dir=Vec2(1, 1)),
                    ],
                ),
                SeqHoldDirectionUntilCombat(
                    name="Start fight",
                    joy_dir=Vec2(1, 0.5),
                    mash_confirm=True,
                ),
                SeqCombat("Fight Bushtroo"),
                SeqMove(
                    name="Move into tunnel",
                    coords=[
                        Vec3(-124.578, 1.002, 95.514),
                        InteractMove(-123.700, 2.002, 96.360),
                        HoldDirection(-89.183, 1.010, 9.094, joy_dir=Vec2(1, 1)),
                    ],
                ),
                SeqMove(
                    name="Move to windtrap",
                    coords=[
                        InteractMove(-85.500, 9.002, 17.700),
                        Vec3(-80.324, 9.002, 17.700),
                        Vec3(-79.380, 9.058, 19.709),
                    ],
                ),
                SeqBracelet("Windtrap"),
                SeqMove(
                    name="Move to ladder",
                    coords=[
                        Vec3(-80.175, 9.002, 16.542),
                        Vec3(-80.175, 9.002, 14.841),
                        Vec3(-76.165, 11.002, 14.841),
                        Vec3(-72.687, 11.002, 11.457),
                        Vec3(-66.093, 11.002, 11.457),
                        Vec3(-62.864, 11.002, 14.924),
                        Vec3(-62.419, 11.002, 18.546),
                    ],
                ),
                SeqClimb(
                    name="Climb ladder",
                    coords=[
                        InteractMove(-62.375, 14.988, 18.530),
                        HoldDirection(19.966, 1.002, 18.467, joy_dir=Vec2(0, 1)),
                    ],
                ),
                SeqMove(
                    name="Move away from ladder",
                    coords=[
                        Vec3(21.483, 1.002, 18.467),
                    ],
                ),
            ],
        )


class WindTunnelMines(SeqList):
    """Route through the Wind Tunnel Mines."""

    def __init__(self: Self) -> None:
        super().__init__(
            name="Wind Tunnel Mines",
            children=[
                SeqMove(
                    name="Move left of block",
                    coords=[
                        Vec3(25.177, 1.002, 7.939),
                        Vec3(25.177, 1.002, 5.839),
                    ],
                ),
                # TODO(orkaboy): Continue routing (first floor with Mistral Bracelet)
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
                WindTunnelMinesFirstFloor(),
                SeqCheckpoint("wind_tunnel_mines2"),
                WindTunnelMinesLowerFloor(),
                SeqCheckpoint("wind_tunnel_mines4"),
                WindTunnelMines(),
            ],
        )
