from typing import Self

from memory.core import mem_handle


# NewDialogManager is the internal naming for the class that handles the dialog boxes
# in the game. This class is used to determine if a dialog box is open or not.
# This is used to determine if the game is in a state where the player can
# interact with dialog boxes or not.
class NewDialogManager:
    def __init__(self: Self) -> None:
        self.memory = mem_handle()
        self.base = None
        self.fields_base = None
        self.opened_dialog_boxes_base = None
        self.dialog_open = False

    def update(self: Self) -> None:
        if self.memory.ready_for_updates:
            try:
                if self.base is None or self.fields_base is None:
                    singleton_ptr = self.memory.get_singleton_by_class_name(
                        "NewDialogManager"
                    )
                    if singleton_ptr is None:
                        return
                    self.base = self.memory.get_class_base(singleton_ptr)
                    if self.base == 0x0:
                        return
                    self.fields_base = self.memory.get_class_fields_base(singleton_ptr)
                    self.opened_dialog_boxes_base = self.memory.get_field(
                        self.fields_base, "openedDialogBoxes"
                    )

                else:
                    self._read_dialog_box()
            except Exception as _e:  # noqa: F841
                # logger.debug(f"New Dialog Manager Reloading {type(_e)}")
                self.__init__()

    def _read_dialog_box(self: Self) -> None:
        # NewDialogManager -> openedDialogBoxes -> 0x18 -> 0x30 (NewDialogBox)
        dialog_box_pointer = self.memory.follow_pointer(
            self.base, [self.opened_dialog_boxes_base, 0x18, 0x30, 0x0]
        )
        dialog_box_pointer_2 = self.memory.follow_pointer(
            self.base, [self.opened_dialog_boxes_base, 0x18, 0x48, 0x0]
        )
        if dialog_box_pointer != 0x0 or dialog_box_pointer_2 != 0x0:
            self.dialog_open = True
        else:
            self.dialog_open = False


_new_dialog_manager_mem = NewDialogManager()


def new_dialog_manager_handle() -> NewDialogManager:
    return _new_dialog_manager_mem
