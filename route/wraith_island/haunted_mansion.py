"""Routing of Haunted Mansion and Dweller of Woe section of Wraith Island."""

import logging
from enum import Enum, auto
from typing import Self

from control import sos_ctrl
from engine.combat import SeqCombat, SeqCombatAndMove
from engine.inventory.items import ARMORS, VALUABLES
from engine.mathlib import Vec2, Vec3
from engine.seq import (
    Graplou,
    HoldDirection,
    InteractMove,
    SeqBase,
    SeqBlackboard,
    SeqCheckpoint,
    SeqCliffMove,
    SeqClimb,
    SeqGraplou,
    SeqHoldDirectionDelay,
    SeqHoldDirectionUntilCombat,
    SeqHoldDirectionUntilLostControl,
    SeqInteract,
    SeqList,
    SeqLoot,
    SeqMashUntilIdle,
    SeqMove,
    SeqRouteBranch,
    SeqSelectOption,
    SeqSkipUntilCombat,
    SeqSkipUntilIdle,
)
from memory.combat_manager import PlayerPartyCharacter

logger = logging.getLogger(__name__)


class HeadToMansion(SeqList):
    """Routing of path to get to Haunted Mansion."""

    def __init__(self: Self) -> None:
        """Initialize a new HeadToMansion object."""
        super().__init__(
            name="Head to Mansion",
            children=[
                SeqMove(
                    name="Move to Moraine",
                    coords=[
                        Vec3(35.837, 1.002, 116.869),
                    ],
                ),
                SeqSelectOption("Leave"),
                SeqSkipUntilIdle("The Eclipse begins", hold_cancel=True),
            ],
        )


class RightWing(SeqList):
    """Routing of path through right wing of Haunted Mansion."""

    def __init__(self: Self) -> None:
        """Initialize a new RightWing object."""
        super().__init__(
            name="Right Wing",
            children=[
                # Optionally, grab a chest
                SeqRouteBranch(
                    name="Loot Obsidian Ingot",
                    route=["hm_obsidian_ingot"],
                    when_true=SeqList(
                        name="Secret passage",
                        children=[
                            SeqMove(
                                name="Move to Chandelier",
                                coords=[
                                    Vec3(15.128, 6.010, -11.378),
                                    Vec3(21.481, 6.010, -1.679),
                                ],
                            ),
                            SeqInteract("Chandelier"),
                            SeqMove(
                                name="Move to secret passage",
                                coords=[
                                    Vec3(20.594, 6.002, -0.456),
                                ],
                            ),
                            SeqSelectOption("Secret passage"),
                            SeqMove(
                                name="Move to chest",
                                coords=[
                                    Vec3(26.429, 10.002, -13.152),
                                ],
                            ),
                            SeqLoot(name="Obsidian Ingot", item=VALUABLES.ObsidianIngot),
                            SeqMove(
                                name="Return to path",
                                coords=[
                                    InteractMove(27.126, 1.002, -15.461),
                                ],
                            ),
                        ],
                    ),
                    when_false=SeqMove(
                        name="Move to door",
                        coords=[
                            Vec3(18.681, 1.002, -23.964),
                            Vec3(28.002, 1.002, -14.479),
                        ],
                    ),
                ),
                SeqMove(
                    name="Go into right wing",
                    coords=[
                        Vec3(28.002, 1.002, -11.902),
                        HoldDirection(70.000, 1.002, 21.000, joy_dir=Vec2(0, 1)),
                    ],
                ),
                SeqHoldDirectionUntilLostControl("Move to cutscene", joy_dir=Vec2(0, 1)),
                SeqSkipUntilIdle("Seraï joins"),
                SeqMove(
                    name="",
                    coords=[
                        Vec3(70.100, 1.002, 46.028),
                        HoldDirection(104.000, 1.002, 84.000, joy_dir=Vec2(1, 1)),
                        Vec3(115.930, 1.002, 89.426),
                        Vec3(116.472, 1.002, 92.592),
                    ],
                ),
                SeqCheckpoint("haunted_mansion"),
                # TODO(orkaboy): Better juking
                SeqCombatAndMove(
                    name="Juke enemies",
                    coords=[
                        Vec3(123.076, 1.002, 93.144),
                        Vec3(127.318, 1.002, 88.936),
                        Vec3(132.178, 1.002, 88.534),
                        Vec3(134.416, 1.002, 93.443),
                        HoldDirection(168.167, 1.002, 86.056, joy_dir=Vec2(1, 1)),
                    ],
                ),
                # TODO(orkaboy): Better juking
                SeqCombatAndMove(
                    name="Move to torch",
                    coords=[
                        Vec3(171.051, 1.002, 88.876),
                        Vec3(171.122, 1.002, 97.983),
                        Vec3(176.290, 1.002, 103.029),
                        Vec3(176.334, 1.002, 104.540),
                    ],
                ),
                SeqInteract("Torch"),
                SeqCombatAndMove(
                    name="Move to secret passage",
                    coords=[
                        Vec3(176.638, 1.002, 103.043),
                        Vec3(181.923, 1.002, 103.043),
                        Vec3(181.923, 1.002, 104.540),
                    ],
                ),
                SeqInteract("Secret passage"),
                SeqMove(
                    name="Move to lever",
                    coords=[
                        Vec3(0.959, 10.002, -13.000),
                    ],
                ),
                SeqInteract("Lever"),
                SeqMove(
                    name="Move to left wing",
                    coords=[
                        Vec3(1.491, 10.002, -14.266),
                        InteractMove(1.500, 1.002, -16.253),
                        Vec3(0.050, 1.002, -16.253),
                        Vec3(0.050, 1.002, -11.751),
                        HoldDirection(-36.000, 1.002, 22.200, joy_dir=Vec2(0, 1)),
                    ],
                ),
            ],
        )


