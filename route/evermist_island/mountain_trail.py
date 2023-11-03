"""Routing of Mountain Trail section of Evermist Island."""

import logging
from typing import Self

from engine.combat import SeqCombatAndMove
from engine.mathlib import Vec2, Vec3
from engine.seq import (
    CancelMove,
    HoldDirection,
    InteractMove,
    SeqCheckpoint,
    SeqCliffClimb,
    SeqCliffMove,
    SeqClimb,
    SeqHoldConfirm,
    SeqHoldDirectionUntilLostControl,
    SeqIfMainCharacterValere,
    SeqInteract,
    SeqList,
    SeqLog,
    SeqMove,
    SeqSkipUntilClose,
    SeqSkipUntilCombat,
    SeqSkipUntilIdle,
    SeqTurboMashDelay,
)

logger = logging.getLogger(__name__)


class IntroMountainTrail(SeqList):
    """Route of start of game, up until the flashback to childhood."""

    def __init__(self: Self) -> None:
        """Initialize a new IntroMountainTrail object."""
        super().__init__(
            name="Mountain Trail",
            children=[
                SeqSkipUntilCombat(name="Wait for combat"),
                SeqLog(name="SYSTEM", text="We have control!"),
                SeqCombatAndMove(
                    name="Fights",
                    coords=[
                        InteractMove(31.524, 6.002, 19.951),
                        Vec3(36.021, 5.842, 19.951),
                        Vec3(49.921, 6.002, 6.540),
                        Vec3(54.534, 6.002, 6.543),
                        InteractMove(55.458, 10.002, 9.467),
                        Vec3(57.051, 10.002, 12.404),
                        InteractMove(43.963, 13.010, 26.059),
                        InteractMove(35.870, 13.010, 28.070),  # after fight
                    ],
                ),
                SeqClimb(
                    name="Move down ladder",
                    coords=[
                        InteractMove(34.448, 6.002, 25.407),
                    ],
                ),
                SeqMove(
                    name="Move to cavern",
                    coords=[
                        Vec3(31.505, 6.002, 19.783),
                        InteractMove(23.612, 5.001, 11.401),
                        Vec3(19.979, 5.002, 7.421),
                        Vec3(14.948, 5.001, 7.870),
                        Vec3(-3.976, 5.001, 15.624),
                        Vec3(-8.323, 5.001, 17.491),
                        Vec3(-7.740, 5.002, 21.092),
                        InteractMove(-5.086, 9.002, 23.746),
                        Vec3(-1.139, 9.002, 24.543),
                        InteractMove(-1.223, 13.002, 26.974),
                        Vec3(-29.325, 13.112, 26.818),
                        Vec3(-33.072, 13.002, 23.247),
                        Vec3(-39.808, 11.002, 23.278),
                        HoldDirection(-88.500, 10.002, 32.058, joy_dir=Vec2(0, 1)),
                    ],
                ),
                SeqMove(
                    name="Move through cavern",
                    coords=[
                        Vec3(-82.388, 10.002, 37.691),
                        Vec3(-82.254, 10.002, 42.898),
                        Vec3(-88.219, 10.002, 44.546),
                    ],
                ),
                SeqClimb(
                    name="Climb cliff",
                    coords=[
                        InteractMove(-88.219, 16.000, 45.000),
                    ],
                ),
                SeqCliffMove(
                    name="Climb cliff",
                    coords=[
                        Vec3(-89.280, 16.000, 45.000),
                        Vec3(-92.238, 16.000, 47.673),
                        Vec3(-92.944, 16.000, 48.000),
                    ],
                ),
                SeqCliffClimb(
                    name="Climb cliff",
                    coords=[
                        InteractMove(-93.016, 22.000, 48.000),
                    ],
                ),
                SeqCliffMove(
                    name="Climb cliff",
                    coords=[
                        Vec3(-88.799, 22.000, 45.000),
                    ],
                ),
                # Use the combat node on the off-chance we run into the slug
                SeqCombatAndMove(
                    name="Move to campfire",
                    coords=[
                        Vec3(-87.284, 22.002, 44.522),
                        Vec3(-73.903, 22.002, 34.029),
                        HoldDirection(-35.819, 21.002, 27.816, joy_dir=Vec2(0, -1)),
                        Vec3(-32.177, 21.002, 27.816),
                        Vec3(-30.369, 21.002, 32.300),
                        InteractMove(-20.660, 21.002, 32.300),
                        InteractMove(-17.865, 21.002, 35.382),
                        InteractMove(-7.719, 21.002, 35.382),
                        Vec3(3.729, 21.002, 30.631),
                        InteractMove(16.907, 21.002, 17.446),
                        Vec3(18.852, 21.002, 16.665),
                    ],
                ),
                SeqHoldDirectionUntilLostControl(
                    name="Go out of cavern",
                    joy_dir=Vec2(1, -0.2),
                ),
                SeqSkipUntilIdle(name="Wait for control"),
            ],
        )


