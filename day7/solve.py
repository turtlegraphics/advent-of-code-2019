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

args = aocutils.parse_args()

numamps = 5

with open(args.file, 'r') as memfile:
    content = memfile.read()
    mem = [int(x) for x in content.split(',')]

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

def amploop(phases):
    amps = []
    for p in phases:
        amps.append(intcode.Machine(mem,[p]))
    
    a = 0
    signal = 0
    for i in range(100):
        amps[a].input.append(signal)
        if args.verbose > 2:
            print 'running',a,'with input',amps[a].input
        try:
            amps[a].run()
        except intcode.EOutput:
            signal = amps[a].output.pop()
        except intcode.EQuit:
            return signal
        a = (a + 1) % numamps
        if args.verbose > 2:
            if a == 0:
                print 'thrust',signal

maxthrust = 0
for i in range(5**numamps):
    phases = numberToBase(i,5)
    while len(phases) < numamps:
        phases.insert(0,0)
    if len(set(phases)) < 5:
        continue
    phases = [x+5 for x in phases]
    thrust = amploop(phases)

    if args.verbose > 1:
        print phases,thrust

    if thrust > maxthrust:
        maxthrust = thrust

print maxthrust

