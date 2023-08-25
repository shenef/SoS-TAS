from enum import Enum

from memory.core import mem_handle


class TitleCursorPosition(Enum):
    NONE = 0
    Continue = 1
    NewGame = 2
    LoadGame = 3
    Options = 4
    HowToPlay = 5
    Quit = 6


class TitleSequenceManager:
    def __init__(self):
        self.memory = mem_handle()
        self.base = None
        self.fields_base = None
        self.title_screen = None
        # True if there was a save to load and the continue button shows up
        self.load_save_done = False
        # True if you pressed start on the "press start" screen before the title menu shows up
        self.pressed_start = False
        self.title_cursor_position = TitleCursorPosition.NONE
        self.title_position_set = False

    def update(self):
        if self.memory.ready_for_updates():
            if self.base is None or self.fields_base is None:
                singleton_ptr = self.memory.get_singleton_by_class_name(
                    "TitleSequenceManager"
                )

                self.base = self.memory.get_class_base(singleton_ptr)

                if self.base == 0x0:
                    return

                self.fields_base = self.memory.get_class_fields_base(singleton_ptr)
            else:
                self.title_screen = self.memory.get_field(
                    self.fields_base, "titleScreen"
                )

                # Update fields
                self.title_position_set = False
                self._read_load_save_done()
                self._read_pressed_start()
                self._read_continue_selected()
                self._read_new_game_selected()
                self._read_load_game_selected()
                self._read_options_selected()
                self._read_how_to_play_selected()
                self._read_quit_selected()

            if not self.title_position_set:
                self.title_cursor_position = TitleCursorPosition.NONE

    def _read_title_cursor_position(self):
        return self.title_cursor_position

    def _read_continue_selected(self):
        # titleScreen -> continueButton -> selected
        ptr = self.memory.follow_pointer(self.base, [self.title_screen, 0x78, 0x148])
        value = self.memory.read_bool(ptr)
        if value:
            self.title_cursor_position = TitleCursorPosition.Continue
            self.title_position_set = True

    def _read_new_game_selected(self):
        # titleScreen -> newGameButton -> selected
        ptr = self.memory.follow_pointer(self.base, [self.title_screen, 0x70, 0x148])
        value = self.memory.read_bool(ptr)
        if value:
            self.title_cursor_position = TitleCursorPosition.NewGame
            self.title_position_set = True

    def _read_load_game_selected(self):
        # titleScreen -> loadGameButton -> selected
        ptr = self.memory.follow_pointer(self.base, [self.title_screen, 0x80, 0x148])
        value = self.memory.read_bool(ptr)
        if value:
            self.title_cursor_position = TitleCursorPosition.LoadGame
            self.title_position_set = True

    def _read_options_selected(self):
        # titleScreen -> optionsButton -> selected
        ptr = self.memory.follow_pointer(self.base, [self.title_screen, 0x88, 0x148])
        value = self.memory.read_bool(ptr)
        if value:
            self.title_cursor_position = TitleCursorPosition.Options
            self.title_position_set = True

    def _read_how_to_play_selected(self):
        # titleScreen -> howToPlayButton -> selected
        ptr = self.memory.follow_pointer(self.base, [self.title_screen, 0x90, 0x148])
        value = self.memory.read_bool(ptr)
        if value:
            self.title_cursor_position = TitleCursorPosition.HowToPlay
            self.title_position_set = True

    def _read_quit_selected(self):
        # titleScreen -> quitGameButton -> selected
        ptr = self.memory.follow_pointer(self.base, [self.title_screen, 0x98, 0x148])
        value = self.memory.read_bool(ptr)
        if value:
            self.title_cursor_position = TitleCursorPosition.Quit
            self.title_position_set = True

    # True if there was a save to load and the continue button shows up
    def _read_load_save_done(self):
        if self.memory.ready_for_updates():
            ptr = self.memory.follow_pointer(self.base, [0xA8])
            value = self.memory.read_bool(ptr)
            self.load_save_done = value
            return
        self.load_save_done = False

    # True if you pressed start on the "press start" screen before the title menu shows up
    def _read_pressed_start(self):
        if self.memory.ready_for_updates():
            ptr = self.memory.follow_pointer(self.base, [self.title_screen, 0xB0])
            value = self.memory.read_bool(ptr)
            self.pressed_start = value
            return
        self.pressed_start = False


_title_sequence_manager = TitleSequenceManager()
_title_sequence_manager.update()


def title_sequence_manager_handle() -> TitleSequenceManager:
    return _title_sequence_manager