class MakeMeASandwich(SeqList):
    """Routing of sandwich-making section of Haunted Mansion."""

    def __init__(self: Self) -> None:
        """Initialize a new MakeMeASandwich object."""
        super().__init__(
            name="Make me a sandwich",
            children=[
                SeqInteract("Talk to ghost"),
                SeqSkipUntilIdle("I crave sandwich"),
                SeqMove(
                    name="Move into kitchen",
                    coords=[
                        Vec3(-65.648, 1.002, 100.037),
                        HoldDirection(-100.000, 1.002, 85.000, joy_dir=Vec2(-1, 1)),
                    ],
                ),
                SeqHoldDirectionUntilLostControl("Move to cutscene", joy_dir=Vec2(-1, 1)),
                SeqSkipUntilIdle("I'll just wait here"),
                SeqMove(
                    name="Move to rust",
                    coords=[
                        Vec3(-98.458, 1.002, 91.533),
                    ],
                ),
                SeqSelectOption("Rust", option=0, skip_dialog_check=True),
                SeqMove(
                    name="Move to Loaf of Dread",
                    coords=[
                        Vec3(-100.291, 1.002, 91.533),
                        Vec3(-104.024, 1.002, 94.699),
                        Vec3(-104.024, 1.002, 96.540),
                    ],
                ),
                SeqSelectOption("Loaf of Dread", option=1, skip_dialog_check=True),
                SeqMove(
                    name="Move to sugar",
                    coords=[
                        Vec3(-105.546, 1.002, 92.470),
                    ],
                ),
                SeqSelectOption("Sugar", option=2, skip_dialog_check=True),
                SeqMove(
                    name="Move to dust",
                    coords=[
                        Vec3(-105.546, 1.002, 90.911),
                        Vec3(-108.200, 1.002, 89.457),
                        Vec3(-110.094, 1.002, 89.889),
                        Vec3(-110.522, 1.002, 90.350),
                    ],
                ),
                SeqSelectOption("Dust", option=3, skip_dialog_check=True),
                SeqMove(
                    name="Move to Hepar",
                    coords=[
                        Vec3(-106.271, 1.002, 83.458),
                    ],
                ),
                SeqSelectOption("Hepar", option=1, skip_dialog_check=True),
                SeqMove(
                    name="Move to cook",
                    coords=[
                        Vec3(-102.284, 1.002, 93.717),
                    ],
                ),
                SeqSelectOption("Let him cook", skip_dialog_check=True),
                SeqMashUntilIdle("Let him cook"),
                SeqMove(
                    name="Move to ghost",
                    coords=[
                        Vec3(-100.463, 1.002, 85.880),
                        HoldDirection(-64.777, 1.002, 99.649, joy_dir=Vec2(1, -1)),
                        Vec3(-56.938, 1.002, 100.669),
                    ],
                ),
                SeqSelectOption("Here's your sandwich", skip_dialog_check=True),
                SeqMashUntilIdle("Nom nom nom"),
            ],
        )


