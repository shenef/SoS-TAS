"""Routing of Torment Peak segment of Watcher Island."""

import logging
from enum import Enum, auto
from typing import Self

from control import sos_ctrl
from engine.combat import SeqCombat, SeqCombatAndMove
from engine.mathlib import Vec2, Vec3
from engine.seq import (
    Graplou,
    HoldDirection,
    InteractMove,
    MistralBracelet,
    SeqAwaitLostControl,
    SeqBase,
    SeqBoat,
    SeqBraceletPuzzle,
    SeqChangeTimeOfDay,
    SeqCheckpoint,
    SeqCliffClimb,
    SeqCliffMove,
    SeqClimb,
    SeqDelay,
    SeqGraplou,
    SeqHoldDirectionDelay,
    SeqHoldDirectionUntilCombat,
    SeqHoldDirectionUntilLostControl,
    SeqInteract,
    SeqList,
    SeqLoot,
    SeqMove,
    SeqSelectOption,
    SeqSkipUntilClose,
    SeqSkipUntilIdle,
)

logger = logging.getLogger(__name__)


class OnToTormentPeak(SeqList):
    """Routing from Lake Docarria to Torment Peak."""

    def __init__(self: Self) -> None:
        """Initialize a new OnToTormentPeak object."""
        super().__init__(
            name="On to Torment Peak",
            children=[
                SeqMove(
                    name="Navigate Lake Docarria",
                    coords=[
                        Vec3(63.480, 43.002, 64.460),
                        InteractMove(63.459, 40.803, 63.540),
                        Vec3(50.394, 40.803, 62.848),
                        Vec3(28.628, 40.803, 65.011),
                        Vec3(24.992, 40.803, 74.351),
                        InteractMove(24.148, 43.002, 75.156),
                        Vec3(24.148, 43.002, 77.281),
                        Vec3(39.631, 48.002, 76.688),
                        Vec3(41.845, 48.002, 75.835),
                        Vec3(47.688, 48.002, 75.835),
                        Vec3(53.691, 48.002, 82.063),
                        Vec3(54.618, 48.002, 86.572),
                        HoldDirection(237.500, 3.002, 71.498, joy_dir=Vec2(0, 1)),
                    ],
                ),
                SeqMove(
                    name="Navigate overworld",
                    coords=[
                        Vec3(237.500, 3.002, 73.000),
                        Vec3(238.000, 3.002, 73.000),
                        Vec3(238.000, 3.002, 77.000),
                        Vec3(237.500, 3.002, 77.000),
                        Vec3(237.500, 3.002, 77.500),
                    ],
                ),
                SeqInteract("Torment Peak"),
                SeqChangeTimeOfDay("Right rune", time_target=16.0),
                SeqMove(
                    name="Move close to pedestal",
                    coords=[
                        Vec3(26.130, 5.002, -43.551),
                    ],
                ),
                SeqDelay("Wait for rune to fill", timeout_in_s=3.0),
                SeqChangeTimeOfDay("Left rune", time_target=8.0),
                SeqMove(
                    name="Move close to left rune",
                    coords=[
                        Vec3(19.323, 5.002, -40.471),
                    ],
                ),
                SeqSkipUntilIdle("Wait for idle"),
                SeqAwaitLostControl("Wait for cutscene"),
                SeqBraceletPuzzle(
                    name="Push blocks",
                    coords=[
                        Vec3(14.345, 5.002, -38.635),
                        Vec3(14.345, 5.002, -37.384),
                        MistralBracelet(joy_dir=Vec2(1, 0)),
                        Vec3(19.535, 5.002, -38.687),
                        Vec3(21.650, 5.002, -38.738),
                        MistralBracelet(joy_dir=Vec2(0, 1)),
                        Vec3(38.709, 5.002, -38.753),
                        Vec3(38.709, 5.002, -37.319),
                        MistralBracelet(joy_dir=Vec2(-1, 0)),
                        Vec3(33.369, 5.002, -38.883),
                        Vec3(32.552, 5.002, -38.883),
                        MistralBracelet(joy_dir=Vec2(0, 1)),
                    ],
                ),
                # Cutscene is a little finicky
                SeqSkipUntilIdle("Wait for control"),
                SeqHoldDirectionUntilLostControl("Move to cutscene", joy_dir=Vec2(-1, 1)),
                SeqSkipUntilIdle("No turning back now"),
                # Enter Torment Peak
                SeqMove(
                    name="Move to save branch",
                    coords=[
                        Vec3(26.280, 5.002, -30.670),
                        HoldDirection(27.500, 5.002, 4.301, joy_dir=Vec2(0, 1)),
                        Vec3(27.500, 5.002, 34.756),
                    ],
                ),
            ],
        )


