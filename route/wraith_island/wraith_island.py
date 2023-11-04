"""Routing of Wraith Island."""

import logging
from typing import Self

from engine.seq import SeqCheckpoint, SeqList, SeqSkipUntilIdle
from route.wraith_island.brisk_destroyed import BriskDestroyed
from route.wraith_island.cursed_woods import CursedWoods
from route.wraith_island.docks import WraithIslandDocks
from route.wraith_island.haunted_mansion import HauntedMansion
from route.wraith_island.lucent import LucentArrival
from route.wraith_island.necromancers_lair import (
    FloodedGraveyard,
    FloodedGraveyardLeave,
    NecromancersLair,
)

logger = logging.getLogger(__name__)


class WraithIsland(SeqList):
    """Top-level routing of Wraith Island, from arrival to returning to Brisk."""

    def __init__(self: Self) -> None:
        """Initialize a new WraithIsland object."""
        super().__init__(
            name="Wraith Island",
            children=[
                WraithIslandDocks(),
                LucentArrival(),
                CursedWoods(),
                FloodedGraveyard(),
                NecromancersLair(),
                FloodedGraveyardLeave(),
                SeqSkipUntilIdle("A soul restored"),
                SeqCheckpoint("lucent"),
                HauntedMansion(),
                BriskDestroyed(),
            ],
        )
