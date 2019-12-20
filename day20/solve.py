#
# Advent of Code 2019
# Bryan Clair
#
# Day 20
#
import sys
import re
sys.path.append("..")
import aocutils

args = aocutils.parse_args()

dirs = [(0,1),(0,-1),(-1,0),(1,0)]

maze = aocutils.Grid()
y = 0
inputlines = [x.strip('\n') for x in open(args.file).readlines()]
inputlines.reverse()
for line in inputlines:
    for x in range(len(line)):
        maze[x,y] = line[x]
    y += 1


class Gate:
    def __init__(self,name):
        self.name = name
        self.endpoints = []

    def set_end(self,p,updown):
        self.endpoints.append((p,updown))

    def other_end(self,p):
        if self.endpoints[0][0] == p:
            return self.endpoints[1]
        assert(self.endpoints[1][0] == p)
        return self.endpoints[0]

    def __str__(self):
        return '@'

gates = {}

def make_gate(name,x,y,updown):
    if args.verbose > 2:
        print 'gate',name,'at',x,y,
        print 'outer' if updown == -1 else 'innner'
    if name not in gates:
        gates[name] = Gate(name)
    gates[name].set_end((x,y),updown)

y = 0
for line in inputlines:
    # find left gates
    for m in re.finditer('[A-Z][A-Z][#\.]',line):
        x = m.end()-1
        updown = -1 if (x == 2) else 1
        make_gate(m.group(0)[:2],x,y,updown)

    # find right gates
    for m in re.finditer('[#\.][A-Z][A-Z]',line):
        x = m.start()
        updown = -1 if (x == maze.xmax-2) else 1
        make_gate(m.group(0)[1:],x,y,updown)

    # find bottom gates
    for m in re.finditer(' [A-Z](?= )',line):
        try:
            x = m.end()-1
            assert(inputlines[y+1][x].isupper() and inputlines[y+2][x] == '.')
            name = inputlines[y+1][x] + m.group(0)[1]
        except (IndexError, AssertionError):
            continue
        updown = -1 if y == 0 else 1
        make_gate(name,x,y+2,updown)

    # find top gates
    for m in re.finditer(' [A-Z](?= )',line):
        try:
            x = m.end()-1
            assert(inputlines[y-1][x].isupper() and inputlines[y-2][x] == '.')
            name = m.group(0)[1] + inputlines[y-1][x]
        except (IndexError, AssertionError):
            continue
        updown = -1 if y == maze.ymax else 1
        make_gate(name,x,y-2,updown)

    y += 1

for g in gates:
    for pos,updown in gates[g].endpoints:
        x,y = pos
        maze[x,y] = gates[g]
    if args.verbose > 2:
        print 'gate',gates[g].name,gates[g].endpoints

if args.verbose > 1:
    maze.display()


visited = {}
unexplored = [(gates['AA'].endpoints[0][0],0,0)]
while unexplored:
    pos,level,steps = unexplored.pop(0)
    if (pos,level) in visited:
        continue
    visited[(pos,level)] = steps
    
    x,y = pos
    for dir in dirs:
        dx,dy = dir
        newpos = x+dx,y+dy
        obj = maze[newpos]
        if obj == '#':
            pass
        elif obj == '.' or isinstance(obj,Gate):
            unexplored.append( ( newpos, level, steps+1 ) )
        elif obj.isupper():
            g = maze[pos]
            assert(isinstance(g,Gate))

            if g.name == 'ZZ':
                if level == 0:
                    print 'Found it in',steps,'steps.'
                    sys.exit()
                continue
            if g.name == 'AA':
                continue
            newpos,updown = g.other_end(pos)
            unexplored.append( ( newpos, level, steps+1 ) )
            