class ActivatePillars(SeqList):
    """Routing of pillar segment of first room in Torment Peak."""

    def __init__(self: Self) -> None:
        """Initialize a new ActivatePillars object."""
        super().__init__(
            name="Activate Pillars",
            children=[
                # Move to left pillar
                SeqMove(
                    name="Move left to cliff",
                    coords=[
                        Vec3(98.217, 3.002, 139.748),
                        Vec3(86.964, 3.002, 142.767),
                        Vec3(82.333, 2.002, 144.076),
                        Vec3(80.692, 2.002, 146.227),
                    ],
                ),
                SeqCliffClimb(
                    name="Climb cliff",
                    coords=[
                        InteractMove(81.016, 8.000, 147.000),
                    ],
                ),
                SeqCliffMove(
                    name="Move along ledge",
                    coords=[
                        Vec3(80.280, 8.000, 146.714),
                        Vec3(78.493, 8.000, 145.000),
                        Vec3(76.769, 8.000, 145.000),
                        Vec3(75.388, 8.000, 146.000),
                        Vec3(71.215, 8.002, 146.466),
                    ],
                ),
                SeqMove(
                    name="Move to top of cliff",
                    coords=[
                        InteractMove(66.327, 8.002, 146.466),
                        Vec3(64.541, 8.002, 145.454),
                        Vec3(62.842, 8.002, 145.801),
                    ],
                ),
                SeqCliffClimb(
                    name="Jump off cliff",
                    coords=[
                        InteractMove(63.088, 5.000, 145.000),
                        Vec3(61.950, 5.000, 145.484),
                        InteractMove(61.381, 2.002, 144.755),
                    ],
                    precision=0.5,
                ),
                SeqMove(
                    name="Move to pillar",
                    coords=[
                        Vec3(55.559, 2.002, 145.228),
                        Vec3(54.716, 2.002, 146.669),
                    ],
                ),
                SeqInteract("Pillar"),
                # Return to central area
                SeqMove(
                    name="Move to wall",
                    coords=[
                        Vec3(55.784, 2.002, 145.218),
                        Vec3(61.870, 2.002, 145.483),
                    ],
                ),
                SeqCliffClimb(
                    name="Climb cliff",
                    coords=[
                        InteractMove(62.200, 5.000, 145.234),
                        InteractMove(62.787, 8.002, 145.959),
                    ],
                ),
                SeqMove(
                    name="Move to ledge",
                    coords=[
                        Vec3(65.421, 8.002, 145.959),
                        Vec3(66.543, 8.002, 146.867),
                        InteractMove(69.481, 8.002, 146.867),
                        Vec3(70.842, 8.002, 146.035),
                    ],
                ),
                SeqCliffMove(
                    name="Move along ledge",
                    coords=[
                        HoldDirection(74.526, 8.000, 146.000, joy_dir=Vec2(1, 0)),
                        HoldDirection(79.744, 8.000, 146.178, joy_dir=Vec2(1, 0)),
                    ],
                ),
                SeqCliffClimb(
                    name="Get off ledge",
                    coords=[
                        InteractMove(79.784, 2.002, 144.920),
                    ],
                ),
                SeqMove(
                    name="Move to central area",
                    coords=[
                        Vec3(82.774, 2.002, 143.708),
                        Vec3(96.873, 3.002, 143.708),
                    ],
                ),
                # Move to right pillar
                SeqMove(
                    name="Move to right pillar",
                    coords=[
                        Vec3(102.581, 3.002, 146.689),
                        Vec3(104.815, 3.002, 147.458),
                        Vec3(107.566, 3.002, 147.458),
                        InteractMove(109.483, 0.002, 145.542),
                        Vec3(110.448, 0.002, 143.505),
                        Vec3(111.616, 0.002, 143.505),
                    ],
                ),
                SeqInteract("Pillar"),
                # Return to central area
                SeqMove(
                    name="Move to door",
                    coords=[
                        Vec3(109.719, 0.002, 144.372),
                        Vec3(108.428, 0.002, 145.482),
                        InteractMove(108.451, 3.002, 146.467),
                        Vec3(107.286, 3.002, 147.460),
                        Vec3(100.502, 3.002, 147.415),
                        Vec3(97.234, 3.002, 150.688),
                    ],
                ),
            ],
        )


