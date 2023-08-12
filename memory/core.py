# Libraries and Core Files
import logging

import pymem

logger = logging.getLogger(__name__)


class SoSMemory:
    def __init__(self):
        self.pm = None

    def update(self):
        # try:
        if self.pm is None:
            pm = pymem.Pymem("SeaOfStars.exe")
            self.base_addr = pymem.process.module_from_name(
                pm.process_handle, "GameAssembly.dll"
            ).lpBaseOfDll
            print(
                f"Base address of GameAssembly.dll in SeaOfStars.exe: {hex(self.base_addr)}"
            )

            self.pm = pm
        # except:
        #     return self

    def get_pointer(self, root, offsets):
        """
        Follow the pointer from the application and add the last offset.
        """
        # try:

        addr = self.pm.read_longlong(self.base_addr + root)
        last = offsets.pop()
        for i in offsets:
            addr = self.pm.read_longlong(addr + i)

        return addr + last

    # except:
    #     return None

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


_mem = SoSMemory()
_mem.update()


def mem_handle() -> SoSMemory:
    return _mem
