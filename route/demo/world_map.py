import logging
from typing import Self

from engine.mathlib import Vec3
from engine.seq import SeqInteract, SeqList, SeqMove

logger = logging.getLogger(__name__)


class DemoWorldBriskToTower(SeqList):
    def __init__(self: Self) -> None:
        super().__init__(
            name="World map",
            children=[
                SeqMove(
                    name="Move to wizard lab",
                    coords=[
                        Vec3(133.750, 1.002, 151.750),
                        Vec3(133.750, 1.002, 160.250),
                        Vec3(143.750, 1.002, 160.250),
                        Vec3(143.750, 1.002, 161.250),
                    ],
                ),
                SeqInteract("Enter wizard lab"),
            ],
        )
