"""Routing of Glacial Peak segment of Watcher Island."""

import logging
from typing import Self

from engine.combat import SeqCombat, SeqCombatAndMove
from engine.mathlib import Vec2, Vec3
from engine.seq import (
    Graplou,
    HoldDirection,
    InteractMove,
    MistralBracelet,
    SeqAwaitLostControl,
    SeqBracelet,
    SeqBraceletPuzzle,
    SeqChangeTimeOfDay,
    SeqCheckpoint,
    SeqCliffClimb,
    SeqCliffMove,
    SeqClimb,
    SeqDelay,
    SeqHoldDirectionDelay,
    SeqHoldDirectionUntilCombat,
    SeqHoldDirectionUntilLostControl,
    SeqInteract,
    SeqList,
    SeqMove,
    SeqSelectOption,
    SeqSkipUntilCombat,
    SeqSkipUntilIdle,
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
                SeqMove(
                    name="Navigate to bluffs",
                    coords=[
                        Vec3(-2.335, 15.002, 17.315),
                        HoldDirection(-55.000, -0.998, 4.500, joy_dir=Vec2(-1, 1)),
                        Vec3(-63.112, -0.998, 12.760),
                        Vec3(-66.407, -0.998, 14.040),
                        InteractMove(-78.405, -0.998, 14.000),
                        Vec3(-87.395, -0.998, 4.542),
                        HoldDirection(-246.000, 10.002, 8.000, joy_dir=Vec2(-1, -1)),
                    ],
                ),
                SeqCombatAndMove(
                    name="Navigate past enemies",
                    coords=[
                        Vec3(-249.242, 10.002, 8.000),
                        Vec3(-254.644, 10.002, 12.824),
                        Vec3(-260.541, 10.002, 11.346),
                        InteractMove(-279.072, 10.002, 11.346),
                        Vec3(-287.983, 10.002, 11.346),
                        Vec3(-299.510, 10.002, 15.407),
                    ],
                ),
                SeqBraceletPuzzle(
                    name="Move block out of the way",
                    coords=[
                        Vec3(-299.448, 10.002, 18.687),
                        Vec3(-298.356, 10.002, 18.687),
                        MistralBracelet(joy_dir=Vec2(0, -1)),
                        Vec3(-298.033, 10.002, 17.193),
                    ],
                ),
                SeqChangeTimeOfDay("Melt block", time_target=15.0),
                SeqMove(
                    name="Move to wall",
                    coords=[
                        Vec3(-295.426, 10.002, 15.308),
                        Vec3(-292.024, 10.002, 15.308),
                    ],
                ),
                SeqClimb(
                    name="Climb wall",
                    coords=[
                        InteractMove(-291.651, 13.786, 14.986),
                        Vec3(-288.666, 17.748, 13.535),
                        Vec3(-286.366, 21.457, 13.528),
                        Vec3(-282.159, 21.540, 17.191),
                        HoldDirection(-281.367, 20.002, 16.410, joy_dir=Vec2(1, -1)),
                    ],
                ),
                SeqMove(
                    name="Move across first rope",
                    coords=[
                        Vec3(-280.484, 20.002, 17.709),
                        InteractMove(-273.973, 20.010, 24.026),
                        Vec3(-273.467, 20.002, 23.578),
                        Vec3(-269.747, 20.002, 23.617),
                    ],
                ),
                SeqCliffMove(
                    name="Move across second rope",
                    coords=[
                        Vec3(-268.340, 19.800, 23.340),
                        InteractMove(-262.795, 20.008, 17.901),
                    ],
                ),
                SeqCombatAndMove(
                    name="Navigate past enemies",
                    coords=[
                        Vec3(-261.797, 20.002, 17.179),
                        Vec3(-257.820, 20.002, 17.179),
                        InteractMove(-257.820, 23.002, 18.467),
                        InteractMove(-256.533, 25.002, 18.467),
                        Vec3(-246.702, 25.002, 14.493),
                        Vec3(-238.615, 25.002, 14.493),
                        Vec3(-233.111, 25.002, 20.520),
                        InteractMove(-221.869, 25.002, 20.500),
                    ],
                ),
                SeqMove(
                    name="Move to block",
                    coords=[
                        Vec3(-208.327, 25.002, 17.981),
                        Vec3(-205.641, 25.002, 15.954),
                        Vec3(-194.078, 25.002, 15.954),
                        Vec3(-187.012, 25.002, 20.475),
                        Vec3(-186.955, 25.002, 22.419),
                    ],
                ),
                SeqBraceletPuzzle(
                    name="Move block into position",
                    coords=[
                        Vec3(-190.435, 25.002, 22.968),
                        MistralBracelet(joy_dir=Vec2(0, -1)),
                        Vec3(-190.493, 25.002, 19.336),
                        Vec3(-189.364, 25.002, 8.821),
                        Vec3(-189.368, 25.002, 7.618),
                        MistralBracelet(joy_dir=Vec2(-1, 0)),
                        Vec3(-196.592, 25.002, 5.351),
                        Vec3(-197.485, 25.002, 5.351),
                        MistralBracelet(joy_dir=Vec2(0, 1)),
                    ],
                ),
                SeqMove(
                    name="Climb block",
                    coords=[
                        Vec3(-198.067, 25.002, 17.535),
                        InteractMove(-198.067, 30.002, 20.460),
                        Vec3(-198.417, 30.002, 22.540),
                    ],
                ),
                SeqCombatAndMove(
                    name="",
                    coords=[
                        InteractMove(-198.373, 32.002, 23.659),
                    ],
                ),
                SeqHoldDirectionDelay("Turn", joy_dir=Vec2(1, 0), timeout_s=0.1),
                # TODO(orkaboy): Disrupt doesn't work?
                SeqBracelet("Disrupt"),
                SeqCombatAndMove(
                    name="Move to next enemy",
                    coords=[
                        Vec3(-197.908, 32.002, 31.557),
                    ],
                ),
                SeqHoldDirectionDelay("Turn", joy_dir=Vec2(1, 0), timeout_s=0.1),
                # TODO(orkaboy): Disrupt doesn't work?
                SeqBracelet("Disrupt"),
                SeqCombatAndMove(
                    name="Climb wall",
                    coords=[
                        InteractMove(-197.908, 39.002, 35.467),
                    ],
                    # If juking fails
                    recovery_path=SeqMove(
                        name="Move to wall",
                        coords=[
                            Vec3(-197.885, 32.002, 33.651),
                        ],
                    ),
                ),
                SeqHoldDirectionUntilCombat("Attack enemies", joy_dir=Vec2(-1, 1)),
                SeqCombatAndMove(
                    name="Move to ledge",
                    coords=[
                        Vec3(-212.174, 39.002, 44.828),
                    ],
                ),
                SeqCliffMove(
                    name="Traverse ledge",
                    coords=[
                        HoldDirection(-215.389, 39.000, 48.000, joy_dir=Vec2(-1, 1)),
                        HoldDirection(-221.989, 39.002, 47.014, joy_dir=Vec2(-1, 0)),
                    ],
                ),
                SeqMove(
                    name="Move to wall",
                    coords=[
                        Vec3(-222.567, 39.002, 44.411),
                        InteractMove(-243.169, 39.002, 44.365),
                        Vec3(-245.114, 39.002, 46.337),
                        Vec3(-245.114, 39.002, 51.833),
                    ],
                ),
                SeqClimb(
                    name="Climb wall",
                    coords=[
                        InteractMove(-245.134, 44.048, 52.469),
                    ],
                ),
                SeqCliffMove(
                    name="Cross platforms",
                    coords=[
                        HoldDirection(-244.472, 49.002, 53.132, joy_dir=Vec2(0, 1)),
                        HoldDirection(-239.784, 49.000, 48.427, joy_dir=Vec2(1, -1)),
                        InteractMove(-232.001, 49.002, 48.519),
                        InteractMove(-225.306, 49.002, 48.600),
                        HoldDirection(-220.431, 49.000, 48.424, joy_dir=Vec2(1, 0)),
                        HoldDirection(-216.845, 49.002, 52.195, joy_dir=Vec2(1, 1)),
                    ],
                ),
                SeqCombatAndMove(
                    name="Navigate around enemies",
                    coords=[
                        InteractMove(-215.820, 46.002, 53.483),
                        Vec3(-215.820, 46.002, 58.011),
                        Vec3(-209.237, 46.002, 64.566),
                        Vec3(-204.814, 46.002, 64.546),
                    ],
                ),
                SeqClimb(
                    name="Climb wall",
                    coords=[
                        InteractMove(-204.814, 50.633, 64.530),
                        Vec3(-193.348, 51.540, 64.530),
                        Vec3(-193.332, 55.217, 64.530),
                    ],
                ),
                SeqMove(
                    name="Drop into hole",
                    coords=[
                        HoldDirection(-193.332, 58.002, 65.951, joy_dir=Vec2(0, 1)),
                        Vec3(-191.574, 58.002, 65.951),
                        Vec3(-189.811, 58.002, 64.188),
                        Vec3(-189.811, 58.002, 62.460),
                        InteractMove(-189.811, 39.002, 61.542),
                        Vec3(-192.927, 39.002, 59.300),
                    ],
                ),
                SeqHoldDirectionUntilCombat("Move into ambush", joy_dir=Vec2(-1, 0)),
                SeqCombat("Ambush"),
            ],
        )


