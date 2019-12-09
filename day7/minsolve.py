import sys
sys.path.append("..")
import intcode
from itertools import permutations

mem = [int(x) for x in open('input.txt').read().split(',')]

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
    print max([amploop(phases) for phases in permutations(range(part*5,5+part*5))])

