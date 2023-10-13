"""Routing of Final Trial section of Evermist Island."""

import logging
from typing import Self

from engine.combat import SeqCombat, SeqCombatAndMove
from engine.mathlib import Vec2, Vec3
from engine.seq import (
    HoldDirection,
    InteractMove,
    SeqAmulet,
    SeqClimb,
    SeqHoldDirectionUntilCombat,
    SeqInteract,
    SeqList,
    SeqMashUntilIdle,
    SeqMove,
    SeqRouteBranch,
    SeqSkipUntilClose,
    SeqSkipUntilCombat,
)

logger = logging.getLogger(__name__)


class IntroFinalTrial(SeqList):
    """
    The Final Trials of young Solstice Warriors.

    Route from the entrance of the trial grounds, beating the Wyrd boss and
    leaving for the Forbidden Cave.
    """

    def __init__(self: Self) -> None:
        """Initialize a new IntroFinalTrial object."""
        super().__init__(
            name="Final trials",
            children=[
                SeqMove(
                    name="Move to ladder",
                    coords=[
                        InteractMove(33.059, -12.998, -345.326),
                        Vec3(37.050, -12.998, -344.937),
                        Vec3(42.429, -12.998, -350.327),
                        Vec3(43.500, -12.998, -349.470),
                    ],
                ),
                SeqClimb(
                    name="Climb ladder",
                    coords=[
                        InteractMove(43.500, -7.998, -348.533),
                    ],
                ),
                SeqMove(
                    name="Move near lever",
                    coords=[
                        Vec3(41.925, -7.998, -344.613),
                        Vec3(40.825, -7.998, -338.668),
                    ],
                ),
                SeqMove(
                    name="Move to lever",
                    coords=[
                        Vec3(37.852, -7.998, -334.758),
                    ],
                    precision=0.1,
                ),
                SeqInteract("Lever"),
                SeqMove(
                    name="Move to chest",
                    coords=[
                        Vec3(41.031, -7.998, -338.552),
                        Vec3(40.723, -7.998, -340.119),
                        InteractMove(24.618, -7.998, -340.119),
                        Vec3(24.618, -7.998, -334.883),
                    ],
                ),
                SeqInteract("Chest"),
                SeqMashUntilIdle("Chest"),
                SeqMove(
                    name="Move to brazier",
                    coords=[
                        Vec3(24.567, -7.998, -340.309),
                        InteractMove(41.214, -7.998, -340.309),
                        Vec3(41.550, -7.998, -334.885),
                    ],
                ),
                SeqInteract("Brazier"),
                SeqMashUntilIdle("Brazier"),
                SeqMove(
                    name="Jump into pit",
                    coords=[
                        Vec3(37.523, -7.998, -335.876),
                        InteractMove(36.012, -12.998, -335.664),
                    ],
                ),
                SeqHoldDirectionUntilCombat(
                    name="Attack enemies",
                    joy_dir=Vec2(0, -1),
                    mash_confirm=True,
                ),
                SeqCombatAndMove(
                    name="Fight enemies",
                    coords=[
                        Vec3(32.868, -12.998, -336.460),
                    ],
                ),
                SeqClimb(
                    name="Climb wall",
                    coords=[
                        InteractMove(32.868, -10.140, -336.470),
                        Vec3(32.881, -2.998, -335.533),
                    ],
                ),
                SeqMove(
                    name="Jump gaps",
                    coords=[
                        Vec3(32.453, -2.998, -323.957),
                        InteractMove(32.453, -2.998, -316.460),
                        InteractMove(35.481, -2.998, -316.460),
                        InteractMove(35.540, -2.998, -313.519),
                        InteractMove(38.415, -2.998, -313.519),
                        InteractMove(38.452, -2.998, -309.460),
                        InteractMove(43.540, -2.998, -309.454),
                        InteractMove(43.540, -2.998, -304.052),
                    ],
                ),
                SeqMove(
                    name="Move to chest",
                    coords=[
                        Vec3(39.416, -2.998, -302.099),
                        InteractMove(32.931, -2.995, -308.069),
                        Vec3(24.997, -2.998, -301.194),
                        Vec3(24.997, -2.998, -296.224),
                    ],
                ),
                SeqInteract("Chest"),
                SeqMashUntilIdle("Chest"),
                SeqCombatAndMove(
                    name="Move to brazier",
                    coords=[
                        Vec3(24.954, -2.998, -301.107),
                        InteractMove(31.489, -2.998, -308.173),
                        Vec3(32.657, -2.998, -308.173),
                        InteractMove(39.358, -2.998, -301.492),
                        Vec3(41.340, -2.998, -297.060),
                    ],
                ),
                SeqInteract("Brazier"),
                SeqMashUntilIdle("Brazier"),
                SeqMove(
                    name="Move to platform",
                    coords=[
                        Vec3(39.415, -2.998, -297.149),
                        Vec3(32.923, -2.998, -292.023),
                    ],
                ),
                SeqInteract("Elevator"),
                SeqMashUntilIdle("Erlina and Brugaves"),
                SeqMove(
                    name="Move to pillar",
                    coords=[
                        Vec3(81.996, -9.998, -195.727),
                    ],
                ),
                SeqInteract("Pillar"),
                SeqSkipUntilCombat("Wyrd"),
                SeqCombat("Wyrd"),
                SeqMashUntilIdle("Wyrd cutscene"),
                SeqMove(
                    name="Leave dungeon",
                    coords=[
                        Vec3(82.074, -9.998, -198.437),
                        HoldDirection(33.000, 4.002, -128.083, joy_dir=Vec2(0, -1)),
                    ],
                ),
                # Jumping into a cutscene here
                SeqMove(
                    name="Leave dungeon",
                    precision=2.0,
                    coords=[
                        InteractMove(33.000, -6.990, -130.200),
                    ],
                ),
                # Detect entering world map
                SeqSkipUntilClose("Leaving home", coord=Vec3(109.500, 2.002, 61.698)),
                # Activate storytelling amulet
                SeqRouteBranch(
                    name="Storytelling Amulet",
                    when_true=SeqAmulet("Activate Amulet"),
                    route=["amulet"],
                ),
                SeqMove(
                    name="Move to Forbidden Cave",
                    coords=[
                        Vec3(109.500, 2.002, 64.000),
                        Vec3(108.000, 2.002, 64.000),
                        Vec3(108.000, 2.002, 66.500),
                    ],
                ),
                SeqInteract("Forbidden Cave"),
            ],
        )
