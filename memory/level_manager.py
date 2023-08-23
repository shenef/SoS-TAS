from memory.core import mem_handle


class LevelManager:
    def __init__(self):
        self.memory = mem_handle()
        self.base = None
        self.fields_base = None
        self.current_level_base = None
        self.level_loader_base = None
        self.scene_name = None
        self.current_level = None

    def update(self):
        try:
            self.memory.update()
            if self.memory.ready_for_updates():
                singleton_ptr = self.memory.get_singleton_by_class_name("LevelManager")

                self.base = self.memory.get_class_base(singleton_ptr)
                self.fields_base = self.memory.get_class_fields_base(singleton_ptr)
                self.current_level_base = self.memory.get_field(
                    self.fields_base, "currentLevel"
                )
                self.level_loader_base = self.memory.get_field(
                    self.fields_base, "levelLoader"
                )

                # Update fields
                self.title_position_set = False
                self._read_current_level()
                self._read_main_scene_name()

            else:
                self.__init__()

        except Exception:
            return

    def _read_current_level(self):
        # LevelManager -> currentLevel
        ptr = self.memory.follow_pointer(self.base, [self.current_level_base, 0x0])

        length = self.memory.read_int(ptr + 0x10)
        value = self.memory.read_string(ptr + 0x14, length * 2)
        if value:
            self.current_level = value

    def _read_main_scene_name(self):
        # LevelManager -> LevelLoader -> mainSceneName
        ptr = self.memory.follow_pointer(self.base, [self.level_loader_base, 0x30, 0x0])
        length = self.memory.read_int(ptr + 0x10)
        value = self.memory.read_string(ptr + 0x14, length * 2)
        if value:
            self.scene_name = value


_level_manager_mem = LevelManager()
_level_manager_mem.update()


def handle() -> LevelManager:
    return _level_manager_mem
