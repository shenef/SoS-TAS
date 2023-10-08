"""Routing of Abandoned Wizard Lab section of Sleeper Island."""

import logging
from typing import Self

from engine.combat import (
    SeqCombat,
    SeqCombatAndMove,
)
from engine.mathlib import Vec2, Vec3
from engine.seq import (
    HoldDirection,
    InteractMove,
    MistralBracelet,
    MoveToward,
    SeqAwaitLostControl,
    SeqBlockPuzzle,
    SeqCheckpoint,
    SeqDelay,
    SeqHoldDirectionUntilCombat,
    SeqHoldDirectionUntilLostControl,
    SeqInteract,
    SeqList,
    SeqMove,
    SeqSelectOption,
    SeqSkipUntilIdle,
)

logger = logging.getLogger(__name__)


class FirstBlockPuzzle(SeqBlockPuzzle):
    """Block puzzle in first room."""

    def __init__(self: Self) -> None:
        super().__init__(
            name="Block Puzzle #1",
            coords=[
                Vec3(-3.831, 1.002, 15.133),
                Vec3(-3.831, 1.002, 17.216),
                MistralBracelet(joy_dir=Vec2(0, 1)),
                Vec3(-6.202, 1.002, 27.352),
                Vec3(-5.454, 1.002, 27.401),
                MistralBracelet(joy_dir=Vec2(1, 0)),
                Vec3(-1.966, 1.002, 24.339),
                Vec3(-1.966, 1.002, 25.815),
                MistralBracelet(joy_dir=Vec2(0, 1)),
            ],
        )


class WizardLabEnterTower(SeqList):
    """Route up to entering the green portal."""

    def __init__(self: Self) -> None:
        super().__init__(
            name="Enter tower",
            children=[
                # Cutscene
                SeqAwaitLostControl("Scene transition"),
                SeqSkipUntilIdle("Scene transition"),
                SeqHoldDirectionUntilLostControl("Move to cutscene", joy_dir=Vec2(1, -0.5)),
                SeqSkipUntilIdle(name="Making a door"),
                SeqMove(
                    name="Move to cutscene",
                    coords=[
                        Vec3(22.317, 1.002, -70.433),
                        HoldDirection(8.000, 1.002, -13.399, joy_dir=Vec2(0, 1)),
                        Vec3(4.424, 1.002, -11.310),
                        Vec3(3.040, 1.005, 9.869),
                    ],
                ),
                # Cutscene
                SeqSkipUntilIdle(name="Keenathan leaves"),
                # Block puzzle
                FirstBlockPuzzle(),
                SeqMove(
                    name="Go to chest",
                    coords=[
                        InteractMove(-1.806, 6.002, 32.876),
                        InteractMove(7.100, 6.002, 33.171),
                    ],
                ),
                SeqInteract("Green crystal"),
                SeqSkipUntilIdle("Green crystal"),
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
                SeqSelectOption("Place Green Crystal", skip_dialog_check=True),
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
                SeqCheckpoint(checkpoint_name="wizard_lab"),
                SeqMove(
                    name="Enter green portal",
                    coords=[
                        Vec3(-3.187, 1.002, 24.928),
                        Vec3(3.932, 1.002, 29.996),
                        HoldDirection(-80.000, 1.002, -29.498, joy_dir=Vec2(0, 1)),
                    ],
                ),
            ],
        )


class WizardLabGreenArea(SeqList):
    """Route through the green portal area."""

    def __init__(self: Self) -> None:
        super().__init__(
            name="Green area",
            children=[
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
                SeqInteract("Blue Crystal"),
                SeqSkipUntilIdle(name="Blue Crystal"),
                SeqMove(
                    name="Leave room",
                    coords=[
                        InteractMove(-78.839, 1.010, -10.512),
                        Vec3(-80.122, 1.002, -17.544),
                        Vec3(-80.122, 1.002, -30.838),
                        HoldDirection(4.000, 1.002, 28.775, joy_dir=Vec2(0, -1)),
                    ],
                ),
            ],
        )


