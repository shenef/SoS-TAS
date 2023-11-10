"""Routing of Sacred Grove segment of Watcher Island."""

import logging
from typing import Self

from engine.combat import SeqCombat, SeqCombatAndMove
from engine.mathlib import Vec2, Vec3
from engine.seq import (
    HoldDirection,
    InteractMove,
    SeqChangeTimeOfDay,
    SeqCheckpoint,
    SeqDelay,
    SeqGraplou,
    SeqHoldDirectionDelay,
    SeqInteract,
    SeqList,
    SeqLoot,
    SeqMove,
    SeqRouteBranch,
    SeqSelectOption,
    SeqSkipUntilIdle,
)
from memory.mappers.items import WEAPONS
from memory.player_party_manager import PlayerPartyCharacter

logger = logging.getLogger(__name__)


class SacredGrove(SeqList):
    """Routing of Sacred Grove segment of Watcher Island."""

    def __init__(self: Self) -> None:
        """Initialize a new SacredGrove object."""
        super().__init__(
            name="Sacred Grove",
            children=[
                SeqCheckpoint(
                    "sacred_grove",
                    return_path=SeqMove(
                        name="Return to path",
                        coords=[
                            Vec3(5.940, 5.002, 14.295),
                            Vec3(10.550, 5.002, 9.684),
                        ],
                    ),
                ),
                SeqMove(
                    name="Navigate to high ground",
                    coords=[
                        Vec3(20.623, 5.002, 9.792),
                        Vec3(29.524, 5.002, 17.252),
                        InteractMove(29.524, 10.002, 20.467),
                        Vec3(22.610, 10.002, 27.874),
                        InteractMove(8.426, 10.002, 27.874),
                        Vec3(6.453, 10.002, 25.519),
                    ],
                ),
                SeqHoldDirectionDelay("Turn", joy_dir=Vec2(-1, 0), timeout_s=0.1),
                SeqGraplou("Pull block"),
                SeqMove(
                    name="Climb to higher ground",
                    coords=[
                        InteractMove(-0.467, 13.002, 25.519),
                        InteractMove(-0.467, 15.002, 26.467),
                    ],
                ),
                SeqGraplou("Attack enemies", until_combat=True),
                SeqCombat("Birds"),
                SeqRouteBranch(
                    name="Coral Daggers",
                    route=["sg_coral_daggers"],
                    when_true=SeqList(
                        name="Coral Daggers",
                        children=[
                            SeqMove(
                                name="Move into secret cave",
                                coords=[
                                    Vec3(8.394, 15.002, 34.960),
                                    InteractMove(12.021, 15.002, 38.718),
                                    Vec3(12.962, 15.002, 39.541),
                                    Vec3(13.540, 15.002, 39.541),
                                    InteractMove(16.518, 15.002, 39.541),
                                    InteractMove(19.389, 11.803, 44.079),
                                    HoldDirection(-53.900, -1.397, 75.167, joy_dir=Vec2(0, 1)),
                                    InteractMove(-53.900, 1.002, 77.467),
                                    Vec3(-53.900, 1.002, 78.540),
                                ],
                            ),
                            SeqLoot(
                                "Coral Daggers",
                                item=WEAPONS.CoralDaggers,
                                equip_to=PlayerPartyCharacter.Serai,
                            ),
                            SeqMove(
                                name="Return to path",
                                coords=[
                                    InteractMove(-53.900, -1.397, 75.342),
                                    HoldDirection(19.499, 11.803, 43.201, joy_dir=Vec2(0, -1)),
                                    Vec3(6.638, 11.803, 41.000),
                                    InteractMove(4.926, 15.002, 38.147),
                                ],
                            ),
                        ],
                    ),
                ),
                SeqMove(
                    name="Move to block",
                    coords=[
                        Vec3(8.236, 15.002, 35.121),
                        InteractMove(11.943, 15.002, 38.737),
                        Vec3(12.727, 15.002, 39.541),
                        Vec3(13.540, 15.002, 39.541),
                        InteractMove(25.073, 15.002, 39.541),
                        Vec3(28.534, 15.002, 39.541),
                    ],
                ),
                SeqHoldDirectionDelay("Turn", joy_dir=Vec2(0, 1), timeout_s=0.1),
                SeqGraplou("Pull block"),
                SeqCombatAndMove(
                    name="Move to rune",
                    coords=[
                        InteractMove(28.635, 20.002, 48.467),
                        Vec3(27.168, 20.002, 49.747),
                        Vec3(14.631, 20.002, 50.971),
                    ],
                ),
                # TODO(orkaboy): Could get issues if seen by enemies
                SeqChangeTimeOfDay("Time puzzle", time_target=10.0),
                SeqMove(
                    name="Cross pillars",
                    coords=[
                        InteractMove(5.460, 20.002, 51.080),
                    ],
                ),
                SeqDelay("Wait", timeout_in_s=0.7),
                SeqMove(
                    name="Cross pillars",
                    coords=[
                        InteractMove(-2.740, 20.002, 50.971),
                        Vec3(-2.740, 20.002, 59.474),
                    ],
                ),
                SeqHoldDirectionDelay("Turn", joy_dir=Vec2(1, 1), timeout_s=0.1),
                SeqGraplou("Pull block"),
                SeqCombatAndMove(
                    name="Go to block",
                    coords=[
                        Vec3(3.601, 20.002, 65.533),
                        InteractMove(3.601, 25.002, 68.467),
                        Vec3(7.459, 25.002, 77.872),
                    ],
                ),
                SeqHoldDirectionDelay("Turn", joy_dir=Vec2(0, 1), timeout_s=0.1),
                SeqGraplou("Pull block"),
                SeqCombatAndMove(
                    name="Go to altar",
                    coords=[
                        InteractMove(7.459, 30.002, 84.467),
                        Vec3(8.103, 30.002, 86.766),
                        Vec3(13.556, 30.002, 94.009),
                        Vec3(15.546, 30.002, 103.746),
                        InteractMove(19.265, 30.002, 103.746),
                        Vec3(28.525, 27.002, 104.288),
                        Vec3(28.525, 30.010, 110.194),
                        InteractMove(28.569, 30.002, 113.481),
                        Vec3(23.460, 30.002, 113.481),
                        InteractMove(20.252, 30.002, 113.481),
                        Vec3(15.369, 30.002, 113.411),
                    ],
                ),
                SeqSelectOption("Seashell", skip_dialog_check=True),
                SeqSkipUntilIdle("Magic Seashell"),
                SeqMove(
                    name="Move to whirlpool",
                    coords=[
                        InteractMove(14.544, 25.803, 104.941),
                    ],
                ),
                SeqInteract("Whirlpool"),
                SeqMove(
                    name="Underwater passage",
                    coords=[
                        Vec3(85.366, 1.803, 68.619),
                        Vec3(85.359, 1.803, 59.916),
                        Vec3(86.669, 1.803, 55.496),
                        Vec3(86.669, 1.803, 30.687),
                    ],
                ),
                SeqInteract("Whirlpool"),
                SeqMove(
                    name="Leave Sacred Grove",
                    coords=[
                        InteractMove(15.511, 5.002, 10.650),
                        Vec3(14.644, 5.002, 5.075),
                        HoldDirection(231.000, 3.002, 73.998, joy_dir=Vec2(0, -1)),
                    ],
                ),
            ],
        )
