import logging

from engine.combat import SeqCombatMash
from engine.mathlib import Vec2, Vec3
from engine.seq import (
    InteractMove,
    SeqCheckpoint,
    SeqClimb,
    SeqHoldDirectionUntilClose,
    SeqHoldDirectionUntilLostControl,
    SeqList,
    SeqLog,
    SeqManualUntilClose,
    SeqMove,
    SeqTurboMashUntilIdle,
)

logger = logging.getLogger(__name__)


class IntroMountainTrail(SeqList):
    def __init__(self):
        super().__init__(
            name="Mountain Trail",
            children=[
                SeqTurboMashUntilIdle(name="Wait for control"),
                SeqLog(name="SYSTEM", text="We have control!"),
                SeqMove(
                    name="Move to fight",
                    coords=[
                        InteractMove(33.253, 6.002, 20.273),
                        Vec3(37.799, 5.477, 18.084),
                        Vec3(49.640, 6.010, 6.719),
                        Vec3(55.897, 6.002, 6.543),
                        InteractMove(56.819, 13.002, 13.466),
                        InteractMove(44.829, 13.010, 25.305),
                    ],
                ),
                # TODO: Need to be able to do special ability (mash fails for Zale)
                SeqCombatMash(
                    name="Fight",
                    coords=[
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
                    ],
                ),
                SeqHoldDirectionUntilClose(
                    name="Go inside cavern",
                    target=Vec3(-88.500, 10.002, 32.058),
                    joy_dir=Vec2(0, 1),
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
                # TODO: Issue here, position isn't tracked while on the wall
                SeqManualUntilClose(
                    name="MANUAL: Go up cliff",
                    target=Vec3(-87.284, 22.002, 44.522),
                    precision=1.0,
                ),
                SeqCombatMash(
                    name="Fight slug",
                    coords=[
                        Vec3(-73.903, 22.002, 34.029),
                    ],
                ),
                SeqHoldDirectionUntilClose(
                    name="Go out of cavern",
                    target=Vec3(-35.819, 21.002, 27.816),
                    joy_dir=Vec2(0, -1),
                ),
                SeqMove(
                    name="Move to campfire",
                    coords=[
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
    def __init__(self):
        super().__init__(
            name="Mooncradle",
            children=[
                SeqCheckpoint(checkpoint_name="intro_mooncradle"),
                SeqMove(
                    name="Move to cave entrance",
                    coords=[
                        Vec3(-68.930, -10.998, 26.150),
                    ],
                ),
                SeqHoldDirectionUntilClose(
                    name="Go out of cavern",
                    target=Vec3(-13.969, -11.998, 38.757),
                    joy_dir=Vec2(0, -1),
                ),
                # TODO: Continue routing Mooncradle
            ],
        )


class EvermistIsland(SeqList):
    def __init__(self):
        super().__init__(
            name="Evermist Island",
            children=[
                IntroMountainTrail(),
                IntroMooncradle(),
            ],
        )