class FirstRoom(SeqList):
    """Routing of first room segment of Torment Peak."""

    def __init__(self: Self) -> None:
        """Initialize a new FirstRoom object."""
        super().__init__(
            name="First room",
            children=[
                SeqCombatAndMove(
                    name="Move past enemies",
                    coords=[
                        Vec3(26.728, 5.002, 36.403),
                        Vec3(23.302, 5.002, 43.818),
                        Vec3(21.771, 5.002, 47.806),
                        Vec3(20.935, 6.010, 67.021),
                        Vec3(18.899, 6.010, 76.710),
                        Vec3(18.899, 6.010, 80.903),
                        Vec3(24.369, 6.002, 82.771),
                        Vec3(23.349, 6.002, 89.874),
                        Vec3(20.072, 6.487, 94.292),
                        Vec3(20.072, 7.010, 98.013),
                        Vec3(21.974, 7.010, 104.817),
                        Vec3(21.974, 7.010, 108.524),
                        Vec3(18.791, 7.010, 111.626),
                        Vec3(13.347, 7.002, 113.644),
                        Vec3(12.879, 7.002, 114.232),
                    ],
                ),
                # TODO(orkaboy): Juke enemies instead
                SeqHoldDirectionDelay("Turn", joy_dir=Vec2(-1, 1), timeout_s=0.1),
                SeqGraplou("Attack enemies", until_combat=True),
                SeqCombatAndMove(
                    name="Move to pillar",
                    coords=[
                        Vec3(11.675, 7.002, 122.052),
                        Vec3(14.904, 7.002, 125.164),
                        Vec3(15.851, 7.002, 133.204),
                        Vec3(18.433, 7.002, 135.543),
                        InteractMove(21.481, 7.002, 135.543),
                        InteractMove(21.481, 7.002, 141.540),
                        InteractMove(16.509, 7.002, 141.540),
                        Vec3(9.460, 7.002, 141.540),
                        InteractMove(5.986, 7.002, 141.540),
                        Vec3(2.264, 8.002, 138.505),
                        Vec3(2.469, 8.002, 134.382),
                    ],
                ),
                SeqInteract("Pillar"),
                SeqMove(
                    name="Navigate moving platforms",
                    coords=[
                        Vec3(2.469, 8.002, 138.560),
                        Vec3(6.540, 7.002, 141.482),
                        InteractMove(10.073, 7.002, 141.482),
                        Vec3(17.476, 7.002, 141.482),
                        InteractMove(21.481, 7.002, 141.482),
                        InteractMove(21.481, 7.002, 138.519),
                        InteractMove(33.481, 7.002, 138.519),
                        InteractMove(33.481, 4.002, 132.460),
                        InteractMove(27.460, 4.002, 132.460),
                        InteractMove(24.461, 3.667, 132.457),
                        InteractMove(24.461, 2.002, 128.394),
                        Vec3(25.416, 2.002, 127.496),
                        Vec3(34.344, 2.002, 127.496),
                        Vec3(37.536, 2.002, 129.519),
                        Vec3(39.540, 2.002, 129.519),
                        InteractMove(42.540, 2.402, 129.519),
                        InteractMove(42.546, 4.002, 132.481),
                        InteractMove(45.806, 4.002, 132.481),
                    ],
                ),
                # TODO(orkaboy): Better juking
                SeqCombatAndMove(
                    name="Juke around enemies",
                    coords=[
                        Vec3(54.137, 4.002, 127.589),
                        Vec3(65.143, 3.010, 120.959),
                        Vec3(60.294, 3.010, 125.546),
                        Vec3(56.356, 3.010, 121.626),
                        Vec3(62.005, 3.002, 116.193),
                        Vec3(68.437, 3.002, 113.369),
                        Vec3(70.112, 3.002, 111.762),
                        InteractMove(72.668, 3.002, 109.367),
                        InteractMove(76.731, 3.002, 109.452),
                    ],
                ),
                SeqMove(
                    name="Navigate platforms",
                    coords=[
                        Vec3(77.670, 3.002, 109.324),
                        Vec3(79.428, 3.002, 107.460),
                        InteractMove(79.428, -2.998, 106.542),
                        Vec3(81.721, -2.998, 106.542),
                        Vec3(83.948, -2.998, 108.699),
                        Vec3(84.515, -2.998, 112.540),
                        Graplou(84.460, -2.403, 121.530, joy_dir=Vec2(0, 1), hold_timer=0.1),
                        Vec3(84.460, 3.002, 122.467),
                        Vec3(87.066, 3.002, 123.520),
                        Vec3(90.174, 3.002, 121.911),
                        InteractMove(92.781, 3.002, 119.510),
                    ],
                ),
                # TODO(orkaboy): Better juking
                SeqCombatAndMove(
                    name="Juke around enemies",
                    coords=[
                        InteractMove(97.073, 3.002, 119.510),
                        Vec3(98.587, 3.002, 121.869),
                        Vec3(98.587, 3.002, 126.828),
                        Vec3(99.861, 3.002, 129.492),
                        InteractMove(99.811, 3.002, 133.223),
                        InteractMove(99.501, 3.002, 138.073),
                    ],
                ),
                # Activate the two pillars to open the door
                ActivatePillars(),
                # Enter the previously locked door
                SeqMove(
                    name="Move to save branch",
                    coords=[
                        HoldDirection(93.000, 5.002, 210.013, joy_dir=Vec2(0, 1)),
                        Vec3(93.000, 5.002, 228.420),
                    ],
                ),
            ],
        )


