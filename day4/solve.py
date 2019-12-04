#
# Advent of Code 2019
# Bryan Clair
#
# Day 4
#
import sys
sys.path.append("..")
import aocutils

args = aocutils.parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

for line in inputlines:
    start,finish = [int(x) for x in line.split('-')]

def ok(i):
    digits = [int(x) for x in list(str(i))]
    for d in range(len(digits)-1):
        if digits[d] > digits[d+1]:
            return False
    for d in range(len(digits)-1):
        if digits[d] == digits[d+1]:
            if args.part == 2:
                try:
                    if digits[d-1] == digits[d]:
                        continue
                except IndexError:
                    pass
                try:
                    if digits[d+2] == digits[d]:
                        continue
                except IndexError:
                    pass
            return True
    return False

count = 0
for i in range(start,finish):
    if ok(i):
        if args.verbose > 1:
            print i,'ok'
        count += 1

print count
