"""Routing of Flooded Graveyard and Necromancer's Lair section of Wraith Island."""

import logging
from typing import Self

from engine.combat import SeqCombat, SeqCombatAndMove
from engine.mathlib import Vec2, Vec3
from engine.seq import (
    HoldDirection,
    InteractMove,
    SeqCheckpoint,
    SeqClimb,
    SeqDelay,
    SeqHoldDirectionUntilLostControl,
    SeqInteract,
    SeqList,
    SeqMove,
    SeqRaft,
    SeqSkipUntilCombat,
    SeqSkipUntilIdle,
)

logger = logging.getLogger(__name__)


class FloodedGraveyard(SeqList):
    """
    Routing of Flooded Graveyard.

    From arrival at Ferryman's Vigil until entering Necromancer's Lair.
    """

    def __init__(self: Self) -> None:
        """Initialize a new FloodedGraveyard object."""
        super().__init__(
            name="Flooded Graveyard",
            children=[
                SeqMove(
                    name="Move to ferryman",
                    coords=[
                        Vec3(23.214, 5.002, 9.606),
                        Vec3(29.489, 5.002, 9.491),
                    ],
                ),
                SeqInteract("Ferryman"),
                SeqSkipUntilIdle("Ferryman"),
                SeqCheckpoint("flooded_graveyard"),
                SeqMove(
                    name="Move to Solstice Door",
                    coords=[
                        Vec3(25.952, 6.002, 23.202),
                        Vec3(14.912, 4.002, 26.811),
                        Vec3(9.879, 4.002, 32.508),
                        Vec3(-7.284, 4.002, 33.666),
                        InteractMove(-11.113, 5.002, 37.315),
                        Vec3(-12.947, 5.002, 39.915),
                        Vec3(-12.947, 5.002, 48.040),
                    ],
                ),
                SeqInteract("Door"),
                SeqMove(
                    name="Move to wall",
                    coords=[
                        HoldDirection(72.000, 1.002, 205.968, joy_dir=Vec2(0, 1)),
                        Vec3(67.982, 1.002, 210.076),
                        Vec3(65.735, 1.002, 210.010),
                        Vec3(64.058, 1.002, 213.063),
                        Vec3(64.344, 1.002, 217.946),
                        Vec3(65.215, 1.002, 219.546),
                    ],
                ),
                SeqClimb(
                    name="Climb wall",
                    coords=[
                        InteractMove(65.215, 4.540, 219.540),
                        Vec3(67.701, 5.343, 219.530),
                        Vec3(69.491, 10.947, 219.530),
                        Vec3(70.752, 10.947, 219.530),
                    ],
                ),
                SeqMove(
                    name="Move to chest",
                    coords=[
                        InteractMove(70.752, 6.002, 217.542),
                        Vec3(71.857, 6.002, 217.437),
                    ],
                ),
                SeqInteract("Shimmering Daggers"),
                SeqSkipUntilIdle("Shimmering Daggers"),
                SeqMove(
                    name="Move to crypt",
                    coords=[
                        InteractMove(71.857, 1.002, 207.191),
                        HoldDirection(-13.107, 5.002, 47.962, joy_dir=Vec2(0, -1)),
                        Vec3(-16.711, 5.002, 34.460),
                        InteractMove(-16.711, 4.002, 30.092),
                        Vec3(-25.252, 4.002, 20.940),
                        Vec3(-36.434, 4.002, 20.122),
                        Vec3(-47.895, 4.191, 15.422),
                        HoldDirection(-126.500, 1.002, 14.500, joy_dir=Vec2(-1, 1)),
                    ],
                ),
                SeqCombatAndMove(
                    name="Juke enemies",
                    coords=[
                        Vec3(-131.003, 1.002, 16.390),
                        Vec3(-136.443, 1.002, 16.390),
                        Vec3(-141.507, 1.002, 21.453),
                    ],
                ),
                # Needed to be able to climb the wall
                SeqDelay("Wait", timeout_in_s=0.5),
                SeqCombatAndMove(
                    name="Juke enemies",
                    coords=[
                        Vec3(-141.507, 1.002, 21.453),
                        Vec3(-144.498, 1.002, 21.495),
                        Vec3(-144.498, 1.002, 29.598),
                        Vec3(-137.449, 1.002, 31.540),
                    ],
                ),
                SeqClimb(
                    name="Climb wall",
                    coords=[
                        InteractMove(-137.449, 6.696, 31.530),
                    ],
                ),
                SeqMove(
                    name="Navigate heights",
                    coords=[
                        HoldDirection(-55.083, 13.002, 31.467, joy_dir=Vec2(0, 1)),
                        Vec3(-52.931, 13.002, 32.716),
                        InteractMove(-52.350, 11.002, 31.999),
                        Vec3(-46.928, 11.002, 31.999),
                        Vec3(-36.362, 11.002, 42.431),
                        InteractMove(-36.154, 9.002, 45.423),
                        Vec3(-35.638, 9.002, 47.900),
                        Vec3(-40.052, 9.002, 53.301),
                        InteractMove(-40.739, 4.002, 53.911),
                        InteractMove(-40.642, 6.002, 78.013),
                    ],
                ),
                SeqCombatAndMove(
                    name="Juke enemies",
                    coords=[
                        Vec3(-37.690, 6.002, 81.320),
                        Vec3(-33.451, 6.002, 85.562),
                        Vec3(-33.451, 6.002, 92.702),
                        Vec3(-31.905, 6.002, 94.257),
                        InteractMove(-31.197, 0.819, 94.849),
                        Vec3(-26.660, 1.303, 100.696),
                        InteractMove(-25.267, 3.335, 100.691),
                    ],
                ),
                SeqRaft(
                    name="Rafting",
                    coords=[
                        Vec3(-33.105, 3.334, 100.691),
                        Vec3(-36.480, 3.485, 104.957),
                        Vec3(-36.480, 3.503, 117.610),
                        Vec3(-27.761, 3.413, 117.972),
                    ],
                ),
                SeqMove(
                    name="Get off raft",
                    coords=[
                        InteractMove(-27.761, 6.002, 124.300),
                    ],
                ),
                SeqHoldDirectionUntilLostControl("Move to cutscene", joy_dir=Vec2(0, 1)),
                SeqSkipUntilCombat("None shall pass"),
                SeqCombat("Duke Aventry"),
                SeqSkipUntilIdle("Learning Dash Strike"),
                SeqMove(
                    name="Enter Necromancer's Lair",
                    coords=[
                        Vec3(-27.888, 6.002, 133.250),
                        HoldDirection(10.000, 2.002, -9.000, joy_dir=Vec2(0, 1)),
                    ],
                ),
            ],
        )


