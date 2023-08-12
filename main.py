import config
from engine.seq import SeqList, SeqLog, SequencerEngine
from GUI import Window
from log_init import initialize_logging

if __name__ == "__main__":
    # Read config data from file
    config_data = config.open_config()
    initialize_logging(config_data)

    gui = Window()

    root = SeqList(
        name="Sea of Stars Any%",
        # func=setup_memory,
        children=[
            SeqLog(name="LOG", text="Logging something"),
        ],
    )

    # TODO: Pick category
    sequencer = SequencerEngine(window=gui, config=config_data, root=root)
    sequencer.run_engine()

    # Cleanup
    gui.close()
