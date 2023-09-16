import logging
from typing import Self

from engine.mathlib import Vec2, Vec3
from engine.seq import (
    SeqCheckpoint,
    SeqHoldDirectionUntilClose,
    SeqList,
    SeqLog,
    SeqMove,
    SeqSkipUntilIdle,
)

logger = logging.getLogger(__name__)


class DemoBrisk(SeqList):
    def __init__(self: Self) -> None:
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
                SeqSkipUntilIdle(name="Arm wrestling!!!"),
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
                SeqHoldDirectionUntilClose(
                    name="Leave tavern",
                    target=Vec3(109.384, 3.002, -23.672),
                    joy_dir=Vec2(-1, -1),
                ),
                # Move to the save point
                SeqMove(
                    name="Move to save point",
                    coords=[
                        Vec3(103.120, 3.002, -29.640),
                        Vec3(86.787, 4.002, -17.680),
                        Vec3(73.078, 4.002, -20.183),
                        Vec3(49.560, 4.002, -18.947),
                    ],
                ),
                # Checkpoint: Brisk
                SeqCheckpoint(checkpoint_name="brisk"),
                # Leave town
                SeqMove(
                    name="Leave town",
                    coords=[
                        Vec3(40.665, 4.002, -16.496),
                        Vec3(16.387, 4.002, 6.839),
                        Vec3(11.540, 4.002, 9.433),
                        Vec3(11.540, 4.002, 21.027),
                        Vec3(3.395, 4.002, 29.848),
                        Vec3(-1.318, 4.002, 54.476),
                    ],
                ),
                SeqHoldDirectionUntilClose(
                    name="Leave Brisk",
                    target=Vec3(134.750, 1.010, 151.750),
                    joy_dir=Vec2(-1, 1),
                ),
            ],
        )
