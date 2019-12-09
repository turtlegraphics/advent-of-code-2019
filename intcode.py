#
# intcode machine
#
from inspect import getargspec

instruction_set = {}
def opcode(code):
    def add_to_set(func):
        instruction_set[code] = (func)
    return add_to_set


_instruction_set = {}
def instruction(code):
    def add_to_set(func):
        _instruction_set[code] = func
    return add_to_set

@instruction(1)
def _addppp(m):
    """addppp (%d)+(%d)->(%d)"""
    m[m[m.ip+3]] = m[m[m.ip+1]] + m[m[m.ip+2]]
    m.ip += 4 

@instruction(101)
def _addipp(m):
    """addipp #%d+(%d)->(%d)"""
    m[m[m.ip+3]] = m[m.ip+1] + m[m[m.ip+2]]
    m.ip += 4 

@instruction(1001)
def _addpip(m):
    """addpip (%d)+#%d->(%d)"""
    m[m[m.ip+3]] = m[m[m.ip+1]] + m[m.ip+2]
    m.ip += 4 

@instruction(1101)
def _addiip(m):
    """addiip #%d+#%d->(%d)"""
    m[m[m.ip+3]] = m[m.ip+1] + m[m.ip+2]
    m.ip += 4 

@instruction(2)
def _mulppp(m):
    """mulppp (%d)+(%d)->(%d)"""
    m[m[m.ip+3]] = m[m[m.ip+1]] * m[m[m.ip+2]]
    m.ip += 4 

@instruction(102)
def _mulipp(m):
    """mulipp #%d+(%d)->(%d)"""
    m[m[m.ip+3]] = m[m.ip+1] * m[m[m.ip+2]]
    m.ip += 4 

@instruction(1002)
def _mulpip(m):
    """mulpip (%d)+#%d->(%d)"""
    m[m[m.ip+3]] = m[m[m.ip+1]] * m[m.ip+2]
    m.ip += 4 

@instruction(1102)
def _muliip(m):
    """muliip #%d+#%d->(%d)"""
    m[m[m.ip+3]] = m[m.ip+1] * m[m.ip+2]
    m.ip += 4 

@instruction(7)
def _lthppp(m):
    """lthppp (%d)+(%d)->(%d)"""
    m[m[m.ip+3]] = 1 if m[m[m.ip+1]] < m[m[m.ip+2]] else 0
    m.ip += 4 

@instruction(107)
def _lthipp(m):
    """lthipp #%d+(%d)->(%d)"""
    m[m[m.ip+3]] = 1 if m[m.ip+1] < m[m[m.ip+2]] else 0
    m.ip += 4 

@instruction(1007)
def _lthpip(m):
    """lthpip (%d)+#%d->(%d)"""
    m[m[m.ip+3]] = 1 if m[m[m.ip+1]] < m[m.ip+2] else 0
    m.ip += 4 

@instruction(1107)
def _lthiip(m):
    """lthiip #%d+#%d->(%d)"""
    m[m[m.ip+3]] = 1 if m[m.ip+1] < m[m.ip+2] else 0
    m.ip += 4 

@instruction(8)
def _equppp(m):
    """equppp (%d)+(%d)->(%d)"""
    m[m[m.ip+3]] = 1 if m[m[m.ip+1]] == m[m[m.ip+2]] else 0
    m.ip += 4 

@instruction(108)
def _equipp(m):
    """equipp #%d+(%d)->(%d)"""
    m[m[m.ip+3]] = 1 if m[m.ip+1] == m[m[m.ip+2]] else 0
    m.ip += 4 

@instruction(1008)
def _equpip(m):
    """equpip (%d)+#%d->(%d)"""
    m[m[m.ip+3]] = 1 if m[m[m.ip+1]] == m[m.ip+2] else 0
    m.ip += 4 

@instruction(1108)
def _equiip(m):
    """equiip #%d+#%d->(%d)"""
    m[m[m.ip+3]] = 1 if m[m.ip+1] == m[m.ip+2] else 0
    m.ip += 4 

@instruction(5)
def _jmptpp(m):
    """jmptpp if (%d) goto (%d)"""
    if m[m[m.ip+1]] != 0:
        m.ip = m[m[m.ip+2]]
    else:
        m.ip += 3

@instruction(105)
def _jmptip(m):
    """jmptip if #%d goto (%d)"""
    if m[m.ip+1] != 0:
        m.ip = m[m[m.ip+2]]
    else:
        m.ip += 3

