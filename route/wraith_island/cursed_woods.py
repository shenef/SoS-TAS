"""Routing of Cursed Woods section of Wraith Island."""

import logging
from typing import Self

from engine.combat import SeqCombatAndMove
from engine.inventory import ARMORS
from engine.mathlib import Vec2, Vec3
from engine.seq import (
    HoldDirection,
    InteractMove,
    SeqCheckpoint,
    SeqCliffClimb,
    SeqCliffMove,
    SeqHoldDirectionUntilCombat,
    SeqHoldDirectionUntilLostControl,
    SeqInteract,
    SeqList,
    SeqLoot,
    SeqMove,
    SeqSkipUntilIdle,
)
from memory.player_party_manager import PlayerPartyCharacter

logger = logging.getLogger(__name__)


class ClearingWeeds(SeqList):
    """Routing of Cursed Woods, from arrival until the gates."""

    def __init__(self: Self) -> None:
        """Initialize a new ClearingWeeds object."""
        super().__init__(
            name="Clearing Weeds",
            children=[
                SeqCombatAndMove(
                    name="Move to save point",
                    coords=[
                        Vec3(13.792, 3.002, -4.069),
                        Vec3(22.023, 3.002, 5.332),
                        Vec3(22.042, 3.002, 11.359),
                        Vec3(16.289, 3.002, 14.189),
                        Vec3(16.289, 2.998, 18.318),
                        Vec3(13.945, 2.998, 20.659),
                        Vec3(13.945, 2.997, 24.292),
                        Vec3(12.358, 2.993, 26.526),
                        Vec3(15.350, 3.001, 33.157),
                    ],
                ),
                SeqCheckpoint("cursed_woods"),
                SeqMove(
                    name="Navigate to first Boulbe",
                    coords=[
                        Vec3(15.350, 3.001, 33.157),
                        Vec3(14.492, 3.002, 39.770),
                        Vec3(5.105, 3.002, 39.770),
                        Vec3(0.460, 3.002, 36.673),
                        InteractMove(-0.458, 1.002, 36.673),
                        Vec3(-6.456, 1.002, 35.741),
                        InteractMove(-7.256, 4.002, 36.406),
                        Vec3(-13.196, 4.002, 36.406),
                        Vec3(-16.442, 4.002, 38.908),
                        InteractMove(-19.913, 5.002, 40.430),
                        Vec3(-23.362, 5.002, 43.091),
                        Vec3(-23.362, 5.002, 46.776),
                        Vec3(-21.668, 5.002, 46.712),
                    ],
                ),
                SeqHoldDirectionUntilCombat("Boulbe", joy_dir=Vec2(0, -1), mash_confirm=True),
                SeqCombatAndMove(
                    name="Navigate to second Boulbe",
                    coords=[
                        Vec3(-18.234, 5.002, 38.474),
                        InteractMove(-16.383, 4.002, 36.597),
                        Vec3(-8.457, 4.002, 33.393),
                        InteractMove(-4.411, 1.002, 33.393),
                        Vec3(0.209, 1.002, 35.144),
                        InteractMove(2.999, 3.002, 37.864),
                        Vec3(13.140, 3.002, 44.209),
                        Vec3(14.039, 3.002, 73.714),
                        Vec3(14.039, 2.998, 80.577),
                        Vec3(11.899, 2.994, 83.651),
                        Vec3(11.899, 3.010, 95.651),
                        Vec3(12.829, 3.010, 99.029),
                        Vec3(12.829, 3.010, 106.833),
                        Vec3(10.639, 3.010, 111.916),
                        Vec3(6.847, 3.002, 127.611),
                        Vec3(9.637, 3.002, 130.623),
                        Vec3(13.521, 3.002, 130.623),
                        Vec3(16.759, 3.002, 127.250),
                        Vec3(16.759, 2.985, 119.705),
                        Vec3(18.704, 2.977, 117.849),
                        Vec3(21.988, 2.977, 117.849),
                        Vec3(23.685, 2.985, 110.097),
                        Vec3(25.119, 2.976, 109.122),
                        Vec3(30.674, 2.977, 109.122),
                        Vec3(32.105, 2.977, 111.490),
                        Vec3(32.105, 5.005, 123.044),
                        InteractMove(31.983, 8.002, 126.460),
                        Vec3(28.534, 8.002, 129.846),
                        Vec3(28.534, 8.002, 143.319),
                        Vec3(26.409, 8.002, 143.319),
                    ],
                ),
                SeqHoldDirectionUntilCombat("Boulbe", joy_dir=Vec2(0, -1), mash_confirm=True),
                SeqCombatAndMove(
                    name="Move to save point",
                    coords=[
                        Vec3(22.143, 8.002, 136.876),
                        InteractMove(20.463, 3.002, 135.953),
                        Vec3(17.576, 3.002, 136.772),
                        Vec3(12.382, 3.002, 139.367),
                        Vec3(12.382, 3.002, 150.958),
                        Vec3(23.616, 3.002, 162.191),
                        Vec3(23.616, 2.998, 169.872),
                        Vec3(25.577, 2.992, 173.535),
                        Vec3(25.577, 2.985, 175.915),
                        Vec3(23.750, 2.985, 177.239),
                        Vec3(20.362, 2.990, 177.239),
                        InteractMove(20.362, 2.999, 180.807),
                        Vec3(22.651, 2.991, 182.937),
                        Vec3(27.029, 2.977, 182.937),
                        Vec3(28.679, 2.977, 185.037),
                        Vec3(28.679, 2.977, 187.254),
                        Vec3(27.197, 2.977, 188.943),
                        Vec3(24.954, 2.977, 188.943),
                        Vec3(23.063, 2.977, 190.892),
                        Vec3(23.063, 2.998, 195.964),
                        Vec3(22.224, 3.005, 215.183),
                        Vec3(22.224, 2.997, 222.274),
                        Vec3(24.139, 2.995, 224.397),
                        Vec3(24.139, 3.006, 228.369),
                        Vec3(26.531, 3.002, 230.644),
                        InteractMove(26.531, 3.002, 233.985),
                        InteractMove(29.294, 3.002, 236.658),
                        Vec3(28.739, 3.002, 238.056),
                        InteractMove(23.532, 3.002, 243.426),
                    ],
                ),
                SeqCheckpoint(
                    "cursed_woods2",
                    return_path=SeqMove(
                        name="Return to path",
                        coords=[
                            Vec3(18.750, 3.002, 250.375),
                            Vec3(20.158, 3.002, 248.967),
                            Vec3(20.158, 3.002, 246.859),
                            InteractMove(23.364, 3.002, 243.640),
                        ],
                    ),
                ),
                SeqCombatAndMove(
                    name="Navigate to third Boulbe",
                    coords=[
                        InteractMove(26.417, 3.002, 246.110),
                        InteractMove(26.417, 3.002, 251.081),
                        InteractMove(29.737, 3.002, 254.338),
                        InteractMove(29.737, 3.002, 259.339),
                        Vec3(32.678, 3.002, 260.382),
                        Vec3(41.927, 2.977, 259.609),
                        Vec3(43.235, 2.977, 257.548),
                        Vec3(43.235, 2.977, 255.574),
                        Vec3(44.808, 2.977, 254.316),
                        Vec3(47.090, 2.993, 253.630),
                        Vec3(49.298, 3.007, 250.866),
                        Vec3(48.690, 3.002, 242.738),
                        Vec3(47.444, 3.002, 237.512),
                        Vec3(47.562, 3.002, 224.309),
                        InteractMove(54.569, 5.002, 224.358),
                        Vec3(59.532, 5.002, 229.172),
                    ],
                ),
                SeqHoldDirectionUntilCombat("Boulbe", joy_dir=Vec2(0.5, 1), mash_confirm=True),
                SeqCombatAndMove(
                    name="Move to chest",
                    coords=[
                        Vec3(56.990, 5.002, 247.276),
                    ],
                ),
                # TODO(orkaboy): Equip Bone Armor to whom? Maybe move equipment with equip_node?
                SeqLoot("Bone Armor", item=ARMORS.BoneArmor, equip_to=PlayerPartyCharacter.Valere),
                SeqMove(
                    name="Navigate to fourth Boulbe",
                    coords=[
                        Vec3(55.439, 5.002, 247.276),
                        InteractMove(54.050, 3.002, 248.697),
                        Vec3(48.360, 3.002, 252.054),
                        Vec3(46.112, 2.999, 254.261),
                        Vec3(44.505, 2.977, 254.319),
                        Vec3(42.457, 2.977, 256.495),
                        Vec3(42.457, 2.977, 259.154),
                        Vec3(40.507, 2.977, 260.223),
                        Vec3(30.006, 3.002, 261.347),
                        Vec3(20.435, 3.002, 262.952),
                        Vec3(17.139, 2.977, 262.703),
                        Vec3(15.619, 2.977, 261.151),
                        Vec3(15.619, 2.977, 258.851),
                        Vec3(14.070, 2.977, 257.315),
                        Vec3(5.284, 3.002, 256.184),
                        Vec3(6.410, 3.002, 242.492),
                        InteractMove(6.410, 3.002, 238.393),
                        InteractMove(3.410, 3.002, 235.495),
                        InteractMove(3.410, 3.002, 225.185),
                        Vec3(-1.607, 3.002, 219.429),
                        Vec3(-4.883, 3.002, 219.429),
                        InteractMove(-6.861, 4.002, 221.497),
                        Vec3(-9.328, 4.002, 233.382),
                        InteractMove(-9.306, 2.002, 241.910),
                        InteractMove(-15.896, 5.002, 248.563),
                    ],
                ),
                SeqHoldDirectionUntilCombat("Boulbe", joy_dir=Vec2(0.5, 1), mash_confirm=True),
                SeqCombatAndMove(
                    name="Go to gates",
                    coords=[
                        Vec3(-6.569, 5.002, 262.930),
                        InteractMove(-4.108, 3.002, 262.930),
                        Vec3(4.314, 3.002, 257.224),
                        Vec3(14.010, 2.977, 257.224),
                        Vec3(16.203, 2.977, 259.592),
                        Vec3(16.203, 2.977, 262.767),
                        Vec3(21.950, 3.002, 262.767),
                        Vec3(27.801, 3.002, 268.706),
                        HoldDirection(-45.792, 1.002, 356.667, joy_dir=Vec2(0, 1)),
                        HoldDirection(28.417, 6.382, 289.186, joy_dir=Vec2(0, 1)),
                    ],
                ),
                SeqHoldDirectionUntilLostControl("Follow that man!", joy_dir=Vec2(0, 1)),
                SeqSkipUntilIdle("Garl nooo v2"),
            ],
        )


