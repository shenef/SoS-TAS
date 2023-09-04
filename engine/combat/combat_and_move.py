from engine.combat.combat_controller import CombatController
from engine.mathlib import Vec3
from engine.seq.move import InteractMove, SeqMove
from memory.combat_manager import combat_manager_handle

combat_manager = combat_manager_handle()


# TODO: Temporary code, moves along path, pausing while combat is active
class SeqCombatAndMove(SeqMove):
    _TOGGLE_TIME = 0.05

    def __init__(
        self,
        name: str,
        coords: list[Vec3 | InteractMove],
    ):
        super().__init__(name, coords)
        self.timer = 0.0
        self.combat_controller = CombatController()

    # Override
    def navigate_to_checkpoint(self, delta: float) -> None:
        if combat_manager.encounter_done:
            # If there is no active fight, move along the designated path
            super().navigate_to_checkpoint(delta)
        else:
            self.combat_controller.execute_combat()

    def __repr__(self) -> str:
        return f"Executing Combat Sequence ({self.name})."
