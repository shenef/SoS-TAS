import logging
from enum import Enum, auto
from typing import Self

from control import sos_ctrl
from engine.combat import SeqCombat, SeqCombatManual
from engine.mathlib import Vec3
from engine.seq import (
    InteractMove,
    SeqBase,
    SeqCheckpoint,
    SeqClimb,
    SeqInteract,
    SeqList,
    SeqMove,
    SeqSkipUntilCombat,
    SeqSkipUntilIdle,
)
from memory import new_dialog_manager_handle

logger = logging.getLogger(__name__)

new_dialog_manager = new_dialog_manager_handle()


class ElderMistTrialsRight(SeqList):
    def __init__(self: Self) -> None:
        super().__init__(
            name="Right Trial",
            children=[
                SeqMove(
                    name="Navigate right Trial",
                    coords=[
                        Vec3(87.691, -5.998, 80.466),
                        Vec3(92.032, -5.998, 80.164),
                        InteractMove(94.589, -8.998, 78.182),
                        InteractMove(97.268, -5.998, 75.787),
                        Vec3(101.543, -3.998, 76.107),
                        InteractMove(108.939, -3.998, 76.190),
                        Vec3(118.863, -5.998, 76.819),
                        InteractMove(118.863, -10.998, 74.542),
                        Vec3(120.543, -10.998, 73.459),
                        InteractMove(123.539, -10.998, 73.459),
                        InteractMove(129.062, -10.998, 78.701),
                        InteractMove(127.996, -7.998, 80.362),
                        Vec3(127.004, -7.998, 81.354),
                    ],
                ),
                SeqClimb(
                    name="Climb cliff",
                    coords=[
                        InteractMove(126.832, -3.956, 81.168),
                        Vec3(126.170, 8.002, 81.830),
                    ],
                ),
                SeqMove(
                    name="Navigate right trial",
                    coords=[
                        Vec3(127.200, 8.002, 88.541),
                        InteractMove(127.200, 8.002, 91.673),
                        Vec3(127.200, 8.002, 95.574),
                        Vec3(125.267, 8.002, 100.462),
                        Vec3(121.495, 8.002, 104.859),
                    ],
                ),
                SeqClimb(
                    name="Climb cliff",
                    coords=[
                        InteractMove(121.168, 11.253, 105.168),
                        Vec3(121.830, 16.002, 105.830),
                    ],
                ),
                # TODO(orkaboy): Manual. Fix with correct combat
                SeqCombatManual(
                    name="Navigate to lever",
                    coords=[
                        Vec3(116.468, 16.002, 111.341),
                        Vec3(109.964, 16.002, 111.458),
                        Vec3(108.043, 16.002, 110.545),
                        InteractMove(102.052, 16.002, 110.545),
                        Vec3(99.781, 16.002, 110.523),
                        InteractMove(99.781, 8.002, 107.825),
                        Vec3(99.453, 8.002, 99.120),
                        InteractMove(99.453, 1.002, 91.542),
                        Vec3(96.941, 1.002, 93.634),
                    ],
                ),
                SeqInteract("Flip lever"),
                SeqMove(
                    name="Move to cliff",
                    coords=[
                        Vec3(102.188, 1.002, 83.490),
                        InteractMove(114.565, 1.002, 83.490),
                        Vec3(117.486, 1.002, 87.864),
                    ],
                ),
                SeqClimb(
                    name="Climb cliff",
                    coords=[
                        InteractMove(117.168, 3.847, 88.168),
                        Vec3(117.830, 8.002, 88.830),
                    ],
                ),
                # TODO(orkaboy): Manual. Fix with correct combat
                SeqCombatManual(  # Can also get into the fight in this segment
                    name="Move to trigger",
                    coords=[
                        Vec3(116.617, 8.002, 98.078),
                        Vec3(114.460, 8.002, 100.543),
                        Vec3(93.543, 8.002, 100.543),
                        Vec3(85.471, 8.002, 92.376),
                        Vec3(85.015, 8.002, 90.035),
                    ],
                ),
                SeqInteract("Doodad"),
            ],
        )


class SelectOption(SeqBase):
    class State(Enum):
        Approach = auto()
        WaitForDialog = auto()
        ClearPrompt = auto()
        Answer = auto()

    TIMEOUT = 0.2

    def __init__(self: Self, name: str, option: int = 0) -> None:
        super().__init__(name)
        self.timer = 0
        self.option = option
        self.state = self.State.Approach

    def execute(self: Self, delta: float) -> bool:
        ctrl = sos_ctrl()
        match self.state:
            case self.State.Approach:
                ctrl.confirm()
                self.state = self.State.WaitForDialog
            case self.State.WaitForDialog:
                if new_dialog_manager.dialog_open:
                    ctrl.toggle_turbo(state=True)
                    ctrl.toggle_confirm(state=True)
                    self.state = self.State.ClearPrompt
            case self.State.ClearPrompt:
                self.timer += delta
                if self.timer >= self.TIMEOUT:
                    self.state = self.State.Answer
                    ctrl.toggle_turbo(state=False)
                    ctrl.toggle_confirm(state=False)
            case self.State.Answer:
                for _ in range(self.option):
                    ctrl.dpad.tap_down()
                ctrl.confirm()
                return True
        return False

    def __repr__(self: Self) -> str:
        return f"{self.state} ({self.state})"