class SkullPuzzleFlip(SeqBase):
    """Node to flip skulls as part of the library puzzle."""

    FLIP_DELAY = 0.5

    class FSM(Enum):
        """Finite State Machine states."""

        FLIP = auto()
        WAIT = auto()

    def __init__(self: Self, name: str, num_flips: int) -> None:
        """Initialize a SkullPuzzleFlip object."""
        super().__init__(name)
        self.num_flips = num_flips
        self.step = 0
        self.state = SkullPuzzleFlip.FSM.FLIP
        self.timer = 0.0

    def execute(self: Self, delta: float) -> bool:
        if self.step < self.num_flips:
            ctrl = sos_ctrl()
            match self.state:
                case SkullPuzzleFlip.FSM.FLIP:
                    self.step += 1
                    ctrl.confirm()
                    self.state = SkullPuzzleFlip.FSM.WAIT
                case SkullPuzzleFlip.FSM.WAIT:
                    self.timer += delta
                    if self.timer >= SkullPuzzleFlip.FLIP_DELAY:
                        self.timer = 0.0
                        self.state = SkullPuzzleFlip.FSM.FLIP
            return False
        return True

    def __repr__(self: Self) -> str:
        return f"SkullPuzzleFlip({self.name}): Flipping {self.step + 1}/{self.num_flips}"


