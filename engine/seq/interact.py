# Libraries and Core Files
from typing import Self

from control import sos_ctrl
from engine.seq.base import SeqBase
from memory import (
    PlayerMovementState,
    combat_manager_handle,
    player_party_manager_handle,
)

player_party_manager = player_party_manager_handle()
combat_manager = combat_manager_handle()


class SeqInteract(SeqBase):
    def __init__(self: Self, name: str = "Interact") -> None:
        super().__init__(name)

    def execute(self: Self, delta: float) -> bool:
        sos_ctrl().confirm()
        return True


class SeqBracelet(SeqBase):
    def __init__(self: Self, name: str = "Bracelet") -> None:
        super().__init__(name)

    def execute(self: Self, delta: float) -> bool:
        sos_ctrl().bracelet()
        return True


class SeqTapDown(SeqBase):
    def __init__(self: Self, name: str = "Tap down") -> None:
        super().__init__(name)

    def execute(self: Self, delta: float) -> bool:
        sos_ctrl().dpad.tap_down()
        return True


class SeqTurboMashUntilIdle(SeqBase):
    # Hold confirm through cutscene while holding the turbo button
    def execute(self: Self, delta: float) -> bool:
        sos_ctrl().toggle_turbo(state=True)
        sos_ctrl().toggle_confirm(state=True)

        # Check if we have control
        done = self.is_done()
        if done:
            sos_ctrl().toggle_confirm(state=False)
            sos_ctrl().toggle_turbo(state=False)
        return done

    def is_done(self: Self) -> bool:
        return player_party_manager.movement_state == PlayerMovementState.Idle

    def __repr__(self: Self) -> str:
        return f"Mashing confirm while waiting for control ({self.name})."


class SeqTurboMashSkipCutsceneUntilIdle(SeqTurboMashUntilIdle):
    # Mash through cutscene while holding the turbo button
    def execute(self: Self, delta: float) -> bool:
        ctrl = sos_ctrl()
        ctrl.toggle_cancel(state=True)
        if super().execute(delta):
            ctrl.toggle_cancel(state=False)
            return True
        return False

    def __repr__(self: Self) -> str:
        return f"Mashing confirm and holding cancel while waiting for control ({self.name})."


class SeqTurboMashSkipCutsceneUntilCombat(SeqTurboMashSkipCutsceneUntilIdle):
    def is_done(self: Self) -> bool:
        return combat_manager.encounter_done is False

    def __repr__(self: Self) -> str:
        return f"Mashing confirm and holding cancel while waiting for combat ({self.name})."
