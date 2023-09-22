import logging
from typing import Self

from engine.seq import (
    SeqCheckpoint,
    SeqList,
)
from route.evermist_island.final_trials import IntroFinalTrial
from route.evermist_island.forbidden_cave import IntroForbiddenCave
from route.evermist_island.mooncradle import IntroMooncradle, IntroZenithAcademy
from route.evermist_island.mountain_trail import IntroMountainTrail, MountainTrail

logger = logging.getLogger(__name__)


class EvermistIsland(SeqList):
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
            ],
        )
