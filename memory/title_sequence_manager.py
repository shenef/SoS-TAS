from engine.mathlib import Vec3
from memory.core import mem_handle
from enum import Enum

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
        self.load_save_done = False # does the continue button show up
        self.title_cursor_position = TitleCursorPosition.NONE

    def update(self):
        try:
            self.memory.update()
            if self.memory.ready_for_updates():
                if self.base is None or self.fields_base is None:
                    singleton_ptr = self.memory.get_singleton_by_class_name("TitleSequenceManager")
                    self.base = self.memory.get_class_base(singleton_ptr)
                    self.fields_base = self.memory.get_class_fields_base(singleton_ptr)
                    self.title_screen = self.memory.get_field(self.fields_base, "titleScreen")


                # Update fields
                self.get_load_save_done()
                self.get_continue_selected()
                self.get_new_game_selected()
                self.get_load_game_selected()
                self.get_options_selected()
                self.get_how_to_play_selected()
                self.get_quit_selected()
            else:
                self.__init__()
        except Exception:
            return
    
    def get_title_cursor_position(self):
        return self.title_cursor_position

    def get_continue_selected(self):
        # titleScreen -> continueButton -> selected
        if self.memory.ready_for_updates():
            ptr = self.memory.follow_pointer(
                self.base, [self.title_screen, 0x78, 0x148]
            )
            value = self.memory.read_bool(ptr)
            if value:
                self.title_cursor_position = TitleCursorPosition.Continue

    def get_new_game_selected(self):
        # titleScreen -> newGameButton -> selected
        ptr = self.memory.follow_pointer(
            self.base, [self.title_screen, 0x70, 0x148]
        )
        value = self.memory.read_bool(ptr)
        if value:
            self.title_cursor_position = TitleCursorPosition.NewGame

    def get_load_game_selected(self):
        # titleScreen -> loadGameButton -> selected
        ptr = self.memory.follow_pointer(
            self.base, [self.title_screen, 0x80, 0x148]
        )
        value = self.memory.read_bool(ptr)
        if value:
            self.title_cursor_position = TitleCursorPosition.LoadGame

    def get_options_selected(self):
        # titleScreen -> optionsButton -> selected
        ptr = self.memory.follow_pointer(
            self.base, [self.title_screen, 0x88, 0x148]
        )
        value = self.memory.read_bool(ptr)
        if value:
            self.title_cursor_position = TitleCursorPosition.Options

    def get_how_to_play_selected(self):
        # titleScreen -> howToPlayButton -> selected
        ptr = self.memory.follow_pointer(
            self.base, [self.title_screen, 0x90, 0x148]
        )
        value = self.memory.read_bool(ptr)
        if value:
            self.title_cursor_position = TitleCursorPosition.HowToPlay

    def get_quit_selected(self):
        # titleScreen -> quitGameButton -> selected
        ptr = self.memory.follow_pointer(
            self.base, [self.title_screen, 0x98, 0x148]
        )
        value = self.memory.read_bool(ptr)
        if value:
            self.title_cursor_position = TitleCursorPosition.Quit
        
    def get_load_save_done(self):
        if self.memory.ready_for_updates():
            field_addr = self.memory.get_field(self.fields_base, "loadSaveDone")
            ptr = self.memory.follow_pointer(
                self.base, [field_addr]
            )
            value = self.memory.read_bool(ptr)
            self.load_save_done = value
            return
        self.load_save_done = False
