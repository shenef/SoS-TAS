"""Routing of Tower of Antsudlo segment of Watcher Island."""

import logging
from typing import Self

from engine.combat import SeqCombatAndMove
from engine.inventory.items import ARMORS
from engine.mathlib import Vec2, Vec3
from engine.seq import (
    Graplou,
    HoldDirection,
    InteractMove,
    SeqBracelet,
    SeqCheckpoint,
    SeqCliffMove,
    SeqClimb,
    SeqDelay,
    SeqHoldDirectionDelay,
    SeqInteract,
    SeqList,
    SeqLoot,
    SeqMove,
    SeqRaft,
    SeqSelectOption,
)
from memory.player_party_manager import PlayerPartyCharacter

logger = logging.getLogger(__name__)


class Seafloor(SeqList):
    """Routing of Seafloor part of Tower of Antsudlo."""

    def __init__(self: Self) -> None:
        """Initialize a new Seafloor object."""
        super().__init__(
            name="Seafloor",
            children=[
                SeqMove(
                    name="Move to Sapphire Key",
                    coords=[
                        Vec3(12.266, 1.303, 26.810),
                        Vec3(12.229, 1.303, 73.225),
                        Vec3(14.009, 1.303, 80.817),
                        Vec3(13.441, 1.303, 93.140),
                    ],
                ),
                SeqInteract("Sapphire Key"),
                SeqMove(
                    name="Move to slot",
                    coords=[
                        Vec3(13.156, 1.303, 80.951),
                        Vec3(11.570, 1.303, 64.146),
                        Vec3(8.674, 1.303, 63.873),
                    ],
                ),
                SeqSelectOption("Place Sapphire Key", skip_dialog_check=True),
                SeqCombatAndMove(
                    name="Navigate water maze",
                    coords=[
                        Vec3(6.414, 1.303, 61.795),
                        Vec3(4.084, 1.303, 62.271),
                        Vec3(-26.913, 1.303, 94.066),
                        Vec3(-22.859, 1.303, 97.681),
                    ],
                ),
                SeqDelay("Wait", 0.7),
                SeqCombatAndMove(
                    name="Navigate water maze",
                    coords=[
                        Vec3(-23.645, 1.303, 97.867),
                        Vec3(-24.697, 1.303, 102.931),
                        Vec3(-20.898, 1.303, 108.235),
                        Vec3(-17.660, 1.303, 111.515),
                        Vec3(-17.134, 1.303, 118.142),
                        Vec3(2.101, 1.303, 138.048),
                        Vec3(5.703, 1.303, 129.874),
                        Vec3(10.148, 1.303, 127.798),
                        Vec3(17.531, 1.303, 127.151),
                        Vec3(20.928, 1.303, 129.472),
                        Vec3(20.959, 1.303, 134.865),
                        Vec3(17.626, 1.303, 140.475),
                        Vec3(-5.102, 1.303, 163.280),
                    ],
                ),
                SeqCombatAndMove(
                    name="Move to bell",
                    coords=[
                        Vec3(-5.628, 1.303, 173.090),
                        Vec3(-8.013, 1.303, 175.695),
                        Vec3(-8.925, 1.303, 179.404),
                        Vec3(-8.766, 1.303, 186.246),
                        Vec3(-14.254, 1.303, 191.446),
                    ],
                    recovery_path=SeqMove(
                        name="Return to path",
                        coords=[
                            Vec3(-8.805, 1.303, 186.843),
                        ],
                    ),
                ),
                SeqSelectOption("Ring bell", skip_dialog_check=True),
                SeqMove(
                    name="Move to Sapphire Key",
                    coords=[
                        Vec3(-25.629, 1.303, 191.307),
                    ],
                ),
                SeqInteract("Sapphire Key"),
                SeqCombatAndMove(
                    name="Move to slot",
                    coords=[
                        Vec3(-16.323, 1.303, 190.511),
                        Vec3(-9.281, 1.303, 187.140),
                        Vec3(-5.488, 1.303, 180.250),
                        Vec3(11.788, 1.303, 176.246),
                    ],
                ),
                SeqSelectOption("Place Sapphire Key", skip_dialog_check=True),
                SeqMove(
                    name="Cross waterway",
                    coords=[
                        Vec3(14.424, 1.303, 171.363),
                        Vec3(26.432, 1.303, 157.933),
                    ],
                ),
                SeqHoldDirectionDelay("Turn", joy_dir=Vec2(-1, -1), timeout_s=0.1),
                SeqInteract("Sapphire Ore"),
                SeqMove(
                    name="Move to bell",
                    coords=[
                        InteractMove(26.439, 1.303, 166.361),
                        Vec3(25.033, 1.303, 170.297),
                    ],
                ),
                SeqSelectOption("Ring bell", skip_dialog_check=True),
                SeqMove(
                    name="Enter tower",
                    coords=[
                        Vec3(26.106, 1.303, 167.506),
                        Vec3(26.106, 1.303, 162.503),
                        Vec3(23.841, 1.303, 162.789),
                        Vec3(9.689, 1.303, 174.963),
                        Vec3(0.862, 1.303, 181.930),
                        HoldDirection(261.583, 1.303, -6.600, joy_dir=Vec2(0, 1)),
                        Vec3(261.608, 1.303, 0.360),
                    ],
                ),
                SeqInteract("Turn wheel"),
                SeqMove(
                    name="Move to save branch",
                    coords=[
                        Vec3(262.855, 1.002, 2.046),
                        Vec3(261.274, 1.002, 6.941),
                        Vec3(261.462, 1.002, 20.499),
                    ],
                ),
            ],
        )


