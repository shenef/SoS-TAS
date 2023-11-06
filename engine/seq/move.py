import logging
import math
from collections.abc import Callable
from typing import Self

from imgui_bundle import imgui

from control import sos_ctrl
from engine.mathlib import Vec2, Vec3
from engine.seq.base import SeqBase
from engine.seq.time import SeqDelay
from memory import (
    PlayerMovementState,
    boat_manager_handle,
    combat_manager_handle,
    player_party_manager_handle,
)

logger = logging.getLogger(__name__)

player_party_manager = player_party_manager_handle()
boat_manager = boat_manager_handle()
combat_manager = combat_manager_handle()


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
        func: Callable = None,
    ) -> None:
        self.joy_dir = joy_dir
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


class SeqHoldDirectionDelay(SeqBase):
    """Sequencer node to move in a direction for a specified period of time."""

    def __init__(
        self: Self,
        name: str,
        joy_dir: Vec2,
        timeout_s: float,
        func: Callable = None,
    ) -> None:
        self.joy_dir = joy_dir
        self.timeout_s = timeout_s
        self.timer = 0
        super().__init__(name, func)

    def execute(self: Self, delta: float) -> bool:
        self.timer += delta

        ctrl = sos_ctrl()
        ctrl.set_joystick(self.joy_dir)
        # If arrived, go to next coordinate in the list
        if self.timer >= self.timeout_s:
            logger.debug(f"Hold direction done after {self.timeout_s} seconds.")
            ctrl.set_neutral()
            return True
        return False

    def __repr__(self: Self) -> str:
        return f"{self.name}: Holding joystick dir {self.joy_dir} until timeout {self.timer}/{self.timeout_s}"  # noqa: E501


class SeqHoldDirectionUntilCombat(SeqBase):
    """Sequencer node to move in a direction until combat starts."""

    TOGGLE_TIME = 0.1

    def __init__(self: Self, name: str, joy_dir: Vec2, mash_confirm: bool = False) -> None:
        super().__init__(name)
        self.joy_dir = joy_dir
        self.mash_confirm = mash_confirm
        self.timer = 0
        self.toggle_state = False

    def execute(self: Self, delta: float) -> bool:
        player_pos = player_party_manager.position
        if player_pos.x is None:
            return False

        ctrl = sos_ctrl()

        if self.mash_confirm:
            self.timer += delta
            if self.timer >= self.TOGGLE_TIME:
                self.timer = 0
                self.toggle_state = not self.toggle_state
                ctrl.toggle_confirm(state=self.toggle_state)

        ctrl.set_joystick(self.joy_dir)
        if combat_manager.encounter_done is False:
            ctrl.set_neutral()
            ctrl.toggle_confirm(state=False)
            return True
        return False

    def __repr__(self: Self) -> str:
        return f"Holding direction while waiting for combat ({self.name})."


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