class SecondRoom(SeqMove):
    """Routing of first room segment of Torment Peak."""

    def __init__(self: Self) -> None:
        """Initialize a new SecondRoom object."""
        super().__init__(
            name="Second room",
            coords=[
                Vec3(93.000, 5.002, 228.420),
                Vec3(98.343, 5.002, 234.393),
                Vec3(100.546, 5.002, 234.237),
                InteractMove(103.398, 4.002, 234.454),
                InteractMove(103.398, -3.998, 233.536),
                Vec3(107.017, -3.998, 229.666),
                InteractMove(110.023, -6.998, 226.918),
                InteractMove(111.126, -9.998, 219.352),
                Vec3(112.257, -9.998, 209.968),
                HoldDirection(386.500, 0.002, 157.117, joy_dir=Vec2(0, -1)),
            ],
        )


class ThirdRoom(SeqList):
    """Routing of third room segment of Torment Peak."""

    def __init__(self: Self) -> None:
        """Initialize a new ThirdRoom object."""
        super().__init__(
            name="Third room",
            children=[
                SeqCombatAndMove(
                    name="Navigate to cavern",
                    coords=[
                        Vec3(381.065, 0.002, 137.485),
                        Vec3(381.092, 0.002, 131.739),
                        InteractMove(378.763, 0.002, 129.315),
                        InteractMove(375.530, 0.002, 126.253),
                        InteractMove(372.437, 0.002, 129.085),
                        InteractMove(369.629, 0.002, 126.124),
                        InteractMove(364.185, 0.002, 126.190),
                        Vec3(356.879, 0.002, 130.527),
                        Vec3(352.955, 0.002, 136.893),
                        Vec3(346.250, 0.002, 136.893),
                        Vec3(344.723, 0.002, 133.457),
                        InteractMove(344.723, -4.998, 130.442),
                        Vec3(356.104, -4.998, 128.028),
                        HoldDirection(360.730, 4.002, 47.730, joy_dir=Vec2(1, 1)),
                    ],
                ),
                SeqCombatAndMove(
                    name="Move to pillar",
                    coords=[
                        Vec3(365.140, 4.002, 51.583),
                        Vec3(367.311, 4.002, 60.121),
                        Vec3(367.238, 4.002, 63.700),
                    ],
                ),
                SeqInteract("Pillar"),
                SeqCombatAndMove(
                    name="Leave cavern",
                    coords=[
                        Vec3(363.775, 4.002, 51.266),
                        Vec3(359.661, 4.002, 47.067),
                        HoldDirection(355.257, -4.998, 126.798, joy_dir=Vec2(-1, -1)),
                    ],
                ),
                SeqMove(
                    name="Navigate platforms",
                    coords=[
                        Vec3(350.249, -4.998, 127.042),
                        Vec3(346.349, -4.998, 123.079),
                        Vec3(344.940, -4.998, 118.564),
                        InteractMove(340.460, -5.257, 118.548),
                        InteractMove(337.519, -7.457, 118.548),
                        InteractMove(334.460, -8.464, 118.548),
                        InteractMove(331.460, -6.498, 118.548),
                        InteractMove(328.119, -4.998, 118.548),
                        Vec3(326.407, -4.998, 117.526),
                        Vec3(325.177, -4.998, 115.892),
                        Vec3(324.667, -4.998, 113.642),
                        Vec3(320.061, -4.998, 113.377),
                    ],
                ),
                SeqClimb(
                    name="Climb wall",
                    coords=[
                        InteractMove(320.282, 4.540, 113.530),
                        Vec3(321.914, 4.540, 113.530),
                        Vec3(321.914, 9.540, 113.530),
                    ],
                ),
                SeqMove(
                    name="Move to chest",
                    coords=[
                        Vec3(321.914, 12.002, 115.084),
                        Vec3(320.403, 12.002, 116.201),
                    ],
                ),
                SeqLoot("Green Leaf"),
                SeqMove(
                    name="Move to monkeys",
                    coords=[
                        Vec3(315.460, 12.002, 116.201),
                        InteractMove(314.193, 2.002, 116.201),
                        Vec3(312.079, 2.002, 118.655),
                        Vec3(309.879, 2.002, 118.764),
                        InteractMove(309.879, -5.998, 116.454),
                        Vec3(306.864, -5.998, 116.471),
                        Vec3(306.574, -5.998, 118.732),
                        Vec3(306.574, -5.998, 124.602),
                        Vec3(305.414, -5.998, 125.530),
                        InteractMove(300.619, -5.998, 125.530),
                        InteractMove(300.619, -5.998, 130.248),
                        InteractMove(286.423, -5.998, 130.248),
                        Vec3(283.238, -5.998, 130.248),
                        InteractMove(283.238, -1.998, 133.467),
                        InteractMove(279.632, 0.002, 133.467),
                        Vec3(271.719, 0.002, 133.467),
                        HoldDirection(257.399, 6.002, 127.000, joy_dir=Vec2(-1, 0)),
                    ],
                ),
                SeqHoldDirectionUntilLostControl("Move to cutscene", joy_dir=Vec2(-1, 0)),
                SeqSkipUntilIdle("Baby Gorillas"),
                SeqMove(
                    name="Move to save branch",
                    coords=[
                        Vec3(238.321, 6.002, 120.370),
                        Vec3(232.208, 6.002, 126.131),
                    ],
                ),
            ],
        )


