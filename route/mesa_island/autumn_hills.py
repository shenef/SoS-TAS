"""Routing of Autumn Hills segment of Mesa Island."""

import logging
from typing import Self

from engine.mathlib import Vec3
from engine.seq import (
    SeqCheckpoint,
    SeqList,
    SeqMove,
)

logger = logging.getLogger(__name__)


class AutumnHills(SeqList):
    """Routing of Autumn Hills segment of Mesa Island."""

    def __init__(self: Self) -> None:
        """Initialize a new AutumnHills object."""
        super().__init__(
            name="Autumn Hills",
            children=[
                SeqMove(
                    name="Move to save branch",
                    coords=[
                        Vec3(4.066, 7.001, 10.900),
                    ],
                ),
                SeqCheckpoint("autumn_hills"),
                # TODO(orkaboy): Equip Resh'an?
                # TODO(orkaboy): Continue routing
            ],
        )
