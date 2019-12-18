#
# Advent of Code 2019
# Bryan Clair
#
# Day 18
#
import sys
import bisect
sys.path.append("..")
import aocutils

args = aocutils.parse_args()


def addkey(keys,newkey):
    k = set(list(keys))
    k.add(newkey)
    k = list(k)
    k.sort()
    return ''.join(k)

dirs = [(0,1),(0,-1),(-1,0),(1,0)]
def opposite(dir):
    dx,dy = dir
    return (-dx,-dy)

inputlines = [x.strip() for x in open(args.file).readlines()]
inputlines.reverse()

maze = aocutils.Grid()
starts = []
allkeys = ""

y = 0
for line in inputlines:
    for x in range(len(line)):
        if line[x] == '@':
            maze[x,y] = '.'
            starts.append((x,y))
        else:
            if line[x].islower():
                allkeys = addkey(allkeys,line[x])
            maze[x,y] = line[x]
    y += 1


numbots = len(starts)

maze.display()
print numbots,'robots starting at',starts
print 'seeking:',allkeys

def find_full_move(x,y,dir):
    """
    Move the bot at position x,y in direction dir and then
    continue down that path until a decision is reached.
    Returns final position of bot and number of steps taken.
    """
    steps = 0

    while True:
        dx, dy = dir
        newx,newy = x+dx,y+dy
        if maze[newx,newy] != '.':
            return (x,y,steps)
        x,y = newx,newy
        steps += 1
        gooddir = None
        gooddirct = 0
        # find a good direction
        for d in dirs:
            if d != opposite(dir):
                tdx,tdy = d
                tx,ty = x+tdx,y+tdy
                obj = maze[tx,ty]
                if obj == '.':
                    gooddir = d
                    gooddirct += 1
                elif obj != '#':
                    # decision point (key or door)
                    return (x,y,steps)
        if gooddirct != 1:
            # can't decide here
            return (x,y,steps)
        # move in the unique gooddir
        dir = gooddir

visited = {}
nokeys = ""
unexplored = [(0,0,nokeys,tuple(starts))]
topstep = 0
curkeys = ""

while unexplored:
    numkeys,steps,keys,pos = unexplored.pop(0)
    if steps > topstep or keys != curkeys:
        if args.verbose > 1:
            print 'steps:',steps,'keys=',keys,'unexplored:',len(unexplored)
        topstep = steps
        curkeys = keys

#    print 'at',pos,'with',keys,'after',steps,'steps'
    if (pos,keys) in visited:
        continue
    visited[pos,keys] = steps
    
    for bot in range(numbots):
        x,y = pos[bot]
        for dir in dirs:
            dx,dy = dir
            newx,newy = x+dx,y+dy
            obj = maze[newx,newy]

            if obj == '.':
                (newx,newy,stepstaken) = find_full_move(x,y,dir)
                plist = list(pos)
                plist[bot] = (newx,newy)
                newpos = tuple(plist)
                bisect.insort(unexplored,(len(keys),steps+stepstaken, keys, newpos))
                continue

            if obj == '#':
                continue

            plist = list(pos)
            plist[bot] = (newx,newy)
            newpos = tuple(plist)

            if obj.isupper():
                if obj.lower() in keys:
                    bisect.insort(unexplored,(len(keys),steps+1, keys, newpos))
            else:
                assert(obj.islower())
                newkeys = addkey(keys,obj)
                if newkeys == allkeys:
                    print 'found all keys in',steps+1,'steps'
                    sys.exit()
                bisect.insort(unexplored,(len(keys),steps+1, newkeys, newpos))

minsteps = 1000000
for (pos,keys) in visited:
    if keys == allkeys:
        minsteps = min(minsteps,visited[pos,keys])

print minsteps

