#
# Advent of Code 2019
# Bryan Clair
#
# Day 16
#

# Slow version not using numpy, but maybe easier to use for part 2

import sys
sys.path.append("..")
import aocutils

args = aocutils.parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

for line in inputlines:
    signal = [int(x) for x in list(line)]

print(signal)


mask_base = [0,1,0,-1]

def mask(stage,index):
    return mask_base[(index + 1)//(stage + 1) % 4]

def fft(signal):
    v = list(signal)
    for stage in range(len(signal)):
        dot = 0
        for index in range(len(signal)):
            dot += signal[index]*mask(stage,index)
        v[stage] = abs(dot) % 10
    return v

for i in range(100):
    signal = fft(signal)

print signal
