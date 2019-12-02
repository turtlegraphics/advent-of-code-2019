#
# Advent of Code 2019
# Bryan Clair
#
# Day 2
#
import argparse

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


