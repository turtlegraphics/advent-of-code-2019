#
# intcode machine
#
from inspect import getargspec
from warnings import warn

class EInput(Exception):
    """Input blocked."""
    pass

class EOutput(Exception):
    """Output available."""
    pass

class EHalt(Exception):
    """Machine halted."""
    pass

class EFault(Exception):
    """Execution fault."""
    pass

class Machine:
    def __init__(self,mem,input=[],debug=False):
        """
        mem : a filename containing a comma-separated memory image
              OR
              an array of intcode integers, will be copied locally
        input : an array of values to pass as input, or a single integer input
        debug : when true, all instructions print output.
        """
        self.memory = MemoryDict()

        if isinstance(mem,str):
            with open(mem, 'r') as memfile:
                content = memfile.read()
            mem = [int(x) for x in content.split(',')]

        for i in range(len(mem)):
            self.memory[i] = mem[i]

        if isinstance(input, int):
            self.input = [input]
        else:
            self.input = input

        self.output = []

        self.debug = debug

        self.ip = 0
        self.base = 0

    # Execution Routines

    def run(self):
        """Run.  Only escapes via exceptions."""
        while True:
            self.step()

    def runq(self):
        """
        Run until machine halts, not blocking on output.
        Returns output as a list.
        """
        while True:
            try:
                self.step()
            except EOutput:
                pass
            except EHalt:
                return self.output

    def step(self):
        """Execute the instruction at the current ip."""
        # print instruction if debug is on
        if self.debug:
            out, offset = self._disone(self.ip)
            print out

        # instruction fetch and decode
        instruction = self[self.ip]
        self.ip += 1

        offset = 1
        opcode = instruction % 100
        try:
            operation = _instruction_set[opcode]
        except KeyError:
            raise EFault('Illegal opcode: %d' % opcode)

        # build instruction's input arguments
        inargs = len(getargspec(operation).args)-1  # number of input args
        pos = 100
        args = []
        while inargs:
            mode = (instruction / pos) % 10
            param = self[self.ip]
            self.ip += 1

            if mode == 0:
                val = self[param]
            elif mode == 1:
                val = param
            elif mode == 2:
                val = self[param + self.base]
            else:
                raise EFault("Bad mode in instruction %d" % instruction)
            args.append(val)
            pos *= 10
            inargs -= 1

        # execute operation
        result = operation(self,*args)

        # store return value (if any)
        if result != None:
            mode = (instruction / pos) % 10
            param = self[self.ip]
            self.ip += 1

            if mode == 0:
                self[param] = result
            elif mode == 1:
                raise EFault("Immediate mode illegal for store.")
            elif mode == 2:
                self[param + self.base] = result
            else:
                raise EFault("Bad mode in instruction %d" % instruction)

    # Memory access

    def __getitem__(self, address):
        """Read value at address"""
        return self.memory[address]

    def __setitem__(self, address, value):
        """Store value at address"""
        self.memory[address] = value

    # Disassembly Routines

    def _disone(self, addr):
        """
        Disassemble the single instruction at addr.
        Returns a pair (out,offset)
          out : the disassembled string
          offset : how far to advance in memory
                   (or -1 if addr is an illegal address)
        """
        try:
            instruction = self[addr]
        except EFault:
            return('       <bad memory address>',-1)

        head = '%5d: ' % addr
        out = ''
        opcode = instruction % 100
        offset = 1

        try:
            op = _instruction_set[opcode]
        except KeyError:
            return (head + '????   ' + str(instruction), 1)

        nargs = op.__doc__.count('%s')
        inargs = len(getargspec(op).args)-1

        pos = 100
        args = []
        while offset <= inargs:
            mode = (instruction / pos) % 10
            v = self[addr + offset]
            try:
                args.append(_mode_syntax[mode] % v)
            except KeyError:
                return (head + '????   ' + str(instruction), 1)
                
            pos *= 10
            offset += 1

        if nargs > inargs:
            # instruction is a memory store
            mode = (instruction / pos) % 10
            v = self[addr + offset]
            try:
                args.append(_mode_syntax[mode] % v)
            except KeyError:
                return (head + '????   ' + str(instruction), 1)

            offset += 1

        out = head + op.__name__[1:].ljust(6) + ' ' + op.__doc__ % tuple(args)

        return (out,offset)

    def disassemble(self, addr = 0, numinst = -1):
        """
        Dissassemble numinst instructions starting at addr.
        Pass numinst = -1 to disassemble until memory ends or
        four zeros in a row.
        """
        zeros = 0
        while numinst != 0:
            try:
                inst = self[addr]
            except EFault:
                return

            if inst == 0:
                zeros += 1
                if zeros > 4 and numinst < 0:
                    return
            else:
                zeros = 0

            (out, offset) = self._disone(addr)
            if offset < 0:
                return
            print out
            addr += offset
            numinst -= 1

    def dump(self, start = 0, end = None):
        """Memory dump the address range from start to end-1."""
        if end == None:
            end = start + 100

        addr = start - (start % 10)
        while addr < end:
            if (addr % 10 == 0):
                print ("%5d:" % addr),
            if addr >= start:
                try:
                    print ("%5d" % self[addr]),
                except EFault:
                    print
                    return
            else:
                print "     ",
            addr += 1
            if (addr % 10 == 0):
                print
        if (addr % 10 != 0):
            print

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

#
# Machine Instruction Set
#

_mode_syntax = {
    0 : '[%d]',
    1 : '#%d',
    2 : '[%d+b]'
    }

