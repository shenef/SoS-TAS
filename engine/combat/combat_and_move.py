import logging
from collections.abc import Callable
from enum import Enum, auto
from typing import Any, Self

from control.sos import sos_ctrl
from engine.combat.combat_controller import CombatController
from engine.mathlib import Vec3
from engine.seq import (
    CancelMove,
    Graplou,
    HoldDirection,
    InteractMove,
    MoveToward,
    SeqBase,
    SeqMove,
)
from memory import combat_manager_handle, level_up_manager_handle

logger = logging.getLogger(__name__)
combat_manager = combat_manager_handle()
level_up_manager = level_up_manager_handle()


class EncounterState(Enum):
    BEFORE_COMBAT = auto()
    COMBAT = auto()
    POST_COMBAT = auto()
    LEVEL_UP = auto()


LEVEL_UP_TIMEOUT = 5.0


class SeqCombat(SeqBase):
    def __init__(
        self: Self,
        name: str,
        level_up_timeout: float = LEVEL_UP_TIMEOUT,
        func: Callable[..., Any] = None,
    ) -> None:
        super().__init__(name, func)
        self.state = EncounterState.BEFORE_COMBAT
        self.combat_controller = CombatController(level_up_timeout)

    def execute(self: Self, delta: float) -> bool:
        self.combat_controller.update_state(delta)

        encounter_done = self.combat_controller.is_done()
        match self.state:
            case EncounterState.BEFORE_COMBAT:
                if encounter_done is False:
                    self.state = EncounterState.COMBAT
            case EncounterState.COMBAT:
                if encounter_done is True:
                    self.state = EncounterState.POST_COMBAT
                else:
                    self.combat_controller.execute_combat(delta)
            case EncounterState.POST_COMBAT:
                # Assume we are going into some kind of cutscene
                ctrl = sos_ctrl()
                ctrl.set_neutral()
                ctrl.confirm(tapping=True)
                # If the combat controller wants control again, there is a level up screen
                if encounter_done is False:
                    self.state = EncounterState.LEVEL_UP
                # Detect if we've actually exited the combat state + timeout
                elif self.combat_controller.state is CombatController.FSM.IDLE:
                    return True
            case EncounterState.LEVEL_UP:
                if encounter_done is True:
                    return True
                self.combat_controller.execute_combat(delta)

        return False

    def __repr__(self: Self) -> str:
        return (
            f"Executing single Combat Sequence ({self.name}): {self.combat_controller.state.name}."
        )


class SeqCombatAndMove(SeqMove):
    _TOGGLE_TIME = 0.05

    class FSM(Enum):
        """Finite State Machine states."""

        MOVE = auto()
        COMBAT = auto()
        RECOVER = auto()

    def __init__(
        self: Self,
        name: str,
        coords: list[Vec3 | InteractMove | CancelMove | HoldDirection | MoveToward | Graplou],
        recovery_path: SeqBase = None,
        precision: float = 0.2,
        precision2: float = 1.0,
        tap_rate: float = 0.1,
        running: bool = True,
        func: Callable = None,
        emergency_skip: Callable[[], bool] | None = None,
        invert: bool = False,
        level_up_timeout: float = LEVEL_UP_TIMEOUT,
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
        self.combat_controller = CombatController(level_up_timeout)
        self.encounter_done = True
        self.state = SeqCombatAndMove.FSM.MOVE
        self.recovery_path = recovery_path

    # Override
    def navigate_to_checkpoint(self: Self, delta: float) -> None:
        self.combat_controller.update_state(delta)
        encounter_done = self.combat_controller.is_done()

        # If we run into a battle for any reason, switch to the combat state
        if encounter_done is False:
            self.state = SeqCombatAndMove.FSM.COMBAT

        match self.state:
            case SeqCombatAndMove.FSM.MOVE:
                # If there is no active fight, move along the designated path
                super().navigate_to_checkpoint(delta)
            case SeqCombatAndMove.FSM.COMBAT:
                self.combat_controller.execute_combat(delta)
                if encounter_done:
                    ctrl = sos_ctrl()
                    ctrl.set_neutral()
                    ctrl.toggle_confirm(False)
                    if self.recovery_path is not None:
                        logger.info("Finished combat, executing recovery path")
                        self.state = SeqCombatAndMove.FSM.RECOVER
                    else:
                        logger.info("Finished combat, continuing navigation")
                        self.state = SeqCombatAndMove.FSM.MOVE
            case SeqCombatAndMove.FSM.RECOVER:
                # After combat, run the recovery node, then continue regular movement
                if self.recovery_path.execute(delta):
                    logger.info("Finished recovery path, continuing navigation")
                    self.state = SeqCombatAndMove.FSM.MOVE

    def __repr__(self: Self) -> str:
        if self.combat_controller.is_done():
            return super().__repr__()
        return f"Executing Combat Sequence ({self.name}): {self.combat_controller.state.name}."
