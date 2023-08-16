import logging
from collections.abc import Callable

from control import sos_ctrl
from engine.mathlib import Vec2, Vec3
from engine.seq.base import SeqBase
from engine.seq.time import SeqDelay
from memory.player_party_manager import PlayerPartyManager

logger = logging.getLogger(__name__)

player_party_manager = PlayerPartyManager()


def move_to(player: Vec2, target: Vec2, precision: float, invert: bool = False) -> None:
    ctrl = sos_ctrl()

    diff = (target - player).normalized

    joy = diff.invert_y
    if invert:
        joy = Vec2(-joy.x, -joy.y)

    ctrl.set_joystick(joy)


# Temp testing
class SeqManualUntilClose(SeqBase):
    def __init__(self, name: str, target: Vec3, precision: float = 0.2, func=None):
        self.target = target
        self.precision = precision
        super().__init__(name, func)

    def execute(self, delta: float) -> bool:
        super().execute(delta)
        # Stay still
        ctrl = sos_ctrl()
        ctrl.dpad.none()
        ctrl.set_neutral()
        # Check if we have reached the goal
        player_party_manager.update()
        player_pos = player_party_manager.position
        return Vec3.is_close(player_pos, self.target, precision=self.precision)

    def __repr__(self) -> str:
        return f"MANUAL CONTROL({self.name}) until reaching {self.target}"


class SeqHoldInPlace(SeqDelay):
    def __init__(
        self, name: str, target: Vec3, timeout_in_s: float, precision: float = 0.1
    ):
        self.target = target
        self.precision = precision
        self.timer = 0
        super().__init__(name=name, timeout_in_s=timeout_in_s)

    def execute(self, delta: float) -> bool:
        player_party_manager.update()
        player_pos = player_party_manager.position
        # If arrived, go to next coordinate in the list
        if not Vec3.is_close(player_pos, self.target, precision=self.precision):
            move_to(player=player_pos, target=self.target, precision=self.precision)
            return False
        # Stay still
        ctrl = sos_ctrl()
        ctrl.dpad.none()
        ctrl.set_neutral()
        # Wait for a while
        self.timer = self.timer + delta
        if self.timer >= self.timeout:
            self.timer = self.timeout
            return True
        return False

    def __repr__(self) -> str:
        return f"Waiting({self.name}) at {self.target}... {self.timer:.2f}/{self.timeout:.2f}"


class SeqMove(SeqBase):
    def __init__(
        self,
        name: str,
        coords: list[Vec3],
        precision: float = 0.2,
        func=None,
        emergency_skip: Callable[[], bool] | None = None,
        invert: bool = False,
    ):
        self.step = 0
        self.coords = coords
        self.precision = precision
        self.emergency_skip = emergency_skip
        self.invert = invert
        super().__init__(name, func=func)

    def reset(self) -> None:
        self.step = 0

    def _nav_done(self) -> bool:
        num_coords = len(self.coords)
        # If we are already done with the entire sequence, terminate early
        return self.step >= num_coords

    def move_function(self, player_pos: Vec3, target_pos: Vec3):
        move_to(
            player=Vec2(player_pos.x, player_pos.z),
            target=Vec2(target_pos.x, target_pos.z),
            precision=self.precision,
            invert=self.invert,
        )

    def navigate_to_checkpoint(self) -> None:
        # Move towards target
        if self.step >= len(self.coords):
            return
        target = self.coords[self.step]

        player_party_manager.update()
        player_pos = player_party_manager.position

        ctrl = sos_ctrl()
        # If arrived, go to next coordinate in the list
        if Vec3.is_close(player_pos, target, self.precision):
            logger.debug(
                f"Checkpoint reached {self.step}. Player: {player_pos} Target: {target}"
            )
            self.step = self.step + 1
            if self.step >= len(self.coords):
                ctrl.set_neutral()
        else:
            self.move_function(player_pos=player_pos, target_pos=target)

    def execute(self, delta: float) -> bool:
        self.navigate_to_checkpoint()

        done = self._nav_done()

        if done:
            logger.info(f"Finished move section: {self.name}")
            sos_ctrl().set_neutral()
        elif self.emergency_skip and self.emergency_skip():
            logger.warning(f"Finished move section with emergency skip: {self.name}")
            done = True
            sos_ctrl().set_neutral()
        return done

    def __repr__(self) -> str:
        num_coords = len(self.coords)
        if self.step >= num_coords:
            return f"{self.name}[{num_coords}/{num_coords}]"
        target = self.coords[self.step]
        step = self.step + 1
        return f"{self.name}[{step}/{num_coords}]: {target}"