import logging

from engine.mathlib import Vec2, Vec3
from engine.seq import (
    SeqCheckpoint,
    SeqHoldDirectionUntilClose,
    SeqList,
    SeqLog,
    SeqMove,
    SeqTurboMashUntilIdle,
)

logger = logging.getLogger(__name__)


class DemoWizardLab(SeqList):
    def __init__(self):
        super().__init__(
            name="Wizard Lab",
            children=[
                SeqLog(name="SYSTEM", text="We have arrived at the tower!"),
                SeqMove(
                    name="Move to cutscene",
                    coords=[
                        Vec3(14.300, 1.010, -72.600),
                    ],
                ),
                # Cutscene
                SeqTurboMashUntilIdle(name="Making a door"),
                SeqMove(
                    name="Move to entrance",
                    coords=[
                        Vec3(22.317, 1.002, -70.433),
                    ],
                ),
                SeqHoldDirectionUntilClose(
                    name="Go inside tower",
                    target=Vec3(8.000, 1.002, -13.399),
                    joy_dir=Vec2(0, 1),
                ),
                SeqMove(
                    name="Move to cutscene",
                    coords=[
                        Vec3(4.424, 1.002, -11.310),
                        Vec3(3.040, 1.005, 9.869),
                    ],
                ),
                # Cutscene
                SeqTurboMashUntilIdle(name="Pirate leaves"),
                # TODO: Push block with bracelet
                # Checkpoint: Brisk
                SeqCheckpoint(checkpoint_name="wizard_lab1"),
                # TODO: Climb up above archway
                # TODO: Pick up green crystal
                # TODO: Go down to altar and go to right pedistal
                # TODO: Place green crystal on right pedistal (first slot, can mash?)
                # TODO: Move to green portal and go inside
                # TODO: Navigate green area
                # TODO: A lot
                SeqCheckpoint(checkpoint_name="wizard_lab_boss"),
            ],
        )
