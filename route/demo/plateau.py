import logging

from engine.combat import SeqCombatManual
from engine.mathlib import Vec3
from engine.seq import Jump, SeqClimb, SeqList, SeqLog, SeqMove, SeqTurboMashUntilIdle

logger = logging.getLogger(__name__)


class DemoPlateau(SeqList):
    def __init__(self):
        super().__init__(
            name="X'tol's Landing",
            children=[
                SeqTurboMashUntilIdle(name="Wait for control"),
                SeqLog(name="SYSTEM", text="We have control!"),
                SeqMove(
                    name="Move to fight",
                    coords=[
                        Vec3(-445.225, 1.000, -65.075),
                        Jump(),
                        Vec3(-437.325, 0.002, -69.175),
                        Jump(),
                        Vec3(-435.018, 1.019, -73.979),
                        Vec3(-435.754, -6.679, -85.519),
                        Vec3(-436.293, -6.998, -86.561),
                        Jump(),
                        Vec3(-439.192, -9.998, -89.658),
                        Jump(),
                        Vec3(-440.181, -11.998, -90.668),
                        Jump(),
                        Vec3(-441.096, -14.998, -96.372),
                        Vec3(-428.889, -14.998, -108.743),
                        Jump(),
                    ],
                ),
                # TODO: Manual Fight here
                SeqCombatManual(
                    name="Move to ladder (MANUAL combat)",
                    coords=[
                        Vec3(-417.303, -22.998, -97.066),
                        Jump(),
                    ],
                ),
                SeqClimb(
                    name="Climb wall",
                    coords=[
                        Vec3(-417.050, -16.351, -96.470),
                        Vec3(-418.297, -14.450, -96.470),
                        Vec3(-418.202, -8.125, -96.470),
                        Vec3(-416.452, -7.998, -96.470),
                        Jump(),
                    ],
                ),
                SeqMove(
                    name="Ropes",
                    coords=[
                        Vec3(-416.704, -7.998, -98.546),
                        Vec3(-420.761, -7.998, -98.546),
                        Vec3(-425.442, -7.990, -94.944),
                        Vec3(-450.087, -7.990, -119.570),
                        Vec3(-450.087, -7.990, -126.429),
                        Vec3(-448.740, -7.998, -128.591),
                        Jump(),
                        Vec3(-446.455, -9.998, -130.304),
                        Jump(),
                        Vec3(-444.894, -11.998, -131.744),
                        Jump(),
                        Vec3(-443.018, -14.998, -133.867),
                        Jump(),
                        Vec3(-436.437, -16.998, -132.847),
                        Vec3(-433.136, -16.998, -130.010),
                        Jump(),
                        Vec3(-426.227, -16.998, -122.919),
                        Jump(),
                        Vec3(-423.225, -16.998, -120.039),
                        Jump(),
                        Vec3(-419.982, -14.998, -116.633),
                        Jump(),  # Actually activate bridges
                        Vec3(-407.820, -14.998, -129.990),
                        Vec3(-398.300, -14.990, -141.200),
                    ],
                ),
                SeqTurboMashUntilIdle(name="Wait for control"),
            ],
        )
