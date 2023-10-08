"""Routing of Coral Cascades section of Sleeper Island."""

import logging
from typing import Self

from engine.combat import SeqCombatAndMove
from engine.mathlib import Vec2, Vec3
from engine.seq import (
    HoldDirection,
    InteractMove,
    SeqCheckpoint,
    SeqInteract,
    SeqList,
    SeqMove,
    SeqSkipUntilIdle,
)

logger = logging.getLogger(__name__)


class CoralCascadesToBrisk(SeqList):
    """Route from Coral Cascades to Brisk."""

    def __init__(self: Self) -> None:
        super().__init__(
            name="To Brisk",
            children=[
                SeqMove(
                    name="Move to Brisk",
                    coords=[
                        Vec3(132.000, 1.002, 147.000),
                        Vec3(132.000, 1.002, 147.500),
                        Vec3(132.500, 1.002, 147.500),
                        Vec3(132.500, 1.002, 149.000),
                        Vec3(133.000, 1.002, 149.000),
                        Vec3(133.000, 1.002, 150.000),
                        Vec3(133.500, 1.002, 150.000),
                        Vec3(133.500, 1.002, 151.500),
                        Vec3(135.000, 1.002, 151.500),
                    ],
                ),
                SeqInteract("Brisk"),
            ],
        )


class CoralCascades(SeqList):
    """Route from arrival at Coral Cascades until leaving."""

    # TODO(orkaboy): Movement through this entire segment is somewhat difficult due to the rapids.
    # TODO(orkaboy): Might need to decrease precision on some parts.
    def __init__(self: Self) -> None:
        super().__init__(
            name="Coral Cascades",
            children=[
                SeqMove(
                    name="Jump into water",
                    coords=[
                        Vec3(10.535, 22.002, 15.884),
                        Vec3(10.535, 22.002, 14.460),
                        InteractMove(10.535, -1.297, 13.542),
                    ],
                ),
                SeqCheckpoint("coral_cascades"),
                SeqCombatAndMove(
                    name="Navigate water",
                    coords=[
                        Vec3(18.461, -1.297, 6.995),
                        Vec3(18.348, -17.297, -2.051),
                        Vec3(25.789, -16.998, 0.943),
                        Vec3(32.311, -16.998, 2.819),
                        Vec3(41.456, -16.998, 2.819),
                        Vec3(47.805, -16.998, -2.090),
                    ],
                ),
                # TODO(orkaboy): There are some route options here.
                # TODO(orkaboy): Can go right for a Rainbow Conch
                SeqMove(
                    name="Center path",
                    coords=[
                        Vec3(46.116, -17.297, -9.958),
                        Vec3(46.116, -46.297, -24.641),
                    ],
                ),
                # TODO(orkaboy): Another potential branch
                SeqMove(
                    name="Move to chest",
                    coords=[
                        InteractMove(46.117, -43.998, -13.533),
                        Vec3(25.632, -43.998, -12.539),
                        Vec3(18.498, -43.998, -15.138),
                        Vec3(18.498, -43.998, -17.651),
                    ],
                ),
                SeqInteract("50 Gold"),
                SeqSkipUntilIdle("50 Gold"),
                SeqMove(
                    name="Rapids",
                    coords=[
                        Vec3(15.309, -43.998, -19.999),
                        InteractMove(14.382, -41.998, -21.042),
                        Vec3(15.448, -41.998, -22.543),
                        InteractMove(15.338, -47.025, -23.461),
                        HoldDirection(61.518, -73.301, -69.543, joy_dir=Vec2(1, -1)),
                    ],
                ),
                SeqCombatAndMove(
                    name="Navigate falls",
                    coords=[
                        Vec3(50.966, -73.297, -74.558),
                        Vec3(40.105, -72.998, -63.458),
                        InteractMove(40.105, -70.998, -62.531),
                        Vec3(35.460, -70.998, -62.531),
                        InteractMove(34.533, -68.998, -62.531),
                        Vec3(28.160, -68.998, -62.531),
                        InteractMove(27.128, -70.998, -63.775),
                        Vec3(25.483, -70.998, -63.775),
                        InteractMove(24.849, -72.998, -64.498),
                        Vec3(14.983, -73.297, -73.090),
                        HoldDirection(7.576, -85.297, -85.981, joy_dir=Vec2(-0.5, -1)),
                    ],
                ),
                SeqCombatAndMove(
                    name="Leave for world map",
                    coords=[
                        Vec3(15.423, -85.297, -91.432),
                        HoldDirection(18.378, -89.998, -96.483, joy_dir=Vec2(1, -1)),
                        Vec3(23.293, -89.998, -101.281),
                        InteractMove(25.467, -88.998, -101.281),
                        Vec3(30.690, -88.998, -96.323),
                        Vec3(43.714, -88.998, -96.323),
                        Vec3(48.019, -88.998, -92.496),
                        Vec3(57.559, -88.998, -92.496),
                        Vec3(60.573, -88.998, -94.193),
                        Vec3(72.704, -88.998, -94.193),
                        HoldDirection(130.500, 1.002, 146.998, joy_dir=Vec2(1, 0)),
                    ],
                ),
            ],
        )
