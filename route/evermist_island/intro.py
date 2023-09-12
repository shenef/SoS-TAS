import logging
from typing import Self

from engine.combat import SeqCombatAndMove
from engine.mathlib import Vec2, Vec3
from engine.seq import (
    HoldDirection,
    InteractMove,
    SeqAwaitLostControl,
    SeqCheckpoint,
    SeqCliffClimb,
    SeqCliffMove,
    SeqClimb,
    SeqHoldDirectionUntilLostControl,
    SeqIf,
    SeqInteract,
    SeqList,
    SeqLog,
    SeqMove,
    SeqTurboMashSkipCutsceneUntilIdle,
    SeqTurboMashUntilIdle,
)
from memory import (
    PlayerPartyCharacter,
    player_party_manager_handle,
)

logger = logging.getLogger(__name__)


class IntroMountainTrail(SeqList):
    def __init__(self: Self) -> None:
        super().__init__(
            name="Mountain Trail",
            children=[
                SeqTurboMashUntilIdle(name="Wait for control"),
                SeqLog(name="SYSTEM", text="We have control!"),
                # TODO: Need to be able to do special ability (mash fails for Zale)
                SeqCombatAndMove(
                    name="Fights",
                    coords=[
                        InteractMove(33.253, 6.002, 20.273),
                        Vec3(37.799, 5.477, 18.084),
                        Vec3(49.640, 6.010, 6.719),
                        Vec3(55.897, 6.002, 6.543),
                        InteractMove(56.819, 13.002, 13.466),
                        InteractMove(44.829, 13.010, 25.305),
                        InteractMove(34.500, 13.002, 27.500),
                    ],
                ),
                SeqClimb(
                    name="Move down ladder",
                    coords=[
                        InteractMove(34.448, 6.002, 25.407),
                    ],
                    precision=0.5,
                ),
                SeqMove(
                    name="Move to cavern",
                    coords=[
                        InteractMove(23.612, 5.001, 11.401),
                        Vec3(20.193, 5.001, 7.870),
                        Vec3(14.948, 5.001, 7.870),
                        Vec3(-3.976, 5.001, 15.624),
                        Vec3(-8.323, 5.001, 17.491),
                        InteractMove(-7.701, 7.002, 22.365),
                        InteractMove(-0.783, 9.002, 22.563),
                        InteractMove(-0.914, 13.002, 26.750),
                        Vec3(-10.554, 13.002, 27.866),
                        Vec3(-29.087, 13.090, 27.836),
                        Vec3(-34.761, 13.030, 22.203),
                        Vec3(-40.253, 11.002, 22.203),
                        HoldDirection(-88.500, 10.002, 32.058, joy_dir=Vec2(0, 1)),
                    ],
                ),
                SeqMove(
                    name="Move through cavern",
                    coords=[
                        Vec3(-82.388, 10.002, 37.691),
                        Vec3(-82.254, 10.002, 42.898),
                        Vec3(-87.191, 10.002, 44.145),
                    ],
                ),
                SeqClimb(
                    name="Climb cliff",
                    coords=[
                        InteractMove(-87.191, 16.000, 44.900),
                    ],
                ),
                SeqCliffMove(
                    name="Climb cliff",
                    coords=[
                        Vec3(-89.280, 16.000, 45.000),
                        Vec3(-92.238, 16.000, 47.673),
                        Vec3(-92.944, 16.000, 48.000),
                    ],
                ),
                SeqCliffClimb(
                    name="Climb cliff",
                    coords=[
                        InteractMove(-93.016, 22.000, 48.000),
                    ],
                ),
                SeqCliffMove(
                    name="Climb cliff",
                    coords=[
                        Vec3(-88.799, 22.000, 45.000),
                    ],
                ),
                # Use the combat node on the off-chance we run into the slug
                SeqCombatAndMove(
                    name="Move to campfire",
                    coords=[
                        Vec3(-87.284, 22.002, 44.522),
                        Vec3(-73.903, 22.002, 34.029),
                        HoldDirection(-35.819, 21.002, 27.816, joy_dir=Vec2(0, -1)),
                        Vec3(-32.177, 21.002, 27.816),
                        Vec3(-30.369, 21.002, 32.300),
                        InteractMove(-20.660, 21.002, 32.300),
                        InteractMove(-17.865, 21.002, 35.382),
                        InteractMove(-7.719, 21.002, 35.382),
                        Vec3(3.729, 21.002, 30.631),
                        InteractMove(16.907, 21.002, 17.446),
                        Vec3(18.852, 21.002, 16.665),
                    ],
                    precision=0.5,
                ),
                SeqHoldDirectionUntilLostControl(
                    name="Go out of cavern",
                    joy_dir=Vec2(1, -0.2),
                ),
                SeqTurboMashUntilIdle(name="Wait for control"),
            ],
        )


