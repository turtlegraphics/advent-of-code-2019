#
# intcode machine
#

_instruction_set = {}

def _addppp(machine):
    """addppp (%d)+(%d)->(%d)"""
    mem = machine.mem
    ip = machine.ip
    mem[mem[ip+3]] = mem[mem[ip+1]] + mem[mem[ip+2]]
    machine.ip += 4 
_instruction_set[1] = _addppp

def _addipp(machine):
    """addipp #%d+(%d)->(%d)"""
    mem = machine.mem
    ip = machine.ip
    mem[mem[ip+3]] = mem[ip+1] + mem[mem[ip+2]]
    machine.ip += 4 
_instruction_set[101] = _addipp

def _addpip(machine):
    """addpip (%d)+#%d->(%d)"""
    mem = machine.mem
    ip = machine.ip
    mem[mem[ip+3]] = mem[mem[ip+1]] + mem[ip+2]
    machine.ip += 4 
_instruction_set[1001] = _addpip

def _addiip(machine):
    """addiip #%d+#%d->(%d)"""
    mem = machine.mem
    ip = machine.ip
    mem[mem[ip+3]] = mem[ip+1] + mem[ip+2]
    machine.ip += 4 
_instruction_set[1101] = _addiip

def _mulppp(machine):
    """mulppp (%d)+(%d)->(%d)"""
    mem = machine.mem
    ip = machine.ip
    mem[mem[ip+3]] = mem[mem[ip+1]] * mem[mem[ip+2]]
    machine.ip += 4 
_instruction_set[2] = _mulppp

def _mulipp(machine):
    """mulipp #%d+(%d)->(%d)"""
    mem = machine.mem
    ip = machine.ip
    mem[mem[ip+3]] = mem[ip+1] * mem[mem[ip+2]]
    machine.ip += 4 
_instruction_set[102] = _mulipp

def _mulpip(machine):
    """mulpip (%d)+#%d->(%d)"""
    mem = machine.mem
    ip = machine.ip
    mem[mem[ip+3]] = mem[mem[ip+1]] * mem[ip+2]
    machine.ip += 4 
_instruction_set[1002] = _mulpip

def _muliip(machine):
    """muliip #%d+#%d->(%d)"""
    mem = machine.mem
    ip = machine.ip
    mem[mem[ip+3]] = mem[ip+1] * mem[ip+2]
    machine.ip += 4 
_instruction_set[1102] = _muliip

def _lthppp(machine):
    """lthppp (%d)+(%d)->(%d)"""
    mem = machine.mem
    ip = machine.ip
    mem[mem[ip+3]] = 1 if mem[mem[ip+1]] < mem[mem[ip+2]] else 0
    machine.ip += 4 
_instruction_set[7] = _lthppp

def _lthipp(machine):
    """lthipp #%d+(%d)->(%d)"""
    mem = machine.mem
    ip = machine.ip
    mem[mem[ip+3]] = 1 if mem[ip+1] < mem[mem[ip+2]] else 0
    machine.ip += 4 
_instruction_set[107] = _lthipp

def _lthpip(machine):
    """lthpip (%d)+#%d->(%d)"""
    mem = machine.mem
    ip = machine.ip
    mem[mem[ip+3]] = 1 if mem[mem[ip+1]] < mem[ip+2] else 0
    machine.ip += 4 
_instruction_set[1007] = _lthpip

def _lthiip(machine):
    """lthiip #%d+#%d->(%d)"""
    mem = machine.mem
    ip = machine.ip
    mem[mem[ip+3]] = 1 if mem[ip+1] < mem[ip+2] else 0
    machine.ip += 4 
_instruction_set[1107] = _lthiip

def _equppp(machine):
    """equppp (%d)+(%d)->(%d)"""
    mem = machine.mem
    ip = machine.ip
    mem[mem[ip+3]] = 1 if mem[mem[ip+1]] == mem[mem[ip+2]] else 0
    machine.ip += 4 
_instruction_set[8] = _equppp

def _equipp(machine):
    """equipp #%d+(%d)->(%d)"""
    mem = machine.mem
    ip = machine.ip
    mem[mem[ip+3]] = 1 if mem[ip+1] == mem[mem[ip+2]] else 0
    machine.ip += 4 
_instruction_set[108] = _equipp

def _equpip(machine):
    """equpip (%d)+#%d->(%d)"""
    mem = machine.mem
    ip = machine.ip
    mem[mem[ip+3]] = 1 if mem[mem[ip+1]] == mem[ip+2] else 0
    machine.ip += 4 
_instruction_set[1008] = _equpip

def _equiip(machine):
    """equiip #%d+#%d->(%d)"""
    mem = machine.mem
    ip = machine.ip
    mem[mem[ip+3]] = 1 if mem[ip+1] == mem[ip+2] else 0
    machine.ip += 4 
_instruction_set[1108] = _equiip

def _jmptpp(machine):
    """jmptpp if (%d) goto (%d)"""
    mem = machine.mem
    ip = machine.ip
    if mem[mem[ip+1]] != 0:
        machine.ip = mem[mem[ip+2]]
    else:
        machine.ip += 3
