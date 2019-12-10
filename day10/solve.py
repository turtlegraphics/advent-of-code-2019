#
# Advent of Code 2019
# Bryan Clair
#
# Day 10
#
import sys
sys.path.append("..")
import aocutils
from fractions import gcd
import math

args = aocutils.parse_args()

grid = [list(x.strip()) for x in open(args.file).readlines()]

height = len(grid)
width = len(grid[1])

def view(p1,p2):
    """Can p1 see p2?"""
    if (p1 == p2):
        return False

    x1,y1 = p1
    x2,y2 = p2

    dx = x2 - x1
    dy = y2 - y1

    d = gcd(dx,dy)

    if d == 1:
        return True

    for i in range(1,abs(d)):
        (sx,sy) = (x1 + i * dx//abs(d), y1 + i * dy//abs(d))
        if grid[sy][sx] == '#':
            return False

    return True

def countvisible(p1,show=False):
    """How many p2 can p1 see?"""
    x1,y1 = p1
    if show:
        print p1
    count = 0
    for y2 in range(height):
        for x2 in range(width):
            p2 = (x2,y2)
            if grid[y2][x2] == '.':
                if show:
                    print '.',
            else:
                v = view(p1,p2)
                if v:
                    count += 1
                if show:
                    if v:
                        print 'Y',
                    else:
                        print 'N',
        if show:
            print

    return count

#
# Loop over the grid, and for each asteriod count
# the number visible from there.  Track the maximum
# count along the way.
#
counts = {}
maxc = 0
for y in range(height):
    for x in range(width):
        if grid[y][x] == '#':
            c = countvisible((x,y))
            if c > maxc:
                maxc = c
                maxp = (x,y)
            counts[(x,y)] = str(c)
        else:
            counts[(x,y)] = '.'
base = maxp

if args.verbose > 1:
    print('Counts')

    for y in range(height):
        for x in range(width):
            print counts[(x,y)].rjust(3),
        print

print 'Part 1:'
print 'base at',maxp,'sees',maxc

basex, basey = base
grid[basey][basex] = 'X'

# Build a data structure that holds all asteroids (except the base)
# It's a dictionary of (x,y) directions, where x, y are relatively prime
# Each (x,y) direction has a list of asteroids in that direction
targets = {}
for y in range(height):
    for x in range(width):
        if grid[y][x] == '#':
            dx,dy = (x - basex, y - basey)
            d = gcd(dx,dy)
            dirx,diry = dx//abs(d),dy//abs(d)
            if (dirx,diry) in targets:
                targets[(dirx,diry)].append((x,y))
            else:
                targets[(dirx,diry)] = [(x,y)]

# Now arrange that data structure into order
# First, sort each direction by distance from the base:
def dist2(p):
    x,y = p
    return (x-basex)*(x-basex) + (y-basey)*(y-basey)
for dir in targets:
    targets[dir] = sorted(targets[dir], key = dist2, reverse = True)

# Second, sort the directions into targeting order
#    Up is first, then clockwise from there
dirs = list(targets.keys())
def angle(d):
    x,y = d
    return math.atan2(x,y)
dirs = sorted(dirs, key = angle, reverse = True)

# Now start blasting
num = 1    # count the destroyed
twohundred = None
hitsomething = True

while hitsomething:
    hitsomething = False
    # Perform a single rotation
    for dir in dirs:
        if targets[dir]:
            hitsomething = True
            hit = targets[dir].pop()
            if args.verbose > 1:
                print num,hit
            if num == 200:
                twohundred = hit
            num += 1

if twohundred:
    print 'Part 2:'
    print '200th target hit is',twohundred,
    print 'for an answer of',twohundred[0]*100+twohundred[1]
else:
    print 'Part 2:'
    print 'This field has < 200 asteroids'
