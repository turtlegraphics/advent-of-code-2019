#
# Advent of Code 2019
# Bryan Clair
#
# Day 1
#
import argparse

def mass(line):
    val = int(line)
    return val/3 - 2

def mass2(line):
    val = int(line)
    v =  val/3 - 2
    if (v > 0):
        return v + mass2(v)
    else:
        return 0

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

    sum = 0
    for line in data:
        sum += mass(line)
    print 'part 1:',sum

    sum = 0
    for line in data:
        sum += mass2(line)
    print 'part 2:',sum