class WizardLabPlaceBlueCrystal(SeqList):
    """Route to place blue crystal."""

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
                SeqSelectOption("Remove Green Crystal", skip_dialog_check=True),
                SeqDelay("Wait", timeout_in_s=1.0),
                # Place blue crystal
                SeqSelectOption("Place Blue Crystal", skip_dialog_check=True),
                SeqMove(
                    name="Go towards portal",
                    coords=[
                        Vec3(3.976, 2.947, 15.920),
                        Vec3(3.225, 1.010, 13.016),
                        Vec3(0.242, 1.002, 12.798),
                        Vec3(-2.137, 1.002, 15.356),
                        Vec3(-2.137, 1.002, 25.087),
                    ],
                ),
                # Checkpoint: Wizard lab
                SeqCheckpoint(checkpoint_name="wizard_lab2"),
                SeqMove(
                    name="Enter blue portal",
                    coords=[
                        Vec3(-2.137, 1.002, 25.087),
                        Vec3(3.932, 1.002, 29.996),
                        HoldDirection(239.500, 1.002, -48.833, joy_dir=Vec2(0, 1)),
                    ],
                ),
            ],
        )


class WizardLabBlueArea(SeqList):
    """Route through blue area."""

    def __init__(self: Self) -> None:
        super().__init__(
            name="Blue area",
            children=[
                SeqCombatAndMove(
                    name="Navigate to pressure plate",
                    coords=[
                        Vec3(239.500, 1.002, -41.105),
                        Vec3(240.543, 1.002, -38.459),
                        InteractMove(240.900, 1.002, -22.100),
                        Vec3(238.822, 1.002, -16.825),
                        InteractMove(236.793, 6.002, -14.547),
                        Vec3(238.122, 6.002, -10.700),
                        Vec3(248.194, 6.002, -9.731),
                        MoveToward(
                            266.500, 1.002, -21.400, anchor=Vec3(250, 6.002, -9.731), mash=True
                        ),
                        Vec3(266.490, 1.002, -13.180),
                        InteractMove(266.490, 6.002, -9.533),
                        Vec3(266.490, 6.002, -7.465),
                        Vec3(268.632, 6.002, -5.003),
                        Vec3(287.081, 6.002, -4.942),
                        InteractMove(287.081, 1.002, -7.216),
                        Vec3(287.081, 1.002, -14.332),
                        Vec3(283.734, 1.002, -17.692),
                        Vec3(281.465, 1.002, -17.692),
                        InteractMove(281.492, 6.002, -15.232),
                        Vec3(287.499, 6.002, -15.232),
                        Vec3(288.522, 6.002, -16.926),
                        Vec3(288.522, 6.002, -19.260),
                        InteractMove(289.452, 6.002, -25.540),
                        InteractMove(288.460, 6.002, -31.540),
                        InteractMove(288.460, 6.002, -34.481),
                        Vec3(274.506, 1.002, -36.051),
                        MoveToward(
                            278.000, 6.002, -29.000, anchor=Vec3(270, 1.002, -36.051), mash=True
                        ),
                        Vec3(278.000, 6.277, -25.835),
                    ],
                ),
                SeqDelay("Pressure plate", timeout_in_s=0.5),
                SeqMove(
                    name="Move to fight",
                    coords=[
                        Vec3(280.289, 6.010, -23.941),
                        InteractMove(281.119, 1.002, -23.467),
                        Vec3(281.352, 1.002, -17.454),
                        InteractMove(281.492, 6.002, -16.291),
                        Vec3(283.006, 6.002, -15.187),
                        Vec3(287.117, 6.002, -15.187),
                        Vec3(288.602, 6.002, -16.731),
                        Vec3(288.548, 6.002, -19.540),
                        InteractMove(289.452, 6.002, -25.540),
                        InteractMove(288.460, 6.002, -31.540),
                        InteractMove(288.460, 6.002, -34.673),
                        Vec3(274.895, 1.002, -37.225),
                        Vec3(274.895, 1.002, -40.910),
                    ],
                ),
                SeqHoldDirectionUntilCombat(
                    name="Move to fight",
                    joy_dir=Vec2(1, -1),
                    mash_confirm=True,
                ),
                SeqCombat("Fight"),
                SeqMove(
                    name="Move to pressure plate",
                    coords=[
                        Vec3(286.063, 1.252, -42.584),
                    ],
                ),
                SeqDelay("Pressure plate", timeout_in_s=0.5),
                SeqCombatAndMove(
                    name="Move to lever",
                    coords=[
                        Vec3(271.234, 1.002, -40.098),
                        MoveToward(
                            241.000, 1.002, -20.000, anchor=Vec3(260.234, 1.002, -40.098), mash=True
                        ),
                        Vec3(238.329, 1.002, -17.321),
                        InteractMove(236.075, 6.002, -15.265),
                        Vec3(230.432, 6.002, -16.558),
                        Vec3(229.259, 6.002, -31.987),
                    ],
                ),
                SeqInteract("Lever"),
                SeqCombatAndMove(
                    name="Move to button",
                    coords=[
                        Vec3(230.330, 6.002, -17.376),
                        Vec3(233.131, 6.002, -16.538),
                        Vec3(234.332, 6.002, -17.021),
                        InteractMove(234.656, 1.002, -18.112),
                        Vec3(239.207, 1.002, -24.147),
                        MoveToward(
                            240.400, 1.002, -40.100, anchor=Vec3(240.207, 1.002, -25.147), mash=True
                        ),
                        MoveToward(
                            256.400, 1.002, -30.600, anchor=Vec3(245.400, 1.002, -40.100), mash=True
                        ),
                        Vec3(256.460, 1.002, -25.116),
                    ],
                ),
                SeqInteract("Button"),
                SeqMove(
                    name="Move to pillar",
                    coords=[
                        Vec3(256.460, 1.002, -28.540),
                        MoveToward(
                            240.400, 1.002, -40.100, anchor=Vec3(256.460, 1.002, -30.540), mash=True
                        ),
                        Vec3(239.627, 1.002, -50.548),
                        HoldDirection(4.167, 1.002, 28.000, joy_dir=Vec2(0, -1)),
                        Vec3(-1.841, 1.002, 22.102),
                        Vec3(-2.157, 1.002, 15.583),
                        Vec3(0.543, 1.002, 12.914),
                        Vec3(3.528, 1.002, 12.914),
                        Vec3(3.528, 2.960, 16.866),
                        Vec3(1.740, 2.952, 17.852),
                    ],
                ),
                SeqSelectOption("Place Green Crystal", skip_dialog_check=True),
                SeqMove(
                    name="Move to save branch",
                    coords=[
                        Vec3(3.612, 2.952, 16.380),
                        Vec3(3.612, 1.010, 13.163),
                        Vec3(0.769, 1.002, 13.163),
                        Vec3(-1.818, 1.002, 15.481),
                    ],
                ),
            ],
        )


