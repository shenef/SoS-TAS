from enum import Enum, auto
from typing import Self

from memory import PlayerPartyCharacter, mem_handle


class TitleCursorPosition(Enum):
    NONE = auto()
    Store = auto()
    NewGame = auto()
    NewGamePlus = auto()
    Continue = auto()
    LoadGame = auto()
    Options = auto()
    Quit = auto()


class CharacterSelectButton:
    def __init__(self: Self, character: PlayerPartyCharacter, selected: bool) -> None:
        self.character = character
        self.selected = selected


class TitleSequenceManager:
    def __init__(self: Self) -> None:
        """Initialize a new TitleSequenceManager object."""
        self.memory = mem_handle()
        self.base = None
        self.fields_base = None
        self.title_screen = None
        self.character_selection_screen = None
        # True if there was a save to load and the continue button shows up
        self.load_save_done = False
        # True if you pressed start on the "press start" screen before the title menu shows up
        self.pressed_start = False
        self.title_cursor_position = TitleCursorPosition.NONE
        self.title_position_set = False
        self.character_select_left_button = CharacterSelectButton(PlayerPartyCharacter.NONE, False)
        self.character_select_right_button = CharacterSelectButton(PlayerPartyCharacter.NONE, False)

    def update(self: Self) -> None:
        try:
            if self.memory.ready_for_updates:
                if self.base is None or self.fields_base is None:
                    singleton_ptr = self.memory.get_singleton_by_class_name("TitleSequenceManager")

                    if singleton_ptr is None:
                        return

                    self.base = self.memory.get_class_base(singleton_ptr)
                    if self.base == 0x0:
                        return

                    self.fields_base = self.memory.get_class_fields_base(singleton_ptr)
                    self.title_screen = self.memory.get_field(self.fields_base, "titleScreen")
                    self.character_selection_screen = self.memory.get_field(
                        self.fields_base, "characterSelectionScreen"
                    )
                else:
                    # Update fields
                    self.title_position_set = False
                    self._read_load_save_done()
                    self._read_new_game_characters()
                    self._read_pressed_start()
                    self._read_continue_selected()
                    self._read_new_game_selected()
                    self._read_new_game_plus_selected()
                    self._read_load_game_selected()
                    self._read_options_selected()
                    self._read_quit_selected()

                if not self.title_position_set:
                    self.title_cursor_position = TitleCursorPosition.NONE

        except Exception as _e:
            # logger.debug(f"Title Sequence Manager Reloading {type(_e)}")
            self.__init__()

    def _read_new_game_characters(self: Self) -> None:
        try:
            # characterSelectionScreen -> leftButton -> characterDefinitionId
            left_button_character_definition_id_ptr = self.memory.follow_fields(
                self, ["characterSelectionScreen", "leftButton", "characterDefinitionId"]
            )
            left_character_value = self.memory.read_string(
                self.memory.resolve_pointer(left_button_character_definition_id_ptr) + 0x14, 8
            )
            left_character = PlayerPartyCharacter.parse_definition_id(left_character_value)

            # characterSelectionScreen -> rightButton -> characterDefinitionId
            right_button_character_definition_id_ptr = self.memory.follow_fields(
                self, ["characterSelectionScreen", "rightButton", "characterDefinitionId"]
            )
            right_character_value = self.memory.read_string(
                self.memory.resolve_pointer(right_button_character_definition_id_ptr) + 0x14, 8
            )
            right_character = PlayerPartyCharacter.parse_definition_id(right_character_value)
        except Exception:
            right_character = None
            left_character = None

        try:
            selected_character_pointer = self.memory.follow_fields(
                self, ["characterSelectionScreen", "selectedCharacter", "selected"]
            )
            selected_character_value = self.memory.read_bool(selected_character_pointer)
            selected_character = None
            match selected_character_value:
                case False:
                    selected_character = right_character
                case True:
                    selected_character = left_character
                case _:
                    selected_character = None
        except Exception:
            selected_character = PlayerPartyCharacter.NONE
        try:
            # Corrects the weird scenario where both sides can be true when you're in the middle
            # of two results. It makes the value more reasonable to consume.
            right_selected = right_character == selected_character
            left_selected = left_character == selected_character
            self.character_select_right_button = CharacterSelectButton(
                right_character, right_selected
            )

            self.character_select_left_button = CharacterSelectButton(left_character, left_selected)

        except Exception:
            self.character_select_left_button = CharacterSelectButton(
                PlayerPartyCharacter.NONE, False
            )
            self.character_select_right_button = CharacterSelectButton(
                PlayerPartyCharacter.NONE, False
            )

    def _read_store_selected(self: Self) -> None:
        # titleScreen -> storeButton -> selected
        ptr = self.memory.follow_fields(self, ["titleScreen", "storeButton", "selected"])
        value = self.memory.read_bool(ptr)
        if value:
            self.title_cursor_position = TitleCursorPosition.Store
            self.title_position_set = True

    def _read_new_game_selected(self: Self) -> None:
        # titleScreen -> newGameButton -> selected
        ptr = self.memory.follow_fields(self, ["titleScreen", "newGameButton", "selected"])
        value = self.memory.read_bool(ptr)
        if value:
            self.title_cursor_position = TitleCursorPosition.NewGame
            self.title_position_set = True

    def _read_new_game_plus_selected(self: Self) -> None:
        # titleScreen -> newGameButton -> selected
        ptr = self.memory.follow_fields(self, ["titleScreen", "newGamePlusButton", "selected"])
        value = self.memory.read_bool(ptr)
        if value:
            self.title_cursor_position = TitleCursorPosition.NewGamePlus
            self.title_position_set = True

    def _read_continue_selected(self: Self) -> None:
        # titleScreen -> continueButton -> selected
        ptr = self.memory.follow_fields(self, ["titleScreen", "continueButton", "selected"])
        value = self.memory.read_bool(ptr)
        if value:
            self.title_cursor_position = TitleCursorPosition.Continue
            self.title_position_set = True

    def _read_load_game_selected(self: Self) -> None:
        # titleScreen -> loadGameButton -> selected
        ptr = self.memory.follow_fields(self, ["titleScreen", "loadGameButton", "selected"])
        value = self.memory.read_bool(ptr)
        if value:
            self.title_cursor_position = TitleCursorPosition.LoadGame
            self.title_position_set = True

    def _read_options_selected(self: Self) -> None:
        # titleScreen -> optionsButton -> selected
        ptr = self.memory.follow_fields(self, ["titleScreen", "optionsButton", "selected"])
        value = self.memory.read_bool(ptr)
        if value:
            self.title_cursor_position = TitleCursorPosition.Options
            self.title_position_set = True

    def _read_quit_selected(self: Self) -> None:
        # titleScreen -> quitGameButton -> selected
        ptr = self.memory.follow_fields(self, ["titleScreen", "quitGameButton", "selected"])
        value = self.memory.read_bool(ptr)
        if value:
            self.title_cursor_position = TitleCursorPosition.Quit
            self.title_position_set = True

    # True if there was a save to load and the continue button shows up
    def _read_load_save_done(self: Self) -> None:
        if self.memory.ready_for_updates:
            ptr = self.memory.follow_fields(self, ["loadSaveDone"])
            value = self.memory.read_bool(ptr)
            self.load_save_done = value
            return
        self.load_save_done = False

    # True if you pressed start on the "press start" screen before the title menu shows up
    def _read_pressed_start(self: Self) -> None:
        if self.memory.ready_for_updates:
            ptr = self.memory.follow_fields(self, ["titleScreen", "startPressed"])
            value = self.memory.read_bool(ptr)
            self.pressed_start = value
            return
        self.pressed_start = False


_title_sequence_manager = TitleSequenceManager()


def title_sequence_manager_handle() -> TitleSequenceManager:
    return _title_sequence_manager
