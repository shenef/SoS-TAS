# Libraries and Core Files

from control import sos_ctrl
from engine.seq.base import SeqBase
from memory.player_party_manager import PlayerMovementState, player_party_manager_handle

player_party_manager = player_party_manager_handle()


class SeqTurboMashUntilIdle(SeqBase):
    _TOGGLE_TIME = 0.05

    def __init__(self, name: str = "", func=None):
        super().__init__(name, func)
        self.state = False
        self.timer = 0.0

    # Mash through cutscene while holding the turbo button
    def execute(self, delta: float) -> bool:
        self.timer = self.timer + delta

        sos_ctrl().toggle_turbo(state=True)
        if self.timer > self._TOGGLE_TIME:
            self.timer = 0
            self.state = not self.state
            sos_ctrl().toggle_confirm(self.state)

        # Check if we have control
        done = player_party_manager.movement_state == PlayerMovementState.Idle
        if done:
            sos_ctrl().toggle_turbo(state=False)
        return done

    def __repr__(self) -> str:
        return f"Mashing confirm while waiting for control ({self.name})..."
