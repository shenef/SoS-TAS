import logging

from engine.mathlib import Vec3
from engine.seq import InteractMove, SeqList, SeqMove

logger = logging.getLogger(__name__)


class DemoWorldBriskToTower(SeqList):
    def __init__(self):
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
                        # TODO: Doesn't work?
                        InteractMove(143.750, 1.002, 161.250),
                    ],
                ),
            ],
        )
