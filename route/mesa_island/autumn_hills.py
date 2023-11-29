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
    SeqCheckpoint,
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
                        InteractMove(37.072, 12.193, 12.466),
                        Vec3(39.069, 12.193, 11.857),
                        Vec3(45.614, 12.002, 5.510),
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
                        Vec3(145.658, 16.002, 9.667),
                        # TODO(orkaboy): Can jump off this tree ledge which causes desync
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
                # TODO(orkaboy): Continue routing
            ],
        )
