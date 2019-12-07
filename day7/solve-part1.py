#
# Advent of Code 2019
# Bryan Clair
#
# Day 7
#
import sys
sys.path.append("..")
import aocutils
import intcode
from itertools import permutations

numamps = 5
args = aocutils.parse_args()

with open(args.file, 'r') as memfile:
    content = memfile.read()
    mem = [int(x) for x in content.split(',')]

def find_signal(phases):
    input = 0
    for i in range(numamps):
        amp = intcode.Machine(mem,input = [phases[i],input])
        amp.runq()
        input = amp.output[0]
    return input

maxthrust = 0
for phases in permutations(range(numamps)):
    thrust = find_signal(phases)
    if args.verbose > 1:
        print phases,thrust

    if thrust > maxthrust:
        maxthrust = thrust

print maxthrust

