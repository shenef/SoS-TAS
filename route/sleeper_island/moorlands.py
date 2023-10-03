"""Routing of Moorlands section of Sleeper Island."""

import logging
from typing import Self

from engine.combat import SeqCombatAndMove
from engine.mathlib import Vec2, Vec3
from engine.seq import (
    HoldDirection,
    InteractMove,
    MoveToward,
    SeqCheckpoint,
    SeqClimb,
    SeqHoldDirectionUntilCombat,
    SeqHoldDirectionUntilLostControl,
    SeqIfMainCharacterValere,
    SeqInteract,
    SeqList,
    SeqMove,
    SeqSelectOption,
    SeqSkipUntilIdle,
)

logger = logging.getLogger(__name__)


class Moorlands(SeqList):
    def __init__(self: Self) -> None:
        super().__init__(
            name="Moorlands",
            children=[
                SeqCombatAndMove(
                    name="Navigate area",
                    coords=[
                        Vec3(15.245, 3.002, 12.720),
                        Vec3(20.162, 3.002, 12.842),
                        InteractMove(25.479, 1.002, 13.189),
                        Vec3(36.436, 1.002, 11.926),
                        Vec3(44.900, 1.002, 15.560),
                        Vec3(53.079, 1.002, 22.451),
                        Vec3(55.852, 1.002, 22.327),
                        InteractMove(57.668, 0.002, 17.452),
                        Vec3(59.624, 0.002, 8.436),
                        InteractMove(59.624, -1.998, 5.284),
                        Vec3(58.853, -1.998, -3.808),
                        Vec3(54.181, -1.998, -7.913),
                        InteractMove(50.884, -0.998, -5.684),
                        InteractMove(51.183, 2.002, -3.519),
                        Vec3(52.721, 2.002, -1.744),
                        InteractMove(52.721, 5.002, -0.533),
                        Vec3(57.541, 5.002, 4.735),
                        InteractMove(71.864, 5.002, 4.735),
                        Vec3(97.075, 1.002, 4.735),
                        Vec3(102.055, 1.002, -2.203),
                        Vec3(105.231, 1.002, -3.402),
                        Vec3(107.558, 1.002, -0.822),
                        Vec3(107.558, 1.002, 2.501),
                        InteractMove(104.857, 2.002, 5.517),
                        InteractMove(102.533, 5.002, 5.482),
                        Vec3(102.533, 5.002, 7.621),
                        Vec3(106.625, 5.002, 9.549),
                        Vec3(108.326, 5.002, 9.549),
                        InteractMove(111.806, 5.002, 9.549),
                        Vec3(115.034, 5.002, 6.726),
                        Vec3(118.540, 5.002, 7.329),
                        Vec3(118.540, 5.002, 12.063),
                        InteractMove(120.098, 7.002, 13.562),
                        Vec3(123.974, 7.002, 13.562),
                        InteractMove(128.531, 7.002, 13.562),
                        Vec3(135.119, 7.002, 9.886),
                    ],
                ),
                # Can grab Power Belt here
                SeqCombatAndMove(
                    name="Move into cave",
                    coords=[
                        Vec3(135.119, 7.002, 3.857),
                        InteractMove(135.119, 1.002, 2.234),
                        Vec3(135.191, 1.018, -4.184),
                        Vec3(139.329, -1.990, -6.224),
                        Vec3(147.397, -1.998, -6.224),
                        Vec3(150.195, -1.998, -2.842),
                        InteractMove(150.950, 0.002, -2.287),
                        InteractMove(150.950, 2.002, -0.533),
                        HoldDirection(105.000, 1.002, 73.000, joy_dir=Vec2(0, 1)),
                        Vec3(106.206, 1.002, 84.559),
                    ],
                ),
                SeqClimb(
                    name="Climb cliff",
                    coords=[
                        InteractMove(105.911, 4.964, 84.247),
                        Vec3(105.249, 10.002, 84.909),
                    ],
                ),
                SeqMove(
                    name="Move to cliff edge",
                    coords=[
                        Vec3(101.146, 10.002, 83.500),
                        InteractMove(100.092, 8.002, 82.446),
                        Vec3(93.712, 8.002, 76.107),
                        HoldDirection(141.649, 7.002, 0.219, joy_dir=Vec2(-1, -1)),
                        Vec3(140.366, 7.002, 2.152),
                        InteractMove(140.366, 11.002, 4.467),
                        Vec3(141.878, 11.002, 10.836),
                        Vec3(148.706, 11.002, 11.922),
                        Vec3(153.986, 11.002, 9.366),
                        Vec3(153.986, 11.002, 6.197),
                        InteractMove(150.441, 13.002, 6.197),
                        Vec3(147.914, 13.002, 3.127),
                        InteractMove(147.914, 10.002, -3.441),
                        Vec3(147.914, 10.002, -4.540),
                        MoveToward(
                            145.000,
                            1.002,
                            86.750,
                            anchor=Vec3(147.914, 10.002, -14.540),
                            mash=True,
                        ),
                    ],
                ),
                SeqMove(
                    name="Move to wall",
                    coords=[
                        Vec3(150.174, 1.002, 84.164),
                        Vec3(157.766, 1.002, 87.113),
                        Vec3(193.200, 1.002, 87.113),
                        Vec3(197.815, 1.002, 83.857),
                        Vec3(204.740, 1.002, 83.790),
                    ],
                ),
                SeqClimb(
                    name="Climb wall",
                    coords=[
                        InteractMove(204.740, 3.779, 84.530),
                        Vec3(204.740, 11.002, 85.467),
                    ],
                ),
                SeqMove(
                    name="Navigate path",
                    coords=[
                        InteractMove(203.566, 12.002, 86.227),
                        Vec3(199.773, 13.040, 86.454),
                        InteractMove(199.773, 15.002, 87.467),
                        InteractMove(200.619, 16.002, 88.045),
                        Vec3(203.537, 16.002, 87.075),
                        Vec3(205.870, 16.002, 88.524),
                    ],
                ),
                SeqClimb(
                    name="Climb to surface",
                    coords=[
                        InteractMove(205.877, 18.924, 88.530),
                        Vec3(205.718, 22.540, 88.540),
                        Vec3(203.347, 23.343, 88.530),
                        Vec3(203.104, 29.759, 88.530),
                        HoldDirection(171.000, 11.002, 9.467, joy_dir=Vec2(0, 1)),
                    ],
                ),
                SeqMove(
                    name="Move to enemies",
                    coords=[
                        Vec3(174.540, 11.002, 7.487),
                        InteractMove(175.991, 9.002, 7.487),
                        Vec3(180.914, 9.002, 4.799),
                    ],
                ),
                SeqHoldDirectionUntilCombat(
                    name="Attack enemies",
                    joy_dir=Vec2(1, -1),
                    mash_confirm=True,
                ),
                SeqCombatAndMove(
                    name="Fight enemies",
                    coords=[
                        Vec3(184.045, 9.002, 1.365),
                        Vec3(187.282, 9.002, 1.321),
                        InteractMove(186.810, -1.200, -0.461),
                        InteractMove(186.878, 1.002, -9.500),
                    ],
                ),
                # TODO(orkaboy): Can get Teal Amber Ore here to the left
                SeqCombatAndMove(
                    name="Move to chest",
                    coords=[
                        Vec3(186.878, 1.002, -11.525),
                        Vec3(190.721, 1.002, -13.828),
                        Vec3(200.391, 1.002, -13.828),
                        Vec3(208.351, 1.002, -6.498),
                        Vec3(213.028, 1.002, -6.498),
                        Vec3(229.185, 1.002, -13.031),
                        Vec3(237.615, 1.002, -13.022),
                        Vec3(243.422, 1.408, -2.787),
                        Vec3(243.435, 2.010, 0.165),
                        Vec3(241.313, 2.002, 2.957),
                        Vec3(244.486, 2.002, 10.638),
                        Vec3(258.859, 1.002, 11.046),
                        Vec3(267.854, 1.002, 7.500),
                        InteractMove(269.035, 0.002, 6.046),
                        Vec3(271.686, 0.002, 5.454),
                        InteractMove(273.110, -1.197, 4.083),
                        Vec3(274.828, -1.197, -0.691),
                        InteractMove(274.657, 1.002, -2.934),
                        Vec3(275.162, 1.002, -3.794),
                    ],
                ),
                SeqInteract("Rock Lid"),
                SeqSkipUntilIdle("Rock Lid"),
                SeqCombatAndMove(
                    name="Move into cave",
                    coords=[
                        InteractMove(276.818, -1.388, -2.170),
                        Vec3(279.301, -1.197, 3.054),
                        InteractMove(280.061, 0.002, 3.661),
                        Vec3(293.716, 0.002, 5.548),
                        HoldDirection(335.701, 1.002, 74.701, joy_dir=Vec2(1, 1)),
                        Vec3(344.951, 1.002, 77.452),
                        InteractMove(345.613, 2.002, 75.756),
                        HoldDirection(303.958, 1.002, 2.452, joy_dir=Vec2(0, -1)),
                        Vec3(304.188, 1.002, -1.165),
                        InteractMove(305.219, 0.002, -2.222),
                        Vec3(308.214, 0.002, -8.838),
                        Vec3(313.524, 0.002, -8.838),
                        Vec3(318.524, 0.002, -7.358),
                        InteractMove(319.868, 1.002, -7.358),
                        Vec3(324.510, 1.002, -5.557),
                        Vec3(330.526, 1.002, 2.078),
                    ],
                ),
                SeqHoldDirectionUntilLostControl(
                    name="Go to Teaks",
                    joy_dir=Vec2(1, 0),
                ),
                SeqSkipUntilIdle(name="Teaks", hold_cancel=True),
                # Campfire
                # TODO(orkaboy): Position depends on main character, verify for both
                SeqIfMainCharacterValere(
                    name="Campfire",
                    when_true=SeqMove(
                        name="Approach", coords=[Vec3(344.058, 1.002, 0.962)]
                    ),
                    when_false=SeqMove(
                        name="Approach", coords=[Vec3(346.916, 1.002, 1.431)]
                    ),
                ),
                SeqSelectOption("Campfire", option=1),
                SeqSkipUntilIdle("Sleep"),
                SeqCheckpoint("moorlands2"),
                SeqCombatAndMove(
                    name="Fight enemies",
                    coords=[
                        Vec3(352.369, 1.002, 1.654),
                        # Cross bridge
                        Vec3(388.148, 1.002, 1.654),
                        Vec3(404.540, 1.002, 4.868),
                        InteractMove(415.548, 1.002, 4.868),
                        Vec3(423.401, 1.002, -1.406),
                        Vec3(432.121, 1.002, -2.621),
                        # TODO(orkaboy): Continue routing
                    ],
                ),
            ],
        )