class ElderMistTrialsCenter(SeqList):
    def __init__(self: Self) -> None:
        super().__init__(
            name="Center Trial",
            children=[
                SeqMove(
                    name="Move to wall",
                    coords=[
                        Vec3(49.704, 4.010, 55.624),
                        Vec3(50.274, 1.002, 103.499),
                        Vec3(54.201, 1.002, 109.420),
                        Vec3(54.201, 1.002, 115.764),
                        Vec3(50.341, 1.002, 119.543),
                    ],
                ),
                SeqClimb(
                    name="Climb wall",
                    coords=[
                        InteractMove(50.341, 5.811, 119.530),
                        Vec3(49.441, 11.222, 119.530),
                        Vec3(47.783, 11.222, 119.530),
                    ],
                ),
                SeqMove(
                    name="Move to question",
                    coords=[
                        Vec3(47.129, 10.002, 118.084),
                        Vec3(45.391, 10.002, 118.741),
                    ],
                ),
                # TODO(orkaboy): Assumes top is correct answer
                SelectOption("First question"),
                SeqMove(
                    name="Move to wall",
                    coords=[
                        Vec3(47.866, 10.002, 115.756),
                        InteractMove(43.912, 10.002, 111.596),
                        Vec3(41.175, 10.002, 110.298),
                        Vec3(41.204, 10.002, 107.443),
                        Vec3(42.466, 10.002, 105.762),
                        Vec3(42.457, 10.002, 101.229),
                        Vec3(43.476, 10.002, 100.882),
                    ],
                ),
                SeqClimb(
                    name="Climb wall",
                    coords=[
                        InteractMove(43.168, 13.664, 101.168),
                        Vec3(43.851, 17.002, 101.823),
                    ],
                ),
                SeqMove(
                    name="Move to question",
                    coords=[
                        Vec3(45.126, 17.002, 101.581),
                        InteractMove(53.540, 17.002, 101.565),
                        Vec3(53.540, 17.002, 105.540),
                        InteractMove(56.450, 14.002, 105.540),
                        InteractMove(59.651, 7.002, 105.540),
                        Vec3(59.860, 7.002, 108.213),
                    ],
                ),
                # TODO(orkaboy): Assumes top is correct answer
                SelectOption("Second question"),
                SeqMove(
                    name="Move to wall",
                    coords=[
                        Vec3(58.584, 7.002, 106.941),
                    ],
                ),
                SeqClimb(
                    name="Climb wall",
                    coords=[
                        InteractMove(58.707, 10.284, 107.043),
                        Vec3(58.045, 14.002, 107.705),
                    ],
                ),
                SeqMove(
                    name="Move to wall",
                    coords=[
                        Vec3(58.791, 14.002, 110.940),
                        InteractMove(55.071, 14.002, 114.751),
                        Vec3(56.549, 14.002, 117.804),
                    ],
                ),
                SeqClimb(
                    name="Climb wall",
                    coords=[
                        InteractMove(56.168, 19.161, 118.168),
                        Vec3(56.830, 28.002, 118.830),
                    ],
                ),
                SeqMove(
                    name="Move to question",
                    coords=[
                        Vec3(59.421, 28.002, 115.745),
                        Vec3(59.461, 28.002, 109.460),
                        InteractMove(40.986, 28.002, 109.500),
                        Vec3(40.171, 28.002, 110.857),
                        Vec3(40.540, 28.002, 113.208),
                        InteractMove(41.917, 20.002, 113.208),
                        Vec3(43.311, 20.002, 116.665),
                    ],
                ),
                # TODO(orkaboy): Assumes second is correct answer
                SelectOption("Third Question", option=1),
                SeqMove(
                    name="Move to pillar",
                    coords=[
                        Vec3(42.037, 20.002, 113.742),
                        Vec3(41.725, 20.002, 111.109),
                    ],
                ),
                SeqInteract("Doodad"),
            ],
        )