@instruction(1005)
def _jmptpi(m):
    """jmptpi if (%d) goto #%d"""
    if m[m[m.ip+1]] != 0:
        m.ip = m[m.ip+2]
    else:
        m.ip += 3

@instruction(1105)
def _jmptii(m):
    """jmptii if #%d goto #%d"""
    if m[m.ip+1] != 0:
        m.ip = m[m.ip+2]
    else:
        m.ip += 3

@instruction(6)
def _jmpfpp(m):
    """jmpfpp if (%d) goto (%d)"""
    if m[m[m.ip+1]] == 0:
        m.ip = m[m[m.ip+2]]
    else:
        m.ip += 3

@instruction(106)
def _jmpfip(m):
    """jmpfip if #%d goto (%d)"""
    if m[m.ip+1] == 0:
        m.ip = m[m[m.ip+2]]
    else:
        m.ip += 3

@instruction(1006)
def _jmpfpi(m):
    """jmpfpi if (%d) goto #%d"""
    if m[m[m.ip+1]] == 0:
        m.ip = m[m.ip+2]
    else:
        m.ip += 3

@instruction(1106)
def _jmpfii(m):
    """jmpfii if #%d goto #%d"""
    if m[m.ip+1] == 0:
        m.ip = m[m.ip+2]
    else:
        m.ip += 3

class EInput(Exception):
    """Input would block."""
    pass

@instruction(3)
def _inputp(m):
    """inputp (%d)"""
    try:
        val = m.input.pop(0)
    except IndexError:
        raise EInput
    m[m[m.ip+1]] = val
    m.ip += 2

class EOutput(Exception):
    """Output would block."""
    pass

@instruction(4)
def _outptp(m):
    """outptp (%d)"""
    val = m[m[m.ip+1]]
    m.output.append(val)
    m.ip += 2
    m.steps += 1 # exception will skip the step counting
    raise EOutput

@instruction(104)
def _outpti(m):
    """outpti #%d"""
    val = m[m.ip+1]
    m.output.append(val)
    m.ip += 2
    m.steps += 1 # exception will skip the step counting
    raise EOutput

class EQuit(Exception):
    """Intcode machine terminated."""
    pass

@instruction(99)
def _mquit(m):
    """quit"""
    raise EQuit

class EFault(Exception):
    """Execution fault."""
    pass

