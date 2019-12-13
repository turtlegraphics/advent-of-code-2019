#
# Advent of Code 2019
# Bryan Clair
#
# Day 13
#

#
#  To see this in action, run with the -vv option (verbose x 2)
#  in a terminal that is 22 lines high (and at least 77 wide)
#

import sys
import time
sys.path.append("..")
import aocutils
from intcode import *
from itertools import izip

args = aocutils.parse_args()

class Screen:
    tiles = [' ','#','-','_','o']
    def __init__(self):
        self.raster = {}
        self.xmin = 0
        self.xmax = 0
        self.ymin = 0
        self.ymax = 0
        self.score = 0

    def __setitem__(self,p,tile):
        (x,y) = p
        self.xmin = min(self.xmin,x)
        self.xmax = max(self.xmax,x)
        self.ymin = min(self.ymin,y)
        self.ymax = max(self.ymax,y)

        if val == 3:
            self.paddle = (x,y)
        if tile == 4:
            self.ball = (x,y)

        self.raster[p] = tile

    def __getitem__(self,p):
        return self.raster[p]

    def display(self):
        if args.verbose > 2:
            for y in range(self.ymin,self.ymax + 1):
                for x in range(self.xmin,self.xmax + 1):
                    if (x,y) in self.raster:
                        print Screen.tiles[self.raster[(x,y)]],
                    else:
                        print ' ',
                print
        if args.verbose > 1:
            print 'Score:',self.score

screen = Screen()

def do_output(x,y,val):
    if x == -1:
        screen.score = val
    else:
        screen[(x,y)] = val
    screen.display()

def do_joystick():
    bx,by = screen.ball
    px,py = screen.paddle
    if bx < px:
        return -1
    elif bx > px:
        return 1
    else:
        return 0

game = Machine(args.file)

game[0] = 2 # insert two bits

outparity = 0
while True:
    try:
        game.run()
    except EHalt:
        print 'Final score:',screen.score
        break
    except EOutput:
        outparity += 1
        if outparity == 3:
            outparity = 0
            (x,y,val) = game.output
            do_output(x,y,val)
            game.output.pop()
            game.output.pop()
            game.output.pop()
    except EInput:
        move = do_joystick()
        game.input.append(move)
        if args.verbose > 2:
            time.sleep(0.02)
