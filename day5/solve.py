#
# Advent of Code 2019
# Bryan Clair
#
# Day 5
#
import sys
sys.path.append("..")
import aocutils
import intcode

args = aocutils.parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

mem = []
for line in inputlines:
    mem.extend([int(x) for x in line.split(',')])

# part 1
print "Part 1"
machine = intcode.Machine(mem,input=[1])
machine.run()
print machine.output

print "Part 2"
machine = intcode.Machine(mem,input=[5],debug=True)
machine.run()
print machine.output