class Library(SeqList):
    """Routing of path through library of Haunted Mansion."""

    def __init__(self: Self) -> None:
        """Initialize a new Library object."""
        super().__init__(
            name="Library",
            children=[
                SeqCombatAndMove(
                    name="Move to right statue",
                    coords=[
                        Vec3(-58.038, 1.002, 191.313),
                        Vec3(-47.484, 1.002, 191.313),
                        Vec3(-41.560, 1.002, 196.725),
                        Vec3(-35.329, 1.002, 196.725),
                        Vec3(-34.979, 1.002, 200.982),
                    ],
                ),
                SeqSelectOption("Take helmet", skip_dialog_check=True),
                SeqCombatAndMove(
                    name="Move to left statue",
                    coords=[
                        Vec3(-40.493, 1.002, 195.347),
                        Vec3(-50.049, 1.002, 191.377),
                        Vec3(-58.297, 1.002, 191.377),
                        Vec3(-62.562, 1.002, 197.588),
                        Vec3(-69.444, 1.002, 201.336),
                        Vec3(-76.879, 1.002, 206.943),
                    ],
                ),
                SeqSelectOption("Place helmet", skip_dialog_check=True),
                SeqCombatAndMove(
                    name="Move to crown",
                    coords=[
                        Vec3(-82.556, 1.002, 203.363),
                        Vec3(-84.325, 1.002, 204.542),
                        InteractMove(-84.500, 10.002, 205.467),
                        Vec3(-85.724, 10.002, 206.580),
                        Vec3(-87.352, 10.002, 206.580),
                        Vec3(-92.431, 10.002, 202.648),
                    ],
                ),
                SeqLoot("Crown"),
                SeqCliffMove(
                    name="Cross beam(L)",
                    coords=[
                        Vec3(-87.551, 10.002, 206.500),
                        Vec3(-81.742, 10.000, 206.500),
                        InteractMove(-78.252, 10.002, 206.500),
                    ],
                ),
                SeqMove(
                    name="Move across gap",
                    coords=[
                        Vec3(-71.300, 10.002, 203.848),
                        Vec3(-69.630, 10.002, 201.648),
                        Graplou(-58.200, 10.010, 199.600, joy_dir=Vec2(1, 0), hold_timer=0.1),
                    ],
                ),
                SeqCliffMove(
                    name="Cross beam(R)",
                    coords=[
                        Vec3(-58.200, 10.010, 201.178),
                        Vec3(-52.710, 10.002, 206.420),
                        Vec3(-47.855, 10.000, 206.490),
                        InteractMove(-44.227, 10.002, 206.490),
                    ],
                ),
                SeqCombatAndMove(
                    name="Move to right statue",
                    coords=[
                        Vec3(-39.532, 10.002, 205.821),
                        Vec3(-32.726, 10.002, 198.983),
                        InteractMove(-32.892, 1.002, 194.755),
                        Vec3(-34.245, 1.002, 195.179),
                        Vec3(-34.298, 1.002, 200.823),
                    ],
                ),
                SeqSelectOption("Place crown", skip_dialog_check=True),
                # Skull puzzle
                SeqCombatAndMove(
                    name="Move to first skull",
                    coords=[
                        Vec3(-34.235, 1.002, 195.179),
                        Vec3(-32.786, 1.002, 195.179),
                        InteractMove(-32.800, 10.002, 198.926),
                    ],
                ),
                SeqMove(
                    name="Between skulls",
                    coords=[
                        Vec3(-42.594, 10.002, 207.540),
                    ],
                    precision=0.1,
                ),
                SeqHoldDirectionDelay("Turn", joy_dir=Vec2(0, 1), timeout_s=0.1),
                SkullPuzzleFlip("R1&2", num_flips=2),
                SeqCliffMove(
                    name="Move to third skull",
                    coords=[
                        Vec3(-44.383, 10.002, 206.500),
                        Vec3(-46.323, 10.000, 206.500),
                        InteractMove(-49.539, 10.002, 206.500),
                    ],
                ),
                SeqMove(
                    name="Between skulls",
                    coords=[
                        Vec3(-51.510, 10.002, 207.546),
                    ],
                    precision=0.1,
                ),
                SeqHoldDirectionDelay("Turn", joy_dir=Vec2(0, 1), timeout_s=0.1),
                SkullPuzzleFlip("R3&4", num_flips=2),
                SeqMove(
                    name="Move to fifth skull",
                    coords=[
                        Vec3(-58.807, 10.002, 201.421),
                        Graplou(-70.200, 10.010, 199.500, joy_dir=Vec2(-1, 0), hold_timer=0.1),
                        Vec3(-70.200, 10.010, 201.058),
                    ],
                ),
                SeqMove(
                    name="Between skulls",
                    coords=[
                        Vec3(-76.999, 10.002, 207.546),
                        Vec3(-76.358, 10.002, 207.546),
                    ],
                    precision=0.1,
                ),
                SeqHoldDirectionDelay("Turn", joy_dir=Vec2(0, 1), timeout_s=0.1),
                SkullPuzzleFlip("L1&L2", num_flips=1),
                SeqMove(
                    name="Move to sixth skull",
                    coords=[
                        Vec3(-77.733, 10.002, 207.540),
                    ],
                ),
                SkullPuzzleFlip("L2", num_flips=1),
                SeqCliffMove(
                    name="Move to seventh skull",
                    coords=[
                        Vec3(-78.025, 10.002, 206.500),
                        Vec3(-80.156, 10.000, 206.500),
                        InteractMove(-83.881, 10.002, 206.487),
                        Vec3(-84.051, 10.002, 207.543),
                    ],
                ),
                SkullPuzzleFlip("L3", num_flips=1),
                SeqMove(
                    name="Move to eight skull",
                    coords=[
                        Vec3(-85.867, 10.002, 207.546),
                        Vec3(-85.426, 10.002, 207.546),
                    ],
                    precision=0.1,
                ),
                SeqHoldDirectionDelay("Turn", joy_dir=Vec2(0, 1), timeout_s=0.1),
                SkullPuzzleFlip("L3&L4", num_flips=2),
                SeqCliffMove(
                    name="Move to combo scroll",
                    coords=[
                        Vec3(-84.062, 10.002, 206.469),
                        Vec3(-81.589, 10.000, 206.500),
                        InteractMove(-78.194, 10.002, 206.500),
                        Vec3(-75.234, 10.002, 206.500),
                        Vec3(-70.059, 10.002, 201.563),
                        InteractMove(-65.542, 1.002, 201.563),
                        Vec3(-64.710, 1.002, 201.398),
                    ],
                ),
                SeqLoot("X-Strike"),
                SeqBlackboard("X-Strike", key="x_strike", value=True),
            ],
        )


