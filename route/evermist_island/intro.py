import logging
from typing import Self

from engine.combat import SeqCombat, SeqCombatAndMove
from engine.mathlib import Vec2, Vec3
from engine.seq import (
    HoldDirection,
    InteractMove,
    SeqAmulet,
    SeqAwaitLostControl,
    SeqCheckpoint,
    SeqCliffClimb,
    SeqCliffMove,
    SeqClimb,
    SeqDelay,
    SeqHoldDirectionUntilLostControl,
    SeqIf,
    SeqInteract,
    SeqList,
    SeqLog,
    SeqMashUntilIdle,
    SeqMove,
    SeqSkipUntilClose,
    SeqSkipUntilCombat,
    SeqSkipUntilIdle,
    SeqTapDown,
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
                SeqSkipUntilCombat(name="Wait for combat"),
                SeqLog(name="SYSTEM", text="We have control!"),
                SeqCombatAndMove(
                    name="Fights",
                    coords=[
                        InteractMove(31.524, 6.002, 19.951),
                        Vec3(36.021, 5.842, 19.951),
                        Vec3(49.921, 6.002, 6.540),
                        Vec3(54.534, 6.002, 6.543),
                        InteractMove(55.458, 10.002, 9.467),
                        Vec3(57.051, 10.002, 12.404),
                        InteractMove(43.963, 13.010, 26.059),
                        InteractMove(35.870, 13.010, 28.070),  # after fight
                    ],
                ),
                SeqClimb(
                    name="Move down ladder",
                    coords=[
                        InteractMove(34.448, 6.002, 25.407),
                    ],
                ),
                SeqMove(
                    name="Move to cavern",
                    coords=[
                        Vec3(31.505, 6.002, 19.783),
                        InteractMove(23.612, 5.001, 11.401),
                        Vec3(19.979, 5.002, 7.421),
                        Vec3(14.948, 5.001, 7.870),
                        Vec3(-3.976, 5.001, 15.624),
                        Vec3(-8.323, 5.001, 17.491),
                        Vec3(-7.740, 5.002, 21.092),
                        InteractMove(-5.086, 9.002, 23.746),
                        Vec3(-1.139, 9.002, 24.543),
                        InteractMove(-1.223, 13.002, 26.974),
                        Vec3(-29.325, 13.112, 26.818),
                        Vec3(-33.072, 13.002, 23.247),
                        Vec3(-39.808, 11.002, 23.278),
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
                ),
                SeqHoldDirectionUntilLostControl(
                    name="Go out of cavern",
                    joy_dir=Vec2(1, -0.2),
                ),
                SeqSkipUntilIdle(name="Wait for control"),
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
                SeqSkipUntilIdle(name="Meeting Brugaves and Erlina"),
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
                SeqSkipUntilIdle(name="Wait for control"),
                # Forbidden Cave
                SeqHoldDirectionUntilLostControl(
                    name="Move to cutscene",
                    joy_dir=Vec2(0, 1),
                ),
                SeqSkipUntilIdle(name="Garl nooo"),
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


class SkipTutorial(SeqList):
    def __init__(self: Self, name: str) -> None:
        super().__init__(
            name,
            children=[
                SeqInteract("Talk"),
                SeqDelay("Wait", timeout_in_s=1),
                SeqInteract("Skip dialog"),
                SeqDelay("Wait", timeout_in_s=0.2),
                SeqTapDown(),
                SeqInteract("Say no"),
                SeqDelay("Wait", timeout_in_s=1),
                SeqInteract("Skip dialog"),
                SeqDelay("Wait", timeout_in_s=0.2),
                SeqTapDown(),
                SeqInteract("Say no"),
                SeqDelay("Wait", timeout_in_s=1),
                SeqInteract("Skip dialog"),
                SeqDelay("Wait", timeout_in_s=0.2),
                SeqInteract("Skip dialog"),
            ],
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
                SeqDelay("Sleep", timeout_in_s=1),
                SeqInteract("Sleep"),
                SeqSkipUntilIdle(name="Train with Brugaves"),
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
                    coords=[
                        HoldDirection(273.146, 5.002, 47.521, joy_dir=Vec2(0, -1)),
                    ],
                ),
                SeqHoldDirectionUntilLostControl(
                    name="Move to Erlina",
                    joy_dir=Vec2(0, -1),
                ),
                SeqSkipUntilIdle(name="Train with Erlina"),
                SeqAwaitLostControl(name="Train with Erlina"),
                SeqSkipUntilIdle(name="Sewing"),
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
                SeqSkipUntilIdle(name="Eavesdrop"),
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
                SeqSkipUntilIdle(name="Cookies!!!"),
                LoomsToCenter("Move to main area"),
                SeqCheckpoint("intro_dorms2"),
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
                SeqSkipUntilIdle(name="Brugaves and Erlina return"),
                SeqMove(
                    name="Move to Erlina",
                    coords=[
                        Vec3(31.747, -8.998, -141.005),
                    ],
                ),
                SkipTutorial("Skip Erlina Tutorial"),
                SeqMove(
                    name="Move to Brugaves",
                    coords=[
                        Vec3(33.529, -8.932, -141.817),
                    ],
                ),
                SkipTutorial("Skip Brugaves Tutorial"),
                SeqSkipUntilIdle(name="Clear tutorial screen"),
                SeqMove(
                    name="Move to Moraine",
                    coords=[
                        Vec3(33.071, -8.998, -136.126),
                    ],
                ),
                SeqInteract("Headmaster Moraine"),
                SeqDelay("Wait", timeout_in_s=1.0),
                SeqInteract("Confirm"),
                SeqDelay("Wait", timeout_in_s=0.2),
                SeqInteract("Confirm"),
                SeqDelay("Wait", timeout_in_s=0.2),
                SeqInteract("Confirm"),
                SeqSkipUntilIdle(name="Talking to Moraine"),
                SeqMove(
                    name="Move to pit",
                    coords=[
                        Vec3(30.334, 7.013, 191.537),
                    ],
                ),
                SeqInteract("Jump"),
            ],
        )


