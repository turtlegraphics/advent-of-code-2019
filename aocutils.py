#
# Advent of Code 2019
# Bryan Clair
#
# Utilities
#
from argparse import ArgumentParser

def parse_args():
    parser = ArgumentParser()
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
    if args.verbose > 2:
        print args

    return args

class Grid:
    """
    A 2d grid of tile objects (probably characters) that can
    be any size.  Coordinates are tuples (x,y).  Will keep track
    of its own dimensions and display the smallest rectangle that
    contains all data.
    """
    def __init__(self):
        self.raster = {}

    def __setitem__(self,p,tile):
        x,y = p

        if self.raster:
            self.xmin = min(self.xmin,x)
            self.xmax = max(self.xmax,x)
            self.ymin = min(self.ymin,y)
            self.ymax = max(self.ymax,y)
        else:
            self.xmin = x
            self.xmax = x
            self.ymin = y
            self.ymax = y

        self.raster[p] = tile

    def __getitem__(self,p):
        return self.raster[p]

    def display(self):
        for y in range(self.ymax,self.ymin-1,-1):
            out = ''
            for x in range(self.xmin,self.xmax + 1):
                if (x,y) in self.raster:
                    out += self.raster[(x,y)]
                else:
                    out += ' '
            print out