class Acolytes(SeqList):
    """Routing of Acolyte fight segment of Glacial Peak."""

    def __init__(self: Self) -> None:
        """Initialize a new Acolytes object."""
        super().__init__(
            name="Acolytes",
            children=[
                SeqMove(
                    name="Navigate outside",
                    coords=[
                        Vec3(-200.174, 39.002, 63.352),
                        HoldDirection(-195.000, 49.002, 169.859, joy_dir=Vec2(0, 1)),
                        Vec3(-195.213, 49.002, 174.026),
                        Graplou(-195.786, 49.010, 189.786, joy_dir=Vec2(0, 1), hold_timer=0.1),
                        Vec3(-195.786, 52.010, 195.146),
                    ],
                ),
                SeqHoldDirectionUntilLostControl("Move to cutscene", joy_dir=Vec2(0, 1)),
                SeqSkipUntilCombat("Two and Four"),
                # TODO(orkaboy): Need to handle 0 health when one Acolyte is defeated.
                SeqCombat("Two and Four"),
                SeqSkipUntilIdle("And don't come back!"),
                SeqMove(
                    name="Move to wall",
                    coords=[
                        Vec3(-201.444, 52.002, 213.806),
                        Vec3(-206.478, 52.002, 216.546),
                    ],
                ),
                SeqClimb(
                    name="Climb wall",
                    coords=[
                        InteractMove(-206.478, 56.540, 216.540),
                        Vec3(-211.815, 56.540, 220.150),
                        Vec3(-211.665, 52.812, 220.001),
                    ],
                ),
                SeqHoldDirectionDelay("Get off wall", joy_dir=Vec2(0, -1), timeout_s=0.5),
                SeqMove(
                    name="Climb platforms",
                    coords=[
                        Vec3(-212.801, 51.002, 220.502),
                        HoldDirection(-120.600, 61.002, 212.856, joy_dir=Vec2(0, 1)),
                        Vec3(-120.600, 61.002, 215.173),
                        InteractMove(-125.583, 71.002, 220.077),
                        Vec3(-128.424, 71.002, 220.431),
                        Vec3(-130.094, 71.002, 221.513),
                    ],
                ),
                SeqCliffMove(
                    name="Move along ledge",
                    coords=[
                        HoldDirection(-132.132, 71.000, 222.000, joy_dir=Vec2(-1, 1)),
                        Vec3(-137.543, 71.002, 222.189),
                        HoldDirection(-58.542, 62.002, 213.092, joy_dir=Vec2(0, 1)),
                    ],
                ),
                SeqCheckpoint("glacial_peak_auto"),
                SeqMove(
                    name="Grab wall",
                    coords=[
                        Vec3(-58.546, 62.002, 217.033),
                        Vec3(-56.407, 62.002, 219.511),
                        Graplou(-60.097, 62.610, 228.238, joy_dir=Vec2(-0.5, 1), hold_timer=0.1),
                    ],
                ),
                SeqClimb(
                    name="Climb wall",
                    coords=[
                        Vec3(-60.120, 69.540, 228.229),
                        Vec3(-58.005, 69.540, 230.331),
                        Vec3(-58.223, 64.305, 230.113),
                    ],
                ),
                SeqHoldDirectionDelay("Get off wall", joy_dir=Vec2(0, -1), timeout_s=0.25),
                SeqMove(
                    name="Move to ledge",
                    coords=[
                        Vec3(-57.457, 64.002, 230.396),
                        Vec3(-57.457, 64.002, 239.291),
                    ],
                ),
                SeqCliffMove(
                    name="Traverse ledge",
                    coords=[
                        HoldDirection(-55.162, 64.000, 242.273, joy_dir=Vec2(0, 1)),
                    ],
                ),
                SeqCliffClimb(
                    name="Climb up",
                    coords=[
                        Vec3(-55.162, 64.000, 242.273),
                        InteractMove(-55.028, 70.000, 242.407),
                    ],
                ),
                SeqCliffMove(
                    name="Traverse ledge",
                    coords=[
                        Vec3(-52.460, 70.002, 244.256),
                    ],
                ),
                SeqMove(
                    name="Move to peak",
                    coords=[
                        InteractMove(-52.460, 70.002, 252.531),
                        Vec3(-50.737, 70.002, 254.090),
                        InteractMove(-50.135, 56.002, 254.786),
                        Vec3(-48.640, 56.002, 254.998),
                        InteractMove(-46.654, 56.002, 256.976),
                        Vec3(-41.792, 56.002, 273.583),
                    ],
                ),
                SeqHoldDirectionUntilLostControl("Move to cutscene", joy_dir=Vec2(0, 1)),
                SeqSkipUntilIdle("Solstice Amulet", time_target=8.0),
            ],
        )


