#
# Advent of Code 2019
# Bryan Clair
#
# Day 12
#
import sys
sys.path.append("..")
import aocutils
from fractions import gcd

args = aocutils.parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

dim = ['x','y','z']

moonp = []
moonv = []
pot = []
kin = []

for line in inputlines:
    moon = {}
    line = line.strip('<').strip('>')
    for ass in line.split(','):
        var,val = ass.strip().split('=')
        moon[var] = int(val)
    moonp.append(moon)
    moonv.append({'x':0, 'y':0, 'z':0})
    pot.append(0)
    kin.append(0)

n = len(moonp)

def dump():
    for i in range(n):
        print 'Moon',i,':',
        for d in dim:
            print d,'=',moonp[i][d],
        print 'pot:',pot[i],'kin:',kin[i]

def dimstep(d):
    for i in range(n):
        for j in range(n):
            if moonp[i][d] > moonp[j][d]:
                moonv[i][d] -= 1
            elif moonp[i][d] < moonp[j][d]:
                moonv[i][d] += 1
    for i in range(n):
        moonp[i][d] += moonv[i][d]


def lcm(v):
    """Find lcm of a list of numbers."""
    l = 1
    for x in v:
        l = l*x//gcd(l,x)
    return l

periods = {}
for d in dim:
    print 'working dimension',d
    step = 0
    seen = {}
    while True:
        pos = tuple([moonp[i][d] for i in range(n)] +
                    [moonv[i][d] for i in range(n)])
        if pos in seen:
            print 'Found!'
            print 'first seen step',seen[pos]
            print 'currently step',step
            periods[d] = step - seen[pos]
            break
        else:
            seen[pos] = step
        dimstep(d)
        step += 1
        if step % 10000 == 0:
            print step

print periods

print 'Solution:'
print lcm([periods[p] for p in periods])
