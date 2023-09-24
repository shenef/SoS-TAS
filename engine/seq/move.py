import logging
import math
from collections.abc import Callable
from typing import Self

from control import sos_ctrl
from engine.mathlib import Vec2, Vec3
from engine.seq.base import SeqBase
from engine.seq.time import SeqDelay
from memory import PlayerMovementState, boat_manager_handle, player_party_manager_handle

logger = logging.getLogger(__name__)

player_party_manager = player_party_manager_handle()
boat_manager = boat_manager_handle()


def move_to(player: Vec2, target: Vec2, running: bool = True, invert: bool = False) -> None:
    ctrl = sos_ctrl()

    speed = 1.0 if running else 0.5
    joy = speed * (target - player).normalized

    if invert:
        joy = Vec2(-joy.x, -joy.y)

    ctrl.set_joystick(joy)


class SeqHoldDirectionUntilLostControl(SeqBase):
    def __init__(
        self: Self,
        name: str,
        joy_dir: Vec2,
        precision: float = 1.0,
        func: Callable = None,
    ) -> None:
        self.joy_dir = joy_dir
        self.precision = precision
        super().__init__(name, func)

    def execute(self: Self, delta: float) -> bool:
        ctrl = sos_ctrl()
        # Check if we have lost control
        if player_party_manager.movement_state == PlayerMovementState.NONE:
            ctrl.set_neutral()
            return True
        # Hold direction
        ctrl.set_joystick(self.joy_dir)
        return False

    def __repr__(self: Self) -> str:
        return f"{self.name}: Holding joystick dir {self.joy_dir} until control lost"


class SeqHoldDirectionUntilClose(SeqBase):
    def __init__(
        self: Self,
        name: str,
        target: Vec3,
        joy_dir: Vec2,
        precision: float = 1.0,
        func: Callable = None,
    ) -> None:
        self.target = target
        self.joy_dir = joy_dir
        self.precision = precision
        super().__init__(name, func)

    def execute(self: Self, delta: float) -> bool:
        player_pos = player_party_manager.position
        if player_pos.x is None:
            return False

        ctrl = sos_ctrl()
        ctrl.set_joystick(self.joy_dir)
        # If arrived, go to next coordinate in the list
        if Vec3.is_close(player_pos, self.target, self.precision):
            logger.debug(f"Target reached: {self.target}")
            ctrl.set_neutral()
            return True
        return False

    def __repr__(self: Self) -> str:
        return f"{self.name}: Holding joystick dir {self.joy_dir} until reaching {self.target}"


class SeqAwaitLostControl(SeqBase):
    def execute(self: Self, delta: float) -> bool:
        return player_party_manager.movement_state == PlayerMovementState.NONE

    def __repr__(self: Self) -> str:
        return f"{self.name}: Holding until control lost"


# Temp testing
class SeqManualUntilClose(SeqBase):
    def __init__(
        self: Self,
        name: str,
        target: Vec3,
        precision: float = 0.2,
        func: Callable = None,
    ) -> None:
        self.target = target
        self.precision = precision
        super().__init__(name, func)

    def execute(self: Self, delta: float) -> bool:
        super().execute(delta)
        # Stay still
        ctrl = sos_ctrl()
        ctrl.dpad.none()
        ctrl.set_neutral()
        # Check if we have reached the goal
        player_pos = player_party_manager.position
        return Vec3.is_close(player_pos, self.target, precision=self.precision)

    def __repr__(self: Self) -> str:
        return f"MANUAL CONTROL({self.name}) until reaching {self.target}"


class SeqHoldInPlace(SeqDelay):
    def __init__(
        self: Self,
        name: str,
        target: Vec3,
        timeout_in_s: float,
        precision: float = 0.1,
        running: bool = True,
    ) -> None:
        self.target = target
        self.precision = precision
        self.running = running
        self.timer = 0
        super().__init__(name=name, timeout_in_s=timeout_in_s)

    def execute(self: Self, delta: float) -> bool:
        player_pos = player_party_manager.position
        # If arrived, go to next coordinate in the list
        if not Vec3.is_close(player_pos, self.target, precision=self.precision):
            move_to(player=player_pos, target=self.target, running=self.running)
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

    def __repr__(self: Self) -> str:
        return f"Waiting ({self.name}) at {self.target}. {self.timer:.2f}/{self.timeout:.2f}"


class InteractMove(Vec3):
    def __repr__(self: Self) -> str:
        return f"InteractMove({super().__repr__()})"


class CancelMove(Vec3):
    def __repr__(self: Self) -> str:
        return f"CancelMove({super().__repr__()})"


class HoldDirection(Vec3):
    def __init__(self: Self, x: float, y: float, z: float, joy_dir: Vec2) -> None:
        super().__init__(x, y, z)
        self.joy_dir = joy_dir

    def __repr__(self: Self) -> str:
        return f"HoldDirection({super().__repr__()}, joy_dir={self.joy_dir})"


class MoveToward(Vec3):
    def __init__(
        self: Self, x: float, y: float, z: float, anchor: Vec3, mash: bool = False
    ) -> None:
        super().__init__(x, y, z)
        self.anchor = anchor
        self.mash = mash

    def __repr__(self: Self) -> str:
        return f"MoveToward({super().__repr__()}, anchor: {self.anchor}, mash: {self.mash})"


