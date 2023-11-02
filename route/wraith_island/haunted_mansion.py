"""Routing of Haunted Mansion and Dweller of Woe section of Wraith Island."""

import logging
from enum import Enum, auto
from typing import Self

from control import sos_ctrl
from engine.combat import SeqCombatAndMove
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
    SeqHoldDirectionUntilLostControl,
    SeqInteract,
    SeqList,
    SeqLoot,
    SeqMashUntilIdle,
    SeqMove,
    SeqRouteBranch,
    SeqSelectOption,
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
                SeqSelectOption("Let him cook"),
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
                SeqCombatAndMove(
                    name="Move to right statue",
                    coords=[
                        Vec3(-87.988, 10.002, 206.180),
                        InteractMove(-77.410, 10.002, 206.500),
                        Vec3(-71.300, 10.002, 203.848),
                        Vec3(-69.630, 10.002, 201.648),
                        Graplou(-58.200, 10.010, 199.600, joy_dir=Vec2(1, 0), hold_timer=0.1),
                        Vec3(-58.200, 10.010, 201.483),
                        Vec3(-52.327, 10.002, 206.436),
                        InteractMove(-41.868, 10.002, 206.434),
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
                        Vec3(-41.532, 10.002, 207.543),
                    ],
                ),
                SkullPuzzleFlip("R1", num_flips=2),
                SeqMove(
                    name="Move to second skull",
                    coords=[
                        Vec3(-43.974, 10.002, 207.543),
                    ],
                ),
                SeqHoldDirectionDelay("Turn", joy_dir=Vec2(0, 1), timeout_s=0.1),
                SkullPuzzleFlip("R2", num_flips=2),
                SeqCliffMove(
                    name="Move to third skull",
                    coords=[
                        Vec3(-43.660, 10.002, 206.379),
                        Vec3(-45.660, 10.002, 206.500),
                        InteractMove(-50.267, 10.002, 206.500),
                        Vec3(-50.267, 10.002, 207.540),
                    ],
                ),
                SkullPuzzleFlip("R3", num_flips=2),
                SeqMove(
                    name="Move to fourth skull",
                    coords=[
                        Vec3(-52.926, 10.002, 207.540),
                    ],
                ),
                SkullPuzzleFlip("R4", num_flips=2),
                SeqMove(
                    name="Move to fifth skull",
                    coords=[
                        Vec3(-58.807, 10.002, 201.421),
                        Graplou(-70.200, 10.010, 199.500, joy_dir=Vec2(-1, 0), hold_timer=0.1),
                        Vec3(-70.200, 10.010, 201.058),
                        Vec3(-75.132, 10.002, 207.540),
                    ],
                ),
                SkullPuzzleFlip("L1", num_flips=1),
                SeqMove(
                    name="Move to sixth skull",
                    coords=[
                        Vec3(-77.733, 10.002, 207.540),
                    ],
                ),
                SkullPuzzleFlip("L2", num_flips=2),
                SeqMove(
                    name="Move to seventh skull",
                    coords=[
                        Vec3(-77.907, 10.002, 206.439),
                        InteractMove(-84.281, 10.002, 206.500),
                        Vec3(-84.281, 10.002, 207.540),
                    ],
                ),
                SkullPuzzleFlip("L3", num_flips=3),
                SeqMove(
                    name="Move to eight skull",
                    coords=[
                        Vec3(-86.498, 10.002, 207.540),
                    ],
                ),
                SkullPuzzleFlip("L4", num_flips=2),
                SeqMove(
                    name="Move to combo scroll",
                    coords=[
                        Vec3(-84.872, 10.002, 206.547),
                        InteractMove(-77.369, 10.002, 206.500),
                        Vec3(-75.352, 10.002, 206.500),
                        Vec3(-67.838, 10.002, 200.973),
                        InteractMove(-65.542, 1.002, 200.973),
                        Vec3(-64.157, 1.002, 201.083),
                    ],
                ),
                SeqLoot("X-Strike"),
                SeqBlackboard("X-Strike", key="x_strike", value=True),
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
                        Graplou(-110.631, 14.010, 256.036, joy_dir=Vec2(1, 1), hold_timer=0.1),
                    ],
                ),
                SeqClimb(
                    name="Climb wall",
                    coords=[
                        Vec3(-109.812, 21.586, 257.147),
                        Vec3(-110.651, 21.298, 257.986),
                    ],
                ),
                SeqMove(
                    name="Move to chest",
                    coords=[
                        Vec3(-113.106, 21.002, 256.167),
                        Graplou(-103.000, 21.010, 247.000, joy_dir=Vec2(1, -1), hold_timer=0.1),
                        Vec3(-101.594, 21.002, 244.052),
                        InteractMove(-100.531, 14.002, 243.819),
                        Vec3(-101.201, 14.002, 246.154),
                    ],
                ),
                SeqLoot(
                    "Spectral Cape", item=ARMORS.SpectralCape, equip_to=PlayerPartyCharacter.Garl
                ),
                SeqMove(
                    name="Graplou wall",
                    coords=[
                        Graplou(-100.276, 14.010, 246.145, joy_dir=Vec2(1, 0), hold_timer=0.1),
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
                # TODO(orkaboy): Continue routing
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
                # TODO(orkaboy): Continue routing
            ],
        )
