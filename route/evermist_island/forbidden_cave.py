"""Routing of Forbidden Cave section of Evermist Island."""

import logging
from typing import Self

from engine.combat import SeqCombat, SeqCombatAndMove
from engine.mathlib import Vec2, Vec3
from engine.seq import (
    HoldDirection,
    InteractMove,
    SeqCheckpoint,
    SeqCliffMove,
    SeqClimb,
    SeqDelay,
    SeqHoldDirectionDelay,
    SeqHoldDirectionUntilLostControl,
    SeqInteract,
    SeqList,
    SeqMashUntilIdle,
    SeqMove,
    SeqRouteBranch,
    SeqSkipUntilCombat,
    SeqSkipUntilIdle,
)

logger = logging.getLogger(__name__)


class IntroForbiddenCave(SeqList):
    """Forbidden Cave section, from entry, beating Bosslug, and leaving."""

    def __init__(self: Self) -> None:
        """Initialize a new IntroForbiddenCave object."""
        super().__init__(
            name="Forbidden Cave",
            children=[
                SeqMove(
                    name="Move to door",
                    coords=[
                        Vec3(14.000, 1.002, 14.367),
                        Vec3(14.000, 1.002, 17.396),
                    ],
                ),
                SeqInteract("Open door"),
                SeqSkipUntilIdle("Open door"),
                SeqCombatAndMove(
                    name="Move to wall",
                    coords=[
                        Vec3(14.000, 1.002, 17.396),
                        HoldDirection(14.050, -0.998, 69.499, joy_dir=Vec2(0, 1)),
                        Vec3(14.050, -0.998, 120.905),
                        Vec3(6.759, -0.998, 128.605),
                        HoldDirection(-25.425, 5.002, 128.568, joy_dir=Vec2(-1, 1)),
                        Vec3(-28.461, 5.002, 130.157),
                        InteractMove(-46.540, 5.002, 130.157),
                        Vec3(-54.723, 5.002, 132.877),
                        Vec3(-56.857, 5.002, 135.580),
                        Vec3(-56.857, 5.002, 137.540),
                        # TODO(orkaboy): Double back to fight (not optimal)
                        Vec3(-56.857, 5.002, 135.580),
                        Vec3(-56.857, 5.002, 137.540),
                    ],
                ),
                SeqClimb(
                    name="Climb wall",
                    coords=[
                        InteractMove(-56.857, 15.002, 138.467),
                    ],
                ),
                SeqMove(
                    name="Jump to pillar",
                    coords=[
                        Vec3(-54.918, 15.002, 140.050),
                        InteractMove(-51.500, 15.002, 140.050),
                        Vec3(-49.459, 7.002, 139.459),
                    ],
                ),
                SeqDelay("Wait for lock", timeout_in_s=0.2),
                SeqMove(
                    name="Climb tower",
                    coords=[
                        InteractMove(-45.533, 9.002, 139.460),
                        InteractMove(-45.533, 15.002, 141.467),
                        Vec3(-43.460, 15.002, 141.546),
                    ],
                ),
                SeqHoldDirectionDelay(name="Turn", joy_dir=Vec2(0, 1), timeout_s=0.2),
                SeqInteract("Grab wall"),
                SeqClimb(
                    name="Climb wall",
                    coords=[
                        Vec3(-43.460, 16.540, 141.540),
                        Vec3(-35.176, 16.540, 141.530),
                        Vec3(-35.176, 11.002, 141.540),
                    ],
                ),
                SeqMove(
                    name="Move to ledge",
                    coords=[
                        Vec3(-33.449, 11.002, 139.844),
                        Vec3(-25.329, 11.002, 139.354),
                        Vec3(-22.536, 11.002, 136.561),
                        HoldDirection(5.170, 5.002, 132.895, joy_dir=Vec2(1, -1)),
                        Vec3(8.542, 5.002, 136.778),
                        Vec3(11.492, 5.002, 139.500),
                    ],
                ),
                SeqCliffMove(
                    name="Move across ledge",
                    coords=[
                        HoldDirection(13.000, 5.002, 139.500, joy_dir=Vec2(1, 1)),
                        Vec3(16.550, 5.002, 139.500),
                    ],
                ),
                SeqMove(
                    name="Move to fight",
                    coords=[
                        Vec3(19.659, 5.002, 137.594),
                        Vec3(21.075, 5.002, 138.526),
                        HoldDirection(53.465, 1.002, 127.634, joy_dir=Vec2(1, 1)),
                    ],
                ),
                SeqCombatAndMove(
                    name="Navigate to platform",
                    coords=[
                        Vec3(59.844, 1.002, 132.896),
                        Vec3(57.981, 1.018, 139.464),
                        InteractMove(56.926, 4.012, 140.576),
                        InteractMove(59.915, 8.012, 144.015),
                        Vec3(60.501, 8.002, 148.204),
                        Vec3(71.706, 10.002, 148.204),
                        Vec3(73.633, 10.002, 142.899),
                        Vec3(72.258, 10.002, 138.201),
                        InteractMove(69.521, 3.010, 138.381),
                    ],
                ),
                SeqDelay("Wait for lock", timeout_in_s=0.2),
                SeqMove(
                    name="Navigate to key",
                    coords=[
                        InteractMove(61.050, 1.002, 138.381),
                        Vec3(59.146, 1.002, 138.458),
                        InteractMove(56.907, 7.002, 140.756),
                        InteractMove(58.112, 10.002, 142.334),
                        InteractMove(55.871, 16.002, 144.339),
                        Vec3(54.157, 16.002, 144.114),
                    ],
                ),
                SeqInteract("Forbidden Cavern Key"),
                SeqSkipUntilIdle("Forbidden Cavern Key"),
                SeqMove(
                    name="Jump down",
                    coords=[
                        InteractMove(61.458, 1.002, 144.189),
                    ],
                ),
                SeqMove(
                    name="Approach lever",
                    precision=0.1,
                    coords=[
                        Vec3(62.844, 1.002, 144.645),
                    ],
                ),
                SeqInteract("Pull lever"),
                SeqMove(
                    name="Move to door",
                    coords=[
                        Vec3(61.161, 1.002, 140.211),
                        Vec3(58.021, 1.012, 140.371),
                        InteractMove(56.973, 4.012, 141.322),
                        InteractMove(57.899, 7.012, 142.221),
                        InteractMove(56.773, 10.012, 143.094),
                        Vec3(55.502, 10.012, 141.361),
                        Vec3(54.687, 10.012, 141.060),
                    ],
                ),
                SeqInteract("Open lock"),
                SeqMashUntilIdle("Open lock"),
                # TODO(orkaboy): Basket is probably not needed with Amulet?
                SeqMove(
                    name="Move to basket",
                    coords=[
                        HoldDirection(72.100, 6.002, 203.000, joy_dir=Vec2(-1, 1)),
                        Vec3(69.064, 6.002, 205.976),
                    ],
                ),
                SeqInteract("Picnic basket"),
                SeqSkipUntilIdle("Picnic basket"),
                SeqMove(
                    name="Move to scroll",
                    coords=[
                        Vec3(66.875, 6.002, 205.755),
                        Vec3(64.141, 6.002, 208.489),
                        Vec3(63.918, 6.002, 209.744),
                    ],
                ),
                SeqInteract("Combo scroll"),
                SeqSkipUntilIdle("Combo scroll"),
                SeqMove(
                    name="Move to chest",
                    coords=[
                        Vec3(62.138, 6.002, 210.357),
                    ],
                ),
                SeqInteract("Shiny Pearl"),
                SeqSkipUntilIdle("Shiny Pearl"),
                SeqMove(
                    name="Move to wall",
                    coords=[
                        Vec3(63.039, 6.002, 207.960),
                        Vec3(60.519, 6.002, 206.460),
                        Vec3(53.945, 6.002, 203.097),
                        HoldDirection(19.085, 13.002, 136.585, joy_dir=Vec2(-1, -1)),
                        Vec3(16.958, 13.002, 138.682),
                    ],
                ),
                SeqClimb(
                    name="Climb wall",
                    coords=[
                        InteractMove(16.958, 20.143, 140.530),
                        Vec3(19.374, 20.143, 140.530),
                    ],
                ),
                SeqMove(
                    name="Move to split",
                    coords=[
                        Vec3(21.487, 20.002, 137.556),
                        Vec3(22.693, 20.002, 136.291),
                    ],
                ),
                # Optionally, get Leeching Thorn
                SeqRouteBranch(
                    name="Get Leeching Thorn",
                    route=["fc_leeching_thorn"],
                    when_true=SeqList(
                        name="Get Leeching Thorn",
                        children=[
                            SeqMove(
                                name="Move to chest",
                                coords=[
                                    Vec3(22.692, 20.002, 130.813),
                                    Vec3(21.037, 20.002, 128.500),
                                    InteractMove(14.175, 20.002, 128.500),
                                    Vec3(12.018, 20.002, 130.657),
                                    Vec3(12.018, 20.002, 132.492),
                                    Vec3(9.168, 20.002, 135.161),
                                ],
                            ),
                            SeqHoldDirectionDelay("Chest", joy_dir=Vec2(-1, 0), timeout_s=0.2),
                            SeqInteract("Leeching Thorn"),
                            SeqSkipUntilIdle("Leeching Thorn"),
                            SeqMove(
                                name="Return to route",
                                coords=[
                                    Vec3(12.027, 20.002, 132.374),
                                    Vec3(12.027, 20.002, 130.274),
                                    Vec3(13.874, 20.002, 128.622),
                                    InteractMove(20.670, 20.002, 128.500),
                                    Vec3(22.604, 20.002, 130.658),
                                    Vec3(22.670, 20.002, 132.946),
                                ],
                            ),
                        ],
                    ),
                ),
                SeqMove(
                    name="Move to platform",
                    coords=[
                        Vec3(25.451, 20.002, 133.119),
                        Vec3(25.335, 20.002, 132.576),
                        InteractMove(25.335, 1.010, 130.365),
                    ],
                ),
                SeqDelay("Wait for lock", timeout_in_s=0.2),
                SeqCombatAndMove(
                    name="Fight",
                    coords=[
                        InteractMove(25.335, -0.990, 125.800),
                        Vec3(20.202, -0.998, 124.117),
                        Vec3(15.461, -0.998, 134.781),
                        Vec3(14.093, -0.998, 139.361),
                        HoldDirection(13.931, 5.002, 181.026, joy_dir=Vec2(0, 1)),
                    ],
                ),
                SeqHoldDirectionUntilLostControl(
                    name="Move to bridge",
                    joy_dir=Vec2(0, 1),
                ),
                SeqSkipUntilIdle("Cutscene"),
                SeqMove(
                    name="Move to ledge",
                    coords=[
                        Vec3(12.471, 5.002, 200.353),
                        InteractMove(6.260, 5.002, 200.353),
                        Vec3(4.604, 5.002, 203.368),
                    ],
                ),
                SeqCliffMove(
                    name="Enter side cavern",
                    coords=[
                        Vec3(4.602, 5.000, 204.832),
                        HoldDirection(-30.917, 2.002, 203.683, joy_dir=Vec2(-1, 1)),
                    ],
                ),
                SeqMove(
                    name="Move to campfire",
                    coords=[
                        Vec3(-39.117, 2.002, 201.905),
                    ],
                ),
                SeqInteract("Campfire"),
                SeqDelay("Campfire", timeout_in_s=0.4),
                SeqInteract("Campfire"),
                SeqDelay("Campfire", timeout_in_s=0.4),
                SeqInteract("Campfire"),
                # Save point
                SeqCheckpoint("forbidden_cave2"),
                SeqMove(
                    name="Move to boss",
                    coords=[
                        Vec3(-39.370, 2.002, 206.332),
                        Vec3(-39.370, 2.002, 219.607),
                    ],
                ),
                SeqHoldDirectionUntilLostControl(
                    name="Move to boss",
                    joy_dir=Vec2(0, 1),
                ),
                SeqSkipUntilCombat("Boss cutscene"),
                SeqCombat("Bosslug fight"),
                SeqSkipUntilIdle("Post-boss cutscene"),
                # Optionally, can enter cave to the north here and grab items
                SeqRouteBranch(
                    name="Loot boss cave",
                    route=["fc_bosslug_loot"],
                    when_true=SeqList(
                        name="Loot boss cave",
                        children=[
                            SeqMove(
                                name="Move to chest",
                                coords=[
                                    Vec3(-39.493, 2.002, 238.270),
                                    HoldDirection(-39.000, 2.002, 293.358, joy_dir=Vec2(0, 1)),
                                    Vec3(-40.479, 2.002, 302.318),
                                ],
                            ),
                            SeqInteract("60 gold"),
                            SeqSkipUntilIdle("60 gold"),
                            SeqMove(
                                name="Move to chest",
                                coords=[
                                    Vec3(-37.746, 2.002, 302.321),
                                ],
                            ),
                            SeqInteract("Adventurer's Vest"),
                            SeqSkipUntilIdle("Adventurer's Vest"),
                            SeqMove(
                                name="Leave cave",
                                coords=[
                                    Vec3(-39.017, 2.002, 291.219),
                                    HoldDirection(-39.525, 2.002, 238.625, joy_dir=Vec2(0, -1)),
                                ],
                            ),
                        ],
                    ),
                ),
                SeqMove(
                    name="Move to exit",
                    coords=[
                        Vec3(-35.969, 2.002, 236.869),
                        InteractMove(-32.475, 6.002, 237.234),
                        Vec3(-31.291, 6.002, 237.234),
                        HoldDirection(5.796, 11.002, 244.657, joy_dir=Vec2(1, 1)),
                        Vec3(8.675, 11.002, 243.322),
                        InteractMove(12.419, 5.002, 243.322),
                        Vec3(14.032, 5.002, 250.628),
                    ],
                ),
                SeqHoldDirectionUntilLostControl(
                    name="Leave cavern",
                    joy_dir=Vec2(0, 1),
                ),
            ],
        )