class SecretTunnel(SeqList):
    """Routing of path through secret tunnel in Haunted Mansion."""

    def __init__(self: Self) -> None:
        """Initialize a new SecretTunnel object."""
        super().__init__(
            name="Secret Tunnel",
            children=[
                SeqCombatAndMove(
                    name="Enter right corridor",
                    coords=[
                        Vec3(-58.074, 1.002, 201.083),
                        Vec3(-52.599, 1.002, 206.453),
                        Vec3(-41.697, 1.002, 205.997),
                        Vec3(-36.714, 1.002, 204.052),
                        HoldDirection(-141.922, 22.002, 273.992, joy_dir=Vec2(1, 1)),
                        Vec3(-140.093, 22.002, 275.737),
                        Vec3(-130.988, 22.002, 275.737),
                        Vec3(-114.267, 14.002, 258.847),
                        Vec3(-111.176, 14.002, 255.727),
                    ],
                ),
                SeqHoldDirectionDelay("Turn", joy_dir=Vec2(1, 1), timeout_s=0.1),
                SeqGraplou("Grab wall"),
                SeqClimb(
                    name="Climb wall",
                    coords=[
                        Vec3(-109.812, 21.586, 257.147),
                        Vec3(-110.651, 21.298, 257.986),
                    ],
                ),
                SeqMove(
                    name="Graplou across gap",
                    coords=[
                        Vec3(-113.106, 21.002, 256.167),
                        Graplou(-103.000, 21.010, 247.000, joy_dir=Vec2(1, -1), hold_timer=0.1),
                    ],
                    precision2=2,
                ),
                SeqMove(
                    name="Move to chest",
                    coords=[
                        Vec3(-100.819, 21.002, 244.831),
                        InteractMove(-100.170, 14.002, 244.182),
                        Vec3(-102.038, 14.002, 246.043),
                    ],
                ),
                SeqLoot(
                    "Spectral Cape", item=ARMORS.SpectralCape, equip_to=PlayerPartyCharacter.Garl
                ),
                SeqMove(
                    name="Grab wall",
                    coords=[
                        Graplou(-97.875, 14.411, 245.209, joy_dir=Vec2(1, 0), hold_timer=0.1),
                    ],
                ),
                SeqClimb(
                    name="Climb wall",
                    coords=[
                        Vec3(-97.357, 23.851, 244.693),
                        Vec3(-88.365, 24.023, 235.698),
                    ],
                ),
                SeqMove(
                    name="Enter ball room",
                    coords=[
                        Vec3(-88.183, 22.002, 233.834),
                        HoldDirection(124.000, 1.002, 142.000, joy_dir=Vec2(0, -1)),
                        Vec3(119.848, 1.002, 142.000),
                        Vec3(117.898, 1.002, 149.858),
                        Vec3(109.282, 1.002, 153.187),
                        HoldDirection(117.542, 1.002, 193.056, joy_dir=Vec2(0, 1)),
                    ],
                ),
            ],
        )