class NecromancersLair(SeqList):
    """Routing of Necromancer's Lair."""

    def __init__(self: Self) -> None:
        """Initialize a new NecromancersLair object."""
        super().__init__(
            name="Necromancer's Lair",
            children=[
                SeqCombatAndMove(
                    name="Move to platform",
                    coords=[
                        Vec3(13.016, 2.002, -6.291),
                        InteractMove(14.053, -0.197, -5.406),
                        Vec3(17.323, -0.197, -1.029),
                        Vec3(18.546, 4.010, 15.539),
                        Vec3(18.454, 4.010, 18.992),
                        Vec3(14.856, 4.010, 23.758),
                        Vec3(9.911, 4.002, 23.894),
                        HoldDirection(9.905, 1.002, 67.659, joy_dir=Vec2(0, 1)),
                        Vec3(9.905, 1.002, 75.696),
                        Vec3(26.313, 1.002, 91.954),
                        InteractMove(26.313, 1.002, 101.460),
                        Vec3(26.358, 1.002, 102.813),
                    ],
                ),
                SeqInteract("Lever"),
                SeqMove(
                    name="Moving platform",
                    coords=[
                        Vec3(15.452, 1.001, 128.541),
                        InteractMove(15.452, 1.002, 133.465),
                    ],
                ),
                SeqCombatAndMove(
                    name="Juking enemies",
                    coords=[
                        Vec3(12.818, 1.001, 133.465),
                        Vec3(-3.442, 1.002, 149.684),
                        HoldDirection(4.500, 1.002, 206.992, joy_dir=Vec2(0, 1)),
                    ],
                ),
                SeqHoldDirectionUntilLostControl("Move to cutscene", joy_dir=Vec2(0, 1)),
                SeqSkipUntilIdle("Spooky scary skeletons"),
                # Right room
                # TODO(orkaboy): Split into own sequence
                SeqCombatAndMove(
                    name="Move to lever",
                    coords=[
                        Vec3(4.500, 1.002, 215.379),
                        InteractMove(8.214, -0.998, 219.553),
                        Vec3(12.277, -0.998, 225.852),
                        Vec3(19.264, -0.998, 229.676),
                        Vec3(19.264, -0.998, 235.162),
                        Vec3(16.980, -0.998, 238.647),
                        Vec3(16.980, -0.998, 247.327),
                        HoldDirection(77.704, -1.197, 254.698, joy_dir=Vec2(1, 1)),
                        Vec3(79.034, -1.197, 258.540),
                        InteractMove(79.034, 1.002, 262.575),
                        Vec3(80.056, 1.002, 270.713),
                        Vec3(81.839, 1.002, 275.709),
                        Vec3(81.898, 1.002, 275.709),
                        Vec3(81.898, 1.002, 275.709),
                        InteractMove(93.379, 1.002, 281.297),
                        Vec3(102.834, 1.002, 278.158),
                        # Enemy juking
                        Vec3(106.019, 1.002, 269.072),
                        # TODO(orkaboy): Might be off
                        Vec3(111.817, 1.002, 270.460),
                        Vec3(115.089, 1.002, 274.243),
                    ],
                ),
                SeqInteract("Lever"),
                # TODO(orkaboy): Continue routing
            ],
        )
