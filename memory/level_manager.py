from typing import Self

from memory.core import mem_handle


class LevelManager:
    def __init__(self: Self) -> None:
        self.memory = mem_handle()
        self.base = None
        self.fields_base = None
        self.current_level_base = None
        self.level_loader_base = None
        self.loading_base = None
        self.scene_name = None
        self.current_level = None
        self.loading = None

    def update(self: Self) -> None:
        if self.memory.ready_for_updates:
            try:
                if self.base is None or self.fields_base is None:
                    singleton_ptr = self.memory.get_singleton_by_class_name(
                        "LevelManager"
                    )
                    if singleton_ptr is None:
                        return
                    self.base = self.memory.get_class_base(singleton_ptr)
                    if self.base == 0x0:
                        return
                    self.fields_base = self.memory.get_class_fields_base(singleton_ptr)
                    self.current_level_base = self.memory.get_field(
                        self.fields_base, "currentLevel"
                    )

                    self.loading_base = self.memory.get_field(
                        self.fields_base, "loadingLevel"
                    )

                    self.level_loader_base = self.memory.get_field(
                        self.fields_base, "levelLoader"
                    )
                else:
                    self._read_loading()
                    self._read_current_level()
                    self._read_main_scene_name()
            except Exception as _e:  # noqa: F841
                # logger.debug(f"Level Manager Reloading {type(_e)}")
                self.__init__()

    def _read_loading(self: Self) -> None:
        # LevelManager -> loadingLevel
        self.loading = self.memory.read_bool(self.base + self.loading_base)

    def _read_current_level(self: Self) -> None:
        # LevelManager -> currentLevel
        ptr = self.memory.follow_pointer(self.base, [self.current_level_base, 0x0])
        if ptr is None or ptr == 0x0:
            return
        length = self.memory.read_int(ptr + 0x10)
        if length is None:
            return
        value = self.memory.read_string(ptr + 0x14, length * 2)
        if value:
            self.current_level = value.replace("\x00", "")

    def _read_main_scene_name(self: Self) -> None:
        # LevelManager -> LevelLoader -> mainSceneName
        ptr = self.memory.follow_pointer(self.base, [self.level_loader_base, 0x38, 0x0])
        if ptr is None or ptr == 0x0:
            return
        length = self.memory.read_int(ptr + 0x10)
        if length is None:
            return
        value = self.memory.read_string(ptr + 0x14, length * 2)
        if value:
            self.scene_name = value.replace("\x00", "")


_level_manager_mem = LevelManager()


def level_manager_handle() -> LevelManager:
    return _level_manager_mem
