"""Routing of Sea of Nightmare and the Vespertine."""

import logging
from typing import Self

from engine.combat import SeqCombatAndMove
from engine.mathlib import Vec2, Vec3
from engine.seq import (
    Graplou,
    HoldDirection,
    InteractMove,
    SeqBoat,
    SeqCheckpoint,
    SeqCliffMove,
    SeqClimb,
    SeqGraplou,
    SeqHoldDirectionDelay,
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
                        Graplou(-12.777, 2.010, 11.393, joy_dir=Vec2(-1, 0), hold_timer=0.1),
                    ],
                ),
                SeqClimb(
                    name="Climb left mast",
                    coords=[
                        Vec3(-14.091, 24.540, 11.244),
                        Vec3(-15.540, 24.539, 10.530),
                        Vec3(-15.499, 24.002, 9.460),
                    ],
                ),
                SeqMove(
                    name="Move to rope",
                    coords=[
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
                        Graplou(-8.560, 2.010, 11.889, joy_dir=Vec2(-1, 0), hold_timer=0.1),
                        Vec3(-13.996, 2.002, 9.464),
                        Vec3(-15.205, 2.002, 7.478),
                        Vec3(-20.883, 6.002, 7.478),
                        Vec3(-20.883, 6.002, 9.796),
                        Vec3(-19.264, 6.002, 11.614),
                    ],
                ),
                SeqSelectOption("Give map", skip_dialog_check=True),
                # TODO(orkaboy): Cutscene into boat movement
                SeqBoat(
                    "Cutscene into boat",
                    coords=[
                        # TODO(orkaboy): Location near start
                    ],
                    hold_skip=True,
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
                # TODO(orkaboy): Continue routing
            ],
        )
