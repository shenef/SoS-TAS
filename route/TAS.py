import logging
from typing import Self

from imgui_bundle import imgui

from engine.seq import SeqList, SeqLog, SequencerEngine
from GUI import Window
from GUI.menu import Menu
from route.battle_test import BattleTest
from route.demo import DemoBrisk, DemoPlateau, DemoWizardLab, DemoWorldBriskToTower
from route.evermist_island import EvermistIsland
from route.start import SoSStartGame

logger = logging.getLogger("SYSTEM")


class TASMenu(Menu):
    def __init__(self: Self, window: Window, config_data: dict, title: str) -> None:
        super().__init__(window, title)
        self.tas_is_running = False
        self.config_data = config_data
        self.start_game_sequencer = None
        self.sequencer = None

        self.saveslot = config_data.get("saveslot", 0)
        self.checkpoint = config_data.get("checkpoint", "NONE")
        self.load_game_checkbox = self.saveslot != 0
        self.run_start_sequence = True

    def init_start_sequence(self: Self, saveslot: int) -> None:
        # This sequence navigates the main menu into the game
        self.start_game_sequencer = SequencerEngine(
            window=self.window,
            config=self.config_data,
            root=SoSStartGame(saveslot=saveslot),
        )

    # Override this in subclasses to set the TAS sequence
    def init_TAS(self: Self) -> None:
        self.sequencer = SequencerEngine(
            window=self.window,
            config=self.config_data,
            root=SeqLog(name="SYSTEM", text="ERROR, NO TAS SEQUENCE!"),
        )

    def init_saveslot(self: Self, saveslot: int) -> None:
        # Potentially advance the TAS to a particular checkpoint
        if saveslot == 0:
            logger.info("Starting TAS from the beginning")
        elif self.sequencer.advance_to_checkpoint(checkpoint=self.checkpoint):
            logger.info(f"Advanced TAS to checkpoint '{self.checkpoint}'")
        else:
            logger.error(f"Couldn't find checkpoint '{self.checkpoint}'")

    def custom_gui(self: Self) -> None:
        # Override to inject some custom parameters to the run
        pass

    def execute(self: Self, top_level: bool) -> bool:
        self.window.start_window(self.title)
        imgui.set_window_pos(self.title, imgui.ImVec2(5, 5), imgui.Cond_.once)
        imgui.set_window_size(
            self.title, imgui.ImVec2(470, 200), cond=imgui.Cond_.first_use_ever
        )

        ret = False
        if self.tas_is_running:
            # Execute the starting sequence until done (open new game or load game)
            run_main_sequence = (
                not self.run_start_sequence or self.start_game_sequencer.done
            )

            if run_main_sequence:
                # Run the TAS sequencer
                self.sequencer.run()
            else:
                self.start_game_sequencer.run()
            # End the TAS
            if imgui.button("Stop TAS"):
                self.tas_is_running = False
        else:  # Not running
            _, self.load_game_checkbox = imgui.checkbox(
                "Load from checkpoint", self.load_game_checkbox
            )

            if self.load_game_checkbox:
                # TODO(orkaboy): Maybe should check for valid range 1-9
                _, self.saveslot = imgui.input_int("Save slot 1-9", self.saveslot)
                # TODO(orkaboy): Maybe should be a dropdown of valid checkpoints
                _, self.checkpoint = imgui.input_text(
                    "Checkpoint name", self.checkpoint
                )

            _, self.run_start_sequence = imgui.checkbox(
                "Should run start sequence", self.run_start_sequence
            )

            self.custom_gui()

            if imgui.button("Start TAS"):
                saveslot = self.saveslot if self.load_game_checkbox else 0
                if self.run_start_sequence:
                    self.init_start_sequence(saveslot)
                self.init_TAS()
                self.init_saveslot(saveslot)
                self.tas_is_running = True

            if not top_level and imgui.button("Back"):
                ret = True
        self.window.end_window()
        return ret


class SoSDemoAnyPercentMenu(TASMenu):
    def __init__(self: Self, window: Window, config_data: dict) -> None:
        super().__init__(window, config_data, title="Sea of Stars Demo Any%")

    # Override
    def init_TAS(self: Self) -> None:
        # This is the root node of the TAS
        TAS_root = SeqList(
            name="Sea of Stars Demo Any%",
            children=[
                DemoPlateau(),
                DemoBrisk(),
                DemoWorldBriskToTower(),
                DemoWizardLab(),
                SeqLog(name="SYSTEM", text="SoS Demo Any% TAS done!"),
            ],
        )
        # This initializes the sequencer engine that will execute the TAS
        self.sequencer = SequencerEngine(
            window=self.window, config=self.config_data, root=TAS_root
        )

    def custom_gui(self: Self) -> None:
        # Override to inject some custom parameters to the run
        imgui.text_wrapped(
            "Warning! The Demo TAS probably won't work, due to memory layout changes compared to the full game."  # noqa E501
        )


class SoSAnyPercentMenu(TASMenu):
    def __init__(self: Self, window: Window, config_data: dict) -> None:
        super().__init__(window, config_data, title="Sea of Stars Any%")

    # Override
    def init_TAS(self: Self) -> None:
        # This is the root node of the TAS
        TAS_root = SeqList(
            name="Sea of Stars Any%",
            children=[
                EvermistIsland(),
                SeqLog(name="SYSTEM", text="SoS Any% TAS done!"),
            ],
        )
        # This initializes the sequencer engine that will execute the TAS
        self.sequencer = SequencerEngine(
            window=self.window, config=self.config_data, root=TAS_root
        )


class SoSBattleTestMenu(TASMenu):
    def __init__(self: Self, window: Window, config_data: dict) -> None:
        super().__init__(window, config_data, title="Battle Test")

    # Override
    def init_TAS(self: Self) -> None:
        # This is the root node of the TAS
        TAS_root = SeqList(
            name="BattleTest",
            children=[
                BattleTest(),
                SeqLog(name="SYSTEM", text="BattleTest Done!"),
            ],
        )
        # This initializes the sequencer engine that will execute the TAS
        self.sequencer = SequencerEngine(
            window=self.window, config=self.config_data, root=TAS_root
        )

    def custom_gui(self: Self) -> None:
        # Override to inject some custom parameters to the run
        imgui.text_wrapped(
            "Warning! This mode is only intended for testing the Utility AI comabt system."  # noqa E501
        )
