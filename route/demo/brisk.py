import logging

from engine.mathlib import Vec3
from engine.seq import SeqList, SeqLog, SeqMove, SeqTurboMashUntilIdle

logger = logging.getLogger(__name__)


class DemoBrisk(SeqList):
    def __init__(self):
        super().__init__(
            name="Brisk",
            children=[
                SeqLog(name="SYSTEM", text="We have control!"),
                SeqMove(
                    name="Move to pirates",
                    coords=[
                        Vec3(237.037, 1.000, 1.596),
                        Vec3(226.352, 3.004, 9.454),
                    ],
                ),
                # Armwrestle
                SeqTurboMashUntilIdle(name="Arm wrestling!!!"),
                # TODO: Go and save? Checkpoint at least
                SeqMove(
                    name="Move outside",
                    coords=[
                        Vec3(227.916, 3.000, 11.749),
                        Vec3(227.916, 3.007, 8.114),
                        Vec3(237.656, 1.002, 1.956),
                        Vec3(241.342, 1.002, -3.151),
                        Vec3(241.355, 1.002, -9.044),
                        Vec3(237.866, 1.002, -12.564),
                    ],
                ),
                # TODO: Leave tavern
                # TODO: Leave town
            ],
        )