class FirstFloor(SeqList):
    """Routing of first floor of Tower of Antsudlo."""

    def __init__(self: Self) -> None:
        """Initialize a new FirstFloor object."""
        super().__init__(
            name="First Floor",
            children=[
                SeqMove(
                    name="Enter next room",
                    coords=[
                        Vec3(261.556, 1.002, 20.238),
                        HoldDirection(264.500, 1.002, 80.000, joy_dir=Vec2(0, 1)),
                    ],
                ),
                SeqCombatAndMove(
                    name="Enter right waterlock",
                    coords=[
                        Vec3(273.374, 1.002, 83.592),
                        Vec3(278.542, 1.002, 90.069),
                        Vec3(281.028, 1.002, 99.937),
                        Vec3(279.430, 1.002, 108.123),
                        Vec3(279.424, 1.002, 110.239),
                        HoldDirection(329.500, 1.002, 79.500, joy_dir=Vec2(1, 1)),
                        Vec3(334.967, 1.002, 84.574),
                        Vec3(338.789, 1.002, 86.191),
                    ],
                ),
                SeqInteract("Turn valve"),
                SeqMove(
                    name="Navigate to lever",
                    coords=[
                        Vec3(346.546, 1.002, 81.835),
                        Vec3(349.798, 1.002, 78.992),
                        HoldDirection(376.088, 7.002, 99.881, joy_dir=Vec2(1, -1)),
                        Vec3(381.602, 7.002, 100.608),
                        Vec3(384.367, 7.002, 100.608),
                        Vec3(388.072, 7.002, 98.281),
                        Graplou(398.253, 6.540, 99.082, joy_dir=Vec2(1, 0.5), hold_timer=0.1),
                        Vec3(398.916, 9.002, 99.744),
                        InteractMove(398.045, 12.002, 100.705),
                        Vec3(399.799, 12.002, 102.554),
                        InteractMove(400.889, 15.002, 101.180),
                        Vec3(402.267, 15.002, 100.091),
                        InteractMove(402.922, 18.002, 100.746),
                        Vec3(408.052, 18.002, 95.992),
                        InteractMove(407.707, 9.002, 94.646),
                        Vec3(405.835, 9.002, 92.722),
                    ],
                ),
                SeqInteract("Lever"),
                SeqMove(
                    name="Move to pearl",
                    coords=[
                        Vec3(404.268, 9.002, 93.622),
                        InteractMove(397.980, 4.803, 98.849),
                        InteractMove(398.830, 9.002, 99.830),
                        InteractMove(398.000, 12.002, 100.660),
                        Vec3(399.777, 12.002, 102.572),
                        InteractMove(400.989, 15.002, 101.329),
                        Vec3(401.931, 15.002, 100.062),
                        InteractMove(402.837, 18.002, 100.823),
                        Vec3(395.460, 18.002, 108.490),
                        InteractMove(394.823, 9.002, 107.529),
                        Vec3(393.595, 9.002, 106.023),
                    ],
                ),
                SeqInteract("Pick up pearl"),
                SeqCombatAndMove(
                    name="Leave right room",
                    coords=[
                        Vec3(392.225, 9.002, 105.422),
                        # TODO(orkaboy): Better routing
                        InteractMove(391.708, 1.002, 104.641),
                        Vec3(391.708, 1.002, 102.273),
                        Vec3(392.826, 1.002, 93.546),
                        Vec3(390.972, 1.002, 91.585),
                        # TODO(orkaboy): Better juking
                        Vec3(383.162, 1.002, 99.543),
                        InteractMove(383.042, 7.002, 100.467),
                        Vec3(375.954, 7.002, 100.467),
                        HoldDirection(348.500, 1.002, 79.500, joy_dir=Vec2(-1, 1)),
                        Vec3(343.144, 1.002, 84.729),
                        Vec3(339.349, 1.002, 86.153),
                    ],
                ),
                SeqInteract("Turn valve"),
                SeqMove(
                    name="Enter left waterlock",
                    coords=[
                        Vec3(332.023, 1.002, 82.644),
                        Vec3(328.463, 1.002, 79.025),
                        HoldDirection(279.447, 1.002, 110.406, joy_dir=Vec2(-1, -1)),
                        Vec3(270.544, 1.002, 105.343),
                        Vec3(267.248, 1.002, 104.118),
                        Vec3(261.660, 1.002, 104.118),
                        Vec3(251.677, 1.002, 108.733),
                        HoldDirection(215.167, 1.002, 79.444, joy_dir=Vec2(-1, 1)),
                        Vec3(211.700, 1.002, 82.662),
                        Vec3(204.964, 1.002, 86.020),
                    ],
                ),
                SeqInteract("Turn valve"),
                SeqMove(
                    name="Move to pearl",
                    coords=[
                        Vec3(198.050, 1.002, 81.719),
                        Vec3(194.382, 1.002, 77.987),
                        HoldDirection(165.888, 7.002, 103.069, joy_dir=Vec2(-1, -1)),
                        Vec3(160.310, 7.002, 106.638),
                        Vec3(156.209, 7.002, 106.638),
                        Graplou(148.257, 8.173, 104.592, joy_dir=Vec2(-1, 0), hold_timer=0.1),
                        HoldDirection(147.595, 12.002, 105.255, joy_dir=Vec2(0, 1)),
                        Vec3(146.080, 12.002, 106.336),
                    ],
                ),
                SeqInteract("Pick up pearl"),
                SeqMove(
                    name="Move to lever",
                    coords=[
                        Vec3(146.537, 12.002, 104.184),
                        # TODO(orkaboy): Better routing
                        InteractMove(147.247, 1.002, 103.596),
                        Vec3(150.027, 1.002, 104.690),
                        Vec3(151.058, 1.002, 106.210),
                    ],
                ),
                SeqInteract("Lever"),
                SeqMove(
                    name="Move to pedistal",
                    coords=[
                        Vec3(148.064, 1.002, 95.842),
                        Vec3(147.035, 1.002, 93.074),
                        Vec3(144.453, 1.002, 91.318),
                        Vec3(143.290, 1.002, 91.295),
                        Vec3(141.005, 1.002, 93.671),
                        Graplou(135.649, 1.990, 98.984, joy_dir=Vec2(-1, 1), hold_timer=0.1),
                        HoldDirection(134.986, 12.002, 99.646, joy_dir=Vec2(0, 1)),
                        Vec3(129.786, 12.002, 98.380),
                    ],
                ),
                SeqSelectOption("Place pearl", skip_dialog_check=True),
                SeqCombatAndMove(
                    name="Move to lever",
                    coords=[
                        Vec3(134.375, 12.002, 99.021),
                        # TODO(orkaboy): Better routing
                        InteractMove(134.871, 4.303, 98.036),
                        Vec3(142.660, 4.303, 90.953),
                        Vec3(149.909, 4.303, 89.040),
                        Vec3(153.351, 4.303, 90.058),
                        Vec3(158.110, 4.303, 94.243),
                        InteractMove(158.937, 7.002, 95.104),
                        Vec3(156.663, 7.001, 97.984),
                        Vec3(150.126, 7.001, 93.153),
                        Vec3(145.379, 7.001, 95.060),
                        Vec3(137.878, 7.010, 88.241),
                        Vec3(137.980, 7.010, 84.401),
                        Vec3(142.015, 7.002, 77.951),
                    ],
                ),
                SeqInteract("Lever"),
                SeqCombatAndMove(
                    name="Move to pearl",
                    coords=[
                        Vec3(126.870, 7.002, 92.893),
                        InteractMove(127.852, 12.002, 94.884),
                        Vec3(129.679, 12.002, 98.272),
                    ],
                ),
                SeqInteract("Pick up pearl"),
                SeqCombatAndMove(
                    name="Move to waterlock",
                    coords=[
                        Vec3(128.716, 12.002, 93.931),
                        InteractMove(128.015, 7.002, 93.334),
                        Vec3(128.015, 7.002, 91.917),
                        Vec3(136.362, 7.002, 88.661),
                        Vec3(141.947, 9.002, 92.557),
                        Vec3(145.611, 7.010, 95.809),
                        Vec3(150.097, 7.002, 93.412),
                        Vec3(156.021, 7.002, 97.307),
                        Vec3(166.647, 7.002, 103.586),
                        HoldDirection(194.667, 1.002, 79.333, joy_dir=Vec2(1, 1)),
                        Vec3(198.882, 1.002, 83.445),
                        Vec3(204.702, 1.002, 86.141),
                    ],
                ),
                SeqInteract("Turn valve"),
                SeqMove(
                    name="Move to left pedistal",
                    coords=[
                        Vec3(212.472, 1.002, 81.887),
                        Vec3(215.059, 1.002, 79.210),
                        HoldDirection(250.816, 1.002, 109.615, joy_dir=Vec2(1, -1)),
                        Vec3(258.674, 1.002, 105.810),
                        Vec3(261.889, 1.002, 104.404),
                        Vec3(263.955, 1.002, 105.748),
                        Vec3(263.955, 1.002, 107.924),
                        Vec3(261.936, 1.002, 111.054),
                    ],
                ),
                SeqSelectOption("Place pearl", skip_dialog_check=True),
                SeqMove(
                    name="Move to right pedistal",
                    coords=[
                        Vec3(266.962, 1.002, 111.054),
                    ],
                ),
                SeqSelectOption("Place pearl", skip_dialog_check=True),
                SeqMove(
                    name="Move to elevator",
                    coords=[
                        Vec3(264.595, 1.002, 111.054),
                    ],
                ),
                SeqInteract("Move to second floor"),
            ],
        )