class Graplou(Vec3):
    def __init__(
        self: Self,
        x: float,
        y: float,
        z: float,
        joy_dir: Vec2 = None,
        hold_timer: float = 0.0,
    ) -> None:
        super().__init__(x, y, z)
        self.joy_dir = joy_dir
        self.hold_timer = hold_timer

    def __repr__(self: Self) -> str:
        return f"Graplou({super().__repr__()}, joy_dir={self.joy_dir})"


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
        coords: list[Vec3 | InteractMove | CancelMove | Graplou | HoldDirection | MoveToward],
        precision: float = 0.2,
        precision2: float = 1.0,
        tap_rate: float = 0.05,
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
        self.timer = 0
        self.hold_timer = 0
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

    def handle_toggling_input(self: Self, delta: float, player_pos: Vec3, target: Vec3) -> None:
        ctrl = sos_ctrl()
        if isinstance(target, InteractMove) or (isinstance(target, MoveToward) and target.mash):
            # Only tap while outside the secondary precision radius
            if Vec3.is_close(player_pos, target, self.precision2):
                ctrl.toggle_confirm(False)
            else:
                self.timer += delta
                if self.timer >= self.tap_rate:
                    self.confirm_state = not self.confirm_state
                    ctrl.toggle_confirm(self.confirm_state)
                    self.timer = 0
        elif isinstance(target, CancelMove):
            self.timer += delta
            if self.timer >= self.tap_rate:
                self.confirm_state = not self.confirm_state
                ctrl.toggle_cancel(self.confirm_state)
                self.timer = 0
        elif isinstance(target, Graplou):
            self.hold_timer += delta
            if target.joy_dir is None:
                target.joy_dir = Vec2(target.x - player_pos.x, target.z - player_pos.z)
            if self.hold_timer >= target.hold_timer:
                # Only Graplou while outside the secondary precision radius
                if Vec3.is_close(player_pos, target, self.precision2):
                    ctrl.toggle_graplou(False)
                else:
                    self.timer += delta
                    if self.timer >= self.tap_rate:
                        self.confirm_state = not self.confirm_state
                        ctrl.toggle_graplou(self.confirm_state)
                        self.timer = 0

    def handle_movement(self: Self, player_pos: Vec3, target: Vec3) -> None:
        ctrl = sos_ctrl()
        precision = (
            self.precision2 if isinstance(target, Graplou | HoldDirection) else self.precision
        )
        # If arrived, go to next coordinate in the list
        if Vec3.is_close(player_pos, target, precision):
            logger.debug(
                f"Checkpoint {self.step}, "
                + f"Δ: {Vec3.dist(player_pos, target):.3f}, "
                + f"Pos: {player_pos}, "
                + f"{target}"
            )
            self.step = self.step + 1
            # Reset state variables
            self.timer = 0
            self.hold_timer = 0
            self.confirm_state = False
            # Clear potentially held buttons
            ctrl.toggle_cancel(False)
            ctrl.toggle_confirm(False)
        elif isinstance(target, HoldDirection | Graplou):
            ctrl.set_joystick(target.joy_dir)
        elif isinstance(target, MoveToward):
            self.move_function(player_pos=player_pos, target_pos=target.anchor)
        else:
            self.move_function(player_pos=player_pos, target_pos=target)

    def navigate_to_checkpoint(self: Self, delta: float) -> None:
        # Move towards target
        if self.step >= len(self.coords):
            return
        target = self.coords[self.step]

        player_pos = self.player_position()
        if player_pos.x is None:
            return

        self.handle_toggling_input(delta, player_pos, target)
        self.handle_movement(player_pos, target)

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
            return f"{self.name} [{num_coords}/{num_coords}]"
        target = self.coords[self.step]
        step = self.step + 1
        return f"{self.name} [{step}/{num_coords}]: {target}"

    def render_tree(self: Self, parent_path: str, selected: bool) -> None:
        """Render imgui tree view."""
        imgui.push_id(parent_path)
        if selected:
            imgui.push_style_color(imgui.Col_.text, imgui.ImVec4(0.1, 0.9, 0.1, 1.0))
        tree_node = imgui.tree_node_ex(
            f"{self.__class__.__name__}({self.name})", imgui.TreeNodeFlags_.span_full_width
        )
        if selected:
            imgui.pop_style_color()
        if tree_node:
            self.render_coords(selected)
            imgui.tree_pop()
        imgui.pop_id()

    def render_coords(self: Self, selected: bool) -> None:
        """Render imgui tree leaf (coords)."""
        for idx, coord in enumerate(self.coords):
            child_selected = selected and idx == self.step
            if child_selected:
                imgui.push_style_color(imgui.Col_.text, imgui.ImVec4(0.1, 0.5, 0.1, 1.0))
            imgui.tree_node_ex(
                f"[{idx}] {coord}",
                imgui.TreeNodeFlags_.no_tree_push_on_open
                | imgui.TreeNodeFlags_.leaf
                | imgui.TreeNodeFlags_.span_full_width,
            )
            if child_selected:
                imgui.pop_style_color()


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
        hold_skip: bool = False,
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
        self.hold_skip = hold_skip

    def player_position(self: Self) -> Vec3:
        boat_pos = boat_manager.position
        if boat_pos is None:
            return Vec3(0.0, 0.0, 0.0)
        return boat_pos

    def move_function(self: Self, player_pos: Vec3, target_pos: Vec3) -> None:
        ctrl = sos_ctrl()
        if self.hold_skip:
            ctrl.toggle_turbo(state=True)
            ctrl.toggle_confirm(state=True)
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
        if self.hold_skip:
            ctrl.toggle_turbo(state=False)
            ctrl.toggle_confirm(state=False)


class SeqRaft(SeqMove):
    """
    Movement function for navigating raft segments.

    Use the dpad and Mistral Bracelet to move around.
    """

    def __init__(
        self: Self,
        name: str,
        coords: list[Vec3],
        precision: float = 3,
        precision2: float = 3,
        tap_rate: float = 0.05,
    ) -> None:
        super().__init__(name, coords, precision, precision2, tap_rate)

    def move_function(self: Self, player_pos: Vec3, target_pos: Vec3) -> None:
        # Turn away from the direction we want to go
        target_vec = player_pos - target_pos
        target_vec_norm = Vec3.normalize(target_vec)
        joy_dir = Vec2(target_vec_norm.x, target_vec_norm.z)

        ctrl = sos_ctrl()
        ctrl.set_joystick(joy_dir)

    def handle_toggling_input(self: Self, delta: float, player_pos: Vec3, target: Vec3) -> None:
        ctrl = sos_ctrl()
        # Only tap while outside the secondary precision radius
        if Vec3.is_close(player_pos, target, self.precision2):
            ctrl.toggle_bracelet(False)
        else:
            self.timer += delta
            if self.timer >= self.tap_rate:
                self.confirm_state = not self.confirm_state
                ctrl.toggle_bracelet(self.confirm_state)
                self.timer = 0

    def on_done(self: Self) -> None:
        ctrl = sos_ctrl()
        ctrl.set_neutral()
        ctrl.toggle_bracelet(state=False)
