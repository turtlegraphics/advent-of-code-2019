#
# intcode machine
#
    
instruction_set[1] = {
    'execute' : lambda 
        
class Intcode:
    def __init__(self,state):
        self.mem = list(state)
        self.ip = 0

    def step(self):
        self.ip = instruction_set[self.mem[self.ip]](self.mem,self.ip)

    def disassemble(self, loc):
        """Return a string representing the instruction at the
        memory location given by loc."""
        instruction_set[self.mem[loc]].

    def addi(mem,ip):
        mem[mem[ip+3]] = mem[mem[ip+1]] + mem[mem[ip+2]]
    
    
        
def value(mem,noun,verb):
    mem[1] = noun
    mem[2] = verb
    ip = 0
    while True:
        if mem[ip] == 99:
            break
        if mem[ip] == 1:
            mem[mem[ip+3]] = mem[mem[ip+1]] + mem[mem[ip+2]]
        elif mem[ip] == 2:
            mem[mem[ip+3]] = mem[mem[ip+1]] * mem[mem[ip+2]]
        else:
            print 'error at ip=',ip,'(noun,verb)=',noun,verb
            break
        ip += 4
    return mem[0]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose",
                        action = "count",
                        dest = "verbose",
                        default = 1,
                        help = "Set verbosity level (-v, -vv, -vvv,...)")
    parser.add_argument("-q", "--quiet",
                        action = "store_const",
                        const = 0,
                        dest = "verbose",
                        help = "Suppress output.")
    
    parser.add_argument("-p", "--part",
                        action="store",
                        dest = "part",
                        default = 1,
                        type = int,
                        help = "Which part of the problem to solve (1 or 2)")
    
    parser.add_argument("file",
                        nargs = "?",
                        default = "input.txt",
                        help = "Problem input file (optional).")
                        
    args = parser.parse_args()

    data = open(args.file).readlines()

    mem = []
    for line in data:
        mem.extend([int(x) for x in line.split(',')])

    for noun in range(100):
        for verb in range(100):
            if value(mem[:],noun,verb) == 19690720:
                print noun, verb, 100*noun + verb


