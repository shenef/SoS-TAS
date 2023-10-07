"""
TAS Module.

Contains general code for a TAS sub-menu in imgui, and the
root nodes for the routes. These classes are instantiated in main.py.
"""

import logging
from typing import Self

import yaml

try:
    from yaml import CDumper as Dumper
except ImportError:
    from yaml import Dumper


from imgui_bundle import imgui

from config import get_route_config, open_route_config, set_route_config
from engine.seq import SeqList, SeqLog, SequencerEngine
from GUI import LayoutHelper, Menu, Window
from route.battle_test import BattleTest

# Old routing, TODO(orkaboy): Remove
from route.demo import DemoBrisk, DemoWizardLab, DemoWorldBriskToTower

# Routing
from route.evermist_island import EvermistIsland
from route.sleeper_island import SleeperIsland
from route.start import SoSStartGame

logger = logging.getLogger("SYSTEM")


class RouteOption:
    """GUI component for a route option."""

    def __init__(self: Self, name: str, description: str, default: bool = False) -> None:
        self.name = name
        self.description = description
        self.default = default


class TASMenu(Menu):
    """
    Generic class for handling a TAS route.

    This class contains common methods used by all routes such as the start
    sequence and loading from a save.

    Individual routes should inherit from the TASMenu class.
    """

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
        """Initialize the sequence that navigates the main menu into the game."""
        self.start_game_sequencer = SequencerEngine(
            window=self.window,
            config=self.config_data,
            root=SoSStartGame(saveslot=saveslot),
        )

    def init_TAS(self: Self) -> None:
        """Override this in subclasses to set the TAS sequence."""
        self.sequencer = SequencerEngine(
            window=self.window,
            config=self.config_data,
            root=SeqLog(name="SYSTEM", text="ERROR, NO TAS SEQUENCE!"),
        )

    def init_saveslot(self: Self) -> None:
        """Potentially advance the TAS to a particular checkpoint."""
        if not self.load_game_checkbox:
            logger.info("Starting TAS from the beginning")
        elif self.sequencer.advance_to_checkpoint(checkpoint=self.checkpoint):
            logger.info(f"Advanced TAS to checkpoint '{self.checkpoint}'")
        else:
            logger.error(f"Couldn't find checkpoint '{self.checkpoint}'")

    def custom_gui(self: Self) -> None:
        """Override to inject some custom ui to the window."""

    def execute(self: Self, top_level: bool) -> bool:
        """Run the TAS gui loop. Sets up the buttons required to navigate the TAS."""
        self.window.start_window(self.title)
        imgui.set_window_pos(self.title, imgui.ImVec2(5, 5), imgui.Cond_.once)
        imgui.set_window_size(self.title, imgui.ImVec2(470, 200), cond=imgui.Cond_.first_use_ever)

        ret = False
        if self.tas_is_running:
            # Execute the starting sequence until done (open new game or load game)
            run_main_sequence = not self.run_start_sequence or self.start_game_sequencer.done

            if run_main_sequence:
                # Run the TAS sequencer (this is the code that actually plays the game)
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
                # TODO(orkaboy): Maybe should be a dropdown of valid checkpoints
                _, self.checkpoint = imgui.input_text("Checkpoint name", self.checkpoint)
                LayoutHelper.add_tooltip(
                    "intro_mooncradle (First cavern in flashback)\n"
                    + "intro_dorms          (First entering dorms of Zenith Academy)\n"
                    + "intro_dorms2         (Dorms of Zenith Academy, just before final trial)\n"
                    + "forbidden_cave       (Forbidden Cave entrance)\n"
                    + "forbidden_cave2      (Forbidden Cave campfire)\n"
                    + "mountain_trail       (Mountain Trail, just north of campfire)\n"
                    + "mountain_trail2      (Mountain Trail, campfire in cave)\n"
                    + "elder_mist           (Elder Mist trials, campfire after tutorial)\n"
                    + "elder_mist_boss      (Elder Mist trials, just before the boss)\n"
                    + "elder_mist_boss2     (Elder Mist trials, just after the boss)\n"
                    + "moorlands            (When just entering Moorlands)\n"
                    + "moorlands2           (By the campfire at the Runestone)\n"
                    + "wind_tunnel_mines    (First floor, by the elevator)\n"
                    + "wind_tunnel_mines2   (After defeating first Bushtroo)"
                )

            _, self.run_start_sequence = imgui.checkbox(
                "Should run start sequence", self.run_start_sequence
            )
            if self.run_start_sequence and self.load_game_checkbox:
                # TODO(orkaboy): Maybe should check for valid range 1-9
                _, self.saveslot = imgui.input_int("Save slot 1-9", self.saveslot)
                LayoutHelper.add_tooltip(
                    "Save slot 1-9 is valid, mapping to the in-game slot\n"
                    + "that holds the checkpoint save."
                )

            self.custom_gui()

            if imgui.button("Start TAS"):
                # Only set saveslot if loading from main menu
                saveslot = (
                    self.saveslot if (self.load_game_checkbox and self.run_start_sequence) else 0
                )

                if self.run_start_sequence:
                    self.init_start_sequence(saveslot)
                self.init_TAS()
                self.init_saveslot()
                self.tas_is_running = True

            imgui.same_line()

            if not top_level and imgui.button("Back"):
                ret = True
        self.window.end_window()
        return ret


