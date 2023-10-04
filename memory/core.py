# Libraries and Core Files
import codecs
import logging
from typing import Self

import pymem

logger = logging.getLogger(__name__)


class SoSMemory:
    def __init__(self: Self) -> None:
        self.pm = None
        self.module = None
        self.module_base = None
        self.assemblies = None
        self.image = None
        self.type_info_definition_table = None
        self.ready_for_updates = False
        self.offsets = {
            "monoassembly_image": 0x0,
            "monoassembly_aname": 0x18,
            "monoassemblyname_name": 0x0,
            "monoimage_typecount": 0x18,
            "monoimage_metadatahandle": 0x28,
            "monoclass_name": 0x10,
            "monoclass_fields": 0x80,
            "monoclass_field_count": 0x120,
            "monoclass_static_fields": 0xB8,
            "monoclass_parent": 0x58,
            "monoclassfield_structsize": 0x20,
            "monoclassfield_name": 0x0,
            "monoclassfield_offset": 0x18,
        }

    # Helper for setting the `read_for_updates` field to allow depdencies to
    # ensure all the modules for the core are loaded
    def _set_ready_for_updates(self: Self) -> None:
        ready = (
            self.pm is not None
            and self.pm.process_handle is not None
            and self.assemblies is not None
            and self.type_info_definition_table is not None
            and self.module is not None
            and self.module_base is not None
            and self.image is not None
        )

        self.ready_for_updates = ready

    def update(self: Self) -> None:
        try:
            if self.pm is not None and not self.pm.base_address:
                self.__init__()
                return

            if not self.ready_for_updates:
                pm = pymem.Pymem("SeaOfStars.exe")
                self.pm = pm

                self.module = pymem.process.module_from_name(pm.process_handle, "GameAssembly.dll")
                self.module_base = self.module.lpBaseOfDll

                logger.info(
                    f"Base address of GameAssembly.dll in SeaOfStars.exe: {hex(self.module_base)}"
                )

                # Update Sigscans
                self._assemblies_trg_sig()
                self._type_info_definition_table_trg_sig()
                self.get_image()
                self._set_ready_for_updates()

        except Exception as _e:
            # logger.debug(f"Memory Core Reloading {type(_e)}")
            self.__init__()

    # This is a helper function designed to facilitate in finding instanced/dynamically allocated
    # objects. This is used most of the time for classes that inherit from a generic class such
    # as Manager<T>
    #
    # The process is as follows
    # Find the Class
    # Find the parent address (usually 0x10)
    # Find the instance field on the parent, which points to the dynamically allocated instance
    # Find the parent static table address
    # Return the sum of that static table_address on the parent and the instance field on the parent
    # to get the offset from the base image where that instance will be allocated
    def get_singleton_by_class_name(self: Self, class_name: str) -> int:
        local_class = self.get_class(class_name)
        if local_class is None or local_class == 0x0:
            return None
        parent = self.get_parent(local_class)
        if parent is None or parent == 0x0:
            return None
        instance_ptr = self.get_field(parent, "instance")
        if instance_ptr is None or instance_ptr == 0x0:
            return None
        static_table = self.get_static_table(parent)
        if static_table is None or static_table == 0x0:
            return None
        # This casting is probably not necessary but it ensures it should fit so it doesn't crash
        # when trying to debug pointer locations while building memory managers.
        return (static_table + instance_ptr) & 0xFFFFFFFFFFFFFFFF

    # This function allows you to follow an existing pointer created by get_pointer.
    # The purpose is to allow for performance allowing reusability from an existing pointer address
    # Unlike get_pointer, this function doesn't access the base before reading the offsets, however
    # like get_pointer, it does mutate the `offset` array by popping the last value and attaching
    # it at the end, so it can either be read from or used in another follow_pointer.
    def follow_pointer(self: Self, base: int, offsets: list[int]) -> int:
        last = offsets.pop()
        addr = base
        for offset in offsets:
            addr = self.pm.read_longlong(addr + offset)

        return addr + last

    def read_float(self: Self, ptr: int) -> float:
        return self.pm.read_float(ptr)

    def read_bool(self: Self, ptr: int) -> bool:
        return self.pm.read_bool(ptr)

    def read_int(self: Self, ptr: int) -> int:
        return self.pm.read_int(ptr)

    def read_short(self: Self, ptr: int) -> int:
        return self.pm.read_short(ptr)

    # Reads the garbled uuid string utf-8 field provided by Sea Of Stars
    # For example, for "TitleScreen" you may see:
    # this returns as example: 550e8400-e29b-41d4-a716-446655440000
    # b'T\x00i\x00t\x00t\x00l\x00e\x00S\x00c\x00r\x00e\x00e\x00n'
    # To "fix" this string, you will need to run value.replace("\x00", "")
    def read_uuid(self: Self, ptr: int) -> str:
        string_bytes = self.pm.read_bytes(ptr, 71)

        return codecs.decode(string_bytes, "UTF-8")

    # Reads the garbled guid string utf-8 field provided by Sea Of Stars
    # For example, for "TitleScreen" you may see:
    # b'T\x00i\x00t\x00t\x00l\x00e\x00S\x00c\x00r\x00e\x00e\x00n'
    # This returns as example: e6ac627711e4ee44da103c47d1cd5736
    # To "fix" this string, you will need to run value.replace("\x00", "")
    def read_guid(self: Self, ptr: int) -> str:
        string_bytes = self.pm.read_bytes(ptr, 64)

        return codecs.decode(string_bytes, "UTF-8")

    def read_string(self: Self, ptr: int, length: int) -> str:
        string_bytes = self.pm.read_bytes(ptr, length)

        return codecs.decode(string_bytes, "UTF-8")

    def read_longlong(self: Self, ptr: int) -> int:
        return self.pm.read_longlong(ptr)

    # Scans the module/image class list for a specific class name by string.
    def get_class(self: Self, class_name: str) -> int | None:
        unity_classes = self._get_image_classes()
        for item in unity_classes:
            ptr = pymem.memory.read_longlong(
                self.pm.process_handle, item + self.offsets["monoclass_name"]
            )

            name = pymem.memory.read_string(self.pm.process_handle, ptr, 128)
            if name == class_name:
                return item
        return None

    # Gets a pointer to a named field for a provided class pointer
    def get_field(self: Self, class_ptr: int, field_name: str) -> int | None:
        record = None
        unity_fields = self._get_fields(class_ptr)

        for item in unity_fields:
            ptr = pymem.memory.read_longlong(
                self.pm.process_handle, item + self.offsets["monoclassfield_name"]
            )
            name = pymem.memory.read_string(self.pm.process_handle, ptr, 128)
            if name == field_name:
                record = item
                break
        if record is not None:
            return pymem.memory.read_int(
                self.pm.process_handle, record + self.offsets["monoclassfield_offset"]
            )
        return None

    # Get the static table pointer for a provided class pointer. This is an array of pointers
    # to each static field on the class.
    def get_static_table(self: Self, class_ptr: int) -> int:
        return pymem.memory.read_longlong(
            self.pm.process_handle, class_ptr + self.offsets["monoclass_static_fields"]
        )

    # This is used to get the parent class of a type. This should
    # only be used in specific circumstances, like finding the Generic class to
    # find an instanced class. See get_singleton_by_class_name for its usage.
    def get_parent(self: Self, class_ptr: int) -> int:
        return pymem.memory.read_longlong(
            self.pm.process_handle, class_ptr + self.offsets["monoclass_parent"]
        )

    # This is used to get the fields lookup base of the class
    # Provides the field offset relative to the base class.
    def get_class_fields_base(self: Self, class_ptr: int) -> int:
        return pymem.memory.read_longlong(self.pm.process_handle, self.get_class_base(class_ptr))

    # This is used to get the actual base of the class
    # This can be used as the base when following pointer + field offsets
    def get_class_base(self: Self, class_ptr: int) -> int:
        return pymem.memory.read_longlong(self.pm.process_handle, class_ptr)

    # Scans for the assemblies signature for the specific version of unity for SoS
    def _assemblies_trg_sig(self: Self) -> None:
        if self.assemblies is None:
            # "48 FF C5 80 3C ?? 00 75 ?? 48 8B 1D"
            signature = b"\\x48\\xFF\\xC5\\x80\\x3C.\\x00\\x75.\\x48\\x8B\\x1D"
            # 32bit "8A 07 47 84 C0 75 ?? 8B 35"
            # signature = b"\\x8A\\x07\\x47\\x84\\xC0\\x75.\\x8B\\x35"
            address = (
                pymem.pattern.pattern_scan_module(self.pm.process_handle, self.module, signature)
                + 12
            )
            self.assemblies = address + 0x4 + pymem.memory.read_int(self.pm.process_handle, address)

    # Scans for the type info definition table signature for the specific version of unity for SoS
    def _type_info_definition_table_trg_sig(self: Self) -> None:
        if self.type_info_definition_table is None:
            # "48 83 3C ?? 00 75 ?? 8B C? E8"
            signature = b"\\x48\\x83\\x3C.\\x00\\x75.\\x8B.\\xe8"
            address = (
                pymem.pattern.pattern_scan_module(self.pm.process_handle, self.module, signature)
                - 4
            )
            self.type_info_definition_table = (
                address + 0x4 + pymem.memory.read_int(self.pm.process_handle, address)
            )

    # Gets the Assembly-CSharp image where the games code lives so it can be used as a module base
    def get_image(self: Self, assembly_name: str = "Assembly-CSharp") -> int:
        assemblies = pymem.memory.read_longlong(self.pm.process_handle, self.assemblies)

        image = None

        while True:
            mono_assembly = pymem.memory.read_longlong(self.pm.process_handle, assemblies)

            if mono_assembly is None:
                return

            name_addr_pointer = (
                mono_assembly
                + self.offsets["monoassembly_aname"]
                + self.offsets["monoassemblyname_name"]
            )
            name_addr = pymem.memory.read_longlong(self.pm.process_handle, name_addr_pointer)
            name = pymem.memory.read_string(self.pm.process_handle, name_addr, 128)

            if name == assembly_name:
                image = pymem.memory.read_longlong(
                    self.pm.process_handle,
                    mono_assembly + self.offsets["monoassembly_image"],
                )
                break
            assemblies = assemblies + 8

        self.image = image

    # Get the pointers for each field in a class pointer
    def _get_fields(self: Self, class_ptr: int) -> list[int]:
        field_count = (
            pymem.memory.read_longlong(
                self.pm.process_handle,
                class_ptr + self.offsets["monoclass_field_count"],
            )
            & 0xFFFF
        )
        fields_ptr = pymem.memory.read_longlong(
            self.pm.process_handle, class_ptr + self.offsets["monoclass_fields"]
        )
        fields: list[int] = []
        struct_size = self.offsets["monoclassfield_structsize"] & 0xFFFFFFFFFFFFFFFF
        for field in range(0, field_count):
            fields.append(fields_ptr + (field * struct_size))
        return fields

    # Get all Unity Types/Classes in the provided module/dll
    def _get_image_classes(self: Self) -> list[int]:
        type_count = pymem.memory.read_int(
            self.pm.process_handle, self.image + self.offsets["monoimage_typecount"]
        )

        inner_handle = pymem.memory.read_longlong(
            self.pm.process_handle,
            self.image + self.offsets["monoimage_metadatahandle"],
        )
        metadata_handle = pymem.memory.read_int(self.pm.process_handle, inner_handle)
        ptr = pymem.memory.read_longlong(self.pm.process_handle, self.type_info_definition_table)

        ptr = ptr + (metadata_handle * 8)
        classes: list[int] = []
        for field in range(0, type_count):
            field_class = pymem.memory.read_ulonglong(self.pm.process_handle, ptr + (field * 8))

            if field_class:
                classes.append(field_class)
        return classes


_mem = SoSMemory()
_mem.update()


def mem_handle() -> SoSMemory:
    return _mem
