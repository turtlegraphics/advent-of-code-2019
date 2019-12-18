#
# Advent of Code 2019
# Bryan Clair
#
# Day 18
#
import sys
sys.path.append("..")
import aocutils

args = aocutils.parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

maze = aocutils.Grid()
y = 0
inputlines.reverse()
for line in inputlines:
    for x in range(len(line)):
        if line[x] == '@':
            maze[x,y] = '.'
            start = (x,y)
        else:
            maze[x,y] = line[x]
    y += 1

maze.display()

dirs = [(0,1),(0,-1),(-1,0),(1,0)]

visited = {}
nokeys = ""

unexplored = [(start,nokeys,0)]

def addkey(keys,newkey):
    k = set(list(keys))
    k.add(newkey)
    k = list(k)
    k.sort()
    return ''.join(k)

allkeys = ""
while unexplored:
    pos,keys,steps = unexplored.pop(0)
#    print 'at',pos,'with',keys,'after',steps,'steps'
    if (pos,keys) in visited:
        continue
    visited[pos,keys] = steps
    
    x,y = pos
    for dir in dirs:
        dx,dy = dir
        newpos = x+dx,y+dy
        obj = maze[newpos]
        if obj == '#':
            pass
        elif obj == '.':
            unexplored.append( ( newpos, keys, steps+1 ) )
        elif obj.isupper():
            if obj.lower() in keys:
                unexplored.append( ( newpos, keys, steps+1 ) )
        else:
            assert(obj.islower())
            newkeys = addkey(keys,obj)
            allkeys = addkey(allkeys,obj)
            unexplored.append( (newpos, newkeys, steps+1) )

print 'All keys were',allkeys

minsteps = 1000000
for (pos,keys) in visited:
    if keys == allkeys:
        minsteps = min(minsteps,visited[pos,keys])

print minsteps