class SoSDemoAnyPercentMenu(TASMenu):
    """Old and unused code for the demo. Not functional."""

    def __init__(self: Self, window: Window, config_data: dict) -> None:
        super().__init__(window, config_data, title="Sea of Stars Demo Any%")

    # Override
    def init_TAS(self: Self) -> None:
        # This is the root node of the TAS
        TAS_root = SeqList(
            name="Sea of Stars Demo Any%",
            children=[
                # DemoPlateau(),
                DemoBrisk(),
                DemoWorldBriskToTower(),
                DemoWizardLab(),
                SeqLog(name="SYSTEM", text="SoS Demo Any% TAS done!"),
            ],
        )
        # This initializes the sequencer engine that will execute the TAS
        self.sequencer = SequencerEngine(window=self.window, config=self.config_data, root=TAS_root)

    def custom_gui(self: Self) -> None:
        imgui.text_wrapped(
            "Warning! The Demo TAS probably won't work, due to memory layout changes compared to the full game."  # noqa E501
        )


class SoSAnyPercentMenu(TASMenu):
    """Main Any% route."""

    # We can add route configuration parameters here (apply branches with `SeqRouteBranch` node)
    ROUTE_CONFIG_PARAMS: list[RouteOption] = [
        RouteOption(name="amulet", description="Use the Amulet of Storytelling", default=True),
        RouteOption(name="fc_leeching_thorn", description="Grab Leeching Thorn", default=False),
        RouteOption(name="fc_bosslug_loot", description="Loot Bosslug cave", default=True),
        RouteOption(name="xl_solstice_ring", description="X'tol Solstice Ring", default=True),
        RouteOption(name="ml_power_belt", description="Moorland Power Belt", default=True),
        RouteOption(name="ml_teal_amber_ore", description="Moorland Teal Amber Ore", default=True),
        RouteOption(name="ml_solar_rain", description="Moorland Solar Rain scroll", default=True),
        RouteOption(
            name="wtm_green_leaf", description="Wind Tunnel Mines Green Leaf", default=True
        ),
    ]

    def __init__(self: Self, window: Window, config_data: dict) -> None:
        super().__init__(window, config_data, title="Sea of Stars Any%")
        # Initialize all route options to their default values from `ROUTE_CONFIG_PARAMS`
        self.route_config = {param.name: param.default for param in self.ROUTE_CONFIG_PARAMS}
        self.route_config_path = config_data.get("route_config", "route_config.yaml")
        self._load_route_config()

    def _load_route_config(self: Self) -> None:
        """Try to load route config from file."""
        if open_route_config(self.route_config_path):
            route_config = get_route_config()
            # Apply any relevant values to the local cache
            for name, value in self.route_config.items():
                self.route_config[name] = route_config.get(name, value)

    def _save_route_config(self: Self) -> None:
        """Save route config to file."""
        with open(self.route_config_path, mode="w") as file:
            yaml.dump(self.route_config, file, Dumper=Dumper)

    # Override
    def init_TAS(self: Self) -> None:
        # Apply local route config cache to global store
        set_route_config(self.route_config)
        logger.info("Route configuration:")
        for name, value in self.route_config.items():
            logger.info(f"  {name}: {value}")
        # This is the root node of the TAS
        TAS_root = SeqList(
            name="Sea of Stars Any%",
            children=[
                EvermistIsland(),
                SleeperIsland(),
                SeqLog(name="SYSTEM", text="SoS Any% TAS done!"),
            ],
        )
        # This initializes the sequencer engine that will execute the TAS
        self.sequencer = SequencerEngine(window=self.window, config=self.config_data, root=TAS_root)

    def custom_gui(self: Self) -> None:
        imgui.spacing()
        route_config_tab, visible = imgui.collapsing_header("Route config", True, flags=32)
        if route_config_tab and visible:
            # Load/Save route config from file UI
            if imgui.button("Load config"):
                self._load_route_config()
            imgui.same_line()
            if imgui.button("Save config"):
                self._save_route_config()
            _, self.route_config_path = imgui.input_text(
                "Route config path", self.route_config_path
            )
            # TODO(orkaboy): Should be split into multiple columns
            for param in self.ROUTE_CONFIG_PARAMS:
                _, self.route_config[param.name] = imgui.checkbox(
                    param.description, self.route_config.get(param.name, param.default)
                )
            LayoutHelper.add_spacer()


class SoSBattleTestMenu(TASMenu):
    """Used for testing purposes."""

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
        self.sequencer = SequencerEngine(window=self.window, config=self.config_data, root=TAS_root)

    def custom_gui(self: Self) -> None:
        imgui.text_wrapped(
            "Warning! This mode is only intended for testing the Utility AI comabt system."
        )
