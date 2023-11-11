"""Routing of Jungle Path segment of Watcher Island."""

import logging
from typing import Self

from engine.combat import SeqCombat, SeqCombatAndMove
from engine.mathlib import Vec2, Vec3
from engine.seq import (
    Graplou,
    HoldDirection,
    InteractMove,
    SeqCheckpoint,
    SeqHoldDirectionUntilLostControl,
    SeqInteract,
    SeqList,
    SeqMove,
    SeqSkipUntilCombat,
    SeqSkipUntilIdle,
)

logger = logging.getLogger(__name__)


class JunglePath(SeqList):
    """Routing of Jungle Path segment of Watcher Island."""

    def __init__(self: Self) -> None:
        """Initialize a new JunglePath object."""
        super().__init__(
            name="Jungle Path",
            children=[
                SeqMove(
                    name="Move to jungle path",
                    coords=[
                        Vec3(237.500, 1.002, 60.500),
                    ],
                ),
                SeqInteract("Enter jungle path"),
                SeqSkipUntilIdle("Cutscene"),
                SeqCheckpoint("jungle_path"),
                SeqCombatAndMove(
                    name="Move to lever",
                    coords=[
                        Vec3(37.102, 9.002, -226.176),
                        Vec3(50.114, 9.002, -212.863),
                        Vec3(52.992, 9.002, -207.681),
                        InteractMove(53.989, 7.002, -198.533),
                        Vec3(60.992, 7.324, -191.866),
                        Vec3(61.708, 9.001, -189.554),
                        Vec3(61.453, 9.001, -173.468),
                        Vec3(61.453, 9.001, -151.746),
                        Vec3(48.457, 9.001, -148.761),
                        InteractMove(37.729, 4.703, -153.542),
                        InteractMove(37.611, 7.002, -154.472),
                        Vec3(31.671, 7.002, -154.413),
                        Vec3(30.807, 9.002, -144.436),
                        Vec3(27.261, 11.002, -144.436),
                        Vec3(27.261, 11.002, -146.919),
                        Vec3(29.034, 11.002, -154.008),
                        Vec3(29.034, 10.010, -163.834),
                        Vec3(27.893, 10.002, -166.110),
                        Vec3(25.925, 10.002, -166.110),
                        InteractMove(25.850, 15.002, -164.300),
                        Vec3(24.368, 15.002, -162.301),
                    ],
                ),
                SeqInteract("Lever"),
                SeqMove(
                    name="Navigate to wall",
                    coords=[
                        Vec3(26.546, 15.002, -162.210),
                        InteractMove(27.464, 10.002, -162.210),
                        Vec3(29.074, 11.007, -160.725),
                        Vec3(28.336, 11.007, -153.150),
                        Vec3(25.835, 11.002, -151.462),
                        InteractMove(13.021, 11.002, -151.462),
                        Vec3(11.494, 11.002, -154.607),
                        Vec3(7.113, 10.002, -154.607),
                        Vec3(-6.398, 10.002, -146.454),
                        InteractMove(-6.387, 8.002, -138.460),
                        Vec3(-3.789, 8.002, -135.862),
                        InteractMove(-3.197, 10.002, -135.142),
                        Vec3(-2.454, 10.002, -134.100),
                        InteractMove(-3.109, 12.002, -133.445),
                        Vec3(-2.433, 12.010, -131.219),
                        Vec3(4.537, 10.010, -128.680),
                        Vec3(18.932, 10.002, -115.236),
                        Vec3(27.718, 10.002, -106.410),
                        Vec3(32.229, 10.002, -99.880),
                        InteractMove(33.576, 12.002, -99.411),
                        Vec3(39.540, 15.002, -99.455),
                        InteractMove(40.801, 4.703, -117.154),
                        InteractMove(39.531, 7.002, -116.247),
                        Vec3(38.222, 7.002, -114.457),
                        InteractMove(38.222, 10.002, -111.416),
                        Vec3(44.328, 10.002, -110.459),
                        Vec3(47.603, 10.002, -107.423),
                        Graplou(53.660, 10.929, -98.470, joy_dir=Vec2(1, 1), hold_timer=0.1),
                    ],
                ),
                SeqMove(
                    name="Navigate to save branch",
                    coords=[
                        Vec3(53.701, 23.002, -96.625),
                        InteractMove(52.636, 24.002, -94.242),
                        Vec3(46.645, 24.002, -84.018),
                        Vec3(40.607, 26.002, -81.278),
                        Vec3(39.348, 26.002, -73.009),
                        InteractMove(39.348, 31.002, -54.247),
                        Vec3(40.105, 31.002, -49.116),
                    ],
                ),
                SeqCheckpoint("jungle_path2"),
                SeqMove(
                    name="Navigate islands",
                    coords=[
                        Vec3(42.684, 31.002, -44.331),
                        InteractMove(45.538, 31.002, -41.831),
                        Vec3(45.538, 31.002, -37.041),
                        InteractMove(40.784, 31.002, -32.384),
                        InteractMove(36.540, 31.002, -32.384),
                        Vec3(35.234, 31.002, -29.815),
                        InteractMove(35.234, 31.002, -24.335),
                        Vec3(35.445, 31.002, -18.549),
                        Graplou(46.000, 31.007, -7.750, joy_dir=Vec2(1, 1), hold_timer=0.1),
                        InteractMove(50.471, 30.002, -14.204),
                        Vec3(51.963, 30.002, -14.204),
                        Vec3(51.963, 30.002, -5.550),
                        InteractMove(51.963, 31.002, -3.300),
                    ],
                ),
                SeqHoldDirectionUntilLostControl("Move to cutscene", joy_dir=Vec2(-0.5, 1)),
                SeqSkipUntilCombat("One and Three"),
                # TODO(orkaboy): There's a bug here. Once one of the enemies go down to 0,
                #                so does the other, but the TAS won't target it correctly.
                SeqCombat("One and Three"),
                SeqSkipUntilIdle("Retreat"),
                SeqMove(
                    name="Leave Jungle Path",
                    coords=[
                        InteractMove(34.656, 33.002, 13.427),
                        HoldDirection(237.500, 3.002, 64.998, joy_dir=Vec2(0, 1)),
                    ],
                ),
                SeqMove(
                    name="Navigate to Lake Docarria",
                    coords=[
                        Vec3(237.500, 3.002, 68.500),
                    ],
                ),
                SeqInteract("Lake Docarria"),
            ],
        )