class Descent(SeqList):
    """Routing of descent segment of Glacial Peak."""

    def __init__(self: Self) -> None:
        """Initialize a new Descent object."""
        super().__init__(
            name="Descent",
            children=[
                SeqMove(
                    name="Move past ice block",
                    coords=[
                        Vec3(-42.349, 56.002, 248.852),
                    ],
                ),
                SeqChangeTimeOfDay("Ice block", time_target=15.0),
                SeqMove(
                    name="Move to boulder",
                    coords=[
                        Vec3(-43.130, 56.002, 246.801),
                        Vec3(-45.340, 56.002, 241.346),
                    ],
                ),
                SeqDelay("Melt ice", timeout_in_s=1.5),
                SeqChangeTimeOfDay("Boulder", time_target=22.0),
                SeqMove(
                    name="Move past boulder",
                    coords=[
                        Vec3(-43.136, 56.002, 236.628),
                    ],
                ),
                SeqChangeTimeOfDay("Boulder", time_target=3.0),
                SeqMove(
                    name="",
                    coords=[
                        Vec3(-40.814, 56.002, 231.551),
                        Vec3(-37.620, 56.002, 229.954),
                    ],
                ),
                SeqInteract("Lever"),
                SeqChangeTimeOfDay("Ice block", time_target=8.0),
                SeqMove(
                    name="Return to cave under ice",
                    coords=[
                        Vec3(-41.713, 56.002, 221.660),
                        Vec3(-41.713, 56.002, 217.424),
                        HoldDirection(-201.000, 52.002, 220.500, joy_dir=Vec2(0, -1)),
                        Vec3(-201.000, 52.002, 218.190),
                        Vec3(-195.868, 52.002, 205.584),
                        Vec3(-195.607, 49.211, 190.023),
                        Graplou(-195.352, 49.010, 176.511, joy_dir=Vec2(0, -1), hold_timer=0.1),
                        Vec3(-195.352, 49.010, 169.048),
                        HoldDirection(-200.100, 39.002, 63.075, joy_dir=Vec2(0, -1)),
                    ],
                ),
            ],
        )


