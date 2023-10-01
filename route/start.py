"""Contains the sequencer node code for navigating the main menu to start the game."""

import math
from typing import Self

from control import sos_ctrl
from engine.blackboard import blackboard, clear_blackboard
from engine.seq import (
    SeqBase,
    SeqDebug,
    SeqDelay,
    SeqIf,
    SeqInteract,
    SeqList,
    SeqLog,
)
from log_init import reset_logging_time_reference
from memory import (
    TitleCursorPosition,
    title_sequence_manager_handle,
)


def start_timer() -> None:
    """Restart the TAS timer."""
    reset_logging_time_reference()
    blackboard().start()


title_sequence_manager = title_sequence_manager_handle()


class SeqIfNewGame(SeqIf):
    def __init__(
        self: Self,
        name: str,
        when_true: SeqBase,
        when_false: SeqBase,
        default: bool = True,
        saveslot: int = 0,
    ) -> None:
        super().__init__(name, when_true, when_false, default)
        self.saveslot = saveslot

    # saveslot should be 0 for new game, or 1-9 for Load Game
    def condition(self: Self) -> bool:
        return self.saveslot == 0


class SeqMenuStartButton(SeqBase):
    def __init__(self: Self, name: str = "Start button") -> None:
        super().__init__(name)

    def execute(self: Self, delta: float) -> bool:
        sos_ctrl().start()
        return True


class SeqMenuTapLeft(SeqBase):
    def __init__(self: Self, name: str = "Tap left") -> None:
        super().__init__(name)

    def execute(self: Self, delta: float) -> bool:
        sos_ctrl().dpad.tap_left()
        return True


class SeqNavigateMainMenu(SeqBase):
    def __init__(self: Self, name: str, target_state: TitleCursorPosition) -> None:
        super().__init__(name)
        self.target_state = target_state

    def execute(self: Self, delta: float) -> bool:
        if title_sequence_manager.title_cursor_position == self.target_state:
            # We have selected the correct item
            return True
        # Else, we haven't selected the correct item yet, tap down
        sos_ctrl().dpad.tap_down()
        return False


class SeqNewGameFromMenu(SeqList):
    def __init__(self: Self) -> None:
        super().__init__(
            name="Select main character",
            children=[
                SeqDelay(name="Wait for select screen", timeout_in_s=10.0),
                # TODO(orkaboy): Deliberately select Valere/Zale
                # Countdown
                SeqLog(name="SYSTEM", text="Starting in..."),
                SeqLog(name="SYSTEM", text="3"),
                SeqDelay(name="Menu", timeout_in_s=1.0),
                SeqLog(name="SYSTEM", text="2"),
                SeqDelay(name="Menu", timeout_in_s=1.0),
                SeqLog(name="SYSTEM", text="1"),
                SeqDelay(name="Menu", timeout_in_s=1.0),
                SeqMenuTapLeft(),
                SeqBase(func=start_timer),
                SeqLog(name="SYSTEM", text="Starting timer!"),
                SeqInteract("Select character"),
            ],
        )


class SeqSelectSaveSlot(SeqBase):
    def __init__(self: Self, name: str, saveslot: int) -> None:
        self.saveslot = saveslot  # should be 1-9
        super().__init__(name)

    # Navigate to the saveslot in question by tapping down x times
    def execute(self: Self, delta: float) -> bool:
        page = math.trunc((self.saveslot - 1) / 3)  # 0-2 (save page)
        vertical = (self.saveslot - 1) % 3  # 0-2 (save slot in page)
        for _ in range(0, page):
            sos_ctrl().shift_right(tapping=True)
        for _ in range(0, vertical):
            sos_ctrl().dpad.tap_down()
        return True


class SoSStartGame(SeqList):
    def __init__(self: Self, saveslot: int) -> None:
        super().__init__(
            name="Start game",
            children=[
                SeqBase(func=clear_blackboard),
                SeqLog(
                    name="SYSTEM",
                    text="Starting Sea of Stars TAS main menu sequence.",
                ),
                # ! The SoS window will not recognize input unless it is in focus!
                SeqDelay(name="MANUAL: Focus SoS window!", timeout_in_s=2.5),
                SeqDebug(name="SYSTEM", text="Press start to activate main menu."),
                SeqMenuStartButton(),
                SeqDelay(name="Menu", timeout_in_s=1.5),
                SeqIfNewGame(
                    name="Game mode",
                    saveslot=saveslot,
                    when_true=SeqList(
                        name="NEW GAME",
                        children=[
                            SeqNavigateMainMenu(
                                name="Select New Game",
                                target_state=TitleCursorPosition.NewGame,
                            ),
                            SeqInteract(),
                            SeqNewGameFromMenu(),
                        ],
                    ),
                    when_false=SeqList(
                        name=f"LOAD GAME: {saveslot}",
                        children=[
                            SeqNavigateMainMenu(
                                name="Select Load Game",
                                target_state=TitleCursorPosition.LoadGame,
                            ),
                            SeqInteract("Load game"),
                            SeqDelay(name="Load menu", timeout_in_s=1.0),
                            SeqSelectSaveSlot(
                                name="Select save slot", saveslot=saveslot
                            ),
                            SeqInteract("Load slot"),
                            # TODO(orkaboy): Need to select manual save slot if relevant
                            SeqDelay(name="Load menu", timeout_in_s=1.0),
                            SeqBase(func=start_timer),
                            SeqLog(name="SYSTEM", text="Starting timer!"),
                            SeqInteract("Confirm load"),
                        ],
                    ),
                ),
                SeqLog(name="SYSTEM", text="In game!"),
            ],
        )