class SecondFloor(SeqList):
    """Routing of Second Floor of Tower of Antsudlo."""

    def __init__(self: Self) -> None:
        """Initialize a new SecondFloor object."""
        super().__init__(
            name="Second Floor",
            children=[
                SeqMove(
                    name="Enter left room",
                    coords=[
                        Vec3(265.222, 14.303, 105.486),
                        Vec3(276.624, 14.303, 105.542),
                        Vec3(280.072, 14.303, 108.062),
                        InteractMove(279.004, 20.002, 108.875),
                        Vec3(279.721, 20.002, 110.666),
                        HoldDirection(318.000, 1.002, 155.000, joy_dir=Vec2(1, 1)),
                        Vec3(321.039, 1.002, 157.963),
                        Vec3(332.904, 1.002, 157.963),
                        Vec3(337.738, 1.002, 153.750),
                        HoldDirection(379.672, 7.002, 174.745, joy_dir=Vec2(1, -1)),
                    ],
                ),
                SeqMove(
                    name="Navigate to valve",
                    coords=[
                        Vec3(386.519, 7.002, 169.108),
                        Vec3(391.004, 7.002, 169.108),
                        Vec3(396.959, 7.002, 171.891),
                        Vec3(399.010, 7.002, 171.807),
                        Vec3(403.419, 7.002, 176.195),
                        Vec3(403.397, 7.002, 177.385),
                        Vec3(404.900, 7.002, 179.061),
                        Vec3(409.332, 7.002, 180.963),
                        InteractMove(421.318, 1.803, 185.330),
                        InteractMove(423.021, 12.002, 185.948),
                        Vec3(422.222, 12.002, 189.079),
                    ],
                ),
                SeqInteract("Turn valve"),
                SeqMove(
                    name="Navigate to valve",
                    coords=[
                        Vec3(420.441, 12.002, 190.792),
                        InteractMove(419.852, 7.002, 191.503),
                        Graplou(416.658, 7.886, 194.993, joy_dir=Vec2(-1, 1), hold_timer=0.1),
                        HoldDirection(415.995, 12.002, 195.655, joy_dir=Vec2(0, 1)),
                        Vec3(414.081, 12.002, 197.642),
                    ],
                ),
                SeqInteract("Turn valve"),
                SeqMove(
                    name="Move to chest",
                    coords=[
                        Vec3(415.432, 12.002, 195.079),
                        InteractMove(416.156, 7.002, 194.501),
                        Vec3(417.248, 7.002, 188.760),
                        InteractMove(412.908, 1.803, 177.565),
                        Vec3(399.777, 1.803, 164.847),
                        Vec3(396.594, 1.803, 162.961),
                        Vec3(394.734, 1.803, 163.092),
                        InteractMove(393.920, 7.002, 163.580),
                        Vec3(395.792, 7.002, 170.390),
                        Vec3(397.470, 7.002, 171.978),
                        Vec3(398.890, 7.002, 171.807),
                        Vec3(403.317, 7.002, 176.114),
                        # Divert to pick up armor
                        Vec3(403.317, 7.002, 177.473),
                        Vec3(404.896, 7.002, 179.026),
                        Vec3(408.832, 7.002, 179.479),
                        InteractMove(415.078, 7.002, 172.638),
                        Vec3(415.916, 7.002, 171.628),
                    ],
                ),
                SeqLoot(
                    "Thalassic Cloak",
                    item=ARMORS.ThalassicCloak,
                    equip_to=PlayerPartyCharacter.Serai,
                ),
                SeqMove(
                    name="Move to valve",
                    coords=[
                        Vec3(414.208, 7.002, 173.426),
                        InteractMove(407.801, 7.002, 180.212),
                        Vec3(404.409, 7.002, 183.758),
                        InteractMove(398.831, 7.002, 189.232),
                        Vec3(394.856, 7.002, 193.206),
                        InteractMove(394.273, 9.002, 193.934),
                        InteractMove(395.149, 12.002, 194.655),
                        Vec3(398.951, 12.002, 194.655),
                        InteractMove(401.227, 12.002, 196.783),
                        Vec3(403.417, 12.002, 198.909),
                    ],
                ),
                SeqInteract("Turn valve"),
                SeqMove(
                    name="Go to tumblers",
                    coords=[
                        Vec3(401.547, 12.002, 197.049),
                        InteractMove(396.506, 7.002, 191.846),
                        Vec3(399.243, 7.002, 188.893),
                        InteractMove(404.795, 7.002, 183.404),
                        Vec3(403.622, 7.002, 179.556),
                        Vec3(401.340, 7.002, 178.100),
                    ],
                ),
                SeqInteract("Raise tumbler"),
                SeqDelay("Wait", timeout_in_s=1.5),
                SeqInteract("Raise tumbler"),
                SeqMove(
                    name="Move to second tumbler",
                    coords=[
                        Vec3(399.598, 7.002, 176.381),
                    ],
                ),
                SeqInteract("Raise tumbler"),
                SeqMove(
                    name="Move to third tumbler",
                    coords=[
                        Vec3(398.060, 7.002, 174.191),
                    ],
                ),
                SeqInteract("Raise tumbler"),
                SeqDelay("Wait", timeout_in_s=1.5),
                SeqInteract("Raise tumbler"),
                SeqMove(
                    name="Move to pearl",
                    coords=[
                        Vec3(398.887, 7.002, 175.727),
                        Vec3(401.565, 7.002, 178.540),
                        Vec3(402.790, 7.002, 178.540),
                        Vec3(404.953, 7.002, 180.397),
                    ],
                ),
                SeqInteract("Pick up pearl"),
                SeqMove(
                    name="Leave right room",
                    coords=[
                        Vec3(402.178, 7.002, 178.442),
                        Vec3(401.411, 7.002, 178.442),
                        Vec3(396.629, 7.002, 173.638),
                        Vec3(396.629, 7.002, 172.222),
                        Vec3(395.100, 7.002, 170.454),
                        Vec3(390.917, 7.002, 168.630),
                        Vec3(386.969, 7.002, 168.607),
                        Vec3(379.418, 7.002, 174.137),
                        HoldDirection(336.417, 1.002, 154.278, joy_dir=Vec2(-1, 1)),
                    ],
                ),
                SeqMove(
                    name="Move to left room",
                    coords=[
                        Vec3(333.127, 1.002, 157.684),
                        Vec3(320.754, 1.002, 157.684),
                        Vec3(316.670, 1.002, 153.906),
                        HoldDirection(279.257, 20.002, 110.035, joy_dir=Vec2(-1, -1)),
                        Vec3(276.029, 20.002, 106.826),
                        Graplou(267.458, 20.002, 99.460, joy_dir=Vec2(-1, -1), hold_timer=0.1),
                        Graplou(257.995, 20.002, 100.651, joy_dir=Vec2(-1, 0), hold_timer=0.1),
                        Vec3(249.464, 20.002, 110.591),
                        HoldDirection(212.000, 1.002, 155.000, joy_dir=Vec2(-1, 1)),
                    ],
                ),
                SeqMove(
                    name="Move to raft",
                    coords=[
                        Vec3(209.513, 1.002, 157.901),
                        Vec3(196.640, 1.002, 157.901),
                        HoldDirection(167.000, 6.002, 203.500, joy_dir=Vec2(-1, -1)),
                        Vec3(162.782, 6.002, 203.500),
                        Vec3(158.866, 6.002, 208.956),
                        InteractMove(152.137, 4.309, 208.689),
                    ],
                ),
                SeqBracelet("Windtrap"),
                # TODO(orkaboy): All rafting sections have major issues completing
                SeqRaft(
                    name="Rafting",
                    coords=[
                        Vec3(154.755, 4.217, 201.854),
                        Vec3(151.602, 4.265, 199.206),
                        Vec3(143.653, 4.320, 198.966),
                        Vec3(140.325, 4.262, 191.733),
                        Vec3(143.158, 4.268, 183.648),
                        Vec3(148.888, 4.337, 182.980),
                    ],
                ),
                SeqMove(
                    name="Move to windtrap",
                    coords=[
                        Vec3(150.938, 4.383, 184.504),
                    ],
                ),
                SeqHoldDirectionDelay("Turn", joy_dir=Vec2(0, 1), timeout_s=0.1),
                SeqBracelet("Windtrap"),
                SeqRaft(
                    name="Rafting",
                    coords=[
                        Vec3(127.739, 4.318, 181.809),
                    ],
                ),
                SeqMove(
                    name="Move to windtrap",
                    coords=[
                        Vec3(125.515, 4.314, 184.051),
                    ],
                ),
                SeqHoldDirectionDelay("Turn", joy_dir=Vec2(0, 1), timeout_s=0.1),
                SeqBracelet("Windtrap"),
                SeqRaft(
                    name="Rafting",
                    coords=[
                        Vec3(130.288, 4.231, 182.169),
                        Vec3(132.909, 4.306, 188.800),
                        Vec3(134.912, 4.394, 208.540),
                        Vec3(140.693, 4.203, 209.077),
                        Vec3(141.561, 4.207, 212.921),
                    ],
                ),
                SeqMove(
                    name="Move closer",
                    coords=[
                        Vec3(144.118, 4.362, 214.818),
                    ],
                ),
                SeqHoldDirectionDelay("Turn", joy_dir=Vec2(0, -1), timeout_s=0.1),
                SeqBracelet("Nudge raft"),
                SeqMove(
                    name="Move to lever",
                    coords=[
                        InteractMove(144.112, 6.002, 217.467),
                        Vec3(146.545, 6.002, 218.449),
                        InteractMove(146.500, 11.002, 219.642),
                        Vec3(145.051, 11.002, 221.293),
                    ],
                ),
                SeqInteract("Lever"),
                SeqMove(
                    name="Move to raft",
                    coords=[
                        InteractMove(143.817, 4.329, 214.974),
                    ],
                ),
                SeqRaft(
                    name="Rafting",
                    coords=[
                        Vec3(143.489, 4.376, 210.041),
                        Vec3(135.881, 4.325, 208.410),
                    ],
                ),
                SeqMove(
                    name="Move to pearl",
                    coords=[
                        Vec3(136.243, 4.361, 209.126),
                        InteractMove(135.398, 7.002, 210.058),
                        Vec3(134.515, 7.002, 210.501),
                        InteractMove(134.515, 11.002, 213.334),
                        Vec3(134.515, 11.002, 219.244),
                    ],
                ),
                SeqInteract("Pick up pearl"),
                SeqMove(
                    name="Retrace steps",
                    coords=[
                        InteractMove(134.493, 1.002, 203.783),
                        Vec3(137.777, 1.002, 201.476),
                        Vec3(139.669, 1.002, 199.674),
                        Vec3(142.178, 1.002, 199.674),
                        Vec3(148.344, 1.002, 202.208),
                        Vec3(154.675, 1.002, 208.780),
                        Graplou(154.540, 2.466, 216.530, joy_dir=Vec2(0, 1), hold_timer=0.1),
                    ],
                ),
                SeqClimb(
                    name="Climb wall",
                    coords=[
                        Vec3(154.540, 7.540, 216.530),
                        Vec3(153.441, 7.540, 216.540),
                    ],
                ),
                SeqCliffMove(
                    name="Climb wall",
                    coords=[
                        InteractMove(153.320, 6.002, 215.654),
                    ],
                ),
                SeqMove(
                    name="Return to central chamber",
                    coords=[
                        HoldDirection(151.858, 6.002, 214.101, joy_dir=Vec2(0, -1)),
                        Graplou(162.513, 6.002, 205.779, joy_dir=Vec2(1, -1), hold_timer=0.1),
                        Vec3(162.513, 6.002, 204.087),
                        Vec3(167.463, 6.002, 203.539),
                        HoldDirection(193.583, 1.002, 154.556, joy_dir=Vec2(1, 1)),
                        Vec3(196.246, 1.002, 157.785),
                        Vec3(209.870, 1.002, 157.785),
                        Vec3(213.525, 1.002, 154.130),
                        HoldDirection(249.805, 20.002, 110.543, joy_dir=Vec2(1, -1)),
                    ],
                ),
                SeqMove(
                    name="Move to pedistal",
                    coords=[
                        Vec3(253.330, 20.002, 106.715),
                        Graplou(261.540, 20.002, 99.457, joy_dir=Vec2(1, -1), hold_timer=0.1),
                        # TODO(orkaboy): Fails to jump down, running against corner
                        InteractMove(264.922, 14.303, 106.790),
                        Vec3(261.348, 14.303, 111.029),
                    ],
                ),
                # Must wait until water level has stabilized to interact with pedistal
                SeqDelay("Wait", timeout_in_s=0.5),
                SeqHoldDirectionDelay("Turn", joy_dir=Vec2(0, 1), timeout_s=0.1),
                SeqSelectOption("Place pearl", skip_dialog_check=True),
                SeqMove(
                    name="Move to pedistal",
                    coords=[
                        Vec3(267.353, 14.303, 111.013),
                    ],
                ),
                SeqHoldDirectionDelay("Turn", joy_dir=Vec2(0, 1), timeout_s=0.1),
                SeqSelectOption("Place pearl", skip_dialog_check=True),
                SeqMove(
                    name="Move to elevator",
                    coords=[
                        Vec3(267.353, 14.303, 111.013),
                    ],
                ),
                SeqHoldDirectionDelay("Turn", joy_dir=Vec2(0, 1), timeout_s=0.1),
                SeqInteract("Move to third floor"),
            ],
        )


