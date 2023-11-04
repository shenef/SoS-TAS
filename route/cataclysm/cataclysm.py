"""Routing of Cataclysm, the Vespertine and Mirth."""

import logging
from typing import Self

from engine.seq import SeqList
from route.cataclysm.brisk_destroyed import BriskDestroyed
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
                # TODO(orkaboy): Continue routing
            ],
        )
