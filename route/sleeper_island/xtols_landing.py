"""Routing of X'tol's Landing section of Sleeper Island."""

import logging
from typing import Self

from engine.combat import SeqCombatAndMove
from engine.inventory.items import GROUPTRINKETS
from engine.mathlib import Vec2, Vec3
from engine.seq import (
    HoldDirection,
    InteractMove,
    SeqClimb,
    SeqHoldDirectionUntilLostControl,
    SeqInteract,
    SeqList,
    SeqLoot,
    SeqMove,
    SeqRouteBranch,
    SeqSkipUntilClose,
)
from memory.player_party_manager import PlayerPartyCharacter

logger = logging.getLogger(__name__)


class XtolsLanding(SeqList):
    """Route from arrival from Evermist Island to leaving X'tol's Landing for the world map."""

    def __init__(self: Self) -> None:
        """Initialize a new XtolsLanding object."""
        super().__init__(
            name="X'tol's Landing",
            children=[
                # Can get Solstice Ring in a cave and 90 gold
                SeqRouteBranch(
                    name="Solstice Ring",
                    route=["xl_solstice_ring"],
                    when_true=SeqList(
                        name="Solstice Ring",
                        children=[
                            SeqMove(
                                name="Move to chest",
                                coords=[
                                    Vec3(-456.847, 1.002, -62.006),
                                    InteractMove(-459.978, -4.998, -65.169),
                                    Vec3(-453.412, -4.998, -70.543),
                                    InteractMove(-453.412, -9.998, -72.458),
                                    Vec3(-450.379, -9.998, -72.458),
                                    HoldDirection(-491.448, 1.002, -219.789, joy_dir=Vec2(0, 1)),
                                    Vec3(-491.448, 3.002, -206.558),
                                ],
                            ),
                            # TODO(orkaboy): Equip to whom?
                            SeqLoot(
                                "Solstice Ring",
                                item=GROUPTRINKETS.SolsticeMageRing,
                                equip_to=PlayerPartyCharacter.Zale,
                            ),
                            SeqMove(
                                name="Move to chest",
                                coords=[
                                    Vec3(-491.448, 1.010, -220.681),
                                    HoldDirection(-450.196, -9.998, -72.732, joy_dir=Vec2(0, -1)),
                                    Vec3(-446.604, -9.998, -72.457),
                                    InteractMove(-445.176, -14.998, -73.460),
                                    Vec3(-444.577, -14.998, -73.867),
                                ],
                            ),
                            SeqLoot("90 gold"),
                            SeqMove(
                                name="Return to route",
                                coords=[
                                    Vec3(-447.621, -14.998, -76.229),
                                    InteractMove(-450.221, -14.998, -79.093),
                                    Vec3(-449.642, -14.998, -81.495),
                                    InteractMove(-443.687, -14.998, -87.190),
                                    Vec3(-443.687, -14.998, -90.633),
                                    Vec3(-440.434, -14.998, -93.589),
                                ],
                            ),
                        ],
                    ),
                    when_false=SeqMove(
                        name="Move to fight",
                        coords=[
                            InteractMove(-440.880, 0.002, -66.672),
                            InteractMove(-434.989, 1.002, -72.355),
                            Vec3(-435.754, -6.679, -85.519),
                            Vec3(-436.293, -6.998, -86.561),
                            InteractMove(-441.924, -14.998, -92.082),
                        ],
                    ),
                ),
                SeqMove(
                    name="Move to fight",
                    coords=[
                        Vec3(-426.310, -14.998, -98.160),
                    ],
                ),
                SeqClimb(
                    name="Slide down ladder",
                    coords=[
                        InteractMove(-425.293, -20.566, -98.457),
                        HoldDirection(-425.293, -22.998, -100.725, joy_dir=Vec2(0, -1)),
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
                    ],
                ),
                SeqHoldDirectionUntilLostControl("Leave", joy_dir=Vec2(1, -1)),
                SeqSkipUntilClose(name="Mysterious Ninja", coord=Vec3(117.500, 15.000, 161.500)),
                SeqMove(
                    name="Move to Moorlands",
                    coords=[
                        Vec3(117.500, 15.002, 160.500),
                        Vec3(118.000, 15.002, 160.500),
                        Vec3(118.000, 15.002, 159.000),
                        Vec3(120.500, 15.002, 159.000),
                    ],
                ),
                SeqInteract("Moorlands"),
            ],
        )
