"""Routing of Sea of Nightmare and the Vespertine."""

import logging
from typing import Self

from engine.combat import SeqCombatAndMove
from engine.mathlib import Vec2, Vec3
from engine.seq import (
    Graplou,
    HoldDirection,
    InteractMove,
    MistralBracelet,
    SeqBlockPuzzle,
    SeqBoat,
    SeqCheckpoint,
    SeqCliffMove,
    SeqClimb,
    SeqGraplou,
    SeqHoldDirectionDelay,
    SeqInteract,
    SeqList,
    SeqLoot,
    SeqMove,
    SeqSelectOption,
    SeqSkipUntilIdle,
)

logger = logging.getLogger(__name__)


class TheVespertine(SeqList):
    """Routing of clearing The Vespertine."""

    def __init__(self: Self) -> None:
        """Initialize a new TheVespertine object."""
        super().__init__(
            name="The Vespertine",
            children=[
                SeqMove(
                    name="Move to rope ladder",
                    coords=[
                        Vec3(-9.024, 2.010, 17.861),
                        Vec3(-11.835, 2.002, 14.575),
                        Vec3(-11.835, 2.002, 11.381),
                        Graplou(-14.158, 2.946, 11.177, joy_dir=Vec2(-1, 0), hold_timer=0.1),
                    ],
                ),
                SeqClimb(
                    name="Climb left mast",
                    coords=[
                        Vec3(-14.091, 24.540, 11.244),
                        Vec3(-15.540, 24.539, 10.530),
                    ],
                ),
                SeqMove(
                    name="Move to rope",
                    coords=[
                        Vec3(-15.499, 24.002, 9.460),
                        Vec3(-14.324, 24.002, 9.457),
                        Vec3(-13.324, 24.002, 9.457),
                        Vec3(-12.509, 24.002, 10.318),
                        Vec3(-12.509, 24.002, 12.135),
                    ],
                ),
                SeqCliffMove(
                    name="Cross rope",
                    coords=[
                        Vec3(-10.849, 23.829, 11.500),
                        Vec3(0.400, 21.002, 11.500),
                    ],
                ),
                SeqCombatAndMove(
                    name="Clear upper deck",
                    coords=[
                        Vec3(1.680, 21.002, 13.454),
                        Vec3(4.241, 21.002, 13.454),
                        Vec3(7.540, 21.002, 11.641),
                        InteractMove(9.600, 4.002, 13.442),
                        Vec3(7.144, 4.002, 16.434),
                        Vec3(-0.831, 2.002, 16.389),
                        Vec3(-8.035, 2.002, 15.032),
                        Vec3(-8.035, 2.002, 12.982),
                        HoldDirection(-4.414, 3.602, -70.077, joy_dir=Vec2(1, 0)),
                        Vec3(-1.339, 1.002, -68.800),
                    ],
                ),
                SeqHoldDirectionDelay("Turn", joy_dir=Vec2(0, 1), timeout_s=0.1),
                SeqGraplou("Attack enemies", until_combat=True),
                SeqCombatAndMove(
                    name="Clear lower deck",
                    coords=[
                        Vec3(4.933, 1.002, -74.201),
                        Vec3(9.047, 1.002, -77.701),
                        Vec3(13.170, 1.002, -76.310),
                    ],
                ),
                SeqHoldDirectionDelay("Turn", joy_dir=Vec2(0, 1), timeout_s=0.1),
                SeqGraplou("Attack enemies", until_combat=True),
                SeqCombatAndMove(
                    name="Clear lower deck",
                    coords=[
                        Vec3(17.146, 1.002, -77.713),
                        Vec3(7.690, 1.002, -77.713),
                        Vec3(-1.256, 1.002, -66.246),
                        Vec3(-5.607, 1.002, -65.176),
                        Vec3(-10.949, 1.002, -65.176),
                    ],
                ),
                SeqHoldDirectionDelay("Turn", joy_dir=Vec2(-1, -1), timeout_s=0.1),
                SeqGraplou("Attack enemies", until_combat=True),
                SeqCombatAndMove(
                    name="Clear lower deck",
                    coords=[
                        Vec3(-28.997, 1.002, -64.171),
                        Vec3(-31.846, 1.002, -63.572),
                        Vec3(-34.067, 1.002, -65.425),
                        Vec3(-34.067, 1.002, -71.021),
                        Vec3(-43.040, 1.002, -70.846),
                    ],
                ),
                SeqLoot("Map"),
                SeqMove(
                    name="Move to save branch",
                    coords=[
                        Vec3(-34.062, 1.002, -70.846),
                    ],
                ),
                SeqCheckpoint("vespertine"),
                SeqMove(
                    name="Go above deck",
                    coords=[
                        Vec3(-34.062, 1.002, -65.287),
                        Vec3(-33.387, 1.002, -63.840),
                        Vec3(-31.819, 1.002, -62.376),
                        Vec3(-28.240, 1.002, -65.802),
                        Vec3(-13.083, 1.002, -65.802),
                        Vec3(-8.474, 1.002, -64.068),
                        Vec3(-1.206, 1.002, -65.117),
                        Vec3(-1.206, 1.002, -69.077),
                        Vec3(-5.857, 5.053, -69.077),
                        HoldDirection(-6.400, 1.595, 11.889, joy_dir=Vec2(-1, 0)),
                    ],
                ),
                SeqMove(
                    name="Go to Hortence",
                    coords=[
                        Vec3(-7.611, 2.002, 11.889),
                        Graplou(-14.158, 2.946, 11.177, joy_dir=Vec2(-1, 0), hold_timer=0.1),
                        Vec3(-13.996, 2.002, 9.464),
                        Vec3(-15.205, 2.002, 7.478),
                        Vec3(-20.883, 6.002, 7.478),
                        Vec3(-20.883, 6.002, 9.796),
                        Vec3(-19.264, 6.002, 11.614),
                    ],
                ),
                SeqSelectOption("Give map", skip_dialog_check=True),
                # Cutscene into boat movement
                SeqBoat(
                    "Cutscene into boat",
                    coords=[
                        Vec3(-5.286, 0.500, -18.804),
                    ],
                    hold_skip=True,
                ),
            ],
        )


