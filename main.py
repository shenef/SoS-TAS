import config
from engine.seq import SeqList, SeqLog, SequencerEngine
from GUI import Menu, MenuManager, Window
from GUI.debug_menu import DebugMenu
from log_init import initialize_logging

if __name__ == "__main__":
    # Read config data from file
    config_data = config.open_config()
    initialize_logging(config_data)

    gui = Window()

    # This is the root node of the TAS
    # TODO: This should be moved to its own file
    TAS_root = SeqList(
        name="Sea of Stars Any%",
        # func=setup_memory,
        children=[
            SeqLog(name="LOG", text="Logging something"),
        ],
    )
    # This initializes the sequencer engine that will execute the TAS
    sequencer = SequencerEngine(
        window=gui, title="Sea of Stars Any%", config=config_data, root=TAS_root
    )

    # The menu manager will capture control until the GUI window is closed
    # It allows for navigating between submenues and starting the TAS
    menu_manager = MenuManager(
        window=gui,
        root_menues=[
            # This is the main menu. Other menues can be instantiated as its children
            Menu(
                window=gui,
                title="Main Menu",
                children=[
                    sequencer,
                ],
            ),
            DebugMenu(window=gui),
        ],
    )
    menu_manager.run()

    # Cleanup
    gui.close()
