"""Routing of Watcher Island."""

import logging
from typing import Self

from engine.mathlib import Vec3
from engine.seq import SeqBoat, SeqInteract, SeqList
from route.watcher_island.docarri_village import DocarriVillage
from route.watcher_island.jungle_path import JunglePath
from route.watcher_island.lake_docarria import LakeDocarria
from route.watcher_island.sacred_grove import SacredGrove

logger = logging.getLogger(__name__)


class GoToWatcherIsland(SeqList):
    """Route from Mirth to Watcher Island."""

    def __init__(self: Self) -> None:
        """Initialize a new GoToWatcherIsland object."""
        super().__init__(
            name="Go to Watcher Island",
            children=[
                SeqBoat(
                    name="Archives interlude",
                    coords=[
                        Vec3(232.992, 0.500, 182.667),
                    ],
                    hold_skip=True,
                ),
                SeqBoat(
                    name="Cross ocean",
                    coords=[
                        Vec3(220.561, 0.500, 80.364),
                        Vec3(220.625, 0.500, 68.486),
                        Vec3(231.171, 0.500, 59.927),
                        Vec3(236.277, 0.500, 56.823),
                    ],
                ),
                SeqInteract("Disembark"),
            ],
        )


class WatcherIsland(SeqList):
    """Top-level routing of Watcher Island, from leaving Mirth to defeat of Dweller of Torment."""

    def __init__(self: Self) -> None:
        """Initialize a new WatcherIsland object."""
        super().__init__(
            name="Watcher Island",
            children=[
                GoToWatcherIsland(),
                JunglePath(),
                LakeDocarria(),
                SacredGrove(),
                DocarriVillage(),
                # TODO(orkaboy): Continue routing
            ],
        )
