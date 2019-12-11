#
# Advent of Code 2019
# Bryan Clair
#
# Day 11
#
import sys
sys.path.append("..")
import aocutils
from intcode import *

args = aocutils.parse_args()

class Robot:
    turns = [{(0,1) : (-1,0),(-1,0) : (0,-1),(0,-1) : (1,0),(1,0) : (0,1)},
             {(0,1) : (1,0),(1,0) : (0,-1),(0,-1) : (-1,0),(-1,0) : (0,1)}]

    def __init__(self):
        self.brain = Machine(args.file)
        self.position = (0,0)
        self.direction = (0,1)

    def paint(self,panels):
        try:
            while True:
                self.step(panels)
        except EHalt:
            pass
        
    def step(self,panels):
        self.brain.input.append(panels[self.position])

        # paint
        try:
            self.brain.run()
        except EOutput:
            color = self.brain.output.pop()
            panels[self.position] = color
            if args.verbose > 1:
                print 'painting',self.position,'color',color

        # turn
        try:
            self.brain.run()
        except EOutput:
            dir = self.brain.output.pop()
            self.direction = Robot.turns[dir][self.direction]
        
        # move
        (dx,dy) = self.direction
        (x,y) = self.position
        self.position = (x + dx, y + dy)
        if self.position not in panels:
            panels[self.position] = 0

class Hull:
    def __init__(self, startcolor):
        self.panels = {(0,0) : startcolor}
        
    def paint(self):
        robot = Robot()
        robot.paint(self.panels)

    def display(self):
        maxx = max([x for (x,y) in self.panels])
        minx = min([x for (x,y) in self.panels])
        maxy = max([y for (x,y) in self.panels])
        miny = min([y for (x,y) in self.panels])

        for y in range(maxy,miny-1,-1):
            for x in range(minx,maxx+1):
                try:
                    if self.panels[(x,y)] == 1:
                        print '#',
                    else:
                        print '.',
                except KeyError:
                    print ' ',
            print

print "Part 1:"
hull = Hull(0)
hull.paint()
print len(hull.panels)

print "Part 2:"
hull = Hull(1)
hull.paint()
hull.display()
