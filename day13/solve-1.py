#
# Advent of Code 2019
# Bryan Clair
#
# Day --
#
import sys
sys.path.append("..")
import aocutils
import intcode
from itertools import izip

args = aocutils.parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

arcade = intcode.Machine(args.file)

arcade.runq()

out = arcade.output

screen = {}
for x,y,tile in izip(*[iter(out)]*3):
    screen[(x,y)] = tile

print 'Part 1'
print screen.values().count(2)

