"""Routing of Haunted Mansion and Dweller of Woe section of Wraith Island."""

import logging
from typing import Self

from engine.mathlib import Vec3
from engine.seq import (
    SeqList,
    SeqMove,
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


class HauntedMansion(SeqList):
    """Routing of Haunted Mansion."""

    def __init__(self: Self) -> None:
        """Initialize a new HauntedMansion object."""
        super().__init__(
            name="Haunted Mansion",
            children=[
                HeadToMansion(),
                # TODO(orkaboy): Continue routing
            ],
        )
