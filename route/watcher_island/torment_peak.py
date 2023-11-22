"""Routing of Torment Peak segment of Watcher Island."""

import logging
from typing import Self

from engine.combat import SeqCombatAndMove
from engine.mathlib import Vec2, Vec3
from engine.seq import (
    Graplou,
    HoldDirection,
    InteractMove,
    MistralBracelet,
    SeqAwaitLostControl,
    SeqBraceletPuzzle,
    SeqChangeTimeOfDay,
    SeqCheckpoint,
    SeqCliffClimb,
    SeqCliffMove,
    SeqDelay,
    SeqGraplou,
    SeqHoldDirectionDelay,
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


class ActivatePillars(SeqList):
    """Routing of pillar segment of first room in Torment Peak."""

    def __init__(self: Self) -> None:
        """Initialize a new ActivatePillars object."""
        super().__init__(
            name="Activate Pillars",
            children=[
                # Move to left pillar
                SeqMove(
                    name="Move left to cliff",
                    coords=[
                        Vec3(98.217, 3.002, 139.748),
                        Vec3(86.964, 3.002, 142.767),
                        Vec3(82.333, 2.002, 144.076),
                        Vec3(80.692, 2.002, 146.227),
                    ],
                ),
                SeqCliffClimb(
                    name="Climb cliff",
                    coords=[
                        InteractMove(81.016, 8.000, 147.000),
                    ],
                ),
                SeqCliffMove(
                    name="Move along ledge",
                    coords=[
                        Vec3(80.280, 8.000, 146.714),
                        Vec3(78.493, 8.000, 145.000),
                        Vec3(76.769, 8.000, 145.000),
                        Vec3(75.388, 8.000, 146.000),
                        Vec3(71.215, 8.002, 146.466),
                    ],
                ),
                SeqMove(
                    name="Move to top of cliff",
                    coords=[
                        InteractMove(66.327, 8.002, 146.466),
                        Vec3(64.541, 8.002, 145.454),
                        Vec3(62.842, 8.002, 145.801),
                    ],
                ),
                SeqCliffClimb(
                    name="Jump off cliff",
                    coords=[
                        InteractMove(63.088, 5.000, 145.000),
                        Vec3(61.950, 5.000, 145.484),
                        InteractMove(61.381, 2.002, 144.755),
                    ],
                    precision=0.5,
                ),
                SeqMove(
                    name="Move to pillar",
                    coords=[
                        Vec3(55.559, 2.002, 145.228),
                        Vec3(54.716, 2.002, 146.669),
                    ],
                ),
                SeqInteract("Pillar"),
                # Return to central area
                SeqMove(
                    name="Move to wall",
                    coords=[
                        Vec3(55.784, 2.002, 145.218),
                        Vec3(61.870, 2.002, 145.483),
                    ],
                ),
                SeqCliffClimb(
                    name="Climb cliff",
                    coords=[
                        InteractMove(62.200, 5.000, 145.234),
                        InteractMove(62.787, 8.002, 145.959),
                    ],
                ),
                SeqMove(
                    name="Move to ledge",
                    coords=[
                        Vec3(65.421, 8.002, 145.959),
                        Vec3(66.543, 8.002, 146.867),
                        InteractMove(69.481, 8.002, 146.867),
                        Vec3(70.842, 8.002, 146.035),
                    ],
                ),
                SeqCliffMove(
                    name="Move along ledge",
                    coords=[
                        HoldDirection(74.526, 8.000, 146.000, joy_dir=Vec2(1, 0)),
                        HoldDirection(79.744, 8.000, 146.178, joy_dir=Vec2(1, 0)),
                    ],
                ),
                SeqCliffClimb(
                    name="Get off ledge",
                    coords=[
                        InteractMove(79.784, 2.002, 144.920),
                    ],
                ),
                SeqMove(
                    name="Move to central area",
                    coords=[
                        Vec3(82.774, 2.002, 143.708),
                        Vec3(96.873, 3.002, 143.708),
                    ],
                ),
                # Move to right pillar
                SeqMove(
                    name="Move to right pillar",
                    coords=[
                        Vec3(102.581, 3.002, 146.689),
                        Vec3(104.815, 3.002, 147.458),
                        Vec3(107.566, 3.002, 147.458),
                        InteractMove(109.483, 0.002, 145.542),
                        Vec3(110.448, 0.002, 143.505),
                        Vec3(111.616, 0.002, 143.505),
                    ],
                ),
                SeqInteract("Pillar"),
                # Return to central area
                SeqMove(
                    name="Move to door",
                    coords=[
                        Vec3(109.719, 0.002, 144.372),
                        Vec3(108.428, 0.002, 145.482),
                        InteractMove(108.451, 3.002, 146.467),
                        Vec3(107.286, 3.002, 147.460),
                        Vec3(100.502, 3.002, 147.415),
                        Vec3(97.234, 3.002, 150.688),
                    ],
                ),
            ],
        )


class FirstRoom(SeqList):
    """Routing of first room segment of Torment Peak."""

    def __init__(self: Self) -> None:
        """Initialize a new FirstRoom object."""
        super().__init__(
            name="First room",
            children=[
                SeqCombatAndMove(
                    name="Move past enemies",
                    coords=[
                        Vec3(26.728, 5.002, 36.403),
                        Vec3(23.302, 5.002, 43.818),
                        Vec3(21.771, 5.002, 47.806),
                        Vec3(20.935, 6.010, 67.021),
                        Vec3(18.899, 6.010, 76.710),
                        Vec3(18.899, 6.010, 80.903),
                        Vec3(24.369, 6.002, 82.771),
                        Vec3(23.349, 6.002, 89.874),
                        Vec3(20.072, 6.487, 94.292),
                        Vec3(20.072, 7.010, 98.013),
                        Vec3(21.974, 7.010, 104.817),
                        Vec3(21.974, 7.010, 108.524),
                        Vec3(18.791, 7.010, 111.626),
                        Vec3(13.347, 7.002, 113.644),
                        Vec3(12.879, 7.002, 114.232),
                    ],
                ),
                # TODO(orkaboy): Juke enemies instead
                SeqHoldDirectionDelay("Turn", joy_dir=Vec2(-1, 1), timeout_s=0.1),
                SeqGraplou("Attack enemies", until_combat=True),
                SeqCombatAndMove(
                    name="Move to pillar",
                    coords=[
                        Vec3(11.675, 7.002, 122.052),
                        Vec3(14.904, 7.002, 125.164),
                        Vec3(15.851, 7.002, 133.204),
                        Vec3(18.433, 7.002, 135.543),
                        InteractMove(21.481, 7.002, 135.543),
                        InteractMove(21.481, 7.002, 141.540),
                        InteractMove(16.509, 7.002, 141.540),
                        Vec3(9.460, 7.002, 141.540),
                        InteractMove(5.986, 7.002, 141.540),
                        Vec3(2.264, 8.002, 138.505),
                        Vec3(2.469, 8.002, 134.382),
                    ],
                ),
                SeqInteract("Pillar"),
                SeqMove(
                    name="Navigate moving platforms",
                    coords=[
                        Vec3(2.469, 8.002, 138.560),
                        Vec3(6.540, 7.002, 141.482),
                        InteractMove(10.073, 7.002, 141.482),
                        Vec3(17.476, 7.002, 141.482),
                        InteractMove(21.481, 7.002, 141.482),
                        InteractMove(21.481, 7.002, 138.519),
                        InteractMove(33.481, 7.002, 138.519),
                        InteractMove(33.481, 4.002, 132.460),
                        InteractMove(27.460, 4.002, 132.460),
                        InteractMove(24.461, 3.667, 132.457),
                        InteractMove(24.461, 2.002, 128.394),
                        Vec3(25.416, 2.002, 127.496),
                        Vec3(34.344, 2.002, 127.496),
                        Vec3(37.536, 2.002, 129.519),
                        Vec3(39.540, 2.002, 129.519),
                        InteractMove(42.540, 2.402, 129.519),
                        InteractMove(42.546, 4.002, 132.481),
                        InteractMove(45.806, 4.002, 132.481),
                    ],
                ),
                # TODO(orkaboy): Better juking
                SeqCombatAndMove(
                    name="Juke around enemies",
                    coords=[
                        Vec3(54.137, 4.002, 127.589),
                        Vec3(65.143, 3.010, 120.959),
                        Vec3(60.294, 3.010, 125.546),
                        Vec3(56.356, 3.010, 121.626),
                        Vec3(62.005, 3.002, 116.193),
                        Vec3(68.437, 3.002, 113.369),
                        Vec3(70.112, 3.002, 111.762),
                        InteractMove(72.668, 3.002, 109.367),
                        InteractMove(76.731, 3.002, 109.452),
                    ],
                ),
                SeqMove(
                    name="Navigate platforms",
                    coords=[
                        Vec3(77.670, 3.002, 109.324),
                        Vec3(79.428, 3.002, 107.460),
                        InteractMove(79.428, -2.998, 106.542),
                        Vec3(81.721, -2.998, 106.542),
                        Vec3(83.948, -2.998, 108.699),
                        Vec3(84.515, -2.998, 112.540),
                        Graplou(84.460, -2.403, 121.530, joy_dir=Vec2(0, 1), hold_timer=0.1),
                        Vec3(84.460, 3.002, 122.467),
                        Vec3(87.066, 3.002, 123.520),
                        Vec3(90.174, 3.002, 121.911),
                        InteractMove(92.781, 3.002, 119.510),
                    ],
                ),
                # TODO(orkaboy): Better juking
                SeqCombatAndMove(
                    name="Juke around enemies",
                    coords=[
                        InteractMove(97.073, 3.002, 119.510),
                        Vec3(98.587, 3.002, 121.869),
                        Vec3(98.587, 3.002, 126.828),
                        Vec3(99.861, 3.002, 129.492),
                        InteractMove(99.811, 3.002, 133.223),
                        InteractMove(99.501, 3.002, 138.073),
                    ],
                ),
                # Activate the two pillars to open the door
                ActivatePillars(),
                # Enter the previously locked door
                SeqMove(
                    name="Move to save branch",
                    coords=[
                        HoldDirection(93.000, 5.002, 210.013, joy_dir=Vec2(0, 1)),
                        Vec3(93.000, 5.002, 228.420),
                    ],
                ),
            ],
        )


class SecondRoom(SeqList):
    """Routing of first room segment of Torment Peak."""

    def __init__(self: Self) -> None:
        """Initialize a new SecondRoom object."""
        super().__init__(
            name="Second room",
            children=[
                SeqMove(
                    name="",  # TODO(orkaboy): Name
                    coords=[
                        Vec3(93.000, 5.002, 228.420),
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
                FirstRoom(),
                SeqCheckpoint("torment_peak2"),
                SecondRoom(),
                # TODO(orkaboy): Continue routing
            ],
        )