class GorillaMatriarch(SeqList):
    """Routing of Gorilla Matriarch segment of Torment Peak."""

    def __init__(self: Self) -> None:
        """Initialize a new GorillaMatriarch object."""
        super().__init__(
            name="Gorilla Matriarch",
            children=[
                SeqMove(
                    name="Move to Matriarch",
                    coords=[
                        Vec3(226.703, 6.002, 126.198),
                        HoldDirection(208.106, 15.002, 127.570, joy_dir=Vec2(-1, 0)),
                        Vec3(209.544, 15.002, 126.353),
                        # Jump off ledge to lower level
                        InteractMove(210.632, 5.002, 125.453),
                    ],
                ),
                SeqHoldDirectionUntilLostControl("Move to next room", joy_dir=Vec2(1, 0)),
                SeqSkipUntilIdle("Matriach"),
                SeqMove(
                    name="Move to whirlpool",
                    coords=[
                        InteractMove(247.538, 2.303, 74.542),
                        Vec3(247.538, 2.303, 71.839),
                    ],
                ),
                SeqInteract("Whirlpool"),
                SeqMove(
                    name="Underwater segment",
                    coords=[
                        Vec3(201.417, 1.303, 37.126),
                        Vec3(217.356, 1.303, 41.908),
                    ],
                ),
                SeqInteract("Whirlpool"),
                SeqMove(
                    name="Get out of water",
                    coords=[
                        InteractMove(247.502, 5.002, 21.483),
                    ],
                ),
                SeqHoldDirectionUntilLostControl("Move to cutscene", joy_dir=Vec2(0, 1)),
            ],
        )


