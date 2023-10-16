"""Routing of Flooded Graveyard and Necromancer's Lair section of Wraith Island."""

import logging
from typing import Self

from engine.combat import SeqCombat, SeqCombatAndMove
from engine.mathlib import Vec2, Vec3
from engine.seq import (
    Graplou,
    HoldDirection,
    InteractMove,
    SeqCheckpoint,
    SeqCliffMove,
    SeqClimb,
    SeqDelay,
    SeqHoldDirectionDelay,
    SeqHoldDirectionUntilCombat,
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


class NecromancersLairGraplou(SeqList):
    """Routing of Necromancer's Lair, right room (getting Graplou)."""

    def __init__(self: Self) -> None:
        """Initialize a new NecromancersLairGraplou object."""
        super().__init__(
            name="Right room",
            children=[
                SeqMove(
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
                        Vec3(81.437, 1.002, 275.444),
                    ],
                ),
                SeqCliffMove(
                    name="Beam",
                    coords=[
                        Vec3(85.500, 1.000, 279.338),
                        HoldDirection(88.300, 1.000, 278.855, joy_dir=Vec2(1, -0.5)),
                        Vec3(89.257, 1.000, 277.887),
                        HoldDirection(91.335, 1.000, 279.252, joy_dir=Vec2(1, 0.5)),
                        InteractMove(93.127, 1.002, 281.006),
                    ],
                ),
                SeqCombatAndMove(
                    name="Move to lever",
                    coords=[
                        Vec3(102.834, 1.002, 278.158),
                        # Enemy juking
                        Vec3(106.019, 1.002, 269.072),
                        Vec3(111.817, 1.002, 270.460),
                        Vec3(115.089, 1.002, 274.243),
                    ],
                ),
                SeqInteract("Lever"),
                SeqCombatAndMove(
                    name="Move to platform",
                    coords=[
                        Vec3(109.704, 1.002, 268.730),
                        Vec3(104.462, 1.002, 268.730),
                        Vec3(104.462, 1.002, 279.746),
                        Vec3(108.513, 1.002, 284.218),
                        InteractMove(112.073, 1.002, 284.218),
                        Vec3(113.400, 1.002, 283.840),
                    ],
                ),
                SeqInteract("Lever"),
                SeqMove(
                    name="Move to chest",
                    coords=[
                        Vec3(116.414, 1.002, 282.457),
                        Vec3(119.546, 1.002, 284.344),
                        InteractMove(122.481, 1.002, 284.344),
                        Vec3(125.936, 1.002, 276.845),
                        Vec3(128.941, 1.002, 275.544),
                        Vec3(131.501, 1.002, 275.544),
                        InteractMove(131.500, 7.002, 279.209),
                        Vec3(128.389, 7.002, 287.585),
                        Vec3(118.571, 7.002, 297.493),
                    ],
                ),
                SeqHoldDirectionDelay("Face chest", joy_dir=Vec2(0, 1), timeout_s=0.1),
                SeqInteract("Spectral Cape"),
                SeqSkipUntilIdle("Spectral Cape"),
                SeqMove(
                    name="Move to ladder",
                    coords=[
                        Vec3(110.684, 7.002, 289.502),
                        Vec3(105.565, 7.002, 289.618),
                    ],
                ),
                SeqHoldDirectionDelay("Face ladder", joy_dir=Vec2(0, -1), timeout_s=0.1),
                SeqInteract("Ladder"),
                SeqMove(
                    name="Double back",
                    coords=[
                        Vec3(113.015, 7.002, 291.127),
                        Vec3(118.783, 7.002, 291.127),
                        Vec3(123.496, 7.002, 289.109),
                        InteractMove(123.496, 1.002, 285.984),
                        Vec3(122.454, 1.002, 285.454),
                        InteractMove(119.119, 1.002, 285.454),
                        Vec3(117.076, 1.002, 285.454),
                    ],
                ),
                SeqInteract("Lever"),
                SeqMove(
                    name="Move to platform",
                    coords=[
                        Vec3(111.460, 1.002, 285.410),
                        InteractMove(108.060, 1.002, 285.388),
                        Vec3(105.526, 1.002, 287.546),
                        InteractMove(105.500, 7.002, 289.692),
                        Vec3(112.962, 7.002, 291.331),
                        Vec3(119.420, 7.002, 291.331),
                        Vec3(123.620, 7.002, 288.454),
                        InteractMove(123.620, 1.002, 286.254),
                        Vec3(123.533, 1.002, 274.454),
                        InteractMove(123.404, 1.002, 270.957),
                        Vec3(123.448, 1.002, 270.131),
                    ],
                ),
                SeqInteract("Lever"),
                SeqMove(
                    name="Jump off platform",
                    coords=[
                        Vec3(123.381, 1.002, 262.460),
                        InteractMove(123.381, 1.002, 258.527),
                    ],
                ),
                # TODO(orkaboy): RouteBranch?
                # Obsidian Ore
                SeqMove(
                    name="Move to chest",
                    coords=[
                        Vec3(124.625, 1.002, 255.279),
                        Vec3(124.625, 1.002, 251.994),
                        Vec3(117.349, 1.002, 244.872),
                    ],
                ),
                SeqHoldDirectionDelay("Face chest", joy_dir=Vec2(-1, -1), timeout_s=0.1),
                SeqInteract("Obsidian Ore"),
                SeqSkipUntilIdle("Obsidian Ore"),
                SeqMove(
                    name="Return to route",
                    coords=[
                        Vec3(123.782, 1.002, 251.193),
                    ],
                ),
                SeqMove(
                    name="Enter next room",
                    coords=[
                        Vec3(135.786, 1.002, 253.387),
                        Vec3(147.416, 1.002, 253.387),
                        HoldDirection(180.201, -5.998, 251.250, joy_dir=Vec2(1, 0)),
                    ],
                ),
                SeqCombatAndMove(
                    name="Move to boss chest",
                    coords=[
                        Vec3(184.879, -5.998, 251.250),
                        Vec3(191.581, -5.998, 252.052),
                        Vec3(195.462, -5.998, 248.112),
                        InteractMove(198.530, -19.998, 244.986),
                        Vec3(202.577, -19.998, 250.526),
                        Vec3(202.562, -19.998, 258.227),
                        Vec3(201.728, -19.998, 259.081),
                        InteractMove(200.748, -13.998, 260.315),
                        Vec3(200.748, -13.998, 263.925),
                        Vec3(204.221, -13.998, 267.133),
                        InteractMove(204.944, -19.998, 267.707),
                        Vec3(207.069, -19.998, 273.011),
                        HoldDirection(311.500, 1.002, 359.393, joy_dir=Vec2(0, 1)),
                        Vec3(311.500, 1.002, 379.940),
                    ],
                ),
                SeqInteract("Graplou"),
                SeqSkipUntilIdle("Graplou"),
                SeqCombatAndMove(
                    name="Graplouing around",
                    coords=[
                        Vec3(311.500, 1.002, 357.595),
                        HoldDirection(207.000, -19.998, 274.434, joy_dir=Vec2(0, -1)),
                        Vec3(207.000, -19.844, 266.980),
                        Graplou(207.001, -19.998, 256.333, joy_dir=Vec2(0, -1), hold_timer=0.1),
                        Vec3(202.059, -19.998, 259.410),
                        InteractMove(200.707, -13.998, 260.415),
                        Vec3(201.157, -13.998, 262.192),
                        Vec3(203.291, -13.871, 264.427),
                        Graplou(214.562, -13.998, 264.489, joy_dir=Vec2(1, 0), hold_timer=0.1),
                        Vec3(213.405, -13.998, 261.338),
                        Vec3(214.854, -13.998, 259.957),
                        Vec3(216.418, -13.998, 259.936),
                        InteractMove(217.317, -5.998, 261.467),
                        Graplou(223.410, -5.074, 267.926, joy_dir=Vec2(1, 1), hold_timer=0.1),
                    ],
                ),
                SeqClimb(
                    name="Climb wall",
                    coords=[
                        Vec3(223.417, -0.460, 267.933),
                        Vec3(212.424, -0.460, 274.530),
                    ],
                ),
                SeqMove(
                    name="Graplouing around",
                    coords=[
                        Vec3(211.051, -5.865, 271.348),
                        Graplou(199.342, -5.998, 271.478, joy_dir=Vec2(-1, 0), hold_timer=0.1),
                        Vec3(197.031, -5.998, 265.984),
                        Vec3(197.031, -5.871, 261.636),
                        Graplou(187.557, -5.998, 252.106, joy_dir=Vec2(-1, -1), hold_timer=0.1),
                        Vec3(178.095, -5.998, 252.106),
                        HoldDirection(144.973, 1.002, 253.500, joy_dir=Vec2(-1, 0)),
                        Vec3(131.834, 1.002, 253.500),
                        Vec3(124.881, 1.002, 258.056),
                        InteractMove(124.881, 1.002, 262.748),
                        Vec3(125.644, 1.002, 264.052),
                        Vec3(126.644, 1.002, 265.052),
                    ],
                ),
                SeqMove(
                    name="Trick shot",
                    coords=[
                        Graplou(131.500, 1.637, 275.530, joy_dir=Vec2(1, 1), hold_timer=0.2),
                        Vec3(131.476, 1.002, 274.730),
                        Vec3(126.719, 1.002, 275.708),
                        Vec3(124.786, 1.002, 278.202),
                        Vec3(122.454, 1.002, 284.114),
                        InteractMove(117.440, 1.002, 283.777),
                    ],
                ),
                SeqInteract("Lever"),
                SeqMove(
                    name="Head to skeleton chamber",
                    coords=[
                        Vec3(111.460, 1.002, 283.777),
                        InteractMove(108.060, 1.002, 283.777),
                        Vec3(98.131, 1.002, 283.777),
                        Vec3(94.010, 1.002, 287.478),
                        Graplou(93.982, 1.010, 300.000, joy_dir=Vec2(0, 1), hold_timer=0.1),
                        HoldDirection(95.000, 1.002, 354.500, joy_dir=Vec2(0, 1)),
                    ],
                ),
                SeqHoldDirectionUntilCombat("Revenant", joy_dir=Vec2(0, 1), mash_confirm=True),
                SeqCombatAndMove(
                    name="Revenant",
                    coords=[
                        Vec3(94.973, 1.002, 371.278),
                        Vec3(94.973, 6.010, 379.287),
                    ],
                ),
                SeqInteract("Skull"),
                SeqMove(
                    name="Return to central chamber",
                    coords=[
                        Vec3(94.973, 1.010, 354.800),
                        HoldDirection(94.500, 1.002, 302.166, joy_dir=Vec2(0, -1)),
                        Vec3(94.009, 1.002, 299.090),
                        Graplou(93.988, 1.010, 285.500, joy_dir=Vec2(0, -1), hold_timer=0.1),
                        Vec3(91.492, 1.002, 284.515),
                        Graplou(80.500, 1.010, 274.500, joy_dir=Vec2(-1, -1), hold_timer=0.1),
                        Vec3(79.341, 1.002, 269.047),
                        Vec3(78.739, 1.002, 259.457),
                        InteractMove(78.739, -1.197, 258.539),
                        Vec3(74.432, -1.197, 253.188),
                        HoldDirection(21.217, -1.697, 251.380, joy_dir=Vec2(-1, -1)),
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
                SeqCheckpoint("necro_lair"),
                # Right room
                NecromancersLairGraplou(),
                # TODO(orkaboy): Continue routing
            ],
        )
