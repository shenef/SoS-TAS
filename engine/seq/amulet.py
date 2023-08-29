import time

from control import sos_ctrl
from engine.seq.base import SeqBase
from memory.combat_manager import combat_manager_handle

combat_manager = combat_manager_handle()


# TODO: Temporary code, moves along path, pausing while combat is active
class SeqAmulet(SeqBase):
    def __init__(
        self,
        name: str,
    ):
        super().__init__(name)
        self.timer = 0.0
        self.complete = False
        self.steps = ["open_menu", "up_twice", "confirm", "confirm", "cancel", "exit"]
        self.delay = 0.05

    # Override
    def execute(self, delta: float) -> bool:
        step = self.steps.pop(0)
        print(step)

        match step:
            case "open_menu":
                sos_ctrl().menu()
                time.sleep(0.25)
                return False
            case "up_twice":
                sos_ctrl().dpad.tap_up()
                sos_ctrl().dpad.tap_up()
                return False
            case "confirm":
                sos_ctrl().confirm()
                return False
            case "cancel":
                sos_ctrl().cancel()
                return False
            case "exit":
                sos_ctrl().cancel()
                return True
            case _:
                return False

    def __repr__(self) -> str:
        return f"Amulet sequence ({self.name})..."