class IntroFinalTrial(SeqList):
    def __init__(self: Self) -> None:
        super().__init__(
            name="Final trials",
            children=[
                SeqMove(
                    name="Move to ladder",
                    coords=[
                        InteractMove(33.059, -12.998, -345.326),
                        Vec3(37.050, -12.998, -344.937),
                        Vec3(42.429, -12.998, -350.327),
                        Vec3(43.500, -12.998, -349.470),
                    ],
                ),
                SeqClimb(
                    name="Climb ladder",
                    coords=[
                        InteractMove(43.500, -7.998, -348.533),
                    ],
                ),
                SeqMove(
                    name="Move near lever",
                    coords=[
                        Vec3(41.925, -7.998, -344.613),
                        Vec3(40.825, -7.998, -338.668),
                    ],
                ),
                SeqMove(
                    name="Move to lever",
                    coords=[
                        Vec3(37.852, -7.998, -334.758),
                    ],
                    precision=0.1,
                ),
                SeqInteract("Lever"),
                SeqMove(
                    name="Move to chest",
                    coords=[
                        Vec3(41.031, -7.998, -338.552),
                        Vec3(40.723, -7.998, -341.119),
                        InteractMove(24.618, -7.998, -341.119),
                        Vec3(24.618, -7.998, -334.883),
                    ],
                ),
                SeqInteract("Chest"),
                SeqMashUntilIdle("Chest"),
                SeqMove(
                    name="Move to brazier",
                    coords=[
                        Vec3(24.567, -7.998, -340.309),
                        InteractMove(41.214, -7.998, -340.309),
                        Vec3(41.550, -7.998, -334.885),
                    ],
                ),
                SeqInteract("Brazier"),
                SeqMashUntilIdle("Brazier"),
                SeqCombatAndMove(
                    name="Fight enemies",
                    coords=[
                        Vec3(37.523, -7.998, -335.876),
                        InteractMove(34.825, -12.998, -338.872),
                        Vec3(32.868, -12.998, -336.460),
                    ],
                ),
                SeqClimb(
                    name="Climb wall",
                    coords=[
                        InteractMove(32.868, -10.140, -336.470),
                        Vec3(32.881, -2.998, -335.533),
                    ],
                ),
                SeqMove(
                    name="Jump gaps",
                    coords=[
                        Vec3(32.453, -2.998, -323.957),
                        InteractMove(32.453, -2.998, -316.460),
                        InteractMove(35.481, -2.998, -316.460),
                        InteractMove(35.540, -2.998, -313.519),
                        InteractMove(38.415, -2.998, -313.519),
                        InteractMove(38.452, -2.998, -309.460),
                        InteractMove(43.540, -2.998, -309.454),
                        InteractMove(43.540, -2.998, -304.052),
                    ],
                ),
                SeqMove(
                    name="Move to chest",
                    coords=[
                        Vec3(39.416, -2.998, -302.099),
                        InteractMove(32.931, -2.995, -308.069),
                        Vec3(24.997, -2.998, -301.194),
                        Vec3(24.997, -2.998, -296.224),
                    ],
                ),
                SeqInteract("Chest"),
                SeqMashUntilIdle("Chest"),
                SeqCombatAndMove(
                    name="Move to brazier",
                    coords=[
                        Vec3(24.954, -2.998, -301.107),
                        InteractMove(31.489, -2.998, -308.173),
                        Vec3(32.657, -2.998, -308.173),
                        InteractMove(39.358, -2.998, -301.492),
                        Vec3(41.340, -2.998, -297.060),
                    ],
                ),
                SeqInteract("Brazier"),
                SeqMashUntilIdle("Brazier"),
                SeqMove(
                    name="Move to platform",
                    coords=[
                        Vec3(39.415, -2.998, -297.149),
                        Vec3(32.923, -2.998, -292.023),
                    ],
                ),
                SeqInteract("Elevator"),
                SeqMashUntilIdle("Erlina and Brugaves"),
                SeqMove(
                    name="Move to pillar",
                    coords=[
                        Vec3(81.996, -9.998, -195.727),
                    ],
                ),
                SeqInteract("Pillar"),
                SeqSkipUntilCombat("Wyrd"),
                SeqCombat("Wyrd"),
                # TODO(orkaboy): Implement proper level up
                SeqMashUntilIdle("TEMP: Level up & cutscene"),
                SeqMove(
                    name="Leave dungeon",
                    coords=[
                        Vec3(82.074, -9.998, -198.437),
                        HoldDirection(33.000, 4.002, -128.083, joy_dir=Vec2(0, -1)),
                    ],
                ),
                # Jumping into a cutscene here
                SeqMove(
                    name="Leave dungeon",
                    precision=2.0,
                    coords=[
                        InteractMove(33.000, -6.990, -130.200),
                    ],
                ),
                # Detect entering world map
                SeqSkipUntilClose("Leaving home", coord=Vec3(109.500, 2.002, 61.698)),
                # Activate storytelling amulet
                # TODO(orkaboy): Should make this optional (config)
                SeqAmulet("Storytelling Amulet"),
                SeqMove(
                    name="Move to Forbidden Cave",
                    coords=[
                        Vec3(109.500, 2.002, 64.000),
                        Vec3(108.000, 2.002, 64.000),
                        Vec3(108.000, 2.002, 66.500),
                    ],
                ),
                SeqInteract("Forbidden Cave"),
            ],
        )


