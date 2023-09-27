import logging
from typing import Self

from engine.mathlib import Vec3
from engine.seq import (
    SeqList,
    SeqMove,
)

logger = logging.getLogger(__name__)


class Moorlands(SeqList):
    def __init__(self: Self) -> None:
        super().__init__(
            name="Moorlands",
            children=[
                SeqMove(
                    name="WIP Move",  # TODO(orkaboy): Continue routing
                    coords=[
                        Vec3(16.785, 3.002, 10.436),
                    ],
                ),
            ],
        )