class LeftWing(SeqList):
    """Routing of path through left wing of Haunted Mansion."""

    def __init__(self: Self) -> None:
        """Initialize a new LeftWing object."""
        super().__init__(
            name="Left Wing",
            children=[
                SeqMove(
                    name="Move to left wing",
                    coords=[
                        Vec3(-36.000, 1.002, 45.686),
                        HoldDirection(-47.971, 1.002, 85.971, joy_dir=Vec2(-1, 1)),
                    ],
                ),
                SeqGraplou(),
                SeqCombatAndMove(
                    name="Move to ghost",
                    coords=[
                        Vec3(-62.443, 1.002, 92.936),
                        Vec3(-62.443, 1.002, 97.423),
                        Vec3(-57.241, 1.002, 100.993),
                    ],
                ),
                # Kitchen section
                MakeMeASandwich(),
                SeqMove(
                    name="Move to library",
                    coords=[
                        Vec3(-54.052, 1.002, 101.767),
                        HoldDirection(-62.917, 1.002, 130.364, joy_dir=Vec2(0, 1)),
                        Vec3(-62.917, 1.002, 133.265),
                        Vec3(-48.665, 1.002, 152.629),
                        HoldDirection(-63.958, 1.002, 186.600, joy_dir=Vec2(0, 1)),
                    ],
                ),
                # Library section
                Library(),
                # Tunnel section
                SecretTunnel(),
                # Ballroom section
                SeqHoldDirectionDelay("Turn", joy_dir=Vec2(1, 1), timeout_s=0.1),
                SeqGraplou("Grab enemy", until_combat=True),
                SeqCombatAndMove(
                    name="Fight Waltzers",
                    coords=[
                        Vec3(113.645, 1.002, 198.903),
                    ],
                ),
                SeqGraplou("Grab enemy", until_combat=True),
                SeqCombatAndMove(
                    name="Fight Waltzers",
                    coords=[
                        Vec3(115.422, 1.002, 204.335),
                    ],
                ),
                SeqInteract("Granny ghost"),
                SeqSkipUntilIdle("Granny ghost"),
                SeqMove(
                    name="Move to garden",
                    coords=[
                        Vec3(86.584, 1.002, 204.335),
                        HoldDirection(62.000, 1.002, 216.058, joy_dir=Vec2(-1, 1)),
                        Vec3(59.488, 1.002, 217.973),
                        Vec3(48.973, 1.002, 217.973),
                        HoldDirection(46.387, 1.002, 145.293, joy_dir=Vec2(-1, -1)),
                    ],
                ),
            ],
        )


