import logging
from typing import Self

from engine.seq import SeqCheckpoint, SeqList
from route.sleeper_island.moorlands import Moorlands
from route.sleeper_island.xtols_landing import XtolsLanding

logger = logging.getLogger(__name__)


class SleeperIsland(SeqList):
    def __init__(self: Self) -> None:
        super().__init__(
            name="Sleeper Island",
            children=[
                XtolsLanding(),
                SeqCheckpoint("moorlands"),
                Moorlands(),
            ],
        )