class IntroMooncradle(SeqList):
    def __init__(self: Self) -> None:
        super().__init__(
            name="Mooncradle",
            children=[
                SeqCheckpoint(checkpoint_name="intro_mooncradle"),
                SeqMove(
                    name="Move to cliff",
                    coords=[
                        Vec3(-68.930, -10.998, 26.150),
                        HoldDirection(-13.969, -11.998, 38.757, joy_dir=Vec2(0, -1)),
                        Vec3(-13.969, -11.998, 36.392),
                        Vec3(-12.504, -11.998, 34.927),
                        Vec3(-9.406, -11.998, 34.927),
                    ],
                ),
                SeqClimb(
                    name="Climb",
                    coords=[
                        InteractMove(-9.500, -6.998, 36.467),
                    ],
                ),
                SeqMove(
                    name="Move to cliff",
                    coords=[
                        Vec3(-13.482, -6.998, 40.543),
                    ],
                ),
                SeqClimb(
                    name="Climb",
                    coords=[
                        InteractMove(-13.500, -0.998, 41.467),
                    ],
                ),
                SeqMove(
                    name="Move to cutscene",
                    coords=[
                        Vec3(-9.222, -0.820, 53.985),
                        Vec3(-7.318, 1.010, 62.634),
                        Vec3(3.432, 1.002, 73.327),
                        Vec3(17.958, 1.002, 76.578),
                    ],
                ),
                SeqHoldDirectionUntilLostControl(
                    name="Move to cutscene",
                    joy_dir=Vec2(1, 0.2),
                ),
                # Hold B as well to skip cutscene
                SeqTurboMashSkipCutsceneUntilIdle(name="Meeting Brugaves and Erlina"),
                SeqMove(
                    name="Move to Forbidden Cave",
                    coords=[
                        Vec3(31.373, 1.002, 89.671),
                        Vec3(31.471, 1.002, 114.862),
                        # Enter world map
                        HoldDirection(109.500, 2.002, 61.998, joy_dir=Vec2(0, 1)),
                        Vec3(109.500, 2.002, 64.000),
                        Vec3(108.000, 2.002, 64.000),
                        Vec3(108.000, 2.002, 66.500),
                    ],
                ),
                SeqInteract("Enter Forbidden Cave"),
                # Move to cutscene
                SeqMove(
                    name="Move to entrance",
                    coords=[
                        Vec3(14.000, 1.002, 17.396),
                    ],
                ),
                SeqInteract("Door"),
                SeqTurboMashUntilIdle(name="Wait for control"),
                # Forbidden Cave
                SeqHoldDirectionUntilLostControl(
                    name="Move to cutscene",
                    joy_dir=Vec2(0, 1),
                ),
                SeqTurboMashUntilIdle(name="Garl nooo"),
                # Zenith Academy
                SeqMove(
                    name="Move to dorms",
                    coords=[
                        Vec3(48.690, -8.990, -136.717),
                        HoldDirection(285.500, 5.002, 58.000, joy_dir=Vec2(1, 1)),
                        Vec3(290.419, 5.002, 61.872),
                        Vec3(295.647, 5.002, 63.663),
                        HoldDirection(72.657, -7.998, -133.640, joy_dir=Vec2(1, 1)),
                        Vec3(82.104, -7.998, -129.590),
                        Vec3(94.005, -11.998, -129.590),
                        Vec3(94.005, -11.998, -133.576),
                    ],
                ),
            ],
        )


