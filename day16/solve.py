#
# Advent of Code 2019
# Bryan Clair
#
# Day 16
#
import sys
sys.path.append("..")
import aocutils
from fractions import gcd

args = aocutils.parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

for line in inputlines:
    signal = [int(x) for x in list(line)]

print(signal)
siglen = len(signal)
print('signal length',siglen)

mask_base = [0,1,0,-1]

def mask(stage,index):
    return mask_base[(index + 1)//(stage + 1) % 4]

def lcm(a,b):
    return a * b // gcd(a,b)

def fft_slow(row,width):
    sum = 0
    for i in range(width):
        sum += signal[i % siglen]*mask(row,i)
    return sum

def fft(row,width):
    period = lcm(siglen, 4*(row+1))
    # print 'period',period
    psum = 0
    for i in range(period):
        psum += signal[i % siglen]*mask(row,i)

    # print 'period sum',psum
    sum = psum * (width // period)
    for i in range(width % period):
        sum += signal[i % siglen]*mask(row,i)

    return sum

for row in range(400):
    print 'row',row,'period',lcm(siglen, 4*(row+1))
    for width in range(400):
        assert(fft(row,width) == fft_slow(row,width))
    print


    
