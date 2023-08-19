import logging

from engine.mathlib import Vec3
from engine.seq import SeqList, SeqLog, SeqMove, SeqTurboMashUntilIdle

logger = logging.getLogger(__name__)


class DemoPlateau(SeqList):
    def __init__(self):
        super().__init__(
            name="Plateau",
            children=[
                SeqTurboMashUntilIdle(name="Wait for control"),
                SeqLog(name="SYSTEM", text="We have control!"),
                # TODO: Real movement, possibly using pathfinding graph
                SeqMove(
                    name="Move test",
                    coords=[
                        Vec3(-450, 1, -62),
                        Vec3(-457, 1, -60),
                        Vec3(-453, 1, -57),
                        Vec3(-447, 1, -64),
                    ],
                ),
                # TODO: Need to press A to jump off ledge
            ],
        )