class SeqIfMainCharacterValere(SeqIf):
    def condition(self: Self) -> bool:
        leader = player_party_manager_handle().leader_character
        if leader == PlayerPartyCharacter.Valere:
            return True
        if leader == PlayerPartyCharacter.Zale:
            return False
        return None


class LoomsToCenter(SeqIfMainCharacterValere):
    def __init__(self: Self, name: str) -> None:
        super().__init__(
            name,
            # Valere branch: Go left
            when_true=SeqMove(
                name="Valere path",
                coords=[
                    Vec3(91.478, -18.998, -156.476),
                    Vec3(88.309, -18.998, -156.476),
                    Vec3(88.127, -14.998, -134.674),
                ],
            ),
            # Zale branch: Go right
            when_false=SeqMove(
                name="Zale path",
                coords=[
                    Vec3(97.745, -18.998, -156.127),
                    Vec3(100.573, -18.998, -156.149),
                    Vec3(101.496, -14.998, -142.680),
                    Vec3(100.851, -14.998, -134.661),
                ],
            ),
        )


class IntroZenithAcademy(SeqList):
    def __init__(self: Self) -> None:
        super().__init__(
            name="Mooncradle",
            children=[
                SeqIfMainCharacterValere(
                    name="Main Character",
                    # Valere branch: Go left
                    when_true=SeqMove(
                        name="Valere path",
                        coords=[
                            Vec3(94.005, -11.998, -133.576),
                            Vec3(86.621, -14.998, -135.924),
                            Vec3(84.091, -14.960, -140.766),
                            Vec3(82.085, -18.998, -147.421),
                            Vec3(78.360, -18.998, -147.465),
                        ],
                    ),
                    # Zale branch: Go right
                    when_false=SeqMove(
                        name="Zale path",
                        coords=[
                            Vec3(94.005, -11.998, -133.576),
                            Vec3(100.395, -14.998, -134.377),
                            Vec3(104.751, -14.998, -139.367),
                            Vec3(106.596, -18.998, -147.793),
                            Vec3(109.640, -18.998, -147.793),
                        ],
                    ),
                ),
                SeqInteract("Sleep"),
                SeqTurboMashUntilIdle(name="Train with Brugaves"),
                SeqMove(
                    name="Move to Erlina",
                    coords=[
                        Vec3(-17.700, -13.998, -136.900),
                        InteractMove(-11.000, -14.998, -143.700),
                        HoldDirection(248.762, 5.002, 56.959, joy_dir=Vec2(1, -1)),
                        Vec3(253.865, 5.002, 56.959),
                        Vec3(257.891, 5.002, 58.706),
                        Vec3(260.734, 5.002, 58.706),
                        HoldDirection(16.980, -8.998, -135.817, joy_dir=Vec2(1, -1)),
                        Vec3(32.789, -8.930, -151.592),
                        Vec3(32.789, -8.990, -176.218),
                    ],
                ),
                SeqMove(
                    name="Move to Erlina",
                    precision=1.0,
                    coords=[
                        HoldDirection(273.146, 5.002, 47.521, joy_dir=Vec2(0, -1)),
                    ],
                ),
                SeqHoldDirectionUntilLostControl(
                    name="Move to Erlina",
                    joy_dir=Vec2(0, -1),
                ),
                SeqTurboMashUntilIdle(name="Train with Erlina"),
                SeqAwaitLostControl(name="Train with Erlina"),
                SeqTurboMashUntilIdle(name="Sewing"),
                LoomsToCenter("Move to main area"),
                SeqMove(
                    name="Move to main area",
                    coords=[
                        Vec3(94.160, -11.998, -133.319),
                        Vec3(94.382, -11.998, -129.766),
                        Vec3(81.351, -7.998, -129.428),
                        Vec3(72.903, -7.998, -133.028),
                        HoldDirection(295.354, 5.002, 64.422, joy_dir=Vec2(-1, -1)),
                        Vec3(292.408, 5.002, 62.065),
                        Vec3(286.460, 5.002, 59.299),
                        HoldDirection(50.042, -8.998, -134.778, joy_dir=Vec2(-1, -1)),
                    ],
                ),
                SeqAwaitLostControl(name="Eavesdrop"),
                SeqTurboMashUntilIdle(name="Eavesdrop"),
                SeqIfMainCharacterValere(
                    name="Main Character",
                    # Valere branch: Go left
                    when_true=SeqMove(
                        name="Valere path",
                        coords=[
                            Vec3(82.936, -18.998, -147.362),
                            Vec3(84.538, -14.990, -138.768),
                            Vec3(89.372, -14.998, -133.939),
                        ],
                    ),
                    # Zale branch: Go right
                    when_false=SeqMove(
                        name="Zale path",
                        coords=[
                            Vec3(106.395, -18.998, -147.455),
                            Vec3(104.039, -14.998, -137.504),
                            Vec3(99.935, -14.998, -133.890),
                        ],
                    ),
                ),
                SeqMove(
                    name="Move to south area",
                    coords=[
                        Vec3(94.014, -11.998, -133.488),
                        Vec3(93.947, -11.998, -129.872),
                        Vec3(80.214, -7.998, -129.872),
                        Vec3(73.745, -7.998, -132.473),
                        HoldDirection(295.354, 5.002, 64.422, joy_dir=Vec2(-1, -1)),
                        Vec3(292.408, 5.002, 62.065),
                        Vec3(286.460, 5.002, 59.299),
                        HoldDirection(49.334, -8.998, -135.486, joy_dir=Vec2(-1, -1)),
                        Vec3(33.021, -8.932, -151.461),
                        Vec3(33.021, -8.990, -176.434),
                        HoldDirection(273.463, 5.002, 48.071, joy_dir=Vec2(0, -1)),
                    ],
                ),
                SeqHoldDirectionUntilLostControl(
                    name="I smell cookies",
                    joy_dir=Vec2(0, -1),
                ),
                SeqTurboMashUntilIdle(name="Cookies!!!"),
                LoomsToCenter("Move to main area"),
                SeqMove(
                    name="Move to Moraine",
                    coords=[
                        Vec3(94.014, -11.998, -133.488),
                        Vec3(93.947, -11.998, -129.872),
                        Vec3(80.214, -7.998, -129.872),
                        Vec3(73.745, -7.998, -132.473),
                        HoldDirection(295.354, 5.002, 64.422, joy_dir=Vec2(-1, -1)),
                        Vec3(292.408, 5.002, 62.065),
                        Vec3(286.460, 5.002, 59.299),
                        HoldDirection(49.334, -8.998, -135.486, joy_dir=Vec2(-1, -1)),
                        Vec3(43.613, -8.998, -141.418),
                        Vec3(35.035, -8.998, -141.418),
                        Vec3(32.954, -8.998, -136.402),
                    ],
                ),
                SeqInteract("Headmaster Moraine"),
                SeqTurboMashUntilIdle(name="Brugaves and Erlina return"),
                SeqMove(
                    name="Move to Erlina",
                    coords=[
                        Vec3(31.747, -8.998, -141.005),
                    ],
                ),
                SeqInteract("Erlina"),
                # TODO: Tap down, skip tutorial (x2)
                # TODO: Go to Brugaves, skip tutorials (x2)
                # TODO: Go to Moraine, skip-mash
                # TODO: Jump into pit
            ],
        )


class EvermistIsland(SeqList):
    def __init__(self: Self) -> None:
        super().__init__(
            name="Evermist Island",
            children=[
                IntroMountainTrail(),
                IntroMooncradle(),
                SeqCheckpoint("intro_dorms"),
                IntroZenithAcademy(),
            ],
        )
