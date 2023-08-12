# Libraries and Core Files
import logging
import pymem

logger = logging.getLogger(__name__)

class SoSMemory():
    def __init__(self):
        self.pm = None
        self.module = None
        self.module_base = None
        self.assemblies = None
        self.image = None
        self.type_info_definition_table = None
        self.offsets = {
            'monoassembly_image': 0x0,
            'monoassembly_aname': 0x18,
            'monoassemblyname_name': 0x0,
            'monoimage_typecount': 0x18,
            'monoimage_metadatahandle': 0x28,
            'monoclass_name': 0x10,
            'monoclass_fields': 0x80,
            'monoclass_field_count': 0x120,
            'monoclass_static_fields': 0xB8,
            'monoclass_parent': 0x58,
            'monoclassfield_structsize': 0x20,
            'monoclassfield_name': 0x0,
            'monoclassfield_offset': 0x18,
        }
        
    def update(self):
        try:
            if self.pm is None:
                pm = pymem.Pymem("SeaOfStars.exe")      
                self.pm = pm

                self.module = pymem.process.module_from_name(
                    pm.process_handle, "GameAssembly.dll"
                )
                self.module_base = self.module.lpBaseOfDll

                print(
                    f"Base address of GameAssembly.dll in SeaOfStars.exe: {hex(self.module_base)}"
                )

                # Update Sigscans
                self._assemblies_trg_sig()
                self._type_info_definition_table_trg_sig()
                self.get_image()
                
                # ppm_class = self.get_class("PlayerPartyManager")

                # parent = self.get_parent(ppm_class)
                # instance_ptr = self.get_field(parent, "instance")
                # print("instance ptr")
                # print(instance_ptr)
                
                # static_table = self.get_static_table(parent) 
                # singleton_ptr = (static_table + instance_ptr) & 0xFFFFFFFFFFFFFFFF
                # # need to double dip into instance results, use pointer stuff instead
                # print("singleton ptr")
                # print(singleton_ptr)
                # print(hex(singleton_ptr))
                # singleton = self.get_class_root(singleton_ptr)
                # print("singleton")
                # print(singleton)
                # print(hex(singleton))
                # max_followers = self.get_field(singleton, "followersCatchUpEnabled") 
                # print("MAX FOLLOWERS")
                # print(max_followers)
                # print(hex(max_followers))
                # out = pymem.memory.read_int(self.pm.process_handle, singleton + 0x60)
                # print(out)
                # print(hex(max_followers))
                # print("singleton 1")
                # print(singleton)
                # print(hex(singleton))
                # singleton = pymem.memory.read_longlong(self.pm.process_handle, singleton)
                # print("singleton 2")
                # print(singleton)
                # print(hex(singleton))              
               

                # out = pymem.memory.read_int(self.pm.process_handle, singleton + max_followers)
                # print(out)
                # get field > can follow a pointer from here
                # 

        except Exception:
            return self
        
    def get_pointer(self, root, offsets):
        """
        Follow the pointer from the application and add the last offset.
        """
        try:

            addr = self.pm.read_longlong(self.base_addr + root)
            last = offsets.pop()
            for i in offsets:
                addr = self.pm.read_longlong(addr + i)

            return addr + last

        except Exception:
            return None

    def follow_pointer(self, base, offsets):
        """
        Follow an existing pointer and add the last offset.
        """
        try:
            last = offsets.pop()
            addr = base
            for i in offsets:
                addr = self.pm.read_longlong(addr + i)

            return addr + last
        except Exception:
            return None

    def read_float(self, ptr):
        try:
            return self.pm.read_float(ptr)
        except Exception:
            return 0.0
        
    def get_class(self, class_name):
        record = None
        unity_classes = self._get_image_classes()
        for item in unity_classes:
            ptr = pymem.memory.read_longlong(self.pm.process_handle, item + self.offsets["monoclass_name"])
            name = pymem.memory.read_string(self.pm.process_handle, ptr, 128)
            if name == class_name:
                record = item
                break
        return record
    
    def get_field(self, class_ptr, field_name):
        record = None
        unity_fields = self._get_fields(class_ptr)
        for item in unity_fields:
            ptr = pymem.memory.read_longlong(self.pm.process_handle, item + self.offsets["monoclassfield_name"])
            name = pymem.memory.read_string(self.pm.process_handle, ptr, 128)
            if name == field_name:
                record = item
                break
        if record is not None:
            return pymem.memory.read_int(self.pm.process_handle, record + self.offsets["monoclassfield_offset"])
        else:
            return None
    
    def get_static_table(self, class_ptr):
        return pymem.memory.read_longlong(self.pm.process_handle, class_ptr + self.offsets["monoclass_static_fields"])
    
    def get_parent(self, class_ptr):
        return pymem.memory.read_longlong(self.pm.process_handle, class_ptr + self.offsets["monoclass_parent"])
    
    # This is used to get the root of the class when evaluating non-parent classes
    def get_class_root(self, class_ptr):
        singleton = pymem.memory.read_longlong(self.pm.process_handle, class_ptr)
        return pymem.memory.read_longlong(self.pm.process_handle, singleton)

    def _assemblies_trg_sig(self):
            if self.assemblies is None:
                # "48 FF C5 80 3C ?? 00 75 ?? 48 8B 1D"
                signature = b"\\x48\\xFF\\xC5\\x80\\x3C.\\x00\\x75.\\x48\\x8B\\x1D"
                # 32bit "8A 07 47 84 C0 75 ?? 8B 35"
                # signature = b"\\x8A\\x07\\x47\\x84\\xC0\\x75.\\x8B\\x35"
                address = pymem.pattern.pattern_scan_module(self.pm.process_handle, self.module, signature) + 12
                self.assemblies = address + 0x4 + pymem.memory.read_int(self.pm.process_handle, address)

            
    def _type_info_definition_table_trg_sig(self):
            if self.type_info_definition_table is None:
                # "48 83 3C ?? 00 75 ?? 8B C? E8"
                signature = b"\\x48\\x83\\x3C.\\x00\\x75.\\x8B.\\xe8"
                address = pymem.pattern.pattern_scan_module(self.pm.process_handle, self.module, signature) - 4
                self.type_info_definition_table = address + 0x4 + pymem.memory.read_int(self.pm.process_handle, address)

    def get_image(self, assembly_name = "Assembly-CSharp"):
        assemblies = pymem.memory.read_longlong(self.pm.process_handle, self.assemblies)

        image = None
        
        while True:
            mono_assembly = pymem.memory.read_longlong(self.pm.process_handle, assemblies)

            if mono_assembly is None:
                return None

            name_addr_pointer = mono_assembly + self.offsets['monoassembly_aname'] + self.offsets['monoassemblyname_name']
            name_addr = pymem.memory.read_longlong(self.pm.process_handle, name_addr_pointer)
            name = pymem.memory.read_string(self.pm.process_handle, name_addr, 128)

            if name == assembly_name:
                image = pymem.memory.read_longlong(self.pm.process_handle, mono_assembly + self.offsets['monoassembly_image'])
                break
            assemblies = assemblies + 8
        
        self.image = image


    def _get_fields(self, class_ptr):
        field_count = pymem.memory.read_longlong(self.pm.process_handle, class_ptr + self.offsets['monoclass_field_count']) & 0xFFFF
        fields_ptr = pymem.memory.read_longlong(self.pm.process_handle, class_ptr + self.offsets['monoclass_fields'])
        fields = []
        struct_size = self.offsets['monoclassfield_structsize'] & 0xFFFFFFFFFFFFFFFF
        for i in range(0, field_count):
            fields.append(fields_ptr + (i * struct_size))
        return fields


    def _get_image_classes(self):
        type_count = pymem.memory.read_int(self.pm.process_handle, self.image + self.offsets['monoimage_typecount'])
        inner_handle =  pymem.memory.read_longlong(self.pm.process_handle, self.image + self.offsets['monoimage_metadatahandle'])
        metadata_handle = pymem.memory.read_int(self.pm.process_handle, inner_handle)
        ptr = pymem.memory.read_longlong(self.pm.process_handle, self.type_info_definition_table)
        
        ptr = ptr + (metadata_handle * 8)
        classes = []
        for i in range(0, type_count):
            i_class = pymem.memory.read_ulonglong(self.pm.process_handle, ptr + ((i * 8)))
            if i_class:
                classes.append(i_class)
        return classes

_mem = SoSMemory()
_mem.update()


def mem_handle() -> SoSMemory:
    return _mem
