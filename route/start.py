from control import sos_ctrl
from engine.blackboard import blackboard, clear_blackboard
from engine.seq.base import SeqBase, SeqIf, SeqList
from engine.seq.log import SeqDebug, SeqLog
from engine.seq.time import SeqDelay, SeqHoldConfirm
from log_init import reset_logging_time_reference
from memory.title_sequence_manager import TitleCursorPosition, TitleSequenceManager


def start_timer():
    reset_logging_time_reference()
    blackboard().start()


title_sequence_manager = TitleSequenceManager()


class SeqIfNewGame(SeqIf):
    def __init__(
        self,
        name: str,
        when_true: SeqBase,
        when_false: SeqBase,
        default: bool = True,
        saveslot: int = 0,
    ):
        super().__init__(name, when_true, when_false, default)
        self.saveslot = saveslot

    # saveslot should be 0 for new game, or 1-9 for Load Game
    def condition(self) -> bool:
        return self.saveslot == 0


class SeqMenuConfirmButton(SeqBase):
    def __init__(self, name: str = "Confirm button"):
        super().__init__(name)

    def execute(self, delta: float) -> bool:
        sos_ctrl().confirm()
        return True


class SeqMenuStartButton(SeqBase):
    def __init__(self, name: str = "Start button"):
        super().__init__(name)

    def execute(self, delta: float) -> bool:
        sos_ctrl().start()
        return True


class SeqMenuTapLeft(SeqBase):
    def __init__(self, name: str = "Tap left"):
        super().__init__(name)

    def execute(self, delta: float) -> bool:
        sos_ctrl().dpad.tap_left()
        return True


class SeqNavigateMainMenu(SeqBase):
    def __init__(self, name: str, target_state: TitleCursorPosition):
        super().__init__(name)
        self.target_state = target_state

    def execute(self, delta: float) -> bool:
        title_sequence_manager.update()
        if title_sequence_manager._read_title_cursor_position() == self.target_state:
            # We have selected the correct item
            return True
        # Else, we haven't selected the correct item yet, tap down
        sos_ctrl().dpad.tap_down()
        return False


class SoSStartGame(SeqList):
    def __init__(self, saveslot: int):
        super().__init__(
            name="Start game",
            children=[
                SeqBase(func=clear_blackboard),
                SeqLog(
                    name="SYSTEM",
                    text="Starting Sea of Stars TAS main menu sequence...",
                ),
                # TODO: The SoS window will not recognize input unless it is in focus!
                SeqDelay("MANUAL: Focus SoS window!", timeout_in_s=5.0),
                SeqHoldConfirm("Holding A to activate controller", timeout_in_s=10.0),
                SeqDebug(name="SYSTEM", text="Press start to activate main menu."),
                SeqMenuStartButton(),
                SeqDelay(name="Menu", timeout_in_s=2.0),
                SeqIfNewGame(
                    name="Game mode",
                    saveslot=saveslot,
                    when_true=SeqNavigateMainMenu(
                        name="Select New Game", target_state=TitleCursorPosition.NewGame
                    ),
                    when_false=SeqList(
                        name="Load game",
                        children=[
                            SeqNavigateMainMenu(
                                name="Select Load Game",
                                target_state=TitleCursorPosition.LoadGame,
                            ),
                            SeqMenuConfirmButton("Load game"),
                            # TODO: Select save slot. Slot 1 selected by default
                        ],
                    ),
                ),
                # Countdown
                SeqLog(name="SYSTEM", text="Starting in..."),
                SeqLog(name="SYSTEM", text="3"),
                SeqDelay(name="Menu", timeout_in_s=1.0),
                SeqLog(name="SYSTEM", text="2"),
                SeqDelay(name="Menu", timeout_in_s=1.0),
                SeqLog(name="SYSTEM", text="1"),
                SeqDelay(name="Menu", timeout_in_s=1.0),
                SeqMenuConfirmButton("Start game"),
                SeqBase(func=start_timer),
                SeqLog(name="SYSTEM", text="Starting timer!"),
                # TODO: Move elsewhere?
                SeqIfNewGame(
                    name="Game mode",
                    saveslot=saveslot,
                    # TODO: Optimize character selection sequence
                    when_true=SeqList(
                        name="Select main character",
                        children=[
                            SeqDelay(name="Wait for select screen", timeout_in_s=10.0),
                            # TODO: Select male/female PC (left/right position is random)?
                            SeqMenuTapLeft(),
                            SeqDelay(name="Wait", timeout_in_s=1.0),
                            SeqMenuConfirmButton("Select character"),
                        ],
                    ),
                    when_false=None,
                ),
                SeqLog(name="SYSTEM", text="In game!"),
            ],
        )