class MountainTrail(SeqList):
    """Route Mountain Trail section. From leaving Forbidden Cave to arrival at Elder Mist."""

    def __init__(self: Self) -> None:
        """Initialize a new MountainTrail object."""
        super().__init__(
            name="Evermist Island",
            children=[
                SeqSkipUntilClose(
                    "Acolytes cutscene",
                    coord=Vec3(104.000, 3.002, 71.498),
                ),
                SeqMove(
                    name="Move to Mountain Trail",
                    coords=[
                        Vec3(104.000, 3.002, 72.500),
                        Vec3(110.000, 3.002, 72.500),
                        Vec3(110.000, 3.002, 75.500),
                    ],
                ),
                SeqInteract("Enter Mountain Trail"),
                SeqSkipUntilIdle("Back to present"),
                # Valere
                SeqIfMainCharacterValere(
                    "Main Char",
                    when_true=SeqMove(
                        "Go around campfire",
                        coords=[Vec3(29.789, 21.002, 12.213)],
                    ),
                    when_false=None,
                ),
                # Grab berries
                SeqMove(
                    "Go to bush",
                    coords=[Vec3(25.386, 21.002, 16.648)],
                ),
                SeqInteract("Berries"),
                SeqMove(
                    "Go to bush",
                    coords=[Vec3(25.505, 21.002, 18.166)],
                ),
                SeqInteract("Berries"),
                # Learn how to cook
                SeqMove(
                    "Go to Garl",
                    coords=[
                        Vec3(28.014, 21.002, 15.256),
                        Vec3(29.175, 21.002, 13.363),
                    ],
                ),
                SeqInteract("Talk to Garl"),
                SeqSkipUntilIdle("Talk to Garl"),
                # Cook Berry Jam
                SeqMove(
                    "Go to campfire",
                    coords=[
                        Vec3(28.414, 21.002, 12.944),
                    ],
                ),
                # TODO(orkaboy): Replace with a better abstraction for cooking
                SeqInteract("Campfire"),
                SeqTurboMashDelay("Cook", timeout_in_s=1.0),
                SeqHoldConfirm("Berry Jam", timeout_in_s=3.5),
                # Sleep and continue
                SeqMove(
                    "Go to Garl",
                    coords=[
                        CancelMove(29.228, 21.002, 13.475),
                    ],
                ),
                SeqInteract("Talk to Garl"),
                SeqSkipUntilIdle("Sleep until morning"),
                SeqMove(
                    name="Move to cliff",
                    coords=[
                        Vec3(27.597, 21.002, 17.912),
                        Vec3(27.597, 21.002, 25.840),
                    ],
                ),
                SeqCheckpoint("mountain_trail"),
                SeqMove(
                    name="Move to cliff",
                    coords=[
                        Vec3(30.493, 21.002, 29.656),
                        Vec3(30.821, 21.002, 32.541),
                    ],
                ),
                SeqClimb(
                    name="Climb cliff",
                    coords=[
                        InteractMove(30.830, 23.977, 32.530),
                        Vec3(30.830, 31.002, 33.467),
                    ],
                ),
                SeqCombatAndMove(
                    name="Navigate trail",
                    coords=[
                        Vec3(35.299, 31.122, 48.027),
                        Vec3(60.728, 31.004, 73.029),
                        Vec3(61.554, 31.002, 82.984),
                        Vec3(63.332, 31.002, 82.457),
                        InteractMove(63.332, 28.002, 79.238),
                        Vec3(68.246, 25.002, 78.686),
                        InteractMove(70.460, 21.002, 77.649),
                        Vec3(69.133, 21.002, 76.458),
                        InteractMove(68.721, 17.002, 73.326),
                        Vec3(61.205, 12.002, 72.609),
                        Vec3(61.278, 12.002, 70.849),
                        Vec3(69.106, 12.002, 70.849),
                        Vec3(71.002, 12.090, 75.768),
                        Vec3(77.707, 12.010, 82.274),
                        Vec3(78.496, 12.010, 94.355),
                        Vec3(88.255, 12.002, 94.355),
                        Vec3(95.261, 12.002, 92.324),
                        InteractMove(105.206, 12.002, 92.452),
                        InteractMove(116.207, 12.002, 92.452),
                        Vec3(119.442, 12.002, 93.462),
                        InteractMove(119.467, 12.002, 101.690),
                        Vec3(117.848, 12.002, 103.540),
                        InteractMove(117.848, 13.002, 105.540),
                    ],
                ),
                SeqClimb(
                    name="Climb cliff",
                    coords=[
                        InteractMove(117.848, 17.028, 105.530),
                        Vec3(116.724, 21.540, 105.530),
                        Vec3(115.592, 21.540, 105.530),
                    ],
                ),
                SeqCliffMove(
                    name="Move along ledge",
                    coords=[
                        Vec3(113.228, 21.002, 98.862),
                        HoldDirection(110.608, 21.000, 96.043, joy_dir=Vec2(-1, -1)),
                        Vec3(104.178, 21.000, 95.089),
                    ],
                ),
                SeqCombatAndMove(
                    name="Fight wanderers",
                    coords=[
                        Vec3(96.910, 21.002, 95.089),
                        InteractMove(93.519, 21.002, 95.089),
                        Vec3(93.519, 21.002, 95.540),
                    ],
                ),
                SeqClimb(
                    name="Climb cliff",
                    coords=[
                        InteractMove(93.519, 23.828, 95.530),
                        Vec3(93.519, 30.002, 96.467),
                    ],
                ),
                SeqCombatAndMove(
                    name="Navigate to cave",
                    coords=[
                        Vec3(96.371, 30.002, 100.611),
                        # TODO(orkaboy): Can drop down and desync
                        InteractMove(103.873, 30.002, 100.548),
                        Vec3(105.732, 30.002, 100.548),
                        Vec3(109.080, 30.002, 105.382),
                        Vec3(101.960, 30.002, 112.436),
                        Vec3(95.286, 30.002, 111.595),
                        HoldDirection(176.000, 2.002, 122.300, joy_dir=Vec2(0, 1)),
                        InteractMove(176.189, 4.002, 129.460),
                        InteractMove(174.247, 6.002, 131.383),
                        Vec3(172.800, 6.002, 132.974),
                    ],
                ),
                # Campfire/Save Point in cavern
                # TODO(orkaboy): There is a merchant here too, do we need to buy anything?
                SeqCheckpoint("mountain_trail2"),
                SeqMove(
                    name="Move to cliff",
                    coords=[
                        Vec3(172.659, 6.002, 135.695),
                    ],
                ),
                SeqClimb(
                    name="Climb cliff",
                    coords=[
                        InteractMove(172.953, 8.250, 135.382),
                        Vec3(172.878, 21.514, 135.458),
                        Vec3(173.540, 24.002, 136.120),
                    ],
                ),
                SeqMove(
                    name="Navigate trail",
                    coords=[
                        Vec3(178.474, 24.002, 132.236),
                        Vec3(184.256, 24.002, 130.992),
                        Vec3(186.408, 24.002, 127.659),
                        Vec3(188.581, 24.002, 124.294),
                        HoldDirection(105.206, 49.002, 123.163, joy_dir=Vec2(1, -1)),
                    ],
                ),
                SeqCombatAndMove(
                    name="Navigate trail",
                    coords=[
                        Vec3(105.206, 49.002, 119.837),
                        Vec3(86.618, 49.002, 116.410),
                        InteractMove(79.059, 45.002, 116.298),
                        Vec3(75.749, 45.002, 118.825),
                        Vec3(69.908, 45.002, 118.803),
                        InteractMove(64.543, 46.002, 114.585),
                        InteractMove(60.470, 49.002, 117.131),
                        InteractMove(61.074, 53.002, 125.875),
                        InteractMove(64.035, 55.002, 125.450),
                        Vec3(65.019, 55.002, 121.584),
                        InteractMove(70.540, 55.002, 121.547),
                        Vec3(70.540, 55.002, 123.540),
                        InteractMove(76.540, 55.002, 123.540),
                        Vec3(76.540, 55.002, 121.460),
                        InteractMove(85.314, 55.002, 121.438),
                        InteractMove(85.715, 60.002, 126.473),
                        Vec3(83.689, 60.001, 134.331),
                        InteractMove(79.365, 60.002, 134.452),
                        Vec3(78.460, 60.002, 134.452),
                        Vec3(78.460, 60.002, 133.460),
                        InteractMove(78.460, 60.002, 130.460),
                        Vec3(76.455, 60.002, 128.748),
                        InteractMove(73.231, 60.002, 128.548),
                        Vec3(72.460, 60.002, 128.548),
                        InteractMove(72.400, 60.002, 131.460),
                        Vec3(71.071, 60.002, 132.540),
                        Vec3(69.460, 60.002, 132.540),
                        InteractMove(66.193, 60.002, 132.540),
                        Vec3(65.320, 60.002, 130.662),
                        Vec3(63.611, 60.002, 129.324),
                    ],
                ),
                SeqClimb(
                    name="Climb cliff",
                    coords=[
                        InteractMove(63.051, 60.411, 129.386),
                        Vec3(62.388, 68.002, 130.048),
                    ],
                    precision2=0,
                ),
                SeqCombatAndMove(
                    name="Move to cliff",
                    coords=[
                        InteractMove(58.533, 69.002, 130.702),
                        InteractMove(57.362, 72.002, 132.022),
                        InteractMove(60.714, 73.002, 137.150),
                        Vec3(66.825, 73.002, 137.150),
                        Vec3(68.642, 73.002, 134.562),
                        InteractMove(83.560, 73.002, 134.500),
                        Vec3(87.935, 73.002, 138.962),
                    ],
                ),
                SeqClimb(
                    name="Climb cliff",
                    coords=[
                        # TODO(orkaboy): There's a risk of being caught by the enemy here
                        InteractMove(87.935, 77.453, 139.530),
                        Vec3(88.451, 83.540, 139.530),
                        Vec3(89.655, 83.986, 139.990),
                        Vec3(88.993, 89.002, 140.653),
                    ],
                ),
                SeqMove(
                    name="Move to cliff",
                    coords=[
                        Vec3(84.256, 89.002, 142.541),
                    ],
                ),
                SeqInteract("Grab cliff"),
                SeqClimb(
                    name="Climb cliff",
                    coords=[
                        InteractMove(84.120, 89.540, 142.530),
                        Vec3(76.192, 89.686, 142.530),
                        Vec3(75.555, 96.002, 143.467),
                    ],
                ),
                SeqHoldDirectionUntilLostControl("Elder Mist", joy_dir=Vec2(0, 1)),
                SeqSkipUntilIdle("Elder Mist"),
            ],
        )
