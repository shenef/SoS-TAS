# Libraries and Core Files
import logging
<<<<<<< HEAD

=======
>>>>>>> 621c191 (Adds initial memory reads and some performance fixes)
import pymem

logger = logging.getLogger(__name__)

<<<<<<< HEAD

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

=======
class SoSMemory():
    def __init__(self):
        self.pm = None
        
    def update(self):
        try:
            if self.pm is None:
                pm = pymem.Pymem("SeaOfStars.exe")
                self.base_addr = pymem.process.module_from_name(
                    pm.process_handle, "GameAssembly.dll"
                ).lpBaseOfDll
                print(
                    f"Base address of GameAssembly.dll in SeaOfStars.exe: {hex(self.base_addr)}"
                )
            
                self.pm = pm
        except:
            return self
        
>>>>>>> 621c191 (Adds initial memory reads and some performance fixes)
    def get_pointer(self, root, offsets):
        """
        Follow the pointer from the application and add the last offset.
        """
<<<<<<< HEAD
        # try:

        addr = self.pm.read_longlong(self.base_addr + root)
        last = offsets.pop()
        for i in offsets:
            addr = self.pm.read_longlong(addr + i)

        return addr + last

    # except:
    #     return None
=======
        try:
            addr = self.pm.read_longlong(self.base_addr + root)
            last = offsets.pop()
            for i in offsets: 
                addr = self.pm.read_longlong(addr + i)
            
            return addr + last
        except:
            return None
>>>>>>> 621c191 (Adds initial memory reads and some performance fixes)

    def follow_pointer(self, base, offsets):
        """
        Follow an existing pointer and add the last offset.
        """
        try:
            last = offsets.pop()
            addr = base
<<<<<<< HEAD
            for i in offsets:
                addr = self.pm.read_longlong(addr + i)

            return addr + last
        except Exception:
=======
            for i in offsets: 
                addr = self.pm.read_longlong(addr + i)
            
            return addr + last
        except:
>>>>>>> 621c191 (Adds initial memory reads and some performance fixes)
            return None

    def read_float(self, ptr):
        try:
            return self.pm.read_float(ptr)
<<<<<<< HEAD
        except Exception:
            return 0.0


=======
        except:
            return 0.0

>>>>>>> 621c191 (Adds initial memory reads and some performance fixes)
_mem = SoSMemory()
_mem.update()


def mem_handle() -> SoSMemory:
<<<<<<< HEAD
    return _mem
=======
    return _mem
>>>>>>> 621c191 (Adds initial memory reads and some performance fixes)
