#
# Advent of Code 2019
# Bryan Clair
#
# Day --
#
import sys
sys.path.append("..")
import aocutils

args = aocutils.parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

for line in inputlines:
    print line