class Garden(SeqList):
    """Routing of Garden section of Haunted Mansion."""

    def __init__(self: Self) -> None:
        """Initialize a new Garden object."""
        super().__init__(
            name="Garden",
            children=[
                # Right Boulbe
                SeqMove(
                    name="Move through maze",
                    coords=[
                        Vec3(27.402, 1.002, 145.293),
                        Vec3(25.066, 1.002, 147.565),
                        Vec3(25.066, 1.002, 155.787),
                        Vec3(28.655, 1.002, 157.689),
                        Vec3(28.655, 1.002, 162.767),
                        Vec3(25.241, 1.002, 164.672),
                        Vec3(25.241, 1.002, 168.433),
                        Vec3(32.407, 1.002, 167.053),
                        Vec3(33.548, 1.002, 164.430),
                        Vec3(43.588, 1.002, 164.430),
                        Vec3(43.588, 1.002, 167.048),
                        Vec3(36.411, 1.002, 168.446),
                        Vec3(36.362, 1.002, 171.522),
                        Vec3(41.688, 1.002, 173.302),
                        Vec3(41.876, 1.002, 176.210),
                    ],
                ),
                SeqGraplou("Attack enemy", until_combat=True),
                SeqCombatAndMove(
                    name="Clearing weeds",
                    coords=[
                        Vec3(32.385, 1.002, 180.989),
                        Vec3(25.324, 1.002, 180.989),
                        Vec3(24.364, 1.002, 172.334),
                        Vec3(22.493, 1.002, 169.067),
                        Vec3(19.566, 1.002, 168.188),
                        Vec3(17.549, 1.002, 168.188),
                        Vec3(16.551, 1.002, 173.557),
                        Vec3(11.269, 1.002, 173.541),
                        Vec3(11.269, 1.002, 174.895),
                    ],
                ),
                SeqGraplou("Attack enemy", until_combat=True),
                SeqCombatAndMove(
                    name="Clearing weeds",
                    coords=[
                        Vec3(12.085, 1.002, 182.295),
                    ],
                ),
                # Before Botanical Horror
                SeqCheckpoint("haunted_mansion2"),
                SeqMove(
                    name="Move to greenhouse",
                    coords=[
                        Vec3(21.485, 1.002, 181.846),
                        Vec3(24.945, 1.002, 184.639),
                    ],
                ),
                SeqHoldDirectionUntilCombat(
                    "Enter greenhouse",
                    joy_dir=Vec2(0, 1),
                ),
                SeqCombat("Botanical Horror", level_up_timeout=10.0),
                SeqSkipUntilIdle("Weeds whacked"),
                SeqMove(
                    name="Leave greenhouse",
                    coords=[
                        Vec3(28.593, 1.002, 257.763),
                    ],
                ),
                SeqHoldDirectionUntilLostControl("Leave greenhouse", joy_dir=Vec2(0, -1)),
                SeqSkipUntilIdle("Seraï leaves party"),
                SeqMove(
                    name="Move to shortcut",
                    coords=[
                        Vec3(25.014, 1.002, 180.197),
                        Vec3(25.587, 1.002, 164.504),
                        Vec3(28.519, 1.002, 162.352),
                        Vec3(28.519, 1.002, 157.425),
                        Vec3(25.477, 1.002, 155.417),
                        Vec3(25.446, 1.002, 146.396),
                        Vec3(45.930, 1.002, 146.396),
                        HoldDirection(47.000, 1.002, 216.000, joy_dir=Vec2(1, 1)),
                        Vec3(48.492, 1.002, 217.312),
                        Vec3(60.130, 1.002, 217.312),
                        HoldDirection(87.132, 1.002, 203.868, joy_dir=Vec2(1, -1)),
                        Vec3(117.301, 1.002, 195.240),
                        HoldDirection(109.000, 1.002, 155.500, joy_dir=Vec2(0, -1)),
                        Vec3(109.000, 1.002, 153.433),
                        Vec3(117.858, 1.002, 148.705),
                        Vec3(120.211, 1.002, 143.474),
                        Vec3(123.055, 1.002, 136.590),
                        Vec3(123.750, 1.002, 125.449),
                    ],
                ),
                SeqInteract("Open shortcut"),
                SeqSkipUntilIdle("Open shortcut"),
                SeqMove(
                    name="Move to save point",
                    coords=[
                        HoldDirection(123.850, 1.002, 97.126, joy_dir=Vec2(0, -1)),
                        Vec3(120.410, 1.002, 93.506),
                        Vec3(116.299, 1.002, 93.506),
                    ],
                ),
            ],
        )