class ElderMistTrialsLeft(SeqList):
    def __init__(self: Self) -> None:
        super().__init__(
            name="Left Trial",
            children=[
                # TODO(orkaboy): Manual. Fix with correct combat
                SeqCombatManual(
                    name="Move to lever",
                    coords=[
                        Vec3(3.565, 1.002, 88.080),
                        Vec3(-2.886, 6.010, 95.497),
                        Vec3(-9.841, 6.002, 94.938),
                        Vec3(-10.918, 6.002, 84.260),
                    ],
                ),
                SeqInteract("Lever"),
                SeqCombatManual(
                    name="Drop ladder",
                    coords=[
                        Vec3(-17.307, 6.002, 94.302),
                        InteractMove(-22.814, 6.002, 94.302),
                        Vec3(-24.680, 6.002, 98.165),
                        InteractMove(-24.680, 8.087, 103.891),
                        Vec3(-24.680, 14.010, 110.938),
                        Vec3(-16.499, 14.002, 110.815),
                        Vec3(-10.784, 14.002, 104.157),
                        Vec3(-6.991, 14.002, 104.157),
                        InteractMove(-7.000, 6.002, 100.389),
                        Vec3(-10.940, 6.002, 84.260),
                    ],
                ),
                SeqInteract("Lever"),
                SeqMove(
                    name="Move to ladder",
                    coords=[
                        Vec3(-6.982, 6.002, 102.546),
                    ],
                ),
                SeqClimb(
                    name="Climb ladder",
                    coords=[
                        InteractMove(-7.000, 10.414, 102.530),
                        Vec3(-7.000, 14.002, 103.467),
                    ],
                ),
                SeqCombatManual(
                    name="Move to doodad",
                    coords=[
                        Vec3(-10.443, 14.002, 103.467),
                        InteractMove(-10.454, 14.002, 97.185),
                        Vec3(-8.907, 14.002, 92.740),
                        InteractMove(-7.124, 14.002, 90.925),
                        InteractMove(-2.371, 14.002, 95.372),
                        InteractMove(-0.431, 15.589, 98.986),
                        Vec3(1.930, 18.888, 103.072),
                        Vec3(8.359, 19.002, 107.734),
                        Vec3(12.489, 19.002, 99.108),
                        # TODO(orkaboy): Temp, double back. Bad
                        Vec3(8.359, 19.002, 107.734),
                        Vec3(12.489, 19.002, 99.108),
                    ],
                ),
                SeqInteract("Doodad"),
            ],
        )


class ElderMistTrials(SeqList):
    def __init__(self: Self) -> None:
        super().__init__(
            name="Elder Mist Trials",
            children=[
                # TODO(orkaboy): Manual. Fix with correct combat
                SeqCombatManual(
                    name="Live Mana Tutorial",
                    coords=[
                        Vec3(48.570, 1.002, -6.019),
                        InteractMove(48.533, 1.002, -1.519),
                        Vec3(50.541, 1.002, 0.470),
                        InteractMove(50.541, 1.002, 3.481),
                        Vec3(51.546, 1.002, 4.541),
                        InteractMove(54.481, 1.002, 4.541),
                        InteractMove(54.481, 1.002, 12.923),
                        Vec3(54.441, 1.002, 15.912),
                        Vec3(49.410, 1.002, 26.971),
                        InteractMove(49.432, 1.002, 30.748),
                    ],
                ),
                SeqCheckpoint("elder_mist"),
                SeqMove(
                    name="Move to right Trial",
                    coords=[
                        Vec3(52.248, 1.002, 33.803),
                        Vec3(53.425, 1.002, 46.139),
                        Vec3(59.055, 4.002, 52.155),
                    ],
                ),
                SeqInteract("Teleporter"),
                # Right Trial
                ElderMistTrialsRight(),
                SeqMove(
                    name="Move to center Trial",
                    coords=[
                        Vec3(49.704, 4.010, 55.624),
                    ],
                ),
                SeqInteract("Teleporter"),
                # Center Trial
                ElderMistTrialsCenter(),
                SeqMove(
                    name="Move to left Trial",
                    coords=[
                        Vec3(39.774, 4.002, 52.453),
                    ],
                ),
                SeqInteract("Teleporter"),
                ElderMistTrialsLeft(),
                # Checkpoint before boss
                SeqCheckpoint("elder_mist_boss"),
                SeqMove(
                    name="Move to boss",
                    coords=[
                        Vec3(49.580, 1.002, 43.000),
                        Vec3(49.580, 1.002, 47.540),
                    ],
                ),
                SelectOption("Elder Mist Boss"),
                SeqSkipUntilCombat("Elder Mist Boss"),
                # TODO(orkaboy): Need combat priority to deal with sword
                SeqCombat("Elder Mist Boss"),
                SeqSkipUntilIdle("Cutscenes"),
                # TODO(orkaboy): Continue routing
            ],
        )