class SouthwestIsland(SeqList):
    """Routing of Southwest Island in the Sea of Nightmare."""

    def __init__(self: Self) -> None:
        """Initialize a new SouthwestIsland object."""
        super().__init__(
            name="Southwest Island",
            children=[
                SeqBoat(
                    name="Move to SW island",
                    coords=[
                        Vec3(-18.638, 0.500, -35.009),
                    ],
                ),
                SeqInteract("Disembark"),
                SeqMove(
                    name="Overworld movement",
                    coords=[
                        Vec3(-22.500, 1.002, -36.500),
                        Vec3(-22.500, 1.002, -36.000),
                        Vec3(-24.000, 1.002, -36.000),
                        Vec3(-24.000, 1.002, -35.000),
                        Vec3(-25.500, 1.002, -35.000),
                        Vec3(-25.500, 1.002, -34.500),
                        Vec3(-26.000, 1.002, -34.500),
                        Vec3(-26.000, 1.002, -34.000),
                        Vec3(-26.500, 1.002, -34.000),
                        Vec3(-26.500, 1.002, -32.000),
                    ],
                ),
                SeqInteract("Enter area"),
                SeqMove(
                    name="Move to save branch",
                    coords=[
                        Vec3(6.564, 5.121, 19.926),
                    ],
                ),
                SeqCheckpoint("sea_of_nightmare"),
                SeqCombatAndMove(
                    name="Move to first doubloon",
                    coords=[
                        Vec3(6.564, 6.010, 30.135),
                        Vec3(9.503, 6.051, 32.809),
                        Vec3(10.422, 6.051, 33.211),
                        Vec3(19.826, 4.341, 33.211),
                        Vec3(26.963, 3.943, 25.204),
                        Vec3(42.216, 6.211, 19.001),
                        Vec3(45.747, 6.206, 17.925),
                    ],
                ),
                SeqInteract("Doubloon #1"),
                SeqCombatAndMove(
                    name="Move to block puzzle",
                    coords=[
                        Vec3(45.821, 6.206, 23.480),
                        Vec3(47.831, 6.002, 35.622),
                        Vec3(51.073, 6.002, 40.090),
                        Vec3(51.073, 6.002, 43.657),
                    ],
                ),
                SeqBlockPuzzle(
                    name="Palm tree block puzzle",
                    coords=[
                        MistralBracelet(joy_dir=Vec2(-1, 0)),
                        Vec3(45.796, 6.010, 44.431),
                        Vec3(40.737, 6.002, 53.732),
                        Vec3(35.032, 6.002, 53.692),
                        MistralBracelet(joy_dir=Vec2(0, -1)),
                        Vec3(34.022, 6.018, 48.563),
                        Vec3(33.117, 6.002, 46.898),
                        MistralBracelet(joy_dir=Vec2(1, 0)),
                        Vec3(36.019, 6.002, 46.471),
                        Vec3(37.404, 6.002, 44.026),
                        Vec3(38.147, 6.002, 44.026),
                        MistralBracelet(joy_dir=Vec2(0, 1)),
                        Vec3(37.025, 6.002, 49.389),
                        MistralBracelet(joy_dir=Vec2(1, 0)),
                        Vec3(41.183, 6.010, 50.671),
                        Vec3(47.257, 6.010, 51.684),
                        Vec3(48.543, 6.002, 51.678),
                        MistralBracelet(joy_dir=Vec2(0, -1)),
                        Vec3(45.028, 6.010, 46.647),
                    ],
                ),
                SeqInteract("Doubloon #2"),
                SeqMove(
                    name="Navigate pillars",
                    coords=[
                        Vec3(43.450, 6.010, 56.313),
                        InteractMove(42.808, 5.002, 64.189),
                        Vec3(40.872, 6.002, 74.222),
                        InteractMove(38.233, 9.002, 76.893),
                        Vec3(34.460, 9.002, 77.531),
                        InteractMove(19.194, 9.002, 77.531),
                        InteractMove(16.783, 11.002, 79.445),
                        InteractMove(14.523, 12.002, 78.866),
                        Vec3(13.715, 12.002, 76.899),
                    ],
                ),
                SeqGraplou("Grab enemy", until_combat=True),
                SeqCombatAndMove(
                    name="Fight for doubloon",
                    coords=[
                        Vec3(11.578, 12.001, 84.648),
                        Vec3(11.578, 12.001, 86.348),
                    ],
                ),
                SeqInteract("Doubloon #3"),
                SeqMove(
                    name="Move to cliff",
                    coords=[
                        Vec3(10.679, 12.002, 84.755),
                        Vec3(2.706, 12.002, 76.692),
                    ],
                ),
                SeqMove(
                    name="Swim south",
                    coords=[
                        InteractMove(-3.656, 3.943, 76.574),
                        Vec3(-7.135, 3.943, 72.118),
                        Vec3(-8.650, 3.943, 54.607),
                    ],
                    precision=1.0,
                ),
                SeqMove(
                    name="Navigate to rope",
                    coords=[
                        InteractMove(-9.768, 5.002, 53.267),
                        InteractMove(-11.655, 8.002, 55.243),
                        Vec3(-15.777, 8.002, 52.932),
                    ],
                ),
                SeqCliffMove(
                    name="Cross rope",
                    coords=[
                        Vec3(-21.196, 8.002, 58.679),
                    ],
                ),
                SeqMove(
                    name="Navigate to doubloon",
                    coords=[
                        Vec3(-21.437, 8.002, 60.791),
                        Vec3(-25.333, 8.002, 60.787),
                        Vec3(-29.741, 8.002, 56.378),
                        Vec3(-29.872, 8.002, 53.775),
                        InteractMove(-28.208, 8.002, 52.112),
                        Vec3(-26.965, 8.002, 52.112),
                        InteractMove(-25.149, 13.002, 53.809),
                        Vec3(-24.454, 13.002, 54.899),
                        Vec3(-24.454, 13.002, 56.566),
                        Vec3(-28.737, 13.002, 60.379),
                        InteractMove(-29.951, 9.002, 61.697),
                        InteractMove(-33.231, 8.002, 61.648),
                    ],
                ),
                SeqInteract("Doubloon #4"),
                SeqMove(
                    name="Swim to doubloon",
                    coords=[
                        InteractMove(-33.231, 5.050, 45.724),
                        Vec3(-37.779, 6.042, 42.497),
                    ],
                ),
                SeqInteract("Doubloon #5"),
                SeqCombatAndMove(
                    name="Move to doubloon",
                    coords=[
                        Vec3(-21.250, 4.735, 27.553),
                        Vec3(-14.485, 4.106, 20.732),
                        Vec3(-14.485, 4.282, 14.242),
                        Vec3(-23.607, 4.997, 9.547),
                        Vec3(-31.403, 5.223, 9.527),
                        Vec3(-33.110, 6.094, 14.048),
                        Vec3(-33.509, 6.094, 15.931),
                        Vec3(-36.296, 8.022, 15.956),
                        Vec3(-41.547, 8.002, 16.193),
                        Vec3(-44.515, 8.002, 18.137),
                    ],
                    recovery_path=SeqMove(
                        name="Return to stairs",
                        coords=[
                            Vec3(-33.509, 6.094, 15.931),
                        ],
                    ),
                ),
                SeqInteract("Doubloon #6"),
                SeqMove(
                    name="Go to mural",
                    coords=[
                        Vec3(-44.274, 8.002, 20.546),
                        InteractMove(-27.678, 3.943, 37.635),
                        Vec3(-5.895, 5.885, 41.695),
                        Vec3(4.864, 6.002, 53.293),
                    ],
                ),
                SeqSelectOption("Place doubloons", skip_dialog_check=True),
                SeqMove(
                    name="Move to left stairs",
                    coords=[
                        Vec3(-8.154, 5.002, 49.027),
                        InteractMove(-14.840, 3.943, 43.058),
                        Vec3(-14.857, 3.943, 33.545),
                        Vec3(-13.336, 3.943, 33.545),
                        Vec3(-11.423, 9.004, 39.577),
                        Vec3(-7.504, 12.001, 39.577),
                    ],
                ),
                SeqGraplou("Crush crystal"),
                SeqMove(
                    name="Aim for north crystal",
                    coords=[
                        Vec3(-5.583, 12.002, 41.541),
                        Vec3(-4.583, 12.002, 41.541),
                    ],
                ),
                SeqGraplou("Crush crystal"),
                SeqMove(
                    name="Move to right stairs",
                    coords=[
                        InteractMove(-2.037, 6.002, 39.317),
                        Vec3(3.336, 6.002, 36.487),
                        Vec3(7.876, 6.052, 33.408),
                        Vec3(19.540, 4.408, 31.933),
                        Vec3(20.771, 3.943, 32.632),
                        Vec3(21.618, 5.951, 35.767),
                        Vec3(20.675, 9.002, 39.744),
                        Vec3(15.889, 12.002, 39.454),
                    ],
                ),
                SeqGraplou("Crush crystal"),
                SeqMove(
                    name="Aim for north crystal",
                    coords=[
                        Vec3(13.832, 12.002, 41.075),
                    ],
                ),
                SeqGraplou("Crush crystal"),
                SeqMove(
                    name="Leave area",
                    coords=[
                        Vec3(2.494, 6.002, 29.362),
                        Vec3(2.494, 6.002, 26.435),
                        Vec3(5.183, 5.847, 11.994),
                        Vec3(5.183, 5.847, -0.704),
                        HoldDirection(-26.500, 1.002, -32.502, joy_dir=Vec2(0, -1)),
                    ],
                ),
                SeqMove(
                    name="Navigate island",
                    coords=[
                        Vec3(-26.500, 1.002, -34.000),
                        Vec3(-26.000, 1.002, -34.000),
                        Vec3(-26.000, 1.002, -34.500),
                        Vec3(-25.500, 1.002, -34.500),
                        Vec3(-25.500, 1.002, -35.000),
                        Vec3(-24.000, 1.002, -35.000),
                        Vec3(-24.000, 1.002, -36.000),
                        Vec3(-22.500, 1.002, -36.000),
                        Vec3(-22.500, 1.002, -36.500),
                        Vec3(-18.500, 1.002, -36.500),
                    ],
                ),
                SeqInteract("Board boat"),
                SeqBoat(
                    name="Cross sea",
                    coords=[
                        Vec3(6.973, 0.500, -33.080),
                        Vec3(29.134, 0.500, -31.778),
                    ],
                ),
                SeqInteract("Disembark"),
            ],
        )


