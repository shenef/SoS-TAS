"""Routing of Docarri Village segment of Watcher Island."""

import logging
from typing import Self

from engine.mathlib import Vec3
from engine.seq import (
    InteractMove,
    SeqCheckpoint,
    SeqInteract,
    SeqList,
    SeqMove,
)

logger = logging.getLogger(__name__)


class DocarriVillage(SeqList):
    """Routing of Docarri Village segment of Watcher Island."""

    def __init__(self: Self) -> None:
        """Initialize a new DocarriVillage object."""
        super().__init__(
            name="Docarri Village",
            children=[
                SeqMove(
                    name="Overworld movement",
                    coords=[
                        Vec3(232.500, 3.002, 73.500),
                        Vec3(232.500, 3.002, 72.500),
                        Vec3(237.500, 3.002, 72.500),
                        Vec3(237.500, 3.002, 71.000),
                    ],
                ),
                SeqInteract("Lake Docarria"),
                SeqMove(
                    name="Swim to whirlpool",
                    coords=[
                        Vec3(53.433, 48.002, 81.845),
                        Vec3(47.994, 48.002, 76.294),
                        Vec3(43.052, 48.002, 74.917),
                        Vec3(40.816, 48.002, 73.454),
                        InteractMove(40.366, 40.803, 54.949),
                        Vec3(40.366, 40.803, 51.447),
                    ],
                ),
                SeqInteract("Whirlpool"),
                SeqCheckpoint("docarri_village"),
                SeqMove(
                    name="",
                    coords=[
                        Vec3(40.200, 37.002, -207.552),
                        # TODO(orkaboy): Continue routing
                    ],
                ),
                # TODO(orkaboy): Continue routing
            ],
        )
