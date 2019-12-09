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
    m.mem[m.mem[m.ip+3]] = m.mem[m.mem[m.ip+1]] + m.mem[m.mem[m.ip+2]]
    m.ip += 4 

@instruction(101)
def _addipp(m):
    """addipp #%d+(%d)->(%d)"""
    m.mem[m.mem[m.ip+3]] = m.mem[m.ip+1] + m.mem[m.mem[m.ip+2]]
    m.ip += 4 

@instruction(1001)
def _addpip(m):
    """addpip (%d)+#%d->(%d)"""
    m.mem[m.mem[m.ip+3]] = m.mem[m.mem[m.ip+1]] + m.mem[m.ip+2]
    m.ip += 4 

@instruction(1101)
def _addiip(m):
    """addiip #%d+#%d->(%d)"""
    m.mem[m.mem[m.ip+3]] = m.mem[m.ip+1] + m.mem[m.ip+2]
    m.ip += 4 

@instruction(2)
def _mulppp(m):
    """mulppp (%d)+(%d)->(%d)"""
    m.mem[m.mem[m.ip+3]] = m.mem[m.mem[m.ip+1]] * m.mem[m.mem[m.ip+2]]
    m.ip += 4 

@instruction(102)
def _mulipp(m):
    """mulipp #%d+(%d)->(%d)"""
    m.mem[m.mem[m.ip+3]] = m.mem[m.ip+1] * m.mem[m.mem[m.ip+2]]
    m.ip += 4 

@instruction(1002)
def _mulpip(m):
    """mulpip (%d)+#%d->(%d)"""
    m.mem[m.mem[m.ip+3]] = m.mem[m.mem[m.ip+1]] * m.mem[m.ip+2]
    m.ip += 4 

@instruction(1102)
def _muliip(m):
    """muliip #%d+#%d->(%d)"""
    m.mem[m.mem[m.ip+3]] = m.mem[m.ip+1] * m.mem[m.ip+2]
    m.ip += 4 

@instruction(7)
def _lthppp(m):
    """lthppp (%d)+(%d)->(%d)"""
    m.mem[m.mem[m.ip+3]] = 1 if m.mem[m.mem[m.ip+1]] < m.mem[m.mem[m.ip+2]] else 0
    m.ip += 4 

@instruction(107)
def _lthipp(m):
    """lthipp #%d+(%d)->(%d)"""
    m.mem[m.mem[m.ip+3]] = 1 if m.mem[m.ip+1] < m.mem[m.mem[m.ip+2]] else 0
    m.ip += 4 

@instruction(1007)
def _lthpip(m):
    """lthpip (%d)+#%d->(%d)"""
    m.mem[m.mem[m.ip+3]] = 1 if m.mem[m.mem[m.ip+1]] < m.mem[m.ip+2] else 0
    m.ip += 4 

@instruction(1107)
def _lthiip(m):
    """lthiip #%d+#%d->(%d)"""
    m.mem[m.mem[m.ip+3]] = 1 if m.mem[m.ip+1] < m.mem[m.ip+2] else 0
    m.ip += 4 

@instruction(8)
def _equppp(m):
    """equppp (%d)+(%d)->(%d)"""
    m.mem[m.mem[m.ip+3]] = 1 if m.mem[m.mem[m.ip+1]] == m.mem[m.mem[m.ip+2]] else 0
    m.ip += 4 

@instruction(108)
def _equipp(m):
    """equipp #%d+(%d)->(%d)"""
    m.mem[m.mem[m.ip+3]] = 1 if m.mem[m.ip+1] == m.mem[m.mem[m.ip+2]] else 0
    m.ip += 4 

@instruction(1008)
def _equpip(m):
    """equpip (%d)+#%d->(%d)"""
    m.mem[m.mem[m.ip+3]] = 1 if m.mem[m.mem[m.ip+1]] == m.mem[m.ip+2] else 0
    m.ip += 4 

@instruction(1108)
def _equiip(m):
    """equiip #%d+#%d->(%d)"""
    m.mem[m.mem[m.ip+3]] = 1 if m.mem[m.ip+1] == m.mem[m.ip+2] else 0
    m.ip += 4 

@instruction(5)
def _jmptpp(m):
    """jmptpp if (%d) goto (%d)"""
    if m.mem[m.mem[m.ip+1]] != 0:
        m.ip = m.mem[m.mem[m.ip+2]]
    else:
        m.ip += 3

@instruction(105)
def _jmptip(m):
    """jmptip if #%d goto (%d)"""
    if m.mem[m.ip+1] != 0:
        m.ip = m.mem[m.mem[m.ip+2]]
    else:
        m.ip += 3

@instruction(1005)
def _jmptpi(m):
    """jmptpi if (%d) goto #%d"""
    if m.mem[m.mem[m.ip+1]] != 0:
        m.ip = m.mem[m.ip+2]
    else:
        m.ip += 3

@instruction(1105)
def _jmptii(m):
    """jmptii if #%d goto #%d"""
    if m.mem[m.ip+1] != 0:
        m.ip = m.mem[m.ip+2]
    else:
        m.ip += 3

@instruction(6)
def _jmpfpp(m):
    """jmpfpp if (%d) goto (%d)"""
    if m.mem[m.mem[m.ip+1]] == 0:
        m.ip = m.mem[m.mem[m.ip+2]]
    else:
        m.ip += 3

@instruction(106)
def _jmpfip(m):
    """jmpfip if #%d goto (%d)"""
    if m.mem[m.ip+1] == 0:
        m.ip = m.mem[m.mem[m.ip+2]]
    else:
        m.ip += 3

@instruction(1006)
def _jmpfpi(m):
    """jmpfpi if (%d) goto #%d"""
    if m.mem[m.mem[m.ip+1]] == 0:
        m.ip = m.mem[m.ip+2]
    else:
        m.ip += 3

