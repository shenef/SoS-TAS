"""Routing of Haunted Mansion and Dweller of Woe section of Wraith Island."""

import logging
from typing import Self

from engine.inventory.items import VALUABLES
from engine.mathlib import Vec2, Vec3
from engine.seq import (
    HoldDirection,
    InteractMove,
    SeqCheckpoint,
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
                # TODO(orkaboy): Continue routing
            ],
        )