class WizardLabTealArea(SeqList):
    """Route through teal area."""

    def __init__(self: Self) -> None:
        super().__init__(
            name="Teal area",
            children=[
                SeqMove(
                    name="Enter teal portal",
                    coords=[
                        Vec3(-1.963, 1.002, 25.120),
                        Vec3(3.996, 1.002, 29.859),
                        HoldDirection(-75.500, 5.002, 133.759, joy_dir=Vec2(0, 1)),
                        Vec3(-75.500, 5.002, 144.314),
                        Vec3(-76.881, 5.002, 145.922),
                        Vec3(-81.252, 5.002, 145.899),
                        Vec3(-82.542, 5.002, 144.847),
                        Vec3(-86.220, 5.002, 144.847),
                        InteractMove(-87.795, 5.002, 146.854),
                        Vec3(-89.049, 5.002, 147.965),
                        Vec3(-87.738, 5.002, 149.087),
                        InteractMove(-83.866, 5.002, 152.797),
                        Vec3(-83.297, 5.002, 153.873),
                        Vec3(-85.221, 5.002, 156.048),
                    ],
                ),
                SeqBlockPuzzle(
                    name="Push block out of the way",
                    coords=[
                        Vec3(-85.221, 5.002, 160.632),
                        Vec3(-84.317, 5.002, 162.782),
                        MistralBracelet(joy_dir=Vec2(-1, 0)),
                        Vec3(-85.595, 5.002, 164.834),
                    ],
                ),
                SeqInteract("Summon enemies"),
                SeqHoldDirectionUntilCombat("Fight", joy_dir=Vec2(0, -1), mash_confirm=True),
                SeqCombat("Fight #1"),
                SeqBlockPuzzle(
                    name="Move block",
                    coords=[
                        Vec3(-98.264, 5.002, 161.106),
                        Vec3(-100.157, 5.002, 161.106),
                        MistralBracelet(joy_dir=Vec2(0, 1)),
                        Vec3(-101.644, 5.002, 164.377),
                        Vec3(-101.644, 5.002, 165.635),
                        MistralBracelet(joy_dir=Vec2(1, 0)),
                    ],
                ),
                SeqMove(
                    name="Climb to pillar",
                    coords=[
                        InteractMove(-96.533, 10.002, 165.635),
                        Vec3(-95.429, 10.002, 166.119),
                    ],
                ),
                SeqInteract("Summon enemies"),
                SeqHoldDirectionUntilCombat("Fight", joy_dir=Vec2(0, -1), mash_confirm=True),
                SeqCombat("Fight #2"),
                SeqMove(
                    name="Move to pillar",
                    coords=[
                        Vec3(-96.902, 5.002, 153.009),
                        Vec3(-96.836, 5.002, 146.755),
                    ],
                ),
                SeqInteract("Summon enemies"),
                SeqMove(
                    name="Move to fight",
                    coords=[
                        Vec3(-96.836, 5.002, 150.098),
                    ],
                ),
                SeqHoldDirectionUntilCombat("Fight", joy_dir=Vec2(1, 1), mash_confirm=True),
                SeqCombat("Fight #3"),
                SeqMove(
                    name="Move to chest",
                    coords=[
                        Vec3(-86.159, 5.002, 156.983),
                        Vec3(-82.586, 5.002, 153.715),
                        Vec3(-77.809, 5.002, 157.422),
                    ],
                ),
                SeqInteract("Red Crystal"),
                SeqSkipUntilIdle("Red Crystal"),
                SeqMove(
                    name="Move to pillar",
                    coords=[
                        Vec3(-82.071, 5.002, 154.542),
                        Vec3(-84.170, 5.002, 152.818),
                        InteractMove(-88.015, 5.002, 148.810),
                        Vec3(-88.844, 5.002, 148.014),
                        Vec3(-87.878, 5.002, 146.769),
                        InteractMove(-86.142, 5.002, 144.907),
                        Vec3(-80.893, 5.002, 144.907),
                        Vec3(-76.602, 5.002, 145.748),
                        Vec3(-75.346, 5.002, 144.281),
                        Vec3(-75.346, 5.002, 133.333),
                        HoldDirection(4.167, 1.002, 28.000, joy_dir=Vec2(0, -1)),
                        Vec3(9.960, 1.002, 22.188),
                        Vec3(9.960, 1.002, 15.787),
                        Vec3(7.335, 1.002, 13.162),
                        Vec3(4.068, 1.002, 13.162),
                        Vec3(4.068, 2.980, 16.149),
                        Vec3(6.218, 2.952, 18.416),
                    ],
                ),
                SeqSelectOption("Remove Blue Crystal", skip_dialog_check=True),
                SeqSelectOption("Place Red Crystal", skip_dialog_check=True),
                SeqMove(
                    name="Move to save branch",
                    coords=[
                        Vec3(3.612, 2.952, 16.380),
                        Vec3(3.612, 1.010, 13.163),
                        Vec3(0.769, 1.002, 13.163),
                        Vec3(-1.818, 1.002, 15.481),
                    ],
                ),
            ],
        )


class WizardLabYellowArea(SeqList):
    """Route through yellow area."""

    def __init__(self: Self) -> None:
        super().__init__(
            name="Yellow area",
            children=[
                SeqMove(
                    name="Enter yellow portal",
                    coords=[
                        Vec3(-1.963, 1.002, 25.120),
                        Vec3(3.996, 1.002, 29.859),
                        HoldDirection(108.500, 1.002, 9.000, joy_dir=Vec2(0, 1)),
                        # TODO(orkaboy): Continue routing
                    ],
                ),
            ],
        )


class WizardLab(SeqList):
    """Route of Abandoned Wizard Lab, from entering to defeating boss."""

    def __init__(self: Self) -> None:
        super().__init__(
            name="Wizard Lab",
            children=[
                WizardLabEnterTower(),
                # Enter green portal
                WizardLabGreenArea(),
                WizardLabPlaceBlueCrystal(),
                WizardLabBlueArea(),
                SeqCheckpoint("wizard_lab3"),
                WizardLabTealArea(),
                SeqCheckpoint("wizard_lab4"),
                WizardLabYellowArea(),
                # TODO(orkaboy): Continue routing
                SeqCheckpoint("wizard_lab_boss"),
                # TODO(orkaboy): Continue routing
            ],
        )
