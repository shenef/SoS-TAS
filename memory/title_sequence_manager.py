from enum import Enum, auto

from memory.core import mem_handle


class TitleCursorPosition(Enum):
    NONE = auto()
    Continue = auto()
    NewGame = auto()
    NewGamePlus = auto()
    LoadGame = auto()
    Options = auto()
    Quit = auto()


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
        try:
            if self.memory.ready_for_updates:
                if self.base is None or self.fields_base is None:
                    singleton_ptr = self.memory.get_singleton_by_class_name(
                        "TitleSequenceManager"
                    )

                    if singleton_ptr is None:
                        return

                    self.base = self.memory.get_class_base(singleton_ptr)

                    if self.base == 0x0:
                        return

                    self.fields_base = self.memory.get_class_fields_base(singleton_ptr)
                    self.title_screen = self.memory.get_field(
                        self.fields_base, "titleScreen"
                    )
                else:
                    # Update fields
                    self.title_position_set = False
                    self._read_load_save_done()
                    self._read_pressed_start()
                    self._read_continue_selected()
                    self._read_new_game_selected()
                    self._read_new_game_plus_selected()
                    self._read_load_game_selected()
                    self._read_options_selected()
                    self._read_quit_selected()

                if not self.title_position_set:
                    self.title_cursor_position = TitleCursorPosition.NONE
        except Exception:
            # logger.debug(f"Title Sequence Manager Reloading {type(_e)}")
            self.__init__()

    def _read_continue_selected(self):
        # titleScreen -> continueButton -> selected
        ptr = self.memory.follow_pointer(self.base, [self.title_screen, 0xA8, 0x148])
        value = self.memory.read_bool(ptr)
        if value:
            self.title_cursor_position = TitleCursorPosition.Continue
            self.title_position_set = True

    def _read_new_game_selected(self):
        # titleScreen -> newGameButton -> selected
        ptr = self.memory.follow_pointer(self.base, [self.title_screen, 0x98, 0x148])
        value = self.memory.read_bool(ptr)
        if value:
            self.title_cursor_position = TitleCursorPosition.NewGame
            self.title_position_set = True

    def _read_new_game_plus_selected(self):
        # titleScreen -> newGameButton -> selected
        ptr = self.memory.follow_pointer(self.base, [self.title_screen, 0xA0, 0x148])
        value = self.memory.read_bool(ptr)
        if value:
            self.title_cursor_position = TitleCursorPosition.NewGamePlus
            self.title_position_set = True

    def _read_load_game_selected(self):
        # titleScreen -> loadGameButton -> selected
        ptr = self.memory.follow_pointer(self.base, [self.title_screen, 0xB0, 0x148])
        value = self.memory.read_bool(ptr)
        if value:
            self.title_cursor_position = TitleCursorPosition.LoadGame
            self.title_position_set = True

    def _read_options_selected(self):
        # titleScreen -> optionsButton -> selected
        ptr = self.memory.follow_pointer(self.base, [self.title_screen, 0xB8, 0x148])
        value = self.memory.read_bool(ptr)
        if value:
            self.title_cursor_position = TitleCursorPosition.Options
            self.title_position_set = True

    def _read_quit_selected(self):
        # titleScreen -> quitGameButton -> selected
        ptr = self.memory.follow_pointer(self.base, [self.title_screen, 0xC0, 0x148])
        value = self.memory.read_bool(ptr)
        if value:
            self.title_cursor_position = TitleCursorPosition.Quit
            self.title_position_set = True

    # True if there was a save to load and the continue button shows up
    def _read_load_save_done(self):
        if self.memory.ready_for_updates:
            ptr = self.memory.follow_pointer(self.base, [0x88])
            value = self.memory.read_bool(ptr)
            self.load_save_done = value
            return
        self.load_save_done = False

    # True if you pressed start on the "press start" screen before the title menu shows up
    def _read_pressed_start(self):
        if self.memory.ready_for_updates:
            ptr = self.memory.follow_pointer(self.base, [self.title_screen, 0xE0])
            value = self.memory.read_bool(ptr)
            self.pressed_start = value
            return
        self.pressed_start = False


_title_sequence_manager = TitleSequenceManager()


def title_sequence_manager_handle() -> TitleSequenceManager:
    return _title_sequence_manager
