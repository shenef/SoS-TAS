"""Routing of Jungle Path segment of Watcher Island."""

import logging
from typing import Self

from engine.mathlib import Vec3
from engine.seq import SeqCheckpoint, SeqInteract, SeqList, SeqMove, SeqSkipUntilIdle

logger = logging.getLogger(__name__)


class JunglePath(SeqList):
    """Routing of Jungle Path segment of Watcher Island."""

    def __init__(self: Self) -> None:
        """Initialize a new JunglePath object."""
        super().__init__(
            name="Jungle Path",
            children=[
                SeqMove(
                    name="Move to jungle path",
                    coords=[
                        Vec3(237.500, 1.002, 60.500),
                    ],
                ),
                SeqInteract("Enter jungle path"),
                SeqSkipUntilIdle("Cutscene"),
                SeqCheckpoint("jungle_path"),
                # TODO(orkaboy): Continue routing
            ],
        )