class WoodsShortcut(SeqList):
    """Routing of Cursed Woods, from Seraï joining until leaving woods."""

    def __init__(self: Self) -> None:
        """Initialize a new WoodsShortcut object."""
        super().__init__(
            name="Woods Shortcut",
            children=[
                SeqMove(
                    name="Move to cliff",
                    coords=[
                        InteractMove(43.587, 4.002, 298.939),
                        Vec3(51.249, 4.002, 298.939),
                    ],
                ),
                SeqCliffClimb(
                    name="Climb ledge",
                    coords=[
                        InteractMove(51.103, 10.000, 299.332),
                    ],
                ),
                SeqCliffMove(
                    name="Move along ledge",
                    coords=[
                        Vec3(54.149, 10.000, 297.285),
                        HoldDirection(55.225, 10.002, 295.178, joy_dir=Vec2(1, -1)),
                    ],
                ),
                SeqMove(
                    name="Move to rapids",
                    coords=[
                        Vec3(55.225, 10.002, 287.701),
                        Vec3(59.106, 10.002, 283.756),
                    ],
                ),
                SeqCombatAndMove(
                    name="Rapids",
                    precision=1.0,
                    coords=[
                        # Run first rapid
                        InteractMove(60.336, 7.212, 277.977),
                        InteractMove(61.945, 10.002, 260.199),
                        Vec3(67.912, 10.002, 259.361),
                        Vec3(73.087, 10.002, 252.734),
                        Vec3(76.214, 10.002, 245.861),
                        # Run second rapid
                        InteractMove(61.192, 7.703, 157.459),
                        InteractMove(61.046, 9.002, 149.483),
                        Vec3(60.870, 9.002, 128.460),
                        InteractMove(51.385, 6.703, 85.460),
                        InteractMove(51.462, 9.002, 83.425),
                    ],
                ),
                SeqCombatAndMove(
                    name="Return to path",
                    coords=[
                        # Go through final stretch of woods
                        Vec3(52.903, 9.002, 81.460),
                        InteractMove(52.903, 8.002, 76.080),
                        Vec3(52.903, 8.002, 60.570),
                        Vec3(45.349, 8.002, 43.257),
                        Vec3(31.886, 8.002, 29.764),
                        InteractMove(31.367, 3.002, 28.981),
                        Vec3(20.653, 3.002, 28.914),
                        InteractMove(18.284, 1.002, 26.333),
                        Vec3(18.284, 1.002, 18.211),
                        Vec3(20.543, 1.002, 15.189),
                        InteractMove(22.200, 3.002, 13.461),
                        Vec3(22.200, 3.002, 3.974),
                        Vec3(15.142, 3.002, -2.004),
                    ],
                ),
                SeqHoldDirectionUntilLostControl("Go to exit", joy_dir=Vec2(0, -1)),
            ],
        )