_instruction_set = {}
def _opcode(code):
    def add_to_set(func):
        _instruction_set[code] = (func)
    return add_to_set

@_opcode(1)
def _add(m,v1,v2):
    """%s + %s -> %s"""
    return v1+v2

@_opcode(2)
def _mult(m,v1,v2):
    """%s * %s -> %s"""
    return v1*v2

@_opcode(3)
def _input(m):
    """IN %s"""
    try:
        val = m.input.pop(0)
        return val
    except IndexError:
        # will need to restart this instruction, so back up
        print 'backup!'
        m.ip -= 1
        raise EInput

@_opcode(4)
def _output(m,v1):
    """OUT %s"""
    m.output.append(v1)
    raise EOutput

@_opcode(5)
def _jmp_t(m,v1,v2):
    """if %s goto %s"""
    if v1:
        m.ip = v2

@_opcode(6)
def _jmp_f(m,v1,v2):
    """if not %s goto %s"""
    if not v1:
        m.ip = v2

@_opcode(7)
def _less(m,v1,v2):
    """(%s < %s) -> %s"""
    return 1 if v1 < v2 else 0

@_opcode(8)
def _equal(m,v1,v2):
    """(%s == %s) -> %s"""
    return 1 if v1 == v2 else 0

@_opcode(9)
def _base(m,v1):
    """b += %s"""
    m.base += v1

@_opcode(99)
def _halt(m):
    """HALT"""
    raise EHalt

if __name__ == "__main__":
    print '==========='
    print 'simple test'
    print '==========='
    machine = Machine([
            1,9,10,3,
            2,3,11,0,
            99,
            30,40,50
            ],debug = True)

    print 'Memory state:'
    machine.dump()

    print 'Data:'
    machine.dump(9,12)

    print 'Disassembly:'
    machine.disassemble()

    print 'Running...'
    machine.runq()

    print 'Memory state:'
    machine.dump(0,12)
    assert(machine[0] == 3500)

    print '==========='
    print ' Faults    '
    print '==========='
    fault_tests = [
        [],
        [80],
        [301,0,0,0],
        [1,4,4,4],
        [10001,2,2,2]
        ]
    for mem in fault_tests:
        machine = Machine(mem,debug=True)
        print 'running:',mem
        try:
            machine.run()
            assert(False)
        except EFault as err:
            print '      ',err

    print '==========='
    print ' aoc day 2 '
    print '==========='
    machine = Machine("day2/input.txt")
    machine[1] = 12
    machine[2] = 2
    print 'Disassembly:'
    machine.disassemble()

    print 'Running...'
    machine.runq()
    print 'Part 1 answer:',machine[0]
    assert(machine[0] == 3058646)

    print '==========='
    print ' aoc day 5 '
    print '==========='
    print 'test 1'
    machine = Machine("day5/test1.txt",input=1,debug=True)
    out = machine.runq()
    print '    output:',out
    assert(out == [1])

    print 'test 2'
    machine = Machine("day5/test2.txt",debug=True)
    machine.runq()
    assert(machine[4] == 99)

    print 'test 3'
    for x in [0,1]:
        machine = Machine("day5/test3.txt",input=x,debug=True)
        out = machine.runq()
        assert(out == [x])
        print '    PASSED'

    print 'test 4'
    # check if input is <, =, or > 8
    inputs =  [  0,   1,   7,    8,    9, 1000]
    outputs = [999, 999, 999, 1000, 1001, 1001]
    for i in range(len(inputs)):
        machine = Machine("day5/test4.txt",input=inputs[i])
        if i == 0:
            machine.disassemble()
        print '    Running on input',inputs[i],
        out = machine.runq()
        print 'got',out
        assert(out == [outputs[i]])
    print '    PASSED'

    print 'Part 2 answer:'
    machine = Machine("day5/input.txt",input=5)
    out = machine.runq()
    print '    Diagnostic code:',out[0]
    assert(out == [15724522])

    print '==========='
    print ' aoc day 7 '
    print '==========='
    amps = [Machine("day7/input.txt",input=p) for p in [7,6,5,8,9]]
    a = 0
    signal = 0
    while True:
        amps[a].input.append(signal)
        try:
            amps[a].run()
        except EOutput:
            signal = amps[a].output.pop()
        except EHalt:
            break
        a = (a + 1) % 5
    print 'Thrust using feedback loop (part 2):',signal
    assert(signal == 36384144)
    print '    PASSED'

    print '==========='
    print ' aoc day 9 '
    print '==========='
    quine = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
    m = Machine(quine + [0]*100)
    m.disassemble(numinst = 6)
    out = m.runq()
    assert(out == quine)
    print '    PASSED'

    print
    m = Machine([1102,34915192,34915192,7,4,7,99,0])
    m.disassemble()
    out = m.runq()
    assert(out == [1219070632396864])
    print '    PASSED'

    print
    m = Machine([104,1125899906842624,99])
    m.disassemble()
    out = m.runq()
    assert(out == [1125899906842624])
    print '    PASSED'

    print 'Part 1:'
    m = Machine("day9/input.txt",input=1)
    out = m.runq()
    print '   ',out[0]
    assert(out == [2775723069])

    from timeit import default_timer as timer
    print 'Part 2 (takes about 4.5 seconds):'
    m = Machine("day9/input.txt",input=2)
    start = timer()
    out = m.runq()
    end = timer()
    print '   ',out[0],'(in',round(end-start,2),'seconds)'
    assert(out == [49115])
