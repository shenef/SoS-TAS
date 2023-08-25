import logging

from engine.seq import SeqList, SeqLog, SequencerEngine
from GUI import Window
from GUI.menu import Menu
from route.demo import DemoBrisk, DemoPlateau, DemoWizardLab, DemoWorldBriskToTower
from route.start import SoSStartGame

logger = logging.getLogger("SYSTEM")


class PerformTAS(Menu):
    # TODO: There's an issue initializing everything like this,
    # TODO: at least if the PerformTAS object is instantiated on start in the main menu.
    def __init__(self, window: Window, config_data: dict) -> None:
        super().__init__(window, title="Sea of Stars Any%")

        # TODO: Maybe load these from GUI?
        saveslot = config_data.get("saveslot", 0)
        checkpoint = config_data.get("checkpoint", "NONE")

        # This sequence navigates the main menu into the game
        self.start_game_sequencer = SequencerEngine(
            window=window,
            config=config_data,
            root=SoSStartGame(saveslot=saveslot),
        )

        # This is the root node of the TAS
        TAS_root = SeqList(
            name="Sea of Stars Any%",
            # func=setup_memory,
            children=[
                DemoPlateau(),
                DemoBrisk(),
                DemoWorldBriskToTower(),
                DemoWizardLab(),
                SeqLog(name="SYSTEM", text="SoS TAS done!"),
            ],
        )
        # This initializes the sequencer engine that will execute the TAS
        self.sequencer = SequencerEngine(
            window=window, config=config_data, root=TAS_root
        )
        # Potentially advance the TAS to a particular checkpoint
        # TODO: This should probably be moved to when the TAS is activated
        # TODO: Potentially, checkpoint and new game/load game could be fetched from the GUI
        if saveslot == 0:
            logger.info("Starting TAS from the beginning")
        elif self.sequencer.advance_to_checkpoint(checkpoint=checkpoint):
            logger.info(f"Advanced TAS to checkpoint '{checkpoint}'")
        else:
            logger.error(f"Couldn't find checkpoint '{checkpoint}'")

    def run(self) -> bool:
        if not self.start_game_sequencer.done:
            return self.start_game_sequencer.run()
        return self.sequencer.run()
