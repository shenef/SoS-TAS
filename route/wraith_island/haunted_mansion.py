"""Routing of Haunted Mansion and Dweller of Woe section of Wraith Island."""

import logging
from typing import Self

from engine.combat import SeqCombatAndMove
from engine.inventory.items import VALUABLES
from engine.mathlib import Vec2, Vec3
from engine.seq import (
    HoldDirection,
    InteractMove,
    SeqCheckpoint,
    SeqGraplou,
    SeqHoldDirectionUntilLostControl,
    SeqInteract,
    SeqList,
    SeqLoot,
    SeqMove,
    SeqRouteBranch,
    SeqSelectOption,
    SeqSkipUntilIdle,
)

logger = logging.getLogger(__name__)


class HeadToMansion(SeqList):
    """Routing of path to get to Haunted Mansion."""

    def __init__(self: Self) -> None:
        """Initialize a new HeadToMansion object."""
        super().__init__(
            name="Head to Mansion",
            children=[
                SeqMove(
                    name="Move to Moraine",
                    coords=[
                        Vec3(35.837, 1.002, 116.869),
                    ],
                ),
                SeqSelectOption("Leave"),
                SeqSkipUntilIdle("The Eclipse begins", hold_cancel=True),
            ],
        )


class RightWing(SeqList):
    """Routing of path through right wing of Haunted Mansion."""

    def __init__(self: Self) -> None:
        """Initialize a new RightWing object."""
        super().__init__(
            name="Right Wing",
            children=[
                # Optionally, grab a chest
                SeqRouteBranch(
                    name="Loot Obsidian Ingot",
                    route=["hm_obsidian_ingot"],
                    when_true=SeqList(
                        name="Secret passage",
                        children=[
                            SeqMove(
                                name="Move to Chandelier",
                                coords=[
                                    Vec3(15.128, 6.010, -11.378),
                                    Vec3(21.481, 6.010, -1.679),
                                ],
                            ),
                            SeqInteract("Chandelier"),
                            SeqMove(
                                name="Move to secret passage",
                                coords=[
                                    Vec3(20.594, 6.002, -0.456),
                                ],
                            ),
                            SeqSelectOption("Secret passage"),
                            SeqMove(
                                name="Move to chest",
                                coords=[
                                    Vec3(26.429, 10.002, -13.152),
                                ],
                            ),
                            SeqLoot(name="Obsidian Ingot", item=VALUABLES.ObsidianIngot),
                            SeqMove(
                                name="Return to path",
                                coords=[
                                    InteractMove(27.126, 1.002, -15.461),
                                ],
                            ),
                        ],
                    ),
                    when_false=SeqMove(
                        name="Move to door",
                        coords=[
                            Vec3(18.681, 1.002, -23.964),
                            Vec3(28.002, 1.002, -14.479),
                        ],
                    ),
                ),
                SeqMove(
                    name="Go into right wing",
                    coords=[
                        Vec3(28.002, 1.002, -11.902),
                        HoldDirection(70.000, 1.002, 21.000, joy_dir=Vec2(0, 1)),
                    ],
                ),
                SeqHoldDirectionUntilLostControl("Move to cutscene", joy_dir=Vec2(0, 1)),
                SeqSkipUntilIdle("Seraï joins"),
                SeqMove(
                    name="",
                    coords=[
                        Vec3(70.100, 1.002, 46.028),
                        HoldDirection(104.000, 1.002, 84.000, joy_dir=Vec2(1, 1)),
                        Vec3(115.930, 1.002, 89.426),
                        Vec3(116.472, 1.002, 92.592),
                    ],
                ),
                SeqCheckpoint("haunted_mansion"),
                # TODO(orkaboy): Better juking
                SeqCombatAndMove(
                    name="Juke enemies",
                    coords=[
                        Vec3(123.076, 1.002, 93.144),
                        Vec3(127.318, 1.002, 88.936),
                        Vec3(132.178, 1.002, 88.534),
                        Vec3(134.416, 1.002, 93.443),
                        HoldDirection(168.167, 1.002, 86.056, joy_dir=Vec2(1, 1)),
                    ],
                ),
                # TODO(orkaboy): Better juking
                SeqCombatAndMove(
                    name="Move to torch",
                    coords=[
                        Vec3(171.051, 1.002, 88.876),
                        Vec3(171.122, 1.002, 97.983),
                        Vec3(176.290, 1.002, 103.029),
                        Vec3(176.334, 1.002, 104.540),
                    ],
                ),
                SeqInteract("Torch"),
                SeqCombatAndMove(
                    name="Move to secret passage",
                    coords=[
                        Vec3(176.638, 1.002, 103.043),
                        Vec3(181.923, 1.002, 103.043),
                        Vec3(181.923, 1.002, 104.540),
                    ],
                ),
                SeqInteract("Secret passage"),
                SeqMove(
                    name="Move to lever",
                    coords=[
                        Vec3(0.959, 10.002, -13.000),
                    ],
                ),
                SeqInteract("Lever"),
                SeqMove(
                    name="Move to left wing",
                    coords=[
                        Vec3(1.491, 10.002, -14.266),
                        InteractMove(1.500, 1.002, -16.253),
                        Vec3(0.050, 1.002, -16.253),
                        Vec3(0.050, 1.002, -11.751),
                        HoldDirection(-36.000, 1.002, 22.200, joy_dir=Vec2(0, 1)),
                    ],
                ),
            ],
        )


