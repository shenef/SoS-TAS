"""Routing of Stonemason's Outpost section of Sleeper Island."""

import logging
from typing import Self

from engine.mathlib import Vec3
from engine.seq import (
    InteractMove,
    SeqCheckpoint,
    SeqList,
    SeqMove,
)

logger = logging.getLogger(__name__)


class CoralCascades(SeqList):
    """Route from arrival at Coral Cascades until leaving."""

    def __init__(self: Self) -> None:
        super().__init__(
            name="Coral Cascades",
            children=[
                SeqMove(
                    name="Jump into water",
                    coords=[
                        Vec3(10.535, 22.002, 15.884),
                        Vec3(10.535, 22.002, 14.460),
                        InteractMove(10.535, -1.297, 13.542),
                    ],
                ),
                SeqCheckpoint("coral_cascades"),
                SeqMove(
                    name="Navigate water",
                    coords=[
                        Vec3(18.461, -1.297, 6.995),
                        # TODO(orkaboy): Continue routing
                    ],
                ),
            ],
        )
