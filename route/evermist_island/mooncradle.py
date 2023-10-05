"""Routing of Mooncradle/Zenith Academy section of Evermist Island."""

import logging
from typing import Self

from engine.mathlib import Vec2, Vec3
from engine.seq import (
    HoldDirection,
    InteractMove,
    MoveToward,
    SeqAwaitLostControl,
    SeqCheckpoint,
    SeqClimb,
    SeqHoldDirectionUntilLostControl,
    SeqIfMainCharacterValere,
    SeqInteract,
    SeqList,
    SeqMove,
    SeqSelectOption,
    SeqSkipUntilIdle,
)

logger = logging.getLogger(__name__)


class IntroMooncradle(SeqList):
    """Childhood, route from cave to Zenith Academy."""

    def __init__(self: Self) -> None:
        super().__init__(
            name="Mooncradle",
            children=[
                SeqCheckpoint(checkpoint_name="intro_mooncradle"),
                SeqMove(
                    name="Move to cliff",
                    coords=[
                        Vec3(-68.930, -10.998, 26.150),
                        HoldDirection(-13.969, -11.998, 38.757, joy_dir=Vec2(0, -1)),
                        Vec3(-13.969, -11.998, 36.392),
                        Vec3(-12.504, -11.998, 34.927),
                        Vec3(-9.406, -11.998, 34.927),
                    ],
                ),
                SeqClimb(
                    name="Climb",
                    coords=[
                        InteractMove(-9.500, -6.998, 36.467),
                    ],
                ),
                SeqMove(
                    name="Move to cliff",
                    coords=[
                        Vec3(-13.482, -6.998, 40.543),
                    ],
                ),
                SeqClimb(
                    name="Climb",
                    coords=[
                        InteractMove(-13.500, -0.998, 41.467),
                    ],
                ),
                SeqMove(
                    name="Move to cutscene",
                    coords=[
                        Vec3(-9.222, -0.820, 53.985),
                        Vec3(-7.318, 1.010, 62.634),
                        Vec3(3.432, 1.002, 73.327),
                        Vec3(17.958, 1.002, 76.578),
                    ],
                ),
                SeqHoldDirectionUntilLostControl(
                    name="Move to cutscene",
                    joy_dir=Vec2(1, 0.2),
                ),
                # Hold B as well to skip cutscene
                SeqSkipUntilIdle(name="Meeting Brugaves and Erlina", hold_cancel=True),
                SeqMove(
                    name="Move to Forbidden Cave",
                    coords=[
                        Vec3(31.373, 1.002, 89.671),
                        Vec3(31.471, 1.002, 114.862),
                        # Enter world map
                        HoldDirection(109.500, 2.002, 61.998, joy_dir=Vec2(0, 1)),
                        Vec3(109.500, 2.002, 64.000),
                        Vec3(108.000, 2.002, 64.000),
                        Vec3(108.000, 2.002, 66.500),
                    ],
                ),
                SeqInteract("Enter Forbidden Cave"),
                # Move to cutscene
                SeqMove(
                    name="Move to entrance",
                    coords=[
                        Vec3(14.000, 1.002, 17.396),
                    ],
                ),
                SeqInteract("Door"),
                SeqSkipUntilIdle(name="Wait for control"),
                # Forbidden Cave
                SeqHoldDirectionUntilLostControl(
                    name="Move to cutscene",
                    joy_dir=Vec2(0, 1),
                ),
                SeqSkipUntilIdle(name="Garl nooo"),
                # Zenith Academy
                SeqMove(
                    name="Move to dorms",
                    coords=[
                        Vec3(48.690, -8.990, -136.717),
                        HoldDirection(285.500, 5.002, 58.000, joy_dir=Vec2(1, 1)),
                        Vec3(290.419, 5.002, 61.872),
                        Vec3(295.647, 5.002, 63.663),
                        HoldDirection(72.657, -7.998, -133.640, joy_dir=Vec2(1, 1)),
                        Vec3(82.104, -7.998, -129.590),
                        Vec3(94.005, -11.998, -129.590),
                        Vec3(94.005, -11.998, -133.576),
                    ],
                ),
            ],
        )