class IntroForbiddenCave(SeqList):
    def __init__(self: Self) -> None:
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
                SeqMove(
                    name="Climb tower",
                    coords=[
                        InteractMove(-46.460, 6.002, 139.104),
                        InteractMove(-43.510, 9.002, 139.460),
                        InteractMove(-43.487, 11.002, 140.467),
                        InteractMove(-44.700, 12.002, 140.467),
                        InteractMove(-44.700, 15.002, 141.540),
                    ],
                ),
                SeqClimb(
                    name="Climb wall",
                    coords=[
                        InteractMove(-44.573, 16.321, 141.530),
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
                    name="Navigate to key",
                    coords=[
                        # TODO(orkaboy): Suboptimal movement. Should fight.
                        Vec3(53.573, 1.010, 133.691),
                        InteractMove(53.353, 4.012, 137.474),
                        Vec3(56.658, 4.012, 140.818),
                        InteractMove(59.915, 8.012, 144.015),
                        Vec3(60.501, 8.002, 148.204),
                        Vec3(71.706, 10.002, 148.204),
                        Vec3(73.633, 10.002, 142.899),
                        Vec3(72.258, 10.002, 138.201),
                        InteractMove(69.521, 3.010, 138.381),
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
                SeqCombatAndMove(
                    name="Fight",
                    coords=[
                        Vec3(21.487, 20.002, 137.556),
                        Vec3(25.335, 20.002, 132.576),
                        InteractMove(25.335, 1.010, 130.365),
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
                # TODO(orkaboy): Fix sequence
                SeqInteract("Campfire"),
                SeqDelay("Campfire", timeout_in_s=0.5),
                SeqInteract("Campfire"),
                SeqDelay("Campfire", timeout_in_s=0.5),
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
                # TODO(orkaboy): Can currently fail the fight.
                # TODO(orkaboy): Need to block/use abilities.
                SeqCombat("Bosslug fight"),
                # TODO(orkaboy): Continue routing.
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
                IntroFinalTrial(),
                SeqCheckpoint("forbidden_cave"),
                IntroForbiddenCave(),
            ],
        )