class ThirdFloor(SeqList):
    """Routing of third floor of Tower of Antsudlo."""

    def __init__(self: Self) -> None:
        """Initialize a new ThirdFloor object."""
        super().__init__(
            name="Third Floor",
            children=[
                SeqMove(
                    name="Enter left room",
                    coords=[
                        Vec3(263.745, 29.303, 105.342),
                        Vec3(257.141, 29.303, 105.323),
                        Vec3(253.459, 29.303, 106.547),
                        InteractMove(253.517, 35.002, 107.467),
                        Vec3(250.078, 35.002, 110.376),
                        HoldDirection(236.000, 1.002, 224.000, joy_dir=Vec2(-1, 1)),
                        Vec3(233.511, 1.002, 225.454),
                        Vec3(220.130, 1.002, 225.454),
                        HoldDirection(199.000, 7.002, 295.000, joy_dir=Vec2(-1, -1)),
                    ],
                ),
                # TODO(orkaboy): Continue routing
            ],
        )


class TowerOfAntsudlo(SeqList):
    """Routing of Tower of Antsudlo segment of Watcher Island."""

    def __init__(self: Self) -> None:
        """Initialize a new TowerOfAntsudlo object."""
        super().__init__(
            name="Tower of Antsudlo",
            children=[
                Seafloor(),
                SeqCheckpoint("antsudlo"),
                FirstFloor(),
                SecondFloor(),
                ThirdFloor(),
                # TODO(orkaboy): Continue routing
            ],
        )