class LeaveMountain(SeqList):
    """Routing of final descent segment of Glacial Peak."""

    def __init__(self: Self) -> None:
        """Initialize a new LeaveMountain object."""
        super().__init__(
            name="Leave mountain",
            children=[
                SeqMove(
                    name="Jump cliffs",
                    coords=[
                        Vec3(-197.702, 39.002, 58.820),
                        Vec3(-198.687, 39.002, 51.033),
                        Vec3(-207.191, 39.002, 34.879),
                    ],
                ),
                SeqChangeTimeOfDay("Activate right rune", time_target=19.0),
                SeqMove(
                    name="Jump cliffs",
                    coords=[
                        InteractMove(-208.213, 32.002, 34.059),
                        Vec3(-209.311, 32.002, 28.953),
                        InteractMove(-209.311, 25.002, 24.366),
                        Vec3(-206.461, 25.027, 15.685),
                        Vec3(-207.518, 25.010, 15.015),
                    ],
                ),
                SeqDelay("Wait", timeout_in_s=1.0),
                SeqChangeTimeOfDay("Activate left rune", time_target=9.0),
                SeqSkipUntilIdle("Wait for control"),
                SeqAwaitLostControl("Await cutscene"),
                SeqChangeTimeOfDay("Prepare", time_target=21.0),
                SeqBraceletPuzzle(
                    name="Push block",
                    coords=[
                        MistralBracelet(joy_dir=Vec2(-1, 0)),
                        Vec3(-218.387, 25.002, 13.133),
                        Vec3(-219.487, 25.002, 13.133),
                        MistralBracelet(joy_dir=Vec2(0, 1)),
                        Vec3(-221.567, 25.007, 18.304),
                        Vec3(-221.567, 25.007, 19.306),
                    ],
                ),
                SeqDelay("Wait", timeout_in_s=1.0),
                SeqChangeTimeOfDay("Activate left rune", time_target=6.0),
                SeqBraceletPuzzle(
                    name="Push block",
                    coords=[
                        MistralBracelet(joy_dir=Vec2(1, 0)),
                        Vec3(-219.601, 25.002, 18.247),
                        Vec3(-219.601, 25.002, 18.247),
                        Vec3(-218.626, 25.002, 18.247),
                        MistralBracelet(joy_dir=Vec2(0, 1)),
                        Vec3(-216.410, 25.010, 24.428),
                        Vec3(-216.410, 25.010, 25.720),
                        MistralBracelet(joy_dir=Vec2(-1, 0)),
                    ],
                ),
                SeqMove(
                    name="Move to ladder",
                    coords=[
                        Vec3(-218.446, 25.019, 27.870),
                        Vec3(-222.381, 25.002, 27.870),
                        Vec3(-224.386, 25.002, 26.454),
                    ],
                ),
                SeqClimb(
                    name="Climb down ladder",
                    coords=[
                        InteractMove(-224.179, 18.922, 25.530),
                        HoldDirection(-66.500, 17.850, 25.530, joy_dir=Vec2(0, -1)),
                    ],
                ),
                SeqMove(
                    name="Move to save branch",
                    coords=[
                        Vec3(-66.500, 9.002, 24.322),
                        Vec3(-64.607, 9.002, 22.978),
                        Vec3(-63.460, 9.002, 18.454),
                        InteractMove(-63.460, 7.002, 17.536),
                        Vec3(-60.495, 7.002, 14.319),
                        InteractMove(-60.522, -0.998, 10.634),
                        Vec3(-55.712, -0.998, 5.571),
                        HoldDirection(-2.434, 15.002, 17.434, joy_dir=Vec2(1, -1)),
                    ],
                ),
                SeqCheckpoint("glacial_peak4"),
                SeqMove(
                    name="Move to portal",
                    coords=[
                        Vec3(1.180, 15.002, 12.849),
                        Vec3(4.119, 15.002, 10.103),
                        Vec3(5.540, 15.002, 10.103),
                        InteractMove(6.458, 9.002, 10.103),
                        Vec3(8.142, 9.002, 10.103),
                        Vec3(17.062, 9.002, 13.347),
                    ],
                ),
                SeqSelectOption("Enter portal"),
                SeqSkipUntilIdle("Tethered Mind Potion"),
                SeqMove(
                    name="Move to Docarri portal",
                    coords=[
                        Vec3(8.253, 0.002, 18.487),
                    ],
                ),
                SeqSelectOption("Enter portal"),
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
                SeqCheckpoint("glacial_peak2"),
                Acolytes(),
                Descent(),
                SeqCheckpoint("glacial_peak3"),
                LeaveMountain(),
            ],
        )
