import logging
from typing import Self

from engine.combat import (
    SeqCombatAndMove,
)
from engine.mathlib import Vec2, Vec3
from engine.seq import (
    InteractMove,
    SeqBracelet,
    SeqCheckpoint,
    SeqDelay,
    SeqHoldDirectionUntilClose,
    SeqInteract,
    SeqList,
    SeqLog,
    SeqMove,
    SeqSkipUntilIdle,
)

logger = logging.getLogger(__name__)


class DemoWizardLabEnterTower(SeqList):
    def __init__(self: Self) -> None:
        super().__init__(
            name="Enter tower",
            children=[
                SeqMove(
                    name="Move to cutscene",
                    coords=[
                        Vec3(14.300, 1.010, -72.600),
                    ],
                ),
                # Cutscene
                SeqSkipUntilIdle(name="Making a door"),
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
                SeqSkipUntilIdle(name="Pirate leaves"),
                SeqMove(
                    name="Move to block",
                    coords=[
                        Vec3(-3.831, 1.002, 15.133),
                        Vec3(-3.831, 1.002, 17.216),
                    ],
                ),
                SeqBracelet("Push block north"),
                SeqMove(
                    name="Move to block",
                    coords=[
                        Vec3(-6.202, 1.002, 27.352),
                        Vec3(-5.454, 1.002, 27.401),
                    ],
                ),
                SeqBracelet("Push block east"),
                SeqMove(
                    name="Move to block",
                    coords=[
                        Vec3(-1.966, 1.002, 24.339),
                        Vec3(-1.966, 1.002, 25.815),
                    ],
                ),
                SeqBracelet("Push block north"),
                SeqMove(
                    name="Go to chest",
                    coords=[
                        InteractMove(-1.806, 6.002, 32.876),
                        InteractMove(7.100, 6.002, 33.171),
                    ],
                ),
                SeqSkipUntilIdle(name="Pick up green crystal"),
                SeqMove(
                    name="Go to altar",
                    coords=[
                        InteractMove(8.006, 1.002, 28.253),
                        Vec3(10.713, 1.002, 19.558),
                        Vec3(9.590, 1.002, 13.294),
                        Vec3(4.452, 1.002, 13.294),
                        Vec3(4.452, 2.954, 16.809),
                        Vec3(6.216, 2.954, 18.675),
                    ],
                ),
                # Place green crystal
                SeqInteract(),
                SeqDelay(name="Menu", timeout_in_s=1.0),
                SeqInteract(),
                SeqMove(
                    name="Go towards portal",
                    coords=[
                        Vec3(3.976, 2.947, 15.920),
                        Vec3(3.225, 1.010, 13.016),
                        Vec3(-1.145, 1.002, 13.016),
                        Vec3(-3.187, 1.002, 19.657),
                    ],
                ),
                # Checkpoint: Wizard lab
                SeqCheckpoint(checkpoint_name="wizard_lab1"),
                SeqMove(
                    name="Go to portal",
                    coords=[
                        Vec3(-3.187, 1.002, 24.928),
                        Vec3(3.932, 1.002, 29.996),
                    ],
                ),
            ],
        )


