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

def _inputp(machine):
    """inputp (%d)"""
    mem = machine.mem
    ip = machine.ip
    mem[mem[ip+1]] = machine.input.pop(0)
    machine.ip += 2
_instruction_set[3] = _inputp

def _outptp(machine):
    """outptp (%d)"""
    mem = machine.mem
    ip = machine.ip
    val = mem[mem[ip+1]]
    machine.output.append(val)
    if machine.debug:
        print "OUTPUT",val
    machine.ip += 2
_instruction_set[4] = _outptp

def _outpti(machine):
    """outpti #%d"""
    mem = machine.mem
    ip = machine.ip
    val = mem[ip+1]
    machine.output.append(val)
    if machine.debug:
        print "OUTPUT",val
    machine.ip += 2
_instruction_set[104] = _outpti

class MachineQuit(Exception):
    """Intcode machine terminated."""
    pass

def _mquit(machine):
    """quit"""
    raise MachineQuit
_instruction_set[99] = _mquit

class Machine:
    def __init__(self,mem,ip=0,input=[],debug=False):
        """
        mem : an array of intcode integers, will be copied locally
        ip  : initial instruction pointer.
        input : an array of values to pass as input
        debug : when true, all instructions print output.
        """
        self.mem = list(mem)
        self.ip = ip
        self.input = input
        self.output = []
        self.debug = debug

    def run(self):
        """Execute until quit instruction. Return number of steps executed."""
        steps = 0
        try:
            while True:
                self.step()
                steps += 1
        except MachineQuit:
            return steps

    def step(self):
        """Execute the instruction at the current ip."""
        if self.debug:
            self.disassemble(self.ip)
        op = _instruction_set[self.mem[self.ip]]
        op(self)

    def disassemble(self, loc, numinst = 1):
        """Disassemble numinst instructions of code starting at loc.
        Pass numinst=0 to disassemble until memory ends."""
        while numinst != 0:
            out = "%5d: " % loc
            try:
                opcode = self.mem[loc]
            except IndexError:
                print '<end of memory>'
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
                out += '???? '+str(opcode)
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
    steps = machine.run()
    assert(steps == 2)
    print 'Done in %d steps' % steps

    print 'Memory state:'
    machine.dump(0,12)
    assert(machine.mem[0] == 3500)


    print '==========='
    print ' aoc day 2 '
    print '==========='
    aocday2 = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,6,19,2,19,6,23,1,23,5,27,1,9,27,31,1,31,10,35,2,35,9,39,1,5,39,43,2,43,9,47,1,5,47,51,2,51,13,55,1,55,10,59,1,59,10,63,2,9,63,67,1,67,5,71,2,13,71,75,1,75,10,79,1,79,6,83,2,13,83,87,1,87,6,91,1,6,91,95,1,10,95,99,2,99,6,103,1,103,5,107,2,6,107,111,1,10,111,115,1,115,5,119,2,6,119,123,1,123,5,127,2,127,6,131,1,131,5,135,1,2,135,139,1,139,13,0,99,2,0,14,0]
    aocday2[1] = 12
    aocday2[2] = 2
    machine = Machine(aocday2)
    print 'Disassembly:'
    machine.disassemble(0,-1)

    print 'Running...'
    steps = machine.run()
    assert(steps == 36)
    print 'Done in %d steps' % steps

    assert(machine.mem[0] == 3058646)

    print '==========='
    print ' aoc day 5 '
    print '==========='
    print 'test 1'
    machine = Machine([3,0,4,0,99],input=[1],debug=True)
    machine.run()
    print 'Final output:',machine.output
    assert(len(machine.output) == 1 and machine.output[0] == 1)

    print 'test 2'
    machine = Machine([1002,4,3,4,33],debug=True)
    machine.run()
    assert(machine.mem[4] == 99)

    print 'test 3'
    machine = Machine([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9],
                      input=[0],debug=True)
    machine.run()
    assert(len(machine.output) == 1 and machine.output[0] == 0)
    machine = Machine([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9],
                      input=[1],debug=True)
    machine.run()
    assert(len(machine.output) == 1 and machine.output[0] == 1)

