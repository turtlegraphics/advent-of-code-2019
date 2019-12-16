#
# Advent of Code 2019
# Bryan Clair
#
# Day 16
#
import sys
sys.path.append("..")
import aocutils
import numpy as np

args = aocutils.parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

for line in inputlines:
    signal = np.array([int(x) for x in list(line)],dtype=np.int64)

print(signal)


mask_base = [0,1,0,-1]

def mask(stage,index):
    return mask_base[(index + 1)//(stage + 1) % 4]

fft = np.fromfunction(np.vectorize(mask),
                         shape = (len(signal),len(signal)),
                         dtype=np.int64)
print(fft)

for i in range(100):
    signal = abs(np.dot(fft,signal)) % 10
    
print(signal)