class DemoWizardLabGreenArea(SeqList):
    def __init__(self: Self) -> None:
        super().__init__(
            name="Green area",
            children=[
                SeqHoldDirectionUntilClose(
                    name="Enter green portal",
                    target=Vec3(-80.000, 1.002, -29.498),
                    joy_dir=Vec2(0, 1),
                ),
                SeqCombatAndMove(
                    name="Move to fight (AI combat)",
                    coords=[
                        Vec3(-80.000, 1.002, -21.742),
                        Vec3(-84.648, 1.002, -11.011),
                        Vec3(-84.905, 1.260, -4.096),
                    ],
                ),
                SeqDelay("Activate floor plate", timeout_in_s=0.5),
                SeqMove(
                    name="Puzzles",
                    coords=[
                        # Puzzles
                        Vec3(-83.248, 1.010, -5.665),
                        InteractMove(-83.455, 1.002, -16.232),
                        Vec3(-87.502, 1.002, -20.988),
                        InteractMove(-96.415, 1.002, -20.949),
                        InteractMove(-97.350, 6.002, -12.533),
                        Vec3(-92.874, 6.260, -3.122),
                        Vec3(-95.545, 6.010, -10.632),
                        Vec3(-95.545, 6.002, -12.540),
                    ],
                ),
                SeqMove(
                    name="Platforms",
                    precision=0.5,  # Low precision to prevent turning the wrong way
                    coords=[
                        # Jump on platforms
                        InteractMove(-88.460, 6.002, -12.460),
                        InteractMove(-88.460, 6.002, -15.614),
                        InteractMove(-85.332, 1.002, -18.017),
                    ],
                ),
                SeqMove(
                    name="Puzzles",
                    coords=[
                        InteractMove(-73.460, 2.002, -18.017),
                        InteractMove(-73.477, 6.002, -12.533),
                        Vec3(-78.803, 6.002, -7.156),
                        InteractMove(-81.784, 1.002, -4.457),
                        # Floor block
                        Vec3(-85.120, 1.252, -4.049),
                        Vec3(-84.457, 1.010, -10.810),
                        Vec3(-77.946, 1.002, -13.459),
                        InteractMove(-76.533, 4.002, -13.459),
                        InteractMove(-76.533, 6.002, -8.654),
                        InteractMove(-78.839, 6.002, -3.181),
                    ],
                ),
                SeqSkipUntilIdle(name="Pick up blue crystal"),
                SeqMove(
                    name="Leave room",
                    coords=[
                        InteractMove(-78.839, 1.010, -10.512),
                        Vec3(-80.122, 1.002, -17.544),
                        Vec3(-80.122, 1.002, -30.838),
                    ],
                ),
                SeqHoldDirectionUntilClose(
                    name="Leave green portal",
                    target=Vec3(4.000, 1.002, 28.775),
                    joy_dir=Vec2(0, -1),
                ),
            ],
        )


class DemoWizardLabPlaceBlueCrystal(SeqList):
    def __init__(self: Self) -> None:
        super().__init__(
            name="Set blue crystal",
            children=[
                SeqMove(
                    name="Go to altar",
                    coords=[
                        Vec3(10.241, 1.002, 22.438),
                        Vec3(10.241, 1.002, 15.016),
                        Vec3(7.136, 1.002, 13.094),
                        Vec3(4.574, 1.002, 13.549),
                        Vec3(4.518, 2.954, 16.710),
                        Vec3(6.298, 2.946, 17.999),
                    ],
                ),
                # Remove green crystal
                SeqInteract(),
                SeqDelay(name="Menu", timeout_in_s=1.0),
                SeqInteract(),
                SeqDelay(name="Menu", timeout_in_s=1.0),
                # Place blue crystal
                SeqInteract(),
                SeqDelay(name="Menu", timeout_in_s=1.0),
                SeqInteract(),
                SeqMove(
                    name="Go towards portal",
                    coords=[
                        Vec3(3.976, 2.947, 15.920),
                        Vec3(3.225, 1.010, 13.016),
                        Vec3(-1.145, 1.002, 13.016),
                        Vec3(-3.187, 1.002, 19.657),
                    ],
                ),
                # Checkpoint: Wizard lab
                SeqCheckpoint(checkpoint_name="wizard_lab2"),
                SeqMove(
                    name="Go to portal",
                    coords=[
                        Vec3(-3.187, 1.002, 24.928),
                        Vec3(3.932, 1.002, 29.996),
                    ],
                ),
            ],
        )


class DemoWizardLabBlueArea(SeqList):
    def __init__(self: Self) -> None:
        super().__init__(
            name="Blue area",
            children=[
                SeqHoldDirectionUntilClose(
                    name="Enter blue portal",
                    target=Vec3(239.500, 1.002, -48.833),
                    joy_dir=Vec2(0, 1),
                ),
                # TODO: Route blue room
            ],
        )


class DemoWizardLab(SeqList):
    def __init__(self: Self) -> None:
        super().__init__(
            name="Wizard Lab",
            children=[
                SeqLog(name="SYSTEM", text="We have arrived at the tower!"),
                DemoWizardLabEnterTower(),
                # Enter green portal
                DemoWizardLabGreenArea(),
                DemoWizardLabPlaceBlueCrystal(),
                DemoWizardLabBlueArea(),
                # TODO: A lot
                SeqCheckpoint(checkpoint_name="wizard_lab_boss"),
            ],
        )