class ToFerryman(SeqList):
    """Routing of Cursed Woods, cutscene in Lucent until arriving at Ferryman's Vigil."""

    def __init__(self: Self) -> None:
        """Initialize a new ToFerryman object."""
        super().__init__(
            name="To Ferryman",
            children=[
                SeqSkipUntilIdle("Rest well, Warrior Cook"),
                SeqMove(
                    name="",
                    coords=[
                        Vec3(32.272, 1.002, 180.286),
                        Vec3(32.252, 1.002, 182.454),
                        Vec3(44.627, 1.002, 182.454),
                        Vec3(46.004, 1.002, 171.146),
                        HoldDirection(46.000, 9.011, 123.344, joy_dir=Vec2(0, -1)),
                        Vec3(44.703, 1.002, 113.937),
                        Vec3(36.783, 1.002, 110.420),
                        Vec3(34.514, 1.002, 104.122),
                        HoldDirection(26.042, 1.002, 34.900, joy_dir=Vec2(0, -1)),
                        Vec3(26.042, 1.002, 32.391),
                        Vec3(68.098, 1.002, 32.391),
                        HoldDirection(191.500, 1.002, 109.998, joy_dir=Vec2(1, 0)),
                        Vec3(193.500, 1.002, 110.000),
                        Vec3(193.500, 1.002, 108.000),
                        Vec3(196.000, 1.002, 108.000),
                        Vec3(196.000, 1.002, 106.500),
                        Vec3(197.500, 1.002, 106.500),
                        Vec3(197.500, 1.002, 106.000),
                        Vec3(200.500, 1.002, 106.000),
                    ],
                ),
                SeqInteract("Ferryman's Vigil"),
            ],
        )


class CursedWoods(SeqList):
    """Routing of Cursed Woods, from arrival until leaving for Ferryman's Vigil."""

    def __init__(self: Self) -> None:
        """Initialize a new CursedWoods object."""
        super().__init__(
            name="Cursed Woods",
            children=[
                ClearingWeeds(),
                WoodsShortcut(),
                ToFerryman(),
            ],
        )
