#
# Advent of Code 2019
# Bryan Clair
#
# Day 2 (redux, using Intcode module)
#
import sys
sys.path.append("..")
import aocutils
import intcode

args = aocutils.parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

mem = []
for line in inputlines:
    mem.extend([int(x) for x in line.split(',')])

# part 1
machine = intcode.Machine(mem)
machine.mem[1] = 12
machine.mem[2] = 2
machine.runq()
print 'part 1:'
print machine.mem[0]

# part 2
print 'part 2:'
for noun in range(100):
    for verb in range(100):
        machine = intcode.Machine(mem)
        machine.mem[1] = noun
        machine.mem[2] = verb
        machine.runq()
        if machine.mem[0] == 19690720:
            print noun, verb, 100*noun + verb
            break


