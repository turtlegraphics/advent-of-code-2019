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

with open(args.file, 'r') as memfile:
    content = memfile.read()
    mem = [int(x) for x in content.split(',')]

def amploop(phases):
    amps = [intcode.Machine(mem,[p]) for p in phases]
    
    a = 0
    signal = 0
    while True:
        amps[a].input.append(signal)
        try:
            amps[a].run()
        except intcode.EOutput:
            signal = amps[a].output.pop()
        except intcode.EHalt:
            return signal
        a = (a + 1) % len(amps)

for part in [0,1]:
    maxthrust = 0
    for phases in permutations(range(part*5,5+part*5)):
        thrust = amploop(phases)
        if thrust > maxthrust:
            maxthrust, maxphases = thrust, phases

    print 'part ',part+1,':',maxthrust, maxphases

