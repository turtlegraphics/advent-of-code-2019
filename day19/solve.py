#
# Advent of Code 2019
# Bryan Clair
#
# Day 19
#
import sys
sys.path.append("..")
import aocutils
import intcode

args = aocutils.parse_args()


pulled = 0
start = (1850,2000)
startx,starty = start

def test(x,y):
    drone = intcode.Machine(args.file)
    drone.input.append(x)
    drone.input.append(y)
    drone.runq()
    return drone.output.pop()

def row(y):
    inside = 0
    while test(inside,y) == 0:
        inside = inside + 1 + y//100
        assert(inside < y + 30)

    upperout = y + 30
    upperin = inside

    while upperout - upperin > 1:
        x = (upperout + upperin)//2
        if test(x,y):
            upperin = x
        else:
            upperout = x
            
    lowerout = 0
    lowerin = inside

    while lowerout - lowerin > 1:
        x = (lowerout + lowerin)//2
        if test(x,y):
            lowerin = x
        else:
            lowerout = x

    width = upperout - lowerin
    print '.'*lowerout + '#'*width

pulled = 0

def beam(y):
    x = y // 2
    while test(x,y) == 0:
        x += 1
    leftx = x
    while test(x,y) == 1:
        x += 1
    rightx = x-1
    print 'row',y, 'left = ',leftx,'right = ',rightx,'width = ',rightx - leftx + 1
    return (leftx,rightx)

def fits(y):
    top = beam(y)
    bottom = beam(y+99)
    print 'top right',top[1],'bottom left',bottom[0]
    width = top[1] - bottom[0]
    return width

for y in range(1970,1980):
    print fits(y)
