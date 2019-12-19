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

def find_all_moves(pos,keys,bot):
    """
    Return all moves a bot starting at pos can make
    (assuming the bots collective hold keys)
    that result in getting a new key.
    """
    moves = []
    visited = {}
    unexplored = [(pos,0)]
    steps = 0
    while unexplored:
        pos,steps = unexplored.pop(0)
        if pos in visited:
            continue
        if args.verbose > 2:
            print 'fam: bot',bot,'visited',pos,'after',steps,'steps'
        visited[pos] = steps
        x,y = pos
        steps += 1
        for dir in dirs:
            dx,dy = dir
            pos = x+dx,y+dy
            obj = maze[pos]
            if obj == '#':
                pass
            elif obj == '.':
                unexplored.append((pos,steps))
            elif obj.isupper():
                 if obj.lower() in keys:
                     unexplored.append((pos,steps))
            else:
                assert(obj.islower())
                if obj in keys:
                    unexplored.append((pos,steps))
                else:
                    moves.append((pos,steps,obj))
    return moves

def BFS():
    visited = {}
    unexplored = [ (0,'',tuple(starts)) ]

    topsteps = 0
    mostkeys = 0

    while unexplored:
        steps,keys,pos = unexplored.pop(0)
        visited[(pos,keys)] = steps
        if steps > topsteps or len(keys) > mostkeys:
            print 'steps:',steps,'unexplored:',len(unexplored),'with:',keys
            topsteps = steps
            mostkeys = len(keys)
            if mostkeys == len(allkeys):
                print 'Found all keys in',steps,'steps.'
                sys.exit()

        moves = []
        for bot in range(numbots):
            moves.append(find_all_moves(pos[bot],keys,bot))

        for bot in range(numbots):
            for move in moves[bot]:
                botpos,distance,newkey = move
                newpos = list(pos)
                newpos[bot] = botpos
                newkeys = addkey(keys,newkey)
                bisect.insort(unexplored,(steps+distance,newkeys,tuple(newpos)))

def DFS(pos,keys):
    """
    Figure out the best way to get all keys from
    the current state (keys,pos).
    Returns the number of steps it takes, or None if impossible.
    """
    print 'keys:',keys,pos
    moves = []
    for bot in range(numbots):
        moves.append(find_all_moves(pos[bot],keys,bot))

    found = False
    for bot in range(numbots):
        for move in moves[bot]:
            botpos,distance,newkey = move
            newpos = list(pos)
            newpos[bot] = botpos
            newkeys = addkey(keys,newkey)
            steps = DFS(newpos,newkeys)
            if not found:
                found = True
                minsteps = steps
            else:
                minsteps = min(steps,minsteps)

    return minsteps if found else None

print 'Found all keys in ',DFS(starts,'')
#BFS()