class SoutheastIsland(SeqList):
    """Routing of Southeast Island in the Sea of Nightmare."""

    def __init__(self: Self) -> None:
        """Initialize a new SoutheastIsland object."""
        super().__init__(
            name="Southeast Island",
            children=[
                SeqMove(
                    name="Go to area",
                    coords=[
                        Vec3(33.000, 1.002, -31.500),
                        Vec3(33.000, 1.002, -33.000),
                        Vec3(37.500, 1.002, -33.000),
                        Vec3(37.500, 1.002, -31.000),
                    ],
                ),
                SeqInteract("Enter area"),
                SeqMove(
                    name="Move to branch",
                    coords=[
                        Vec3(15.736, 1.002, 3.606),
                        Vec3(24.490, 1.002, 10.855),
                    ],
                ),
                SeqCheckpoint("sea_of_nightmare2"),
                SeqMove(
                    name="",
                    coords=[
                        Vec3(24.490, 1.002, 12.922),
                        # TODO(orkaboy): Continue routing
                    ],
                ),
                # TODO(orkaboy): Continue routing
            ],
        )


class SeaOfNightmare(SeqList):
    """Routing of the Sea of Nightmare."""

    def __init__(self: Self) -> None:
        """Initialize a new SeaOfNightmare object."""
        super().__init__(
            name="Sea of Nightmare",
            children=[
                SeqSkipUntilIdle("Board the Vespertine"),
                TheVespertine(),
                SouthwestIsland(),
                SoutheastIsland(),
                # TODO(orkaboy): Continue routing
            ],
        )