@instruction(1106)
def _jmpfii(m):
    """jmpfii if #%d goto #%d"""
    if m.mem[m.ip+1] == 0:
        m.ip = m.mem[m.ip+2]
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
    m.mem[m.mem[m.ip+1]] = val
    m.ip += 2

class EOutput(Exception):
    """Output would block."""
    pass

@instruction(4)
def _outptp(m):
    """outptp (%d)"""
    val = m.mem[m.mem[m.ip+1]]
    m.output.append(val)
    m.ip += 2
    m.steps += 1 # exception will skip the step counting
    raise EOutput

@instruction(104)
def _outpti(m):
    """outpti #%d"""
    val = m.mem[m.ip+1]
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

class Machine:
    def __init__(self,mem,input=[],ip=0,debug=False):
        """
        mem : a filename containing a comma-separated memory image
              OR
              an array of intcode integers, will be copied locally
        ip  : initial instruction pointer.
        input : an array of values to pass as input
        debug : when true, all instructions print output.
        """
        if isinstance(mem,str):
            with open(mem, 'r') as memfile:
                content = memfile.read()
            self.mem = [int(x) for x in content.split(',')]
        else:
            self.mem = list(mem)

        self.ip = ip
        self.input = input
        self.output = []
        self.debug = debug
        self.steps = 0

    def step(self):
        """Execute the instruction at the current ip."""
        if self.debug:
            out, offset = self._disone(self.ip)
            print out

        op = _instruction_set[self.mem[self.ip]]
        op(self)
        self.steps += 1

    def run(self):
        """Run until an exception (EQuit, EInput, EOutput)"""
        while True:
            self.step()

    def runq(self):
        """
        Run until quit, not blocking for output.
        Returns number of steps.
        This is how programs ran before Day 7.
        """
        while True:
            try:
                self.step()
            except EQuit:
                return self.steps
            except EOutput:
                pass

    mode_desc = {
        0 : '(%d)',
        1 : '#%d',
        2 : '(%d+b)'
        }

    def _disone(self, loc):
        """
        Disassemble the single instruction at loc.
        Returns the disassembled string and how far to advance in memory.
        """
        try:
            instruction = self.mem[loc]
        except IndexError:
            return('       <out of memory range>',-1)

        out = "%5d: " % loc
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
            v = self.mem[loc + offset]
            args.append(Machine.mode_desc[mode] % v)
            pos *= 10
            offset += 1

        if nargs > inargs:
            # instruction is a memory store
            v = self.mem[loc + offset]
            args.append(Machine.mode_desc[0] % v)
            offset += 1

        out += op.__doc__ % tuple(args)

        return (out,offset)

    def disassemble(self, loc = 0, numinst = -1):
        """
        Dissassemble numinst instructions starting at loc.
        Pass numinst = -1 to disassemble until memory ends.
        """
        while numinst != 0:
            (out, offset) = self._disone(loc)
            print out
            if offset < 0:
                return
            loc += offset
            numinst -= 1

    def dump(self, start = 0, end = None):
        """Memory dump from start address to end address."""
        if end == None:
            end = len(self.mem)
        print ("%5d:" % start),
        m = start
        while m < end:
            print ("%5d" % self.mem[m]),
            m += 1
            if (m % 10 == 0):
                print
                print ("%5d:" % m),
        print

    @opcode(1)
    def _add(self,v1,v2):
        """add %s + %s -> %s"""
        self.ip += 4
        return v1+v2

    @opcode(2)
    def _mul(self,v1,v2):
        """mul %s + %s -> %s"""
        self.ip += 4
        return v1*v2

    class EInput(Exception):
        """Input would block."""
        pass

    @opcode(3)
    def _input(self,v1):
        """input %s"""
        try:
            val = self.input.pop(0)
        except IndexError:
            raise EInput
        self.ip += 2
        return val

    class EOutput(Exception):
        """Output would block."""
        pass

    @opcode(4)
    def _output(self,v1):
        """output %s"""
        self.output.append(v1)
        self.ip += 2
        self.steps += 1 # exception will skip the step counting
        raise EOutput

    @opcode(5)
    def _jmpt(self,v1,v2):
        """jmpt if %s goto %s"""
        if v1:
            self.ip = v2
        else:
            self.ip += 3

    @opcode(6)
    def _jmpf(self,v1,v2):
        """jmpt if not %s goto %s"""
        if not v1:
            self.ip = v2
        else:
            self.ip += 3

    @opcode(7)
    def _lt(self,v1,v2):
        """lt %s < %s -> %s"""
        self.ip += 4
        return 1 if v1 < v2 else 0

    @opcode(8)
    def _eq(self,v1,v2):
        """eq %s == %s -> %s"""
        self.ip += 4
        return 1 if v1 == v2 else 0

    class EQuit(Exception):
        """Intcode machine terminated."""
        pass

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
    steps = machine.runq()
    assert(steps == 2)
    print 'Done in %d steps' % steps

    print 'Memory state:'
    machine.dump(0,12)
    assert(machine.mem[0] == 3500)


    print '==========='
    print ' aoc day 2 '
    print '==========='
    machine = Machine("day2/input.txt")
    machine.mem[1] = 12
    machine.mem[2] = 2
    print 'Disassembly:'
    machine.disassemble()

    print 'Running...'
    steps = machine.runq()
    print 'Done in %d steps' % steps
    assert(steps == 36)
    print 'Part 1 answer:',machine.mem[0]
    assert(machine.mem[0] == 3058646)

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
    assert(machine.mem[4] == 99)

    print 'test 3'
    for x in [0,1]:
        machine = Machine("day5/test3.txt",input=[x])
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
