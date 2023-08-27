import config
from GUI import Menu, MenuManager, Window
from GUI.battle_menu import BattleMenu
from GUI.debug_menu import DebugMenu
from GUI.tools.nav_helper import NavHelper
from log_init import initialize_logging
from route.TAS import SoSDemoAnyPercentMenu

if __name__ == "__main__":
    # Read config data from file
    config_data = config.open_config()
    initialize_logging(config_data)
    config_logging = config_data.get("logging", {})
    config_ui = config_data.get("ui", {})

    gui = Window(config_ui)

    # The menu manager will capture control until the GUI window is closed
    # It allows for navigating between submenus and starting the TAS
    menu_manager = MenuManager(
        window=gui,
        root_menus=[
            # This is the main menu. Other menus can be instantiated as its children
            Menu(
                window=gui,
                title="Main Menu",
                children=[
                    SoSDemoAnyPercentMenu(window=gui, config_data=config_data),
                ],
            ),
            DebugMenu(window=gui),
            NavHelper(window=gui),
            BattleMenu(window=gui),
        ],
    )
    menu_manager.run()

    # Cleanup
    gui.close()
