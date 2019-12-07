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

# part 1
print "Part 1"
machine = intcode.Machine(args.file,input=[1])
machine.runq()
print machine.output

print "Part 2"
machine = intcode.Machine(args.file,input=[5])
machine.runq()
print machine.output
