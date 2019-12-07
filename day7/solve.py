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

args = aocutils.parse_args()

numamps = 5

with open(args.file, 'r') as memfile:
    content = memfile.read()
    mem = [int(x) for x in content.split(',')]

def amploop(phases):
    amps = [intcode.Machine(mem,[p]) for p in phases]
    
    a = 0
    signal = 0
    while True:
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

for part in [0,1]:
    maxthrust = 0
    for phases in permutations(range(part*5,5+part*5)):
        thrust = amploop(phases)

        if args.verbose > 1:
            print phases,thrust

        if thrust > maxthrust:
            maxthrust = thrust
            maxphases = phases

    print 'part ',part+1,':',maxthrust, maxphases

