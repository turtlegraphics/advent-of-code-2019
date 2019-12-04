#
# intcode machine
#

def _addi(ip,mem):
    """addi (%d)+(%d)->(%d)"""
    mem[mem[ip+3]] = mem[mem[ip+1]] + mem[mem[ip+2]]
    return ip + 4 

def _muli(ip,mem):
    """muli (%d)*(%d)->(%d)"""
    mem[mem[ip+3]] = mem[mem[ip+1]] * mem[mem[ip+2]]
    return ip + 4 

class MachineQuit(Exception):
    """Intcode machine terminated."""
    pass

def _mquit(ip,mem):
    """quit"""
    raise MachineQuit

_instruction_set = {
    1  : _addi,
    2  : _muli,
    99 : _mquit
    }

class Machine:
    def __init__(self,mem,ip=0,debug=False):
        """
        mem : an array of intcode integers, will be copied locally
        ip  : initial instruction pointer.
        debug : when true, all instructions print output.
        """
        self.mem = list(mem)
        self.ip = ip
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
        self.ip = op(self.ip,self.mem)

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
                loc += nargs
                out += doc % tuple(args)
            except KeyError:
                out += '????'
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
