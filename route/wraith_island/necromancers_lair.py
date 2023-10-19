"""Routing of Flooded Graveyard and Necromancer's Lair section of Wraith Island."""

import logging
from typing import Self

from engine.combat import SeqCombat, SeqCombatAndMove
from engine.inventory import ARMORS, TRINKETS, VALUABLES, WEAPONS
from engine.mathlib import Vec2, Vec3
from engine.seq import (
    Graplou,
    HoldDirection,
    InteractMove,
    SeqCheckpoint,
    SeqCliffMove,
    SeqClimb,
    SeqDelay,
    SeqGraplou,
    SeqHoldDirectionDelay,
    SeqHoldDirectionUntilLostControl,
    SeqInteract,
    SeqList,
    SeqLoot,
    SeqMove,
    SeqRaft,
    SeqRouteBranch,
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
                SeqLoot("Shimmering Daggers", item=WEAPONS.ShimmeringDaggers),
                # TODO(orkaboy): Equip
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


class NecromancersLairEntry(SeqList):
    """Routing of Necromancer's Lair. Entrance to hub area."""

    def __init__(self: Self) -> None:
        """Initialize a new NecromancersLairEntry object."""
        super().__init__(
            name="Entry",
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
                SeqLoot("Spectral Cape", item=ARMORS.SpectralCape),
                # TODO(orkaboy): Equip
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
                SeqLoot("Obsidian Ore", item=VALUABLES.ObsidianOre),
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
                SeqLoot("Graplou"),
                SeqCombatAndMove(
                    name="Graplou movement",
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
                    name="Graplou movement",
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


class NecromancersLairCentral(SeqList):
    """Routing of Necromancer's Lair. Central area."""

    def __init__(self: Self) -> None:
        """Initialize a new NecromancersLairCentral object."""
        super().__init__(
            name="Central area",
            children=[
                SeqCombatAndMove(
                    name="Revenant",
                    coords=[
                        Vec3(16.581, -0.994, 247.063),
                        Vec3(15.544, -0.994, 242.682),
                        InteractMove(14.989, 1.002, 241.347),
                        Vec3(10.539, 1.002, 239.353),
                        Vec3(4.585, 1.002, 240.819),
                        Vec3(4.585, 3.010, 247.820),
                    ],
                ),
                SeqInteract("Skull"),
                SeqMove(
                    name="",
                    coords=[
                        Vec3(3.685, 1.002, 240.677),
                        Vec3(-7.540, 1.002, 236.755),
                        InteractMove(-10.748, 1.002, 236.755),
                        InteractMove(-10.748, -0.998, 241.076),
                    ],
                ),
            ],
        )


class NecromancersLairLeft(SeqList):
    """Routing of Necromancer's Lair. Left area."""

    def __init__(self: Self) -> None:
        """Initialize a new NecromancersLairLeft object."""
        super().__init__(
            name="Left area",
            children=[
                SeqMove(
                    name="Enter left area",
                    coords=[
                        Vec3(-10.280, -0.998, 244.910),
                        InteractMove(-11.135, 1.002, 246.120),
                        Vec3(-12.779, 1.002, 249.426),
                        HoldDirection(-63.000, 1.002, 250.000, joy_dir=Vec2(-1, 1)),
                    ],
                ),
                SeqCombatAndMove(
                    name="Move to Graplou",
                    coords=[
                        Vec3(-72.556, 1.002, 259.556),
                        Vec3(-72.556, 1.002, 277.646),
                    ],
                ),
                SeqGraplou(),
                SeqCombatAndMove(
                    name="Move to lever",
                    coords=[
                        Vec3(-72.542, 1.002, 279.029),
                        InteractMove(-72.542, 3.002, 287.577),
                        Vec3(-72.542, 3.002, 289.840),
                    ],
                ),
                SeqInteract("Lever"),
                SeqCombatAndMove(
                    name="Move to chest",
                    coords=[
                        InteractMove(-72.542, 1.002, 280.075),
                        Vec3(-74.627, 1.002, 280.075),
                        Vec3(-77.852, 1.002, 283.571),
                        InteractMove(-81.748, 1.002, 283.536),
                        InteractMove(-81.748, 8.002, 288.467),
                        Vec3(-81.748, 8.002, 292.302),
                        Vec3(-68.070, 8.002, 295.713),
                        HoldDirection(-48.500, 1.002, 349.626, joy_dir=Vec2(0, 1)),
                        Vec3(-48.500, 1.002, 352.259),
                        Vec3(-51.274, 1.002, 357.259),
                    ],
                ),
                SeqLoot("Osseous Staff", item=WEAPONS.OsseousStaff),
                # TODO(orkaboy): Equip
                SeqMove(
                    name="Graplou movement",
                    coords=[
                        Vec3(-48.152, 1.002, 354.438),
                        Graplou(-34.000, 1.010, 354.593, joy_dir=Vec2(1, 0), hold_timer=0.1),
                        Graplou(-32.980, 1.010, 372.000, joy_dir=Vec2(0, 1), hold_timer=0.1),
                        # TODO(orkaboy): Can grab Mooncradle Fish Pie here
                        Vec3(-33.879, 1.002, 378.421),
                    ],
                ),
                SeqGraplou("Attack enemy"),
                SeqCombatAndMove(
                    name="Move to lever",
                    coords=[
                        Vec3(-38.553, 1.002, 391.033),
                        Vec3(-42.429, 1.002, 389.041),
                        Vec3(-43.863, 1.002, 389.041),
                        Graplou(-47.398, 1.002, 397.596, joy_dir=Vec2(-1, 1), hold_timer=0.1),
                        Graplou(-56.737, 1.002, 404.682, joy_dir=Vec2(-1, 1), hold_timer=0.1),
                        Vec3(-48.205, 2.002, 404.713),
                        Vec3(-47.271, 2.002, 402.209),
                    ],
                ),
                SeqInteract("Lever"),
                SeqCombatAndMove(
                    name="Graplou movement",
                    coords=[
                        Vec3(-48.133, 2.002, 404.808),
                        Vec3(-54.118, 1.002, 404.808),
                        Vec3(-56.543, 1.002, 402.189),
                        Graplou(-64.280, 1.002, 393.939, joy_dir=Vec2(-1, -1), hold_timer=0.1),
                        Graplou(-73.382, 1.002, 396.605, joy_dir=Vec2(-1, 0), hold_timer=0.1),
                        Vec3(-71.100, 1.002, 388.357),
                    ],
                ),
                SeqInteract("Lever"),
                SeqCombatAndMove(
                    name="Move to lever (E)",
                    coords=[
                        Vec3(-72.197, 1.002, 389.641),
                        Vec3(-76.562, 1.002, 389.641),
                        Graplou(-76.407, 1.010, 375.500, joy_dir=Vec2(0, -1), hold_timer=0.1),
                        Vec3(-74.704, 1.010, 373.774),
                        Vec3(-57.002, 1.002, 373.922),
                        Vec3(-54.693, 1.410, 376.214),
                        Vec3(-53.582, 4.002, 381.517),
                        InteractMove(-42.461, 4.008, 381.500),
                        Vec3(-39.627, 4.002, 381.150),
                    ],
                ),
                SeqInteract("Lever"),
                SeqMove(
                    name="Move to lever (N)",
                    coords=[
                        Vec3(-41.149, 4.002, 381.500),
                        InteractMove(-52.939, 4.002, 381.500),
                        Vec3(-53.648, 4.002, 381.500),
                        Vec3(-54.112, 4.002, 388.640),
                    ],
                ),
                SeqInteract("Lever"),
                SeqCombatAndMove(
                    name="Move to lever (SW)",
                    coords=[
                        Vec3(-55.014, 1.249, 376.054),
                        Vec3(-57.790, 1.002, 373.290),
                        Graplou(-64.284, 1.002, 365.943, joy_dir=Vec2(-1, -1), hold_timer=0.1),
                        Graplou(-72.027, 1.002, 358.322, joy_dir=Vec2(-1, -1), hold_timer=0.1),
                        Vec3(-78.681, 1.002, 360.574),
                        Vec3(-78.545, 4.002, 365.740),
                    ],
                ),
                SeqInteract("Lever"),
                SeqMove(
                    name="Leave room",
                    coords=[
                        Vec3(-78.545, 1.010, 360.274),
                        Vec3(-68.693, 1.002, 355.243),
                        Vec3(-53.460, 2.002, 355.243),
                        InteractMove(-51.025, 1.002, 355.243),
                        Vec3(-48.674, 1.002, 352.299),
                        HoldDirection(-67.958, 8.002, 297.500, joy_dir=Vec2(0, -1)),
                    ],
                ),
                SeqCombatAndMove(
                    name="Enter left room",
                    coords=[
                        Vec3(-67.958, 8.002, 295.665),
                        Vec3(-66.901, 8.002, 290.454),
                        InteractMove(-66.901, 1.002, 289.536),
                        Vec3(-66.901, 1.002, 283.203),
                        Vec3(-71.192, 1.002, 278.045),
                        Vec3(-80.092, 1.002, 264.931),
                        Vec3(-86.479, 1.002, 264.886),
                        Vec3(-91.546, 1.002, 269.380),
                        Graplou(-101.540, 1.002, 269.529, joy_dir=Vec2(-1, 0), hold_timer=0.1),
                        Vec3(-100.107, 1.002, 267.457),
                        Graplou(-99.623, 1.002, 258.460, joy_dir=Vec2(0, -1), hold_timer=0.1),
                        Vec3(-101.126, 1.002, 258.773),
                        InteractMove(-101.701, -1.998, 258.050),
                        Vec3(-104.322, -1.998, 255.454),
                        InteractMove(-104.322, -2.998, 254.002),
                        Vec3(-111.388, -2.998, 253.087),
                        Vec3(-115.508, -2.998, 253.087),
                        Vec3(-119.241, -2.998, 257.337),
                        Vec3(-121.934, -2.998, 257.337),
                        Vec3(-125.343, -6.998, 248.814),
                        Vec3(-125.343, -6.998, 248.814),
                        Vec3(-129.058, -6.998, 248.264),
                        Vec3(-132.639, -6.998, 258.660),
                        Vec3(-133.442, -6.998, 278.120),
                        HoldDirection(-157.000, 8.002, 356.258, joy_dir=Vec2(0, 1)),
                    ],
                ),
                SeqMove(
                    name="Go to bottom of stairs",
                    coords=[
                        Vec3(-154.565, 8.002, 400.960),
                        Vec3(-111.077, -2.998, 400.960),
                        Vec3(-111.077, -12.990, 370.477),
                        Vec3(-111.199, -12.998, 370.250),
                        Vec3(-124.295, -18.998, 370.250),
                        Vec3(-125.082, -18.998, 372.540),
                    ],
                ),
                SeqGraplou("Attack wizard", until_combat=True),
                SeqCombatAndMove(
                    name="Move to lever",
                    coords=[
                        Vec3(-130.268, -18.998, 387.240),
                    ],
                ),
                SeqInteract("Lever"),
                SeqMove(
                    name="Move to lever",
                    coords=[
                        Vec3(-125.408, -18.998, 388.546),
                        Graplou(-125.397, -18.998, 397.540, joy_dir=Vec2(0, 1), hold_timer=0.1),
                        Vec3(-123.457, -18.998, 396.815),
                        Graplou(-112.660, -18.998, 395.444, joy_dir=Vec2(1, 0), hold_timer=0.1),
                        Vec3(-117.722, -18.998, 400.543),
                    ],
                ),
                SeqInteract("Lever"),
                SeqCombatAndMove(
                    name="Climb room",
                    coords=[
                        Vec3(-114.319, -18.998, 400.543),
                        InteractMove(-114.319, -11.998, 401.758),
                        Vec3(-119.163, -11.998, 401.758),
                        Graplou(-127.128, -11.998, 393.778, joy_dir=Vec2(-1, -1), hold_timer=0.1),
                        Graplou(-137.647, -11.998, 395.666, joy_dir=Vec2(-1, 0), hold_timer=0.1),
                        Vec3(-137.429, -11.998, 400.742),
                    ],
                ),
                SeqInteract("Lever"),
                SeqCombatAndMove(
                    name="Move to wall",
                    coords=[
                        Vec3(-134.851, -11.998, 400.742),
                        Vec3(-132.460, -11.998, 402.546),
                    ],
                ),
                SeqClimb(
                    name="Climb wall",
                    coords=[
                        InteractMove(-132.460, -3.460, 402.540),
                        Vec3(-136.540, -3.460, 402.530),
                    ],
                ),
                SeqMove(
                    name="Off wall",
                    coords=[
                        Vec3(-136.540, -4.998, 402.460),
                    ],
                ),
                SeqHoldDirectionDelay("Off wall", joy_dir=Vec2(0, -1), timeout_s=0.1),
                SeqMove(
                    name="Move to lever",
                    coords=[
                        Vec3(-138.241, -4.998, 402.460),
                        Vec3(-139.310, -4.998, 403.645),
                    ],
                ),
                SeqInteract("Lever"),
                SeqMove(
                    name="Graplou to lever",
                    coords=[
                        Graplou(-139.485, -4.998, 393.460, joy_dir=Vec2(0, -1), hold_timer=0.1),
                        Graplou(-149.152, -4.998, 384.218, joy_dir=Vec2(-1, -1), hold_timer=0.1),
                        Vec3(-150.770, -4.998, 387.156),
                    ],
                ),
                SeqInteract("Lever"),
                SeqMove(
                    name="Leave room",
                    coords=[
                        Graplou(-150.572, -4.990, 388.782, joy_dir=Vec2(0, 1), hold_timer=0.1),
                        Vec3(-150.552, 8.002, 400.700),
                        Vec3(-154.504, 8.002, 400.700),
                        Vec3(-156.855, 8.002, 374.765),
                        Vec3(-156.855, 8.002, 354.082),
                        HoldDirection(-133.542, -6.990, 277.556, joy_dir=Vec2(0, -1)),
                    ],
                ),
                SeqCombatAndMove(
                    name="Revenant",
                    coords=[
                        Vec3(-132.756, -6.990, 260.468),
                        Vec3(-128.866, -6.998, 248.700),
                        Vec3(-124.913, -6.998, 248.664),
                        Vec3(-122.334, -2.998, 257.327),
                        Vec3(-119.216, -2.998, 257.327),
                        Vec3(-115.207, -2.998, 253.409),
                        Vec3(-113.324, -2.998, 253.409),
                        Vec3(-111.563, 1.010, 260.582),
                        Graplou(-111.479, 1.002, 271.458, joy_dir=Vec2(0, 1), hold_timer=0.1),
                        Graplou(-111.507, 1.002, 280.439, joy_dir=Vec2(0, 1), hold_timer=0.1),
                        Vec3(-111.507, 7.268, 288.073),
                        Vec3(-111.615, 8.002, 298.814),
                        Vec3(-111.615, 10.010, 303.811),
                    ],
                ),
                SeqInteract("Skull"),
                SeqCombatAndMove(
                    name="Leave room",
                    coords=[
                        Vec3(-110.058, 1.010, 278.210),
                        Graplou(-111.546, 1.002, 267.460, joy_dir=Vec2(0, -1), hold_timer=0.1),
                        Vec3(-109.454, 1.002, 269.278),
                        Graplou(-97.460, 1.002, 269.484, joy_dir=Vec2(1, 0), hold_timer=0.1),
                        Graplou(-87.460, 1.002, 269.565, joy_dir=Vec2(1, 0), hold_timer=0.1),
                        Vec3(-87.460, 1.002, 266.588),
                        Vec3(-85.453, 1.002, 264.799),
                        Vec3(-79.549, 1.002, 264.799),
                        Vec3(-65.984, 1.002, 253.451),
                        HoldDirection(-12.525, 1.002, 250.112, joy_dir=Vec2(1, -1)),
                    ],
                ),
            ],
        )


class NecromancersLairBoss(SeqList):
    """Routing of Necromancer's Lair. Fighting Romaya."""

    def __init__(self: Self) -> None:
        """Initialize a new NecromancersLairBoss object."""
        super().__init__(
            name="Romaya",
            children=[
                SeqMove(
                    name="Enter lair",
                    coords=[
                        Vec3(-10.252, 1.002, 249.814),
                        Vec3(-6.378, 1.002, 253.365),
                        Vec3(3.935, 1.002, 253.365),
                        HoldDirection(9.000, 0.002, 292.500, joy_dir=Vec2(0, 1)),
                        Vec3(9.000, 0.039, 307.843),
                    ],
                ),
                SeqHoldDirectionUntilLostControl("Move to cutscene", joy_dir=Vec2(0, 1)),
                SeqSkipUntilCombat("Grumpy necromancer"),
                SeqCombat("Romaya"),
                SeqSkipUntilIdle("Even grumpier necromancer"),
            ],
        )


class NecromancersLairLeave(SeqList):
    """Routing of Necromancer's Lair. Leaving lair."""

    def __init__(self: Self) -> None:
        """Initialize a new NecromancersLairLeave object."""
        super().__init__(
            name="Leave lair",
            children=[
                SeqMove(
                    name="Go to save point",
                    coords=[
                        Vec3(11.410, 1.002, 254.000),
                        Vec3(15.609, 1.002, 249.457),
                        InteractMove(15.609, -0.998, 248.189),
                        Vec3(17.162, -0.998, 240.828),
                        Vec3(17.074, -0.998, 236.540),
                        Vec3(19.727, -0.998, 231.723),
                        Vec3(5.963, -0.999, 217.688),
                        InteractMove(4.278, 1.002, 215.300),
                    ],
                ),
                SeqCheckpoint(
                    "necro_lair_boss2",
                    return_path=SeqMove(
                        name="Return to path",
                        coords=[
                            Vec3(4.349, 1.002, 215.896),
                        ],
                    ),
                ),
                SeqCombatAndMove(
                    name="Move to platform",
                    coords=[
                        Vec3(4.349, 1.002, 207.241),
                        HoldDirection(-3.417, 1.002, 155.808, joy_dir=Vec2(0, -1)),
                        Vec3(-3.391, 1.002, 149.638),
                        Vec3(13.673, 1.001, 132.664),
                        Vec3(15.884, 1.001, 132.570),
                        InteractMove(15.884, 1.002, 127.985),
                        Vec3(15.884, 1.002, 127.333),
                    ],
                ),
                SeqInteract("Lever"),
                SeqCombatAndMove(
                    name="Exit",
                    coords=[
                        Vec3(26.582, 1.002, 101.460),
                        InteractMove(26.582, 1.002, 97.451),
                        Vec3(24.315, 1.002, 91.319),
                        Vec3(10.200, 1.002, 77.056),
                        Vec3(10.200, 1.002, 64.850),
                        HoldDirection(10.000, 4.002, 25.785, joy_dir=Vec2(0, -1)),
                        Vec3(11.203, 4.002, 12.460),
                        InteractMove(12.069, -0.197, 0.674),
                        Vec3(10.367, -0.197, -3.540),
                        InteractMove(10.367, 2.002, -7.034),
                        HoldDirection(-27.888, 6.002, 133.250, joy_dir=Vec2(0, -1)),
                    ],
                ),
            ],
        )


class GetEnchantedScarf(SeqList):
    """Getting Enchanted Scarf in Flooded Graveyard."""

    def __init__(self: Self) -> None:
        """Initialize a new GetEnchantedScarf object."""
        super().__init__(
            name="Get Enchanted Scarf",
            children=[
                SeqMove(
                    name="Enter puzzle room",
                    coords=[
                        Graplou(8.703, 10.010, 49.750, joy_dir=Vec2(1, 1), hold_timer=0.1),
                        Graplou(19.000, 10.010, 59.000, joy_dir=Vec2(1, 1), hold_timer=0.1),
                        Vec3(16.963, 10.002, 58.717),
                        Graplou(8.750, 10.010, 67.000, joy_dir=Vec2(-1, 1), hold_timer=0.1),
                        Vec3(10.902, 10.010, 76.514),
                        HoldDirection(147.503, 1.002, 205.000, joy_dir=Vec2(0, 1)),
                        Graplou(135.459, 1.002, 212.813, joy_dir=Vec2(-1, 1), hold_timer=0.1),
                    ],
                ),
                SeqHoldDirectionDelay("Turn", joy_dir=Vec2(0, 1), timeout_s=0.1),
                SeqGraplou("Pull wall thing"),
                SeqMove(
                    name="Move to right side",
                    coords=[
                        Vec3(138.043, 1.002, 214.166),
                        Graplou(159.540, 1.002, 210.901, joy_dir=Vec2(1, 0), hold_timer=0.1),
                    ],
                ),
                SeqHoldDirectionDelay("Turn", joy_dir=Vec2(0, 1), timeout_s=0.1),
                SeqGraplou("Pull wall thing"),
                SeqMove(
                    name="Move to chest",
                    coords=[
                        Vec3(155.519, 1.002, 213.641),
                        Graplou(144.553, 1.002, 214.465, joy_dir=Vec2(-1, 0), hold_timer=0.1),
                        Vec3(147.533, 1.002, 218.209),
                    ],
                ),
                SeqLoot("Enchanted Scarf", item=TRINKETS.EnchantedScarf),
                # TODO(orkaboy): Equip
                SeqMove(
                    name="Return to path",
                    coords=[
                        Vec3(146.308, 1.002, 214.501),
                        Vec3(147.597, 1.002, 206.166),
                        HoldDirection(11.000, 10.002, 76.889, joy_dir=Vec2(0, -1)),
                        Vec3(11.000, 10.002, 65.193),
                        Graplou(19.000, 10.010, 57.000, joy_dir=Vec2(1, -1), hold_timer=0.1),
                        Graplou(8.000, 10.010, 49.106, joy_dir=Vec2(-1, -1), hold_timer=0.1),
                        Graplou(-1.000, 10.010, 38.750, joy_dir=Vec2(-1, -1), hold_timer=0.1),
                    ],
                ),
            ],
        )


class FloodedGraveyardLeave(SeqList):
    """Routing of Necromancer's Lair. Leaving graveyard."""

    def __init__(self: Self) -> None:
        """Initialize a new FloodedGraveyardLeave object."""
        super().__init__(
            name="Leave graveyard",
            children=[
                SeqMove(
                    name="Graplou movement",
                    coords=[
                        Vec3(-20.813, 6.002, 126.556),
                        InteractMove(-17.078, 6.002, 126.556),
                        Vec3(-14.573, 6.002, 124.200),
                        InteractMove(-12.323, 7.002, 124.358),
                        InteractMove(-12.323, 10.002, 126.709),
                        Vec3(-9.944, 10.002, 127.286),
                        Graplou(1.575, 10.002, 127.368, joy_dir=Vec2(1, 0), hold_timer=0.1),
                        Vec3(-0.731, 10.002, 101.232),
                        Vec3(-7.625, 10.002, 97.911),
                        Vec3(-9.668, 10.002, 96.840),
                        Graplou(-12.000, 10.010, 81.250, joy_dir=Vec2(0, -1), hold_timer=0.1),
                        Vec3(-11.405, 10.002, 67.218),
                        Vec3(-11.451, 10.002, 51.262),
                        Graplou(1.000, 10.010, 39.274, joy_dir=Vec2(1, -1), hold_timer=0.1),
                    ],
                ),
                # Branch to get item
                SeqRouteBranch(
                    name="Enchanted Scarf",
                    route=["fg_enchanted_scarf"],
                    when_true=GetEnchantedScarf(),
                ),
                SeqMove(
                    name="Go to ferryman",
                    coords=[
                        Vec3(2.347, 10.002, 36.994),
                        InteractMove(2.919, 4.002, 36.268),
                        Vec3(4.383, 4.002, 32.687),
                        Vec3(12.199, 4.002, 30.277),
                        Vec3(17.117, 4.002, 25.265),
                        Vec3(25.285, 6.002, 23.540),
                        Vec3(37.547, 6.002, 22.898),
                    ],
                ),
                SeqInteract("Ferryman"),
            ],
        )


class NecromancersLair(SeqList):
    """Routing of Necromancer's Lair."""

    def __init__(self: Self) -> None:
        """Initialize a new NecromancersLair object."""
        super().__init__(
            name="Necromancer's Lair",
            children=[
                NecromancersLairEntry(),
                # In hub area
                SeqCheckpoint("necro_lair"),
                # Right room
                NecromancersLairGraplou(),
                NecromancersLairCentral(),
                SeqCheckpoint(
                    "necro_lair2",
                    return_path=SeqMove(
                        name="Return to path",
                        coords=[
                            Vec3(-12.753, 1.002, 221.117),
                            Vec3(-12.753, 1.002, 223.540),
                            InteractMove(-12.753, -0.998, 226.408),
                            Vec3(-13.009, -0.998, 232.323),
                            Vec3(-13.009, -0.998, 239.893),
                        ],
                    ),
                ),
                NecromancersLairLeft(),
                SeqCheckpoint(
                    "necro_lair_boss",
                    return_path=SeqMove(
                        name="Return to path",
                        coords=[
                            Vec3(-11.630, 1.002, 221.020),
                            Vec3(-12.790, 1.002, 223.540),
                            InteractMove(-12.790, -0.998, 227.318),
                            Vec3(-12.790, -0.998, 240.014),
                            Vec3(-9.769, -0.998, 245.271),
                            InteractMove(-10.252, 1.002, 246.412),
                        ],
                    ),
                ),
                NecromancersLairBoss(),
                NecromancersLairLeave(),
            ],
        )
