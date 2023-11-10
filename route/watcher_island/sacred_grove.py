"""Routing of Sacred Grove segment of Watcher Island."""

import logging
from typing import Self

from engine.mathlib import Vec3
from engine.seq import (
    SeqCheckpoint,
    SeqList,
    SeqMove,
)

logger = logging.getLogger(__name__)


class SacredGrove(SeqList):
    """Routing of Sacred Grove segment of Watcher Island."""

    def __init__(self: Self) -> None:
        """Initialize a new SacredGrove object."""
        super().__init__(
            name="Sacred Grove",
            children=[
                SeqCheckpoint(
                    "sacred_grove",
                    return_path=SeqMove(
                        name="Return to path",
                        coords=[
                            Vec3(5.940, 5.002, 14.295),
                            Vec3(10.550, 5.002, 9.684),
                        ],
                    ),
                ),
                # TODO(orkaboy): Continue routing
            ],
        )
