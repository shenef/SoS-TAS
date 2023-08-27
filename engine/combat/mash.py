from engine.mathlib import Vec3
from engine.seq.move import InteractMove, SeqMove
from memory.combat_manager import combat_manager_handle

combat_manager = combat_manager_handle()


# TODO: Temporary code, moves along path, pausing while combat is active
class SeqCombatMash(SeqMove):
    _TOGGLE_TIME = 0.05

    def __init__(
        self,
        name: str,
        coords: list[Vec3 | InteractMove],
    ):
        super().__init__(name, coords)
        self.state = False
        self.timer = 0.0

    # Override
    def navigate_to_checkpoint(self, delta: float) -> None:
        if combat_manager.encounter_done:
            # If there is no active fight, move along the designated path
            super().navigate_to_checkpoint(delta)
        else:
            # Manual control, do nothing
            self.execute_combat(delta)

    # Mash through cutscene while holding the turbo button
    def execute_combat(self, delta: float) -> bool:
        self.timer = self.timer + delta

        # if self.timer > self._TOGGLE_TIME:
        #     self.timer = 0
        #     self.state = not self.state
        #     sos_ctrl().toggle_confirm(self.state)

        # Do we have

        # Check if we have control
        return combat_manager.encounter_done is True

    def __repr__(self) -> str:
        return f"Mashing confirm while waiting for encounter ({self.name})..."