class Machine:
    def __init__(self,mem,input=[],debug=False):
        """
        mem : a filename containing a comma-separated memory image
              OR
              an array of intcode integers, will be copied locally
        input : an array of values to pass as input
        debug : when true, all instructions print output.
        """
        if isinstance(mem,str):
            with open(mem, 'r') as memfile:
                content = memfile.read()
            self.memory = [int(x) for x in content.split(',')]
        else:
            self.memory = list(mem)

        self.input = input
        self.output = []

        self.debug = debug

        self.ip = 0
        self.base = 0

    # Execution Routines

    def step(self):
        """Execute the instruction at the current ip."""
        if self.debug:
            out, offset = self._disone(self.ip)
            print out

        instruction = self[self.ip]
        self.ip += 1

        offset = 1
        opcode = instruction % 100
        try:
            operation = instruction_set[opcode]
        except KeyError:
            raise EFault('Illegal opcode: %d' % opcode)

        inargs = len(getargspec(operation).args)-1

        # decode instruction's input arguments
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

        # op = _instruction_set[self[self.ip]]
        # op(self)

    def run(self):
        """Run until an exception (EQuit, EInput, EOutput)"""
        while True:
            self.step()

    def runq(self):
        """
        Run until quit, not blocking for output.
        This is how programs ran before Day 7.
        """
        while True:
            try:
                self.step()
            except EOutput:
                pass
            except EQuit:
                return

    # Memory Management

    def __getitem__(self, address):
        """Read value at address"""
        return self.memory[address]

    def __setitem__(self, address, value):
        """Store value at address"""
        self.memory[address] = value

    # Disassembly Routines

    mode_desc = {
        0 : '(%d)',
        1 : '#%d',
        2 : '(%d+b)'
        }

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
        except IndexError:
            return('       <out of memory range>',-1)

        out = "%5d: " % addr
        opcode = instruction % 100
        offset = 1

        try:
            op = instruction_set[opcode]
        except KeyError:
            out += '????   '+str(instruction)
            return (out,offset)

        nargs = op.__doc__.count('%s')
        inargs = len(getargspec(op).args)-1

        pos = 100
        args = []
        while offset <= inargs:
            mode = (instruction / pos) % 10
            v = self[addr + offset]
            args.append(Machine.mode_desc[mode] % v)
            pos *= 10
            offset += 1

        if nargs > inargs:
            # instruction is a memory store
            v = self[addr + offset]
            args.append(Machine.mode_desc[0] % v)
            offset += 1

        out += op.__doc__ % tuple(args)

        return (out,offset)

    def disassemble(self, addr = 0, numinst = -1):
        """
        Dissassemble numinst instructions starting at addr.
        Pass numinst = -1 to disassemble until memory ends.
        """
        while numinst != 0:
            (out, offset) = self._disone(addr)
            print out
            if offset < 0:
                return
            addr += offset
            numinst -= 1

    def dump(self, start = 0, end = None):
        """Memory dump from start address to end address."""
        if end == None:
            end = len(self.memory)
        print ("%5d:" % start),
        addr = start
        while addr < end:
            print ("%5d" % self[addr]),
            addr += 1
            if (addr % 10 == 0):
                print
                print ("%5d:" % addr),
        print

    # Machine Instruction Set

    @opcode(1)
    def _add(self,v1,v2):
        """add %s + %s -> %s"""
        return v1+v2

    @opcode(2)
    def _mul(self,v1,v2):
        """mul %s + %s -> %s"""
        return v1*v2

    @opcode(3)
    def _input(self):
        """input %s"""
        try:
            val = self.input.pop(0)
            return val
        except IndexError:
            # will need to restart this instruction, so back up
            print 'backup!'
            self.ip -= 1
            raise EInput

    @opcode(4)
    def _output(self,v1):
        """output %s"""
        self.output.append(v1)
        raise EOutput

    @opcode(5)
    def _jmpt(self,v1,v2):
        """jmpt if %s goto %s"""
        if v1:
            self.ip = v2

    @opcode(6)
    def _jmpf(self,v1,v2):
        """jmpt if not %s goto %s"""
        if not v1:
            self.ip = v2

    @opcode(7)
    def _lt(self,v1,v2):
        """lt %s < %s -> %s"""
        return 1 if v1 < v2 else 0

    @opcode(8)
    def _eq(self,v1,v2):
        """eq %s == %s -> %s"""
        return 1 if v1 == v2 else 0

    @opcode(99)
    def _quit(self):
        """quit"""
        raise EQuit

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
    machine = Machine([80],debug=True)
    try:
        machine.run()
        assert(False)
    except EFault as err:
        print err

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
    machine = Machine("day5/test1.txt",input=[1],debug=True)
    machine.runq()
    print '    output:',machine.output
    assert(machine.output == [1])

    print 'test 2'
    machine = Machine("day5/test2.txt",debug=True)
    machine.runq()
    assert(machine[4] == 99)

    print 'test 3'
    for x in [0,1]:
        machine = Machine("day5/test3.txt",input=[x], debug=True)
        machine.runq()
        assert(machine.output == [x])
    print '    PASSED'

    print 'test 4'
    # check if input is <, =, or > 8
    inputs =  [  0,   1,   7,    8,    9, 1000]
    outputs = [999, 999, 999, 1000, 1001, 1001]
    for i in range(len(inputs)):
        machine = Machine("day5/test4.txt",input=[inputs[i]])
        if i == 0:
            machine.disassemble()
        print '    Running on input',inputs[i],
        machine.runq()
        print 'got',machine.output
        assert(machine.output == [outputs[i]])
    print '    PASSED'

    print 'Part 2 answer:'
    machine = Machine("day5/input.txt",input=[5])
    machine.runq()
    print '    Diagnostic code:',machine.output[0]
    assert(machine.output == [15724522])

    print '==========='
    print ' aoc day 7 '
    print '==========='
    amps = [Machine("day7/input.txt",[p]) for p in [7,6,5,8,9]]
    a = 0
    signal = 0
    while True:
        amps[a].input.append(signal)
        try:
            amps[a].run()
        except EOutput:
            signal = amps[a].output.pop()
        except EQuit:
            break
        a = (a + 1) % 5
    print 'Thrust using feedback loop (part 2):',signal
    assert(signal == 36384144)
    print '    PASSED'
