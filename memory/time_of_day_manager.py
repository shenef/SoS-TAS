import logging
from typing import Self

from memory.core import mem_handle

logger = logging.getLogger(__name__)


# We are reaching into the AudioManager for Time of Day instead of using
# Sabotage.TODManager simply as a way to avoid having to load the other module
# into memory. The currentTimeOfDay field is provided on the AudioManager as well.
# `current_time`` is a `float` from 0.0 to 23.99~.
class TimeOfDayManager:
    def __init__(self: Self) -> None:
        self.memory = mem_handle()
        self.base = None
        self.fields_base = None
        self.opened_dialog_boxes_base = None
        self.fields_base = None
        self.time_of_day_base = None
        self.current_time = 0.0

    def update(self: Self) -> None:
        if self.memory.ready_for_updates:
            try:
                if self.base is None or self.fields_base is None:
                    singleton_ptr = self.memory.get_singleton_by_class_name(
                        "AudioManager"
                    )
                    if singleton_ptr is None:
                        return
                    self.base = self.memory.get_class_base(singleton_ptr)
                    self.fields_base = self.memory.get_class_fields_base(singleton_ptr)
                    self.time_of_day_base = self.memory.get_field(
                        self.fields_base, "currentTimeOfDay"
                    )

                else:
                    self._read_current_time()
            except Exception as _e:  # noqa: F841
                # logger.debug(f"Audio Manager Reloading {type(_e)}")
                self.__init__()

    def _read_current_time(self: Self) -> None:
        # AudioManager -> currentTime
        self.current_time = self.memory.read_float(self.base + self.time_of_day_base)


_time_of_day_manager_mem = TimeOfDayManager()


def time_of_day_manager_handle() -> TimeOfDayManager:
    return _time_of_day_manager_mem