class LoomsToCenter(SeqIfMainCharacterValere):
    """Reusable section, moving from looms to the center area of Zenith Academy dorms."""

    def __init__(self: Self, name: str) -> None:
        super().__init__(
            name,
            # Valere branch: Go left
            when_true=SeqMove(
                name="Valere path",
                coords=[
                    Vec3(91.478, -18.998, -156.476),
                    Vec3(88.309, -18.998, -156.476),
                    Vec3(88.127, -14.998, -134.674),
                ],
            ),
            # Zale branch: Go right
            when_false=SeqMove(
                name="Zale path",
                coords=[
                    Vec3(97.745, -18.998, -156.127),
                    Vec3(100.573, -18.998, -156.149),
                    Vec3(101.496, -14.998, -142.680),
                    Vec3(100.851, -14.998, -134.661),
                ],
            ),
        )


class SkipTutorial(SeqList):
    """Reusable segment for skipping battle tutorials with Brugaves and Erlina."""

    def __init__(self: Self, name: str) -> None:
        super().__init__(
            name,
            children=[
                SeqSelectOption("First dialog", option=1),
                SeqSelectOption("Second dialog", option=1),
                SeqSkipUntilIdle(name="Clear tutorial screen"),
            ],
        )


class IntroZenithAcademy(SeqList):
    """Route Zenith Academy, from dorms, until jumping into Final Trials."""

    def __init__(self: Self) -> None:
        super().__init__(
            name="Zenith Academy",
            children=[
                SeqIfMainCharacterValere(
                    name="Main Character",
                    # Valere branch: Go left
                    when_true=SeqMove(
                        name="Valere path",
                        coords=[
                            Vec3(94.005, -11.998, -133.576),
                            Vec3(86.621, -14.998, -135.924),
                            Vec3(84.091, -14.960, -140.766),
                            Vec3(82.085, -18.998, -147.421),
                            Vec3(78.360, -18.998, -147.465),
                        ],
                    ),
                    # Zale branch: Go right
                    when_false=SeqMove(
                        name="Zale path",
                        coords=[
                            Vec3(94.005, -11.998, -133.576),
                            Vec3(100.395, -14.998, -134.377),
                            Vec3(104.751, -14.998, -139.367),
                            Vec3(106.596, -18.998, -147.793),
                            Vec3(109.640, -18.998, -147.793),
                        ],
                    ),
                ),
                SeqSelectOption("Sleep"),
                SeqSkipUntilIdle(name="Train with Brugaves"),
                SeqMove(
                    name="Move to Erlina",
                    coords=[
                        Vec3(-17.700, -13.998, -136.900),
                        InteractMove(-11.000, -14.998, -143.700),
                        HoldDirection(248.762, 5.002, 56.959, joy_dir=Vec2(1, -1)),
                        Vec3(253.865, 5.002, 56.959),
                        Vec3(257.891, 5.002, 58.706),
                        Vec3(260.734, 5.002, 58.706),
                        HoldDirection(16.980, -8.998, -135.817, joy_dir=Vec2(1, -1)),
                        Vec3(32.789, -8.930, -151.592),
                        Vec3(32.789, -8.990, -176.218),
                    ],
                ),
                SeqMove(
                    name="Move to Erlina",
                    coords=[
                        HoldDirection(273.146, 5.002, 47.521, joy_dir=Vec2(0, -1)),
                    ],
                ),
                SeqHoldDirectionUntilLostControl(
                    name="Move to Erlina",
                    joy_dir=Vec2(0, -1),
                ),
                SeqSkipUntilIdle(name="Train with Erlina"),
                SeqAwaitLostControl(name="Train with Erlina"),
                SeqSkipUntilIdle(name="Sewing"),
                LoomsToCenter("Move to main area"),
                SeqMove(
                    name="Move to main area",
                    coords=[
                        Vec3(94.160, -11.998, -133.319),
                        Vec3(94.382, -11.998, -129.766),
                        Vec3(81.351, -7.998, -129.428),
                        Vec3(72.903, -7.998, -133.028),
                        HoldDirection(295.354, 5.002, 64.422, joy_dir=Vec2(-1, -1)),
                        Vec3(292.408, 5.002, 62.065),
                        Vec3(286.460, 5.002, 59.299),
                        HoldDirection(50.042, -8.998, -134.778, joy_dir=Vec2(-1, -1)),
                    ],
                ),
                SeqAwaitLostControl(name="Eavesdrop"),
                SeqSkipUntilIdle(name="Eavesdrop"),
                SeqIfMainCharacterValere(
                    name="Main Character",
                    # Valere branch: Go left
                    when_true=SeqMove(
                        name="Valere path",
                        coords=[
                            Vec3(82.936, -18.998, -147.362),
                            Vec3(84.538, -14.990, -138.768),
                            Vec3(89.372, -14.998, -133.939),
                        ],
                    ),
                    # Zale branch: Go right
                    when_false=SeqMove(
                        name="Zale path",
                        coords=[
                            Vec3(106.395, -18.998, -147.455),
                            Vec3(104.039, -14.998, -137.504),
                            Vec3(99.935, -14.998, -133.890),
                        ],
                    ),
                ),
                SeqMove(
                    name="Move to south area",
                    coords=[
                        Vec3(94.014, -11.998, -133.488),
                        Vec3(93.947, -11.998, -129.872),
                        Vec3(80.214, -7.998, -129.872),
                        Vec3(73.745, -7.998, -132.473),
                        HoldDirection(295.354, 5.002, 64.422, joy_dir=Vec2(-1, -1)),
                        Vec3(292.408, 5.002, 62.065),
                        Vec3(286.460, 5.002, 59.299),
                        HoldDirection(49.334, -8.998, -135.486, joy_dir=Vec2(-1, -1)),
                        Vec3(33.021, -8.932, -151.461),
                        Vec3(33.021, -8.990, -176.434),
                        HoldDirection(273.463, 5.002, 48.071, joy_dir=Vec2(0, -1)),
                    ],
                ),
                SeqHoldDirectionUntilLostControl(
                    name="I smell cookies",
                    joy_dir=Vec2(0, -1),
                ),
                SeqSkipUntilIdle(name="Cookies!!!"),
                LoomsToCenter("Move to main area"),
                SeqCheckpoint("intro_dorms2"),
                SeqMove(
                    name="Move to Moraine",
                    coords=[
                        Vec3(94.014, -11.998, -133.488),
                        Vec3(93.947, -11.998, -129.872),
                        Vec3(80.214, -7.998, -129.872),
                        Vec3(73.745, -7.998, -132.473),
                        HoldDirection(295.354, 5.002, 64.422, joy_dir=Vec2(-1, -1)),
                        Vec3(292.408, 5.002, 62.065),
                        Vec3(286.460, 5.002, 59.299),
                        HoldDirection(49.334, -8.998, -135.486, joy_dir=Vec2(-1, -1)),
                        Vec3(43.613, -8.998, -141.418),
                        Vec3(35.035, -8.998, -141.418),
                        Vec3(32.954, -8.998, -136.402),
                    ],
                ),
                SeqInteract("Headmaster Moraine"),
                SeqSkipUntilIdle(name="Brugaves and Erlina return"),
                SeqMove(
                    name="Move to Erlina",
                    coords=[
                        Vec3(31.747, -8.998, -141.005),
                    ],
                ),
                SkipTutorial("Skip Erlina Tutorial"),
                SeqMove(
                    name="Move to Brugaves",
                    coords=[
                        Vec3(33.529, -8.932, -141.817),
                    ],
                ),
                SkipTutorial("Skip Brugaves Tutorial"),
                SeqMove(
                    name="Move to Moraine",
                    coords=[
                        Vec3(33.071, -8.998, -136.126),
                    ],
                ),
                SeqSelectOption("Headmaster Moraine"),
                SeqSkipUntilIdle(name="Talking to Moraine"),
                SeqMove(
                    name="Jump into pit",
                    coords=[
                        MoveToward(
                            33.000,
                            -15.197,
                            -365.500,
                            anchor=Vec3(33.000, 7.013, 189.000),
                            mash=True,
                        ),
                    ],
                ),
            ],
        )