class DwellerOfTorment(SeqList):
    """Routing of Dweller of Torment segment of Torment Peak."""

    def __init__(self: Self) -> None:
        """Initialize a new DwellerOfTorment object."""
        super().__init__(
            name="Dweller of Torment",
            children=[
                SeqHoldDirectionUntilCombat("Come forth, Dweller!", joy_dir=Vec2(0, 1)),
                # TODO(orkaboy): Need custom combat controller (cutscene)
                SeqCombat("Dweller of Torment"),
                # Cutscene ends on world map
                SeqSkipUntilClose("The Cleansing", coord=Vec3(237.484, 3.000, 77.218)),
            ],
        )


class VialPuzzle(SeqBase):
    """Sequencer node to solve the Vial of Time puzzle."""

    class FSM(Enum):
        """Finite State Machine states."""

        START_DELAY = auto()
        NAVIGATE_TO_TILE = auto()
        ROTATE_TILE = auto()
        DELAY = auto()

    # Delay before starting sequence (time it takes for puzzle to activate)
    START_DELAY_TIME = 1.2
    # Delay after rotating a tile
    DELAY_TIME = 0.5

    # Coordinate system is [0, 0] in lower left corner
    # Each entry in the STEPS list indicates to rotate a tile at that coordinate
    STEPS: list[Vec2] = [
        Vec2(0, 0),
        Vec2(0, 0),
        Vec2(0, 0),
        Vec2(0, 1),
        Vec2(0, 1),
        Vec2(0, 2),
        Vec2(0, 2),
        Vec2(0, 2),
        Vec2(1, 2),
        Vec2(1, 2),
        Vec2(2, 2),
        Vec2(2, 1),
        Vec2(2, 1),
        Vec2(2, 0),
        Vec2(2, 0),
        Vec2(1, 0),
        Vec2(1, 1),
        Vec2(1, 1),
        Vec2(1, 1),
    ]

    def __init__(self: Self) -> None:
        """Initialize a new VialPuzzle object."""
        super().__init__(
            name="Vial Puzzle",
        )
        self.timer = 0.0
        self.step = 0
        self.state = VialPuzzle.FSM.START_DELAY
        self.position: Vec2 = Vec2(0, 0)

    def execute(self: Self, delta: float) -> bool:
        # Get the current rotation instruction, or end sequence
        if self.step >= len(self.STEPS):
            logger.info("Completed VialPuzzle sequence.")
            return True
        cur_step = self.STEPS[self.step]

        ctrl = sos_ctrl()

        match self.state:
            # Wait for control when activating the puzzle
            case VialPuzzle.FSM.START_DELAY:
                self.timer += delta
                # Check if we have should have control yet, if so, select first tile
                if self.timer >= self.START_DELAY_TIME:
                    self.timer = 0.0
                    self.state = VialPuzzle.FSM.NAVIGATE_TO_TILE
            # Navigate to the correct coordinate
            case VialPuzzle.FSM.NAVIGATE_TO_TILE:
                if self.position.x < cur_step.x:
                    ctrl.dpad.tap_right()
                    self.position.x += 1
                elif self.position.x > cur_step.x:
                    ctrl.dpad.tap_left()
                    self.position.x -= 1
                elif self.position.y < cur_step.y:
                    ctrl.dpad.tap_up()
                    self.position.y += 1
                elif self.position.y > cur_step.y:
                    ctrl.dpad.tap_down()
                    self.position.y -= 1
                else:
                    # We are already at the correct coordinate
                    self.state = VialPuzzle.FSM.ROTATE_TILE
            # Rotate the tile, once, and advance to the next step in the sequence
            case VialPuzzle.FSM.ROTATE_TILE:
                ctrl.confirm()
                self.state = VialPuzzle.FSM.DELAY
                self.step += 1
            # Wait until puzzle can be interacted with again
            case VialPuzzle.FSM.DELAY:
                self.timer += delta
                if self.timer >= self.DELAY_TIME:
                    self.timer = 0.0
                    # Select the next tile
                    self.state = VialPuzzle.FSM.NAVIGATE_TO_TILE
        return False

    def __repr__(self: Self) -> str:
        return f"VialPuzzle step {self.step}/{len(self.STEPS)}"


