"""Routing of Autumn Hills segment of Mesa Island."""

import logging
from typing import Self

from engine.combat import SeqCombatAndMove
from engine.inventory.items import ARMORS
from engine.mathlib import Vec2, Vec3
from engine.seq import (
    Graplou,
    HoldDirection,
    InteractMove,
    MistralBracelet,
    SeqBraceletPuzzle,
    SeqChangeTimeOfDay,
    SeqCheckpoint,
    SeqCliffMove,
    SeqClimb,
    SeqGraplou,
    SeqHoldDirectionDelay,
    SeqInteract,
    SeqList,
    SeqLoot,
    SeqMove,
)
from memory.player_party_manager import PlayerPartyCharacter

logger = logging.getLogger(__name__)


class AutumnHills(SeqList):
    """Routing of Autumn Hills segment of Mesa Island."""

    def __init__(self: Self) -> None:
        """Initialize a new AutumnHills object."""
        super().__init__(
            name="Autumn Hills",
            children=[
                SeqMove(
                    name="Move to save branch",
                    coords=[
                        Vec3(4.066, 7.001, 10.900),
                    ],
                ),
                SeqCheckpoint("autumn_hills"),
                SeqCombatAndMove(
                    name="Move to chest",
                    coords=[
                        Vec3(8.585, 7.002, 12.500),
                        InteractMove(15.693, 9.002, 10.825),
                        Vec3(17.277, 9.002, 11.077),
                        InteractMove(18.521, 12.002, 12.526),
                        Graplou(33.250, 12.010, 12.466, joy_dir=Vec2(1, 0), hold_timer=0.1),
                        InteractMove(36.481, 12.195, 12.291),
                        Vec3(43.513, 12.002, 6.665),
                        Vec3(49.983, 12.002, 3.945),
                        InteractMove(50.678, 7.002, 3.030),
                        Vec3(57.425, 7.002, 1.586),
                        Vec3(62.981, 7.002, 1.541),
                        Vec3(64.257, 7.002, 0.696),
                        Vec3(67.925, 7.002, 0.547),
                        Vec3(73.799, 7.002, 2.812),
                    ],
                ),
                SeqLoot(
                    "Oaken Armor", item=ARMORS.OakenArmor, equip_to=PlayerPartyCharacter.Valere
                ),
                SeqCombatAndMove(
                    name="Navigate hills",
                    coords=[
                        Vec3(67.539, 7.002, 0.475),
                        Vec3(64.389, 7.002, 0.475),
                        Vec3(62.452, 7.002, 1.730),
                        Vec3(57.810, 7.002, 1.434),
                        Graplou(51.658, 7.552, 3.993, joy_dir=Vec2(-1, 0), hold_timer=0.1),
                        HoldDirection(50.995, 12.002, 4.655, joy_dir=Vec2(0, 1)),
                        Vec3(54.510, 12.002, 10.418),
                        InteractMove(56.158, 13.002, 10.418),
                        Vec3(58.428, 13.002, 12.543),
                        InteractMove(58.428, 16.002, 14.120),
                        Vec3(60.622, 16.002, 14.324),
                        InteractMove(68.531, 16.002, 14.500),
                        Vec3(69.555, 16.002, 13.457),
                        InteractMove(69.548, 13.002, 12.539),
                        Vec3(75.003, 13.002, 10.135),
                        Vec3(84.153, 13.002, 3.797),
                        InteractMove(85.151, 10.002, 3.498),
                        Vec3(89.217, 10.002, 2.863),
                        InteractMove(90.511, 7.002, 2.863),
                        Vec3(95.236, 7.002, 5.370),
                        Vec3(100.202, 7.002, 5.054),
                        Vec3(104.425, 7.002, 2.472),
                        Vec3(107.175, 7.002, 2.472),
                        InteractMove(109.021, 9.002, 3.355),
                        Vec3(112.283, 9.002, 4.222),
                        Vec3(116.936, 9.002, 4.222),
                        Graplou(126.342, 8.100, 5.993, joy_dir=Vec2(1, 0), hold_timer=0.1),
                    ],
                ),
                SeqMove(
                    name="Move to puzzle",
                    coords=[
                        HoldDirection(127.005, 11.002, 6.655, joy_dir=Vec2(0, 1)),
                        Graplou(134.342, 11.450, 6.993, joy_dir=Vec2(1, 0), hold_timer=0.1),
                        HoldDirection(135.005, 14.002, 7.655, joy_dir=Vec2(0, 1)),
                        Graplou(143.317, 13.450, 8.019, joy_dir=Vec2(1, 0), hold_timer=0.1),
                        HoldDirection(143.979, 16.002, 8.681, joy_dir=Vec2(0, 1)),
                        Vec3(146.540, 16.002, 9.463),
                        InteractMove(150.641, 16.193, 9.543),
                        Vec3(154.540, 16.010, 6.455),
                        InteractMove(156.416, 13.002, 6.455),
                        InteractMove(156.416, 7.002, 4.542),
                        Vec3(158.425, 7.002, 2.116),
                        Vec3(161.349, 7.002, 2.116),
                        Vec3(166.545, 7.002, 3.794),
                        InteractMove(167.472, 10.002, 3.794),
                    ],
                ),
                SeqBraceletPuzzle(
                    name="Blow leaves",
                    coords=[
                        Vec3(170.519, 10.002, 5.643),
                        MistralBracelet(joy_dir=Vec2(0, 1)),
                    ],
                ),
                SeqChangeTimeOfDay("Lower right rune", time_target=16.2),
                SeqBraceletPuzzle(
                    name="Blow leaves",
                    coords=[
                        Vec3(171.131, 10.002, 4.702),
                        Vec3(173.924, 10.002, 4.702),
                        Vec3(175.330, 10.002, 5.779),
                        # TODO(orkaboy): Eats up input
                        MistralBracelet(joy_dir=Vec2(0, 1)),
                    ],
                ),
                SeqChangeTimeOfDay("Upper right rune", time_target=22.2),
                SeqMove(
                    name="Move to lever",
                    coords=[
                        Vec3(175.512, 10.002, 3.260),
                    ],
                ),
                SeqInteract("Lever"),
                SeqMove(
                    name="Move into position",
                    coords=[
                        Vec3(175.512, 10.002, 8.294),
                    ],
                ),
                SeqChangeTimeOfDay("Upper left rune", time_target=4.7),
                SeqMove(
                    name="Move to scroll",
                    coords=[
                        Vec3(178.295, 10.002, 12.872),
                    ],
                ),
                SeqLoot("Arcane Moons"),
                SeqMove(
                    name="Jump to platform",
                    coords=[
                        Vec3(178.511, 10.002, 8.361),
                        Vec3(179.543, 10.002, 7.291),
                        InteractMove(181.960, 10.002, 7.291),
                        Vec3(182.680, 10.002, 7.740),
                    ],
                ),
                SeqInteract("Lever"),
                SeqCombatAndMove(
                    name="Move to cavern",
                    coords=[
                        Vec3(190.046, 10.002, 6.460),
                        InteractMove(192.481, 10.002, 6.460),
                        Vec3(197.480, 10.002, 2.386),
                        Vec3(205.440, 10.002, 2.386),
                        Vec3(207.002, 10.002, 5.626),
                        HoldDirection(303.000, 10.002, 13.000, joy_dir=Vec2(1, 1)),
                    ],
                ),
                SeqMove(
                    name="Move to shop",
                    coords=[
                        Vec3(304.295, 10.002, 13.000),
                        Vec3(310.382, 10.002, 13.000),
                        InteractMove(311.458, 0.002, 13.000),
                        Vec3(312.947, 0.002, 15.696),
                    ],
                ),
                # TODO(orkaboy): Shopping
                SeqMove(
                    name="Leave cavern",
                    coords=[
                        Vec3(313.938, 0.002, 9.792),
                        Graplou(316.816, 0.670, 9.520, joy_dir=Vec2(1, 0), hold_timer=0.1),
                        HoldDirection(317.478, 10.002, 10.182, joy_dir=Vec2(0, 1)),
                        Graplou(320.460, 10.587, 16.530, joy_dir=Vec2(0.5, 1), hold_timer=0.1),
                        Vec3(320.559, 10.002, 15.454),
                        Vec3(322.546, 10.002, 15.811),
                        InteractMove(323.464, 0.002, 15.811),
                        Vec3(324.889, 0.002, 12.192),
                        Vec3(326.493, 0.002, 10.557),
                        Vec3(330.967, 0.002, 9.763),
                        HoldDirection(432.223, 4.002, 9.549, joy_dir=Vec2(1, -1)),
                    ],
                ),
                SeqMove(
                    name="Graplou across tree stumps",
                    coords=[
                        Vec3(441.373, 4.002, 12.633),
                        InteractMove(442.200, 6.002, 13.460),
                        Vec3(444.546, 6.002, 13.950),
                        InteractMove(448.340, 6.002, 13.950),
                        Graplou(467.000, 6.010, 14.048, joy_dir=Vec2(1, 0), hold_timer=0.1),
                        Graplou(479.000, 6.010, 3.195, joy_dir=Vec2(1, -1), hold_timer=0.1),
                        Vec3(478.571, 6.002, 2.735),
                    ],
                ),
                SeqInteract("Lower ladder"),
                SeqMove(
                    name="Move to lower level",
                    coords=[
                        Vec3(477.683, 6.002, 5.291),
                        Graplou(476.730, 1.010, 15.245, joy_dir=Vec2(0, 1), hold_timer=0.1),
                        Vec3(475.231, 1.002, 14.648),
                        Vec3(475.231, 1.002, 13.081),
                    ],
                ),
                SeqBraceletPuzzle(
                    name="Push block",
                    coords=[
                        MistralBracelet(joy_dir=Vec2(1, 0)),
                        Vec3(484.518, 1.002, 14.715),
                        Vec3(485.893, 1.002, 14.715),
                        MistralBracelet(joy_dir=Vec2(0, -1)),
                        Vec3(480.784, 1.010, 1.367),
                        Vec3(478.492, 1.002, 1.367),
                    ],
                ),
                SeqMove(
                    name="Climb trees",
                    coords=[
                        InteractMove(478.500, 6.002, 3.691),
                        Graplou(493.000, 6.010, 4.421, joy_dir=Vec2(1, 0), hold_timer=0.1),
                        Vec3(501.466, 6.002, 9.795),
                        Vec3(509.338, 6.002, 9.795),
                        Vec3(513.540, 6.002, 6.356),
                        InteractMove(514.920, 7.002, 6.356),
                        Vec3(515.274, 7.002, 5.386),
                        Vec3(516.574, 7.002, 5.386),
                        InteractMove(516.546, 11.002, 7.467),
                        Vec3(515.460, 11.002, 7.467),
                        Vec3(515.460, 11.002, 6.592),
                        Vec3(513.479, 11.002, 4.457),
                        Graplou(508.882, 11.550, 4.218, joy_dir=Vec2(-1, 0), hold_timer=0.1),
                    ],
                ),
                SeqClimb(
                    name="Climb wall",
                    coords=[
                        Vec3(508.563, 15.535, 3.898),
                        Vec3(505.251, 15.535, 4.084),
                    ],
                ),
                SeqMove(
                    name="Climb trees",
                    coords=[
                        Vec3(505.210, 14.002, 3.460),
                        Vec3(503.240, 14.002, 5.525),
                        Vec3(502.322, 14.002, 5.525),
                        Vec3(501.459, 14.002, 6.443),
                        Graplou(501.471, 14.585, 10.530, joy_dir=Vec2(0, 1), hold_timer=0.1),
                    ],
                ),
                SeqClimb(
                    name="Climb wall",
                    coords=[
                        Vec3(501.471, 16.981, 10.530),
                        Vec3(501.485, 24.050, 10.530),
                        Vec3(502.859, 23.906, 11.208),
                    ],
                ),
                SeqInteract("Jump off wall"),
                SeqCliffMove(
                    name="Cross rope",
                    coords=[
                        InteractMove(504.011, 22.800, 10.500),
                        InteractMove(510.874, 23.002, 10.542),
                    ],
                ),
                SeqMove(
                    name="",
                    coords=[
                        Vec3(511.546, 23.002, 11.965),
                        InteractMove(512.464, 19.002, 11.965),
                        Vec3(513.543, 19.002, 10.642),
                        Vec3(513.543, 19.002, 9.509),
                        Vec3(514.546, 19.002, 8.557),
                        Vec3(514.647, 19.002, 7.000),
                        Vec3(516.335, 19.002, 5.457),
                        Vec3(517.540, 19.002, 5.457),
                        Graplou(517.491, 19.560, 8.530, joy_dir=Vec2(0, 1), hold_timer=0.1),
                    ],
                ),
                SeqClimb(
                    name="",
                    coords=[
                        Vec3(517.491, 22.540, 8.540),
                        Vec3(519.007, 22.540, 9.342),
                    ],
                ),
                SeqInteract("Jump off wall"),
                SeqMove(
                    name="Move to next area",
                    coords=[
                        Vec3(523.540, 22.002, 9.462),
                        InteractMove(524.458, 16.002, 9.462),
                        Vec3(531.885, 16.002, 12.488),
                        HoldDirection(626.272, -2.998, 4.304, joy_dir=Vec2(1, 1)),
                        Vec3(638.540, -2.998, 7.723),
                        InteractMove(639.467, -0.998, 7.723),
                        Vec3(651.859, -0.998, 5.500),
                        Vec3(655.544, -0.998, 5.500),
                        InteractMove(655.589, 1.002, 7.467),
                        Vec3(655.806, 1.002, 9.159),
                        InteractMove(655.400, 3.002, 10.065),
                    ],
                ),
                SeqHoldDirectionDelay("Turn", joy_dir=Vec2(-1, 1), timeout_s=0.1),
                SeqGraplou("Attack enemy", until_combat=True),
                SeqCombatAndMove(
                    name="Fight enemies",
                    coords=[
                        Vec3(668.540, 3.002, 10.859),
                        InteractMove(674.743, -1.998, 10.859),
                        Vec3(682.546, -1.998, 13.248),
                        InteractMove(683.961, -6.197, 15.422),
                        Vec3(686.410, -6.197, 15.707),
                    ],
                ),
                SeqInteract("Whirlpool"),
                SeqMove(
                    name="Underwater passage 1",
                    coords=[
                        Vec3(699.561, -113.697, -65.139),
                        Vec3(703.261, -113.697, -65.152),
                        Vec3(705.371, -113.697, -63.906),
                    ],
                ),
                SeqInteract("Whirlpool"),
                SeqMove(
                    name="Navigate cliffs",
                    coords=[
                        Vec3(704.542, -101.197, -63.188),
                        InteractMove(705.469, -98.998, -63.188),
                        InteractMove(706.114, -96.998, -62.136),
                        InteractMove(709.458, -96.998, -62.136),
                        Vec3(710.355, -96.998, -61.999),
                        InteractMove(711.612, -99.998, -63.341),
                        Vec3(713.801, -99.998, -63.927),
                        Vec3(720.370, -99.998, -64.016),
                        InteractMove(720.716, -96.998, -63.052),
                        InteractMove(724.458, -95.998, -63.052),
                        Vec3(725.588, -95.998, -62.765),
                        InteractMove(726.325, -101.838, -63.327),
                        Vec3(727.417, -101.697, -63.892),
                    ],
                ),
                SeqInteract("Whirlpool"),
                SeqMove(
                    name="Underwater passage 2",
                    coords=[
                        Vec3(732.401, -113.697, -63.500),
                    ],
                ),
                SeqInteract("Whirlpool"),
                SeqMove(
                    name="Underwater passage 3",
                    coords=[
                        Vec3(723.369, -82.697, -65.854),
                        Vec3(719.469, -82.697, -65.861),
                        Vec3(716.453, -82.697, -64.586),
                        Vec3(691.356, -82.697, -63.921),
                    ],
                ),
                SeqInteract("Whirlpool"),
                SeqCombatAndMove(
                    name="Avoid enemies",
                    coords=[
                        Vec3(701.510, -6.197, 15.843),
                        InteractMove(702.843, -1.998, 16.363),
                        Vec3(713.372, -1.808, 9.066),
                        Vec3(714.543, -1.808, 8.420),
                        InteractMove(718.073, -1.998, 8.420),
                        Vec3(722.546, -1.998, 8.096),
                        InteractMove(723.961, -4.697, 8.087),
                        Vec3(727.576, -4.697, 4.586),
                        Vec3(738.365, -4.697, 4.543),
                        Vec3(740.089, -4.697, 6.470),
                        Vec3(739.451, -4.697, 10.914),
                        InteractMove(738.524, -1.998, 10.546),
                        InteractMove(738.524, 0.002, 11.473),
                        Vec3(739.540, 0.002, 11.473),
                        InteractMove(742.481, 0.002, 11.473),
                        Vec3(744.540, 0.002, 9.696),
                        InteractMove(747.481, 0.002, 9.696),
                        Vec3(755.394, -1.998, 9.696),
                        Vec3(761.250, -1.998, 8.150),
                        Vec3(764.268, -1.998, 8.150),
                        Graplou(766.540, -1.409, 11.530, joy_dir=Vec2(1, 1), hold_timer=0.1),
                    ],
                ),
                SeqClimb(
                    name="Climb wall",
                    coords=[
                        Vec3(766.540, 9.540, 11.540),
                        Vec3(765.104, 9.540, 12.245),
                    ],
                ),
                SeqInteract("Get off wall"),
                SeqMove(
                    name="Enter cavern",
                    coords=[
                        Vec3(763.460, 9.002, 12.238),
                        Vec3(763.460, 9.002, 11.460),
                        InteractMove(763.460, 5.002, 10.542),
                        Graplou(777.000, 5.010, 9.000, joy_dir=Vec2(1, 0), hold_timer=0.1),
                        Graplou(778.214, 5.450, 10.121, joy_dir=Vec2(1, 0.5), hold_timer=0.1),
                        HoldDirection(778.892, 8.002, 10.768, joy_dir=Vec2(0, 1)),
                        Vec3(784.993, 8.002, 12.044),
                        HoldDirection(878.750, -10.998, 4.750, joy_dir=Vec2(1, 1)),
                    ],
                ),
                # TODO(orkaboy): Continue routing
            ],
        )
