from typing import Self

from memory.core import mem_handle


# This is actually called LevelUpSceneController, but its a manager
# class, so we'll call it that here.
class LevelUpManager:
    def __init__(self: Self) -> None:
        self.memory = mem_handle()
        self.base = None
        self.fields_base = None

    def update(self: Self) -> None:
        if self.memory.ready_for_updates:
            try:
                if self.base is None or self.fields_base is None:
                    singleton_ptr = self.memory.get_singleton_by_class_name(
                        "LevelUpSceneController"
                    )
                    if singleton_ptr is None:
                        return
                    self.base = self.memory.get_class_base(singleton_ptr)
                    print("level up")
                    print(hex(self.base))
                    if self.base == 0x0:
                        return
                    self.fields_base = self.memory.get_class_fields_base(singleton_ptr)
                else:
                    self._read_loading()
            except Exception as _e:  # noqa: F841
                # logger.debug(f"Level Manager Reloading {type(_e)}")
                self.__init__()

    def _read_loading(self: Self) -> None:
        pass


_level_up_manager_mem = LevelUpManager()


def level_up_manager_handle() -> LevelUpManager:
    return _level_up_manager_mem
