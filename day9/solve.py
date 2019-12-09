#
# Advent of Code 2019
# Bryan Clair
#
# Day 9
#
import sys
sys.path.append("..")
import aocutils
import intcode
from itertools import permutations

args = aocutils.parse_args()

with open(args.file, 'r') as memfile:
    content = memfile.read()
    mem = [int(x) for x in content.split(',')]

BOOST = intcode.Machine(mem + [0]*1000,input=[1])
BOOST.runq()
print BOOST.output

BOOST = intcode.Machine(mem + [0]*1000,input=[2])
BOOST.runq()
print BOOST.output
