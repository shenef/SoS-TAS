"""Routing of Evermist Island (start of the game)."""

import logging
from typing import Self

from engine.seq import (
    SeqCheckpoint,
    SeqList,
)
from route.evermist_island.elder_mist import ElderMistTrials
from route.evermist_island.final_trials import IntroFinalTrial
from route.evermist_island.forbidden_cave import IntroForbiddenCave
from route.evermist_island.mooncradle import IntroMooncradle, IntroZenithAcademy
from route.evermist_island.mountain_trail import IntroMountainTrail, MountainTrail

logger = logging.getLogger(__name__)


class EvermistIsland(SeqList):
    """Top level Evermist Island. Route from beginning of game to being thrown to Sleeper Island."""

    def __init__(self: Self) -> None:
        super().__init__(
            name="Evermist Island",
            children=[
                IntroMountainTrail(),
                IntroMooncradle(),
                SeqCheckpoint("intro_dorms"),
                IntroZenithAcademy(),
                IntroFinalTrial(),
                SeqCheckpoint("forbidden_cave"),
                IntroForbiddenCave(),
                MountainTrail(),
                ElderMistTrials(),
            ],
        )
