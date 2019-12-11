"""
 memory management for intcode machines

 Bryan Clair 2019
"""

# I decided this was unnecessary and that the built in dictionary
# was probably better, but here it is in case I change my mind

#
# Memory managers
#
class Memory:
    """
    Memory store for an intcode computer.
    Models an infinite virtual memory space.
    """
    def __init__(self):
        """Init a virtual memory"""
        self.topmem = -1
        
    def __getitem__(self, address):
        """Read value at address"""
        try:
            val = self.memory[address]
        except (IndexError, KeyError):
            raise EFault('Bad address: %d' % address)
        return val

    def __len__(self):
        """Return the maximum legal address plus one."""
        return self.topmem + 1

class MemoryDict(Memory):
    """
    Implement memory as a dictionary.
    """
    def __init__(self):
        self.memory = {}
        Memory.__init__(self)

    def __setitem__(self, address, value):
        self.memory[address] = value
        self.topmem = max(self.topmem,address)

class MemoryContiguous(Memory):
    """
    Implement a contiguous memory space as an array that
    can be extended when needed.
    """
    PAGESIZE = 4096
    DANGER = 4096 * 4096  # get this big, print a warning
    def __init__(self):
        self.memory = []
        Memory.__init__(self)

    def __setitem__(self, address, value):
        """Store value at address"""
        try:
            self.memory[address] = value
        except IndexError:
            distance = address - len(self.memory)
            needed = (distance // MemoryContiguous.PAGESIZE + 1) * MemoryContiguous.PAGESIZE
            if needed > MemoryContiguous.DANGER:
                warn('About to ask for %d memory.' % needed)
            self.memory.extend([0]*needed)
            self.memory[address] = value
 
        self.topmem = max(self.topmem,address)