class MakeMeASandwich(SeqList):
    """Routing of sandwich-making section of Haunted Mansion."""

    def __init__(self: Self) -> None:
        """Initialize a new MakeMeASandwich object."""
        super().__init__(
            name="Make me a sandwich",
            children=[
                SeqInteract("Talk to ghost"),
                SeqSkipUntilIdle("I crave sandwich"),
                SeqMove(
                    name="Move into kitchen",
                    coords=[
                        Vec3(-65.648, 1.002, 100.037),
                        HoldDirection(-100.000, 1.002, 85.000, joy_dir=Vec2(-1, 1)),
                    ],
                ),
                SeqHoldDirectionUntilLostControl("Move to cutscene", joy_dir=Vec2(-1, 1)),
                SeqSkipUntilIdle("I'll just wait here"),
                SeqMove(
                    name="Move to rust",
                    coords=[
                        Vec3(-98.458, 1.002, 91.533),
                    ],
                ),
                SeqSelectOption("Rust", option=0),
                SeqMove(
                    name="Move to Loaf of Dread",
                    coords=[
                        Vec3(-100.291, 1.002, 91.533),
                        Vec3(-104.024, 1.002, 94.699),
                        Vec3(-104.024, 1.002, 96.540),
                    ],
                ),
                SeqSelectOption("Loaf of Dread", option=1),
                SeqMove(
                    name="Move to sugar",
                    coords=[
                        Vec3(-105.546, 1.002, 92.470),
                    ],
                ),
                SeqSelectOption("Sugar", option=2),
                SeqMove(
                    name="Move to dust",
                    coords=[
                        Vec3(-105.546, 1.002, 90.911),
                        Vec3(-108.200, 1.002, 89.457),
                        Vec3(-110.094, 1.002, 89.889),
                        Vec3(-110.522, 1.002, 90.350),
                    ],
                ),
                SeqSelectOption("Dust", option=3),
                SeqMove(
                    name="Move to Hepar",
                    coords=[
                        Vec3(-106.271, 1.002, 83.458),
                    ],
                ),
                SeqSelectOption("Hepar", option=1),
                SeqMove(
                    name="Move to cook",
                    coords=[
                        Vec3(-102.284, 1.002, 93.717),
                    ],
                ),
                SeqSelectOption("Let him cook"),
                SeqSkipUntilIdle("Let him cook"),
                SeqMove(
                    name="Move to ghost",
                    coords=[
                        Vec3(-100.463, 1.002, 85.880),
                        HoldDirection(-64.777, 1.002, 99.649, joy_dir=Vec2(1, -1)),
                        Vec3(-56.938, 1.002, 100.669),
                    ],
                ),
                SeqSelectOption("Here's your sandwich"),
                SeqSkipUntilIdle("Nom nom nom"),
            ],
        )


class LeftWing(SeqList):
    """Routing of path through left wing of Haunted Mansion."""

    def __init__(self: Self) -> None:
        """Initialize a new LeftWing object."""
        super().__init__(
            name="Left Wing",
            children=[
                SeqMove(
                    name="Move to left wing",
                    coords=[
                        Vec3(-36.000, 1.002, 45.686),
                        HoldDirection(-47.971, 1.002, 85.971, joy_dir=Vec2(-1, 1)),
                    ],
                ),
                SeqGraplou(),
                SeqCombatAndMove(
                    name="Move to ghost",
                    coords=[
                        Vec3(-62.443, 1.002, 92.936),
                        Vec3(-62.443, 1.002, 97.423),
                        Vec3(-57.241, 1.002, 100.993),
                    ],
                ),
                MakeMeASandwich(),
                SeqMove(
                    name="Move to library",
                    coords=[
                        Vec3(-54.052, 1.002, 101.767),
                        HoldDirection(-62.917, 1.002, 130.364, joy_dir=Vec2(0, 1)),
                        Vec3(-62.917, 1.002, 133.265),
                        Vec3(-48.665, 1.002, 152.629),
                        HoldDirection(-63.958, 1.002, 186.600, joy_dir=Vec2(0, 1)),
                    ],
                ),
                # TODO(orkaboy): Continue routing
            ],
        )


class HauntedMansion(SeqList):
    """Routing of Haunted Mansion."""

    def __init__(self: Self) -> None:
        """Initialize a new HauntedMansion object."""
        super().__init__(
            name="Haunted Mansion",
            children=[
                HeadToMansion(),
                RightWing(),
                LeftWing(),
                # TODO(orkaboy): Continue routing
            ],
        )