class TheVialOfTime(SeqList):
    """Routing of The Vial of Time segment of Torment Peak."""

    def __init__(self: Self) -> None:
        """Initialize a new TheVialOfTime object."""
        super().__init__(
            name="The Vial of Time",
            children=[
                SeqMove(
                    name="Move to Mossy Cache",
                    coords=[
                        InteractMove(237.500, 3.002, 75.000),
                        Vec3(238.500, 3.002, 75.000),
                        Vec3(238.500, 3.002, 73.000),
                        Vec3(239.000, 3.002, 73.000),
                    ],
                ),
                SeqChangeTimeOfDay("Reveal secret", time_target=14.5),
                SeqMove(
                    name="Move to Mossy Cache",
                    coords=[
                        Vec3(239.000, 3.002, 72.000),
                        Vec3(243.500, 3.002, 72.000),
                        Vec3(243.500, 3.002, 72.500),
                    ],
                ),
                SeqInteract("Mossy Cache"),
                SeqCheckpoint("TEMP_VIAL"),
                SeqMove(
                    name="Move to Puzzle",
                    coords=[
                        Vec3(33.000, 8.002, 19.340),
                    ],
                ),
                SeqInteract("Start puzzle"),
                VialPuzzle(),
                SeqMove(
                    name="Move to vial",
                    coords=[
                        Vec3(34.303, 8.002, 19.200),
                        Vec3(34.303, 8.002, 34.113),
                        Vec3(32.603, 8.002, 42.546),
                        InteractMove(32.603, 17.002, 45.467),
                        Vec3(32.417, 17.002, 46.394),
                    ],
                ),
                SeqLoot("Vial of Time"),
                SeqMove(
                    name="Move to Lake Doccaria",
                    coords=[
                        InteractMove(32.420, 8.002, 42.275),
                        Vec3(31.701, 8.002, 21.785),
                        Vec3(31.701, 8.002, 18.960),
                        Vec3(32.757, 8.002, 13.492),
                        Vec3(32.757, 6.010, -1.430),
                        HoldDirection(243.500, 3.002, 71.998, joy_dir=Vec2(0, -1)),
                        Vec3(239.500, 3.002, 72.000),
                        Vec3(239.000, 3.002, 72.000),
                        Vec3(239.000, 3.002, 72.500),
                        Vec3(237.500, 3.002, 72.500),
                        Vec3(237.500, 3.002, 71.000),
                    ],
                ),
                SeqInteract("Lake Doccaria"),
                SeqMove(
                    name="Move to portal",
                    coords=[
                        Vec3(54.750, 48.002, 79.460),
                        InteractMove(58.246, 40.803, 66.676),
                        Vec3(61.453, 40.803, 63.112),
                        Vec3(63.453, 40.803, 63.137),
                        InteractMove(63.454, 43.002, 64.467),
                        Vec3(63.419, 43.002, 67.097),
                    ],
                ),
                SeqSelectOption("Archives", skip_dialog_check=True),
                # Cutscene into boat movement
                SeqBoat(
                    name="Resh'an joins",
                    coords=[
                        Vec3(237.500, 0.500, 55.000),
                    ],
                    hold_skip=True,
                ),
                SeqBoat(
                    name="On to Mesa Island",
                    coords=[
                        Vec3(260.709, 0.500, 72.606),
                        Vec3(261.326, 0.500, 132.289),
                        Vec3(247.700, 0.500, 155.610),
                    ],
                ),
                SeqInteract("Disembark"),
            ],
        )


class TormentPeak(SeqList):
    """Routing of Torment Peak segment of Watcher Island."""

    def __init__(self: Self) -> None:
        """Initialize a new TormentPeak object."""
        super().__init__(
            name="Torment Peak",
            children=[
                OnToTormentPeak(),
                SeqCheckpoint("torment_peak"),
                FirstRoom(),
                SeqCheckpoint("torment_peak2"),
                SecondRoom(),
                ThirdRoom(),
                SeqCheckpoint(
                    "torment_peak3",
                    return_path=SeqMove(
                        name="Back to route",
                        coords=[
                            Vec3(239.050, 6.002, 126.198),
                        ],
                    ),
                ),
                GorillaMatriarch(),
                DwellerOfTorment(),
                TheVialOfTime(),
            ],
        )
