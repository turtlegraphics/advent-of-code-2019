#
# Advent of Code 2019
# Bryan Clair
#
# Day 3
#
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose",
                        action = "count",
                        dest = "verbose",
                        default = 1,
                        help = "Set verbosity level (-v, -vv, -vvv,...)")
    parser.add_argument("-q", "--quiet",
                        action = "store_const",
                        const = 0,
                        dest = "verbose",
                        help = "Suppress output.")
    
    parser.add_argument("-p", "--part",
                        action="store",
                        dest = "part",
                        default = 1,
                        type = int,
                        help = "Which part of the problem to solve (1 or 2)")
    
    parser.add_argument("file",
                        nargs = "?",
                        default = "input.txt",
                        help = "Problem input file (optional).")
                        
    args = parser.parse_args()
    data = open(args.file).readlines()

    assert(len(data)==2)

    grid = {}
    x,y = 0,0

    for inst in data[0].strip().split(','):
        dir = inst[0]
        val = int(inst[1:])
        if dir == 'R':
            while val > 0:
                grid[(x,y)] = True
                x += 1
                val -= 1
        elif dir == 'L':
            while val > 0:
                grid[(x,y)] = True
                x -= 1
                val -= 1
        elif dir == 'U':
            while val > 0:
                grid[(x,y)] = True
                y += 1
                val -= 1
        elif dir == 'D':
            while val > 0:
                grid[(x,y)] = True
                y -= 1
                val -= 1
        else:
            print 'Bad direction'
            break

    print 'wire 1 done'

    (x,y) = (0,0)
    collisions = []
    for inst in data[1].strip().split(','):
        dir = inst[0]
        val = int(inst[1:])
        if dir == 'R':
            while val > 0:
                if (x,y) in grid:
                    collisions.append((x,y))
                x += 1
                val -= 1
        elif dir == 'L':
            while val > 0:
                if (x,y) in grid:
                    collisions.append((x,y))
                x -= 1
                val -= 1
        elif dir == 'U':
            while val > 0:
                if (x,y) in grid:
                    collisions.append((x,y))
                y += 1
                val -= 1
        elif dir == 'D':
            while val > 0:
                if (x,y) in grid:
                    collisions.append((x,y))
                y -= 1
                val -= 1
        else:
            print 'Bad direction'
            break

    print 'wire 2 done'
    assert(collisions[0] == (0,0))
    print min([abs(x)+abs(y) for (x,y) in collisions[1:]])



    