_instruction_set[5] = _jmptpp

def _jmptip(machine):
    """jmptip if #%d goto (%d)"""
    mem = machine.mem
    ip = machine.ip
    if mem[ip+1] != 0:
        machine.ip = mem[mem[ip+2]]
    else:
        machine.ip += 3
_instruction_set[105] = _jmptip

def _jmptpi(machine):
    """jmptpi if (%d) goto #%d"""
    mem = machine.mem
    ip = machine.ip
    if mem[mem[ip+1]] != 0:
        machine.ip = mem[ip+2]
    else:
        machine.ip += 3
_instruction_set[1005] = _jmptpi

def _jmptii(machine):
    """jmptii if #%d goto #%d"""
    mem = machine.mem
    ip = machine.ip
    if mem[ip+1] != 0:
        machine.ip = mem[ip+2]
    else:
        machine.ip += 3
_instruction_set[1105] = _jmptii

def _jmpfpp(machine):
    """jmpfpp if (%d) goto (%d)"""
    mem = machine.mem
    ip = machine.ip
    if mem[mem[ip+1]] == 0:
        machine.ip = mem[mem[ip+2]]
    else:
        machine.ip += 3
_instruction_set[6] = _jmpfpp

def _jmpfip(machine):
    """jmpfip if #%d goto (%d)"""
    mem = machine.mem
    ip = machine.ip
    if mem[ip+1] == 0:
        machine.ip = mem[mem[ip+2]]
    else:
        machine.ip += 3
_instruction_set[106] = _jmpfip

def _jmpfpi(machine):
    """jmpfpi if (%d) goto #%d"""
    mem = machine.mem
    ip = machine.ip
    if mem[mem[ip+1]] == 0:
        machine.ip = mem[ip+2]
    else:
        machine.ip += 3
_instruction_set[1006] = _jmpfpi

def _jmpfii(machine):
    """jmpfii if #%d goto #%d"""
    mem = machine.mem
    ip = machine.ip
    if mem[ip+1] == 0:
        machine.ip = mem[ip+2]
    else:
        machine.ip += 3
_instruction_set[1106] = _jmpfii

class EInput(Exception):
    """Input would block."""
    pass

def _inputp(machine):
    """inputp (%d)"""
    mem = machine.mem
    ip = machine.ip
    try:
        val = machine.input.pop(0)
    except IndexError:
        raise EInput
    mem[mem[ip+1]] = val
    machine.ip += 2
_instruction_set[3] = _inputp

class EOutput(Exception):
    """Output would block."""
    pass

def _outptp(machine):
    """outptp (%d)"""
    mem = machine.mem
    ip = machine.ip
    val = mem[mem[ip+1]]
    machine.output.append(val)
    machine.ip += 2
    machine.steps += 1 # exception will skip the step counting
    raise EOutput

_instruction_set[4] = _outptp

def _outpti(machine):
    """outpti #%d"""
    mem = machine.mem
    ip = machine.ip
    val = mem[ip+1]
    machine.output.append(val)
    machine.ip += 2
    machine.steps += 1 # exception will skip the step counting
    raise EOutput
_instruction_set[104] = _outpti

class EQuit(Exception):
    """Intcode machine terminated."""
    pass

def _mquit(machine):
    """quit"""
    raise EQuit
_instruction_set[99] = _mquit

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
            self.disassemble(self.ip)
        op = _instruction_set[self.mem[self.ip]]
        op(self)
        self.steps += 1

    def run(self):
        """Run until an exception (EQuit, EInput, EOutput)"""
        while True:
            self.step()

    def runq(self):
        """Run until quit, not blocking for output.
        Returns number of steps.
        This is how programs ran before Day 7."""
        while True:
            try:
                self.step()
            except EQuit:
                return self.steps
            except EOutput:
                pass

    def disassemble(self, loc, numinst = 1):
        """Disassemble numinst instructions of code starting at loc.
        Pass numinst=0 to disassemble until memory ends."""
        while numinst != 0:
            out = "%5d: " % loc
            try:
                opcode = self.mem[loc]
            except IndexError:
                print '       <end of memory>'
                return

            loc += 1
            numinst -= 1
            try:
                doc = _instruction_set[opcode].__doc__
                nargs = doc.count('%d')
                args = self.mem[loc:loc+nargs]
                out += doc % tuple(args)
                loc += nargs
            except (KeyError,TypeError):
                out += '????   '+str(opcode)
            print out

    def dump(self, start, end):
        print ("%5d:" % start),
        m = start
        while m < end:
            print ("%5d" % self.mem[m]),
            m += 1
            if (m % 10 == 0):
                print
                print ("%5d:" % m),
        print

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
    machine.dump(0,12)

    print 'Disassembly:'
    machine.disassemble(0,10)

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
    machine.disassemble(0,-1)

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
            machine.disassemble(0,1000)
        machine.runq()
        assert(machine.output == [outputs[i]])
    print '    PASSED'

    print 'Part 2 answer:'
    machine = Machine("day5/input.txt",input=[5])
    machine.runq()
    print '    Diagnostic code:',machine.output[0]
    assert(machine.output == [15724522])
