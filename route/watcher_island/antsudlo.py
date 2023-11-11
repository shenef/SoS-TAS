"""Routing of Tower of Antsudlo segment of Watcher Island."""

import logging
from typing import Self

from engine.combat import SeqCombatAndMove
from engine.mathlib import Vec2, Vec3
from engine.seq import (
    HoldDirection,
    InteractMove,
    SeqCheckpoint,
    SeqDelay,
    SeqHoldDirectionDelay,
    SeqInteract,
    SeqList,
    SeqMove,
    SeqSelectOption,
)

logger = logging.getLogger(__name__)


class Seafloor(SeqList):
    """Routing of Seafloor part of Tower of Antsudlo."""

    def __init__(self: Self) -> None:
        """Initialize a new Seafloor object."""
        super().__init__(
            name="Seafloor",
            children=[
                SeqMove(
                    name="Move to Sapphire Key",
                    coords=[
                        Vec3(12.266, 1.303, 26.810),
                        Vec3(12.229, 1.303, 73.225),
                        Vec3(14.009, 1.303, 80.817),
                        Vec3(13.441, 1.303, 93.140),
                    ],
                ),
                SeqInteract("Sapphire Key"),
                SeqMove(
                    name="Move to slot",
                    coords=[
                        Vec3(13.156, 1.303, 80.951),
                        Vec3(11.570, 1.303, 64.146),
                        Vec3(8.674, 1.303, 63.873),
                    ],
                ),
                SeqSelectOption("Place Sapphire Key", skip_dialog_check=True),
                SeqCombatAndMove(
                    name="Navigate water maze",
                    coords=[
                        Vec3(6.414, 1.303, 61.795),
                        Vec3(4.084, 1.303, 62.271),
                        Vec3(-26.913, 1.303, 94.066),
                        Vec3(-22.859, 1.303, 97.681),
                    ],
                ),
                SeqDelay("Wait", 0.7),
                SeqCombatAndMove(
                    name="Navigate water maze",
                    coords=[
                        Vec3(-23.645, 1.303, 97.867),
                        Vec3(-24.697, 1.303, 102.931),
                        Vec3(-20.898, 1.303, 108.235),
                        Vec3(-17.660, 1.303, 111.515),
                        Vec3(-17.134, 1.303, 118.142),
                        Vec3(2.101, 1.303, 138.048),
                        Vec3(5.703, 1.303, 129.874),
                        Vec3(10.148, 1.303, 127.798),
                        Vec3(17.531, 1.303, 127.151),
                        Vec3(20.928, 1.303, 129.472),
                        Vec3(20.959, 1.303, 134.865),
                        Vec3(17.626, 1.303, 140.475),
                        Vec3(-5.102, 1.303, 163.280),
                    ],
                ),
                SeqCombatAndMove(
                    name="Move to bell",
                    coords=[
                        Vec3(-5.628, 1.303, 173.090),
                        Vec3(-8.013, 1.303, 175.695),
                        Vec3(-8.925, 1.303, 179.404),
                        Vec3(-8.766, 1.303, 186.246),
                        Vec3(-14.254, 1.303, 191.446),
                    ],
                    recovery_path=SeqMove(
                        name="Return to path",
                        coords=[
                            Vec3(-8.805, 1.303, 186.843),
                        ],
                    ),
                ),
                SeqSelectOption("Ring bell", skip_dialog_check=True),
                SeqMove(
                    name="Move to Sapphire Key",
                    coords=[
                        Vec3(-25.629, 1.303, 191.307),
                    ],
                ),
                SeqInteract("Sapphire Key"),
                SeqCombatAndMove(
                    name="Move to slot",
                    coords=[
                        Vec3(-16.323, 1.303, 190.511),
                        Vec3(-9.281, 1.303, 187.140),
                        Vec3(-5.488, 1.303, 180.250),
                        Vec3(11.788, 1.303, 176.246),
                    ],
                ),
                SeqSelectOption("Place Sapphire Key", skip_dialog_check=True),
                SeqMove(
                    name="Cross waterway",
                    coords=[
                        Vec3(14.424, 1.303, 171.363),
                        Vec3(26.432, 1.303, 157.933),
                    ],
                ),
                SeqHoldDirectionDelay("Turn", joy_dir=Vec2(-1, -1), timeout_s=0.1),
                SeqInteract("Sapphire Ore"),
                SeqMove(
                    name="Move to bell",
                    coords=[
                        InteractMove(26.439, 1.303, 166.361),
                        Vec3(25.033, 1.303, 170.297),
                    ],
                ),
                SeqSelectOption("Ring bell", skip_dialog_check=True),
                SeqMove(
                    name="Enter tower",
                    coords=[
                        Vec3(26.106, 1.303, 167.506),
                        Vec3(26.106, 1.303, 162.503),
                        Vec3(23.841, 1.303, 162.789),
                        Vec3(9.689, 1.303, 174.963),
                        Vec3(0.862, 1.303, 181.930),
                        HoldDirection(261.583, 1.303, -6.600, joy_dir=Vec2(0, 1)),
                        Vec3(261.608, 1.303, 0.360),
                    ],
                ),
                SeqInteract("Turn wheel"),
                SeqMove(
                    name="Move to save branch",
                    coords=[
                        Vec3(262.855, 1.002, 2.046),
                        Vec3(261.274, 1.002, 6.941),
                        Vec3(261.462, 1.002, 20.499),
                    ],
                ),
            ],
        )


class FirstFloor(SeqList):
    """Routing of first floor of Tower of Antsudlo."""

    def __init__(self: Self) -> None:
        """Initialize a new FirstFloor object."""
        super().__init__(
            name="First Floor",
            children=[
                SeqMove(
                    name="Enter next room",
                    coords=[
                        Vec3(261.556, 1.002, 20.238),
                        HoldDirection(264.500, 1.002, 80.000, joy_dir=Vec2(0, 1)),
                    ],
                ),
                # TODO(orkaboy): Continue routing
            ],
        )


class TowerOfAntsudlo(SeqList):
    """Routing of Tower of Antsudlo segment of Watcher Island."""

    def __init__(self: Self) -> None:
        """Initialize a new TowerOfAntsudlo object."""
        super().__init__(
            name="Tower of Antsudlo",
            children=[
                Seafloor(),
                SeqCheckpoint("antsudlo"),
                FirstFloor(),
                # TODO(orkaboy): Continue routing
            ],
        )
