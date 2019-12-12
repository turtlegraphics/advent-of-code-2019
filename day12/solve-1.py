#
# Advent of Code 2019
# Bryan Clair
#
# Day 12
#
import sys
sys.path.append("..")
import aocutils

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

print moonp
print moonv

n = len(moonp)

def dump():
    for i in range(n):
        print 'Moon',i,':',
        for d in dim:
            print d,'=',moonp[i][d],
        print 'pot:',pot[i],'kin:',kin[i]

def step():
    for i in range(n):
        for j in range(n):
            for d in dim:
                if moonp[i][d] > moonp[j][d]:
                    moonv[i][d] -= 1
                elif moonp[i][d] < moonp[j][d]:
                    moonv[i][d] += 1
    for i in range(n):
        for d in dim:
            moonp[i][d] += moonv[i][d]
        pot[i] = sum([abs(moonp[i][d]) for d in dim])
        kin[i] = sum([abs(moonv[i][d]) for d in dim])


for s in range(1000):
    step()
    if args.verbose > 1:
        print
        print '-'*10
        print 'step',s+1
        print '-'*10
        dump()

        print 'energy',sum([pot[i]*kin[i] for i in range(n)])

print 'energy',sum([pot[i]*kin[i] for i in range(n)])

