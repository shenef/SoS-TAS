"""Routing of the destroyed Brisk during the Cataclysm."""

import logging
from typing import Self

from engine.combat import SeqCombat, SeqCombatAndMove
from engine.mathlib import Vec2, Vec3
from engine.seq import (
    Graplou,
    HoldDirection,
    InteractMove,
    MistralBracelet,
    SeqBlockPuzzle,
    SeqBracelet,
    SeqCheckpoint,
    SeqGraplou,
    SeqHoldDirectionUntilLostControl,
    SeqInteract,
    SeqList,
    SeqMashUntilCombat,
    SeqMove,
    SeqSelectOption,
    SeqSkipUntilIdle,
)

logger = logging.getLogger(__name__)


class BriskDestroyed(SeqList):
    """Routing of the destroyed Brisk."""

    def __init__(self: Self) -> None:
        """Initialize a new BriskDestroyed object."""
        super().__init__(
            name="Brisk destroyed",
            children=[
                SeqMove(
                    name="Go to Yolande",
                    coords=[
                        Vec3(31.780, 1.002, 180.300),
                        Vec3(32.349, 1.002, 182.460),
                        Vec3(44.461, 1.002, 182.460),
                        Vec3(45.978, 1.002, 170.457),
                        HoldDirection(46.000, 9.034, 123.145, joy_dir=Vec2(0, -1)),
                        Vec3(44.741, 1.002, 113.578),
                        Vec3(39.638, 1.002, 113.466),
                        Vec3(32.341, 1.002, 118.699),
                        Vec3(26.524, 1.002, 118.721),
                    ],
                ),
                SeqInteract("Yolande"),
                # Somewhat suboptimal time-wise
                SeqMashUntilCombat("Heading to Brisk"),
                SeqCombat("Dweller minions"),
                SeqSkipUntilIdle("Seraï returns"),
                SeqCheckpoint("brisk3"),
                SeqMove(
                    name="Navigate Brisk",
                    coords=[
                        Vec3(49.408, 4.002, -19.644),
                        Vec3(79.540, 4.002, -19.644),
                        InteractMove(85.894, 3.002, -22.983),
                        Vec3(98.174, 2.525, -36.475),
                        Vec3(100.392, 2.525, -37.033),
                        Vec3(102.785, 2.525, -35.618),
                        Vec3(102.797, 3.010, -29.638),
                        Vec3(109.501, 3.010, -23.529),
                        HoldDirection(237.875, 1.002, -12.278, joy_dir=Vec2(1, 1)),
                        Vec3(237.875, 1.002, -2.175),
                        Vec3(228.486, 2.655, 7.136),
                        Graplou(228.296, 3.009, 8.428, joy_dir=Vec2(0, 1), hold_timer=0.1),
                        HoldDirection(110.503, 7.002, -12.533, joy_dir=Vec2(0, 1)),
                        Vec3(109.633, 7.002, -12.313),
                        Vec3(107.608, 7.002, -14.454),
                        Vec3(99.435, 8.002, -14.454),
                        InteractMove(99.468, 9.002, -12.493),
                        Graplou(97.927, 9.002, -4.345, joy_dir=Vec2(0, 1), hold_timer=0.1),
                        Vec3(89.918, 9.002, -4.097),
                        InteractMove(88.621, 11.002, -5.007),
                        Graplou(79.059, 11.002, -13.259, joy_dir=Vec2(-1, -1), hold_timer=0.1),
                        Vec3(68.854, 11.002, -8.624),
                        InteractMove(68.854, 8.002, -5.542),
                        Vec3(69.271, 8.002, -3.284),
                        Vec3(71.545, 8.002, -0.343),
                        InteractMove(74.457, 12.002, 0.477),
                        InteractMove(74.480, 14.002, 2.805),
                        Vec3(72.837, 14.002, 2.805),
                    ],
                ),
                SeqBracelet("Push block"),
                SeqMove(
                    name="Drop down",
                    coords=[
                        Vec3(68.460, 14.002, 2.527),
                        InteractMove(68.460, 8.002, 1.542),
                    ],
                ),
                SeqBlockPuzzle(
                    "Push block",
                    coords=[
                        Vec3(68.460, 8.002, 3.050),
                        MistralBracelet(joy_dir=Vec2(-1, 0)),
                        Vec3(64.530, 8.002, 1.338),
                        Vec3(63.579, 8.002, 1.338),
                        MistralBracelet(joy_dir=Vec2(0, 1)),
                        Vec3(63.255, 8.002, 8.936),
                    ],
                ),
                SeqCombatAndMove(
                    "Destroy Dweller minions",
                    coords=[
                        InteractMove(63.137, 13.002, 21.416),
                        Vec3(58.445, 13.002, 25.012),
                        Vec3(56.077, 13.002, 27.470),
                        Vec3(56.077, 13.002, 31.355),
                        Vec3(62.645, 13.002, 37.535),
                    ],
                ),
                SeqGraplou("Attack enemies", until_combat=True),
                SeqCombatAndMove(
                    name="Destroy Dweller minions",
                    coords=[
                        Vec3(73.453, 13.002, 39.949),
                    ],
                ),
                SeqHoldDirectionUntilLostControl("Move to cutscene", joy_dir=Vec2(1, 0)),
                SeqSkipUntilIdle("We need a boat"),
                SeqMove(
                    name="Go to Captain Klee'shaë",
                    coords=[
                        Vec3(63.451, 4.002, -17.553),
                    ],
                ),
                SeqSelectOption("Leave"),
            ],
        )
