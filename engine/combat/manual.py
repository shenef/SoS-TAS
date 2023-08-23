from control import sos_ctrl
from engine.seq.move import SeqMove
from memory.combat_manager import combat_manager_handle

combat_manager = combat_manager_handle()


# TODO: Temporary code, moves along path, pausing while combat is active
class SeqCombatManual(SeqMove):
    # Override
    def navigate_to_checkpoint(self) -> None:
        combat_manager.update()

        if combat_manager.encounter_done:
            # If there is no active fight, move along the designated path
            super().navigate_to_checkpoint()
        else:
            # Manual control, do nothing
            sos_ctrl().set_neutral()
