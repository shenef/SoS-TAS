import logging
from typing import Self

from engine.combat import SeqCombatAndMove
from engine.mathlib import Vec3
from engine.seq import (
    InteractMove,
    SeqAmulet,
    SeqClimb,
    SeqInteract,
    SeqList,
    SeqLog,
    SeqMove,
    SeqTurboMashUntilIdle,
)

logger = logging.getLogger(__name__)


class DemoPlateau(SeqList):
    def __init__(self: Self) -> None:
        super().__init__(
            name="X'tol's Landing",
            children=[
                SeqTurboMashUntilIdle(name="Wait for control"),
                SeqLog(name="SYSTEM", text="We have control!"),
                SeqMove(
                    name="Move to fight",
                    coords=[
                        InteractMove(-440.880, 0.002, -66.672),
                        InteractMove(-434.989, 1.002, -72.355),
                        Vec3(-435.754, -6.679, -85.519),
                        Vec3(-436.293, -6.998, -86.561),
                        InteractMove(-441.924, -14.998, -92.082),
                        Vec3(-426.310, -14.998, -98.160),
                    ],
                ),
                SeqAmulet(name="Do Amulet Sequence"),
                SeqClimb(
                    name="Slide down ladder",
                    coords=[
                        InteractMove(-425.293, -22.998, -98.917),
                    ],
                ),
                SeqCombatAndMove(
                    name="Move to ladder (AI combat)",
                    coords=[
                        Vec3(-416.966, -22.998, -96.962),
                    ],
                ),
                SeqClimb(
                    name="Climb wall",
                    coords=[
                        InteractMove(-417.050, -16.351, -96.470),
                        Vec3(-418.297, -14.450, -96.470),
                        Vec3(-418.202, -8.125, -96.470),
                        Vec3(-416.572, -7.998, -96.460),
                    ],
                ),
                SeqMove(
                    name="Ropes",
                    coords=[
                        Vec3(-416.704, -7.998, -98.546),
                        Vec3(-420.761, -7.998, -98.546),
                        Vec3(-425.442, -7.990, -94.944),
                        InteractMove(-450.087, -7.990, -119.570),
                        Vec3(-449.810, -7.998, -127.466),
                        InteractMove(-441.888, -16.998, -135.417),
                        Vec3(-434.682, -16.998, -131.155),
                        InteractMove(-419.919, -14.998, -116.391),
                    ],
                ),
                SeqInteract("Press pillar trigger"),
                SeqMove(
                    name="Leave plateau",
                    coords=[
                        Vec3(-407.820, -14.998, -129.990),
                        Vec3(-398.300, -14.990, -141.200),
                    ],
                ),
                SeqTurboMashUntilIdle(name="Wait for control"),
            ],
        )