class MissionGarl(SeqList):
    """Routing of Garl's section of Dweller of Woe."""

    def __init__(self: Self) -> None:
        """Initialize a new MissionGarl object."""
        super().__init__(
            name="Mission: Garl",
            children=[
                SeqMove(
                    name="Go to ladder",
                    coords=[
                        Vec3(15.939, 1.002, 47.307),
                        Vec3(17.020, 1.002, 44.888),
                        Vec3(19.540, 1.002, 44.888),
                    ],
                ),
                SeqClimb(
                    name="Climb to roof",
                    coords=[
                        InteractMove(19.542, 5.540, 45.530),
                        HoldDirection(75.530, 12.002, 93.370, joy_dir=Vec2(0, 1)),
                    ],
                ),
                SeqSkipUntilIdle("Let's do this!"),
                SeqMove(
                    name="Move to rubble #1",
                    coords=[
                        Vec3(67.363, 12.002, 96.727),
                    ],
                ),
                SeqInteract("Rubble #1"),
                SeqSkipUntilIdle("Rubble #1"),
                SeqMove(
                    name="Move to rubble #2",
                    coords=[
                        Vec3(67.150, 12.002, 90.626),
                        Vec3(67.150, 12.002, 89.443),
                        Vec3(68.860, 12.002, 88.452),
                    ],
                ),
                SeqInteract("Rubble #2"),
                SeqSkipUntilIdle("Rubble #2"),
                SeqMove(
                    name="Move to rubble #3",
                    coords=[
                        Vec3(61.787, 12.002, 91.872),
                        Vec3(60.124, 12.002, 95.233),
                    ],
                ),
                SeqInteract("Rubble #3"),
                SeqSkipUntilIdle("Rubble #3"),
                SeqMove(
                    name="Move to rubble #4",
                    coords=[
                        Vec3(63.202, 12.002, 98.628),
                    ],
                ),
                SeqInteract("Rubble #4"),
                SeqBlackboard("Cooker Surprise", key="cooker_surprise", value=True),
                SeqSkipUntilCombat("Garl's Cooker Surprise"),
            ],
        )


class DwellerOfWoe(SeqList):
    """Routing of Dweller of Woe section of Haunted Mansion."""

    def __init__(self: Self) -> None:
        """Initialize a new HauntedMansion object."""
        super().__init__(
            name="Dweller of Woe",
            children=[
                SeqMove(
                    name="Go to hub area",
                    coords=[
                        Vec3(109.991, 1.002, 92.854),
                        Vec3(104.050, 1.002, 84.236),
                        HoldDirection(70.434, 1.002, 46.434, joy_dir=Vec2(-1, -1)),
                        Vec3(70.077, 1.002, 20.401),
                        HoldDirection(28.000, 1.002, -12.734, joy_dir=Vec2(0, -1)),
                        Vec3(19.711, 1.002, -22.859),
                        Vec3(16.601, 1.002, -22.859),
                        Vec3(14.015, 3.865, -16.015),
                    ],
                ),
                SeqHoldDirectionUntilLostControl("Go to Moraine", joy_dir=Vec2(0, 1)),
                SeqSkipUntilCombat("Brace yourselves!"),
                SeqCombat("DoW Phase 1"),
                SeqSkipUntilIdle("This is pointless!"),
                # Garl goes to the roof and blows a hole in it
                MissionGarl(),
                SeqCombat("DoW Phase 2"),
                SeqSkipUntilIdle("Betrayal! Dweller of Strife descends", hold_cancel=True),
            ],
        )


class HauntedMansion(SeqList):
    """Routing of Haunted Mansion."""

    def __init__(self: Self) -> None:
        """Initialize a new HauntedMansion object."""
        super().__init__(
            name="Haunted Mansion",
            children=[
                HeadToMansion(),
                RightWing(),
                LeftWing(),
                Garden(),
                SeqCheckpoint("haunted_mansion3"),
                DwellerOfWoe(),
            ],
        )