class SeqMove(SeqBase):
    def __init__(
        self: Self,
        name: str,
        coords: list[Vec3 | InteractMove | CancelMove | HoldDirection | MoveToward],
        precision: float = 0.2,
        precision2: float = 1.0,
        tap_rate: float = 0.1,
        running: bool = True,
        func: Callable = None,
        emergency_skip: Callable[[], bool] | None = None,
        invert: bool = False,
    ) -> None:
        self.step = 0
        self.coords = coords
        # Used for detecting endpoint of Vec3/InteractMove
        self.precision = precision
        # Used for detecting endpoint of HoldDirection and end of mashing during InteractMove
        self.precision2 = precision2
        self.running = running
        self.emergency_skip = emergency_skip
        self.invert = invert
        # Interact variables
        self.confirm_state = False
        self.confirm_timer = 0
        self.tap_rate = tap_rate
        super().__init__(name, func=func)

    def reset(self: Self) -> None:
        self.step = 0

    def _nav_done(self: Self) -> bool:
        num_coords = len(self.coords)
        # If we are already done with the entire sequence, terminate early
        return self.step >= num_coords

    def move_function(self: Self, player_pos: Vec3, target_pos: Vec3) -> None:
        move_to(
            player=Vec2(player_pos.x, player_pos.z),
            target=Vec2(target_pos.x, target_pos.z),
            running=self.running,
            invert=self.invert,
        )

    def player_position(self: Self) -> Vec3:
        return player_party_manager.position

    def navigate_to_checkpoint(self: Self, delta: float) -> None:
        # Move towards target
        if self.step >= len(self.coords):
            return
        target = self.coords[self.step]

        player_pos = self.player_position()
        if player_pos.x is None:
            return

        ctrl = sos_ctrl()
        if isinstance(target, InteractMove) or (isinstance(target, MoveToward) and target.mash):
            # Only tap while outside the secondary precision radius
            if Vec3.is_close(player_pos, target, self.precision2):
                ctrl.toggle_confirm(False)
            else:
                self.confirm_timer += delta
                if self.confirm_timer >= self.tap_rate / 2:
                    self.confirm_state = not self.confirm_state
                    ctrl.toggle_confirm(self.confirm_state)
        elif isinstance(target, CancelMove):
            self.confirm_timer += delta
            if self.confirm_timer >= self.tap_rate / 2:
                self.confirm_state = not self.confirm_state
                ctrl.toggle_cancel(self.confirm_state)

        precision = self.precision2 if isinstance(target, HoldDirection) else self.precision
        # If arrived, go to next coordinate in the list
        if Vec3.is_close(player_pos, target, precision):
            logger.debug(f"Checkpoint {self.step}. Pos.: {player_pos} Target: {target}")
            self.step = self.step + 1
            # Clear potentially held buttons
            ctrl.toggle_cancel(False)
            ctrl.toggle_confirm(False)
        elif isinstance(target, HoldDirection):
            ctrl.set_joystick(target.joy_dir)
        elif isinstance(target, MoveToward):
            self.move_function(player_pos=player_pos, target_pos=target.anchor)
        else:
            self.move_function(player_pos=player_pos, target_pos=target)

    def execute(self: Self, delta: float) -> bool:
        self.navigate_to_checkpoint(delta)

        done = self._nav_done()

        if done:
            logger.info(f"Finished move section: {self.name}")
            self.on_done()
        elif self.emergency_skip and self.emergency_skip():
            logger.warning(f"Finished move section with emergency skip: {self.name}")
            done = True
            self.on_done()
        return done

    def on_done(self: Self) -> None:
        sos_ctrl().set_neutral()

    def __repr__(self: Self) -> str:
        num_coords = len(self.coords)
        if self.step >= num_coords:
            return f"{self.name}[{num_coords}/{num_coords}]"
        target = self.coords[self.step]
        step = self.step + 1
        return f"{self.name}[{step}/{num_coords}]: {target}"


class SeqClimb(SeqMove):
    def move_function(self: Self, player_pos: Vec3, target_pos: Vec3) -> None:
        move_to(
            player=Vec2(player_pos.x, player_pos.y),
            target=Vec2(target_pos.x, target_pos.y),
            running=self.running,
            invert=self.invert,
        )


class SeqCliffMove(SeqMove):
    def player_position(self: Self) -> Vec3:
        return player_party_manager.gameobject_position


class SeqCliffClimb(SeqClimb):
    def player_position(self: Self) -> Vec3:
        return player_party_manager.gameobject_position


class SeqBoat(SeqMove):
    def __init__(
        self: Self,
        name: str,
        coords: list[Vec3 | InteractMove | CancelMove | HoldDirection | MoveToward],
        precision: float = 1.0,
        precision2: float = 2.0,
        tap_rate: float = 0.1,
        running: bool = True,
        func: Callable = None,
        emergency_skip: Callable[[], bool] | None = None,
        invert: bool = False,
    ) -> None:
        super().__init__(
            name,
            coords,
            precision,
            precision2,
            tap_rate,
            running,
            func,
            emergency_skip,
            invert,
        )

    def player_position(self: Self) -> Vec3:
        return boat_manager.position

    def move_function(self: Self, player_pos: Vec3, target_pos: Vec3) -> None:
        ctrl = sos_ctrl()
        # Get the trajectory between the player pos and the target
        target_vec = target_pos - player_pos
        target_vec_v2 = Vec2(target_vec.x, target_vec.z)

        # Get the angle to target, and the current angle of the boat
        target_angle = target_vec_v2.angle
        boat_angle = boat_manager.rotation.to_yaw()

        diff_angle = target_angle - boat_angle

        left = (diff_angle > 0 and diff_angle < math.pi) or (
            diff_angle < 0 and diff_angle < -math.pi
        )
        joy = Vec2(-1, 0) if left else Vec2(1, 0)

        ctrl.set_joystick(joy)
        ctrl.toggle_bracelet(state=True)

    def on_done(self: Self) -> None:
        ctrl = sos_ctrl()
        ctrl.set_neutral()
        ctrl.toggle_bracelet(state=False)
