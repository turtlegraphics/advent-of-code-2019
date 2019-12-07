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

numamps = 5
args = aocutils.parse_args()

with open(args.file, 'r') as memfile:
    content = memfile.read()
    mem = [int(x) for x in content.split(',')]

def find_signal(phases):
    input = 0
    for i in range(numamps):
        amp = intcode.Machine(mem,input = [phases[i],input])
        amp.run()
        input = amp.output[0]
    return input

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

maxthrust = 0
for i in range(5**numamps):
    phases = numberToBase(i,5)
    while len(phases) < numamps:
        phases.insert(0,0)
    if len(set(phases)) < 5:
        continue

    thrust = find_signal(phases)
    print phases,thrust
    if thrust > maxthrust:
        maxthrust = thrust
        print 'new max',maxthrust

print maxthrust

