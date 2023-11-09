"""Routing of Cataclysm, the Vespertine and Mirth."""

import logging
from typing import Self

from engine.seq import SeqCheckpoint, SeqList
from route.cataclysm.brisk_destroyed import BriskDestroyed
from route.cataclysm.mirth import BriskRestored, Mirth
from route.cataclysm.sea_of_nightmare import SeaOfNightmare

logger = logging.getLogger(__name__)


class Cataclysm(SeqList):
    """Top-level routing of Cataclysm, from arrival at Brisk until Watcher Island."""

    def __init__(self: Self) -> None:
        """Initialize a new Cataclysm object."""
        super().__init__(
            name="Cataclysm",
            children=[
                BriskDestroyed(),
                SeaOfNightmare(),
                SeqCheckpoint("brisk5"),
                BriskRestored(),
                Mirth(),
            ],
        )
