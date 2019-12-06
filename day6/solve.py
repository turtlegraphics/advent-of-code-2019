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

orbiting = {}
reverse = {}

for line in inputlines:
    center, orbiter = line.split(')')
    if center in orbiting:
        orbiting[center].append(orbiter)
    else:
        orbiting[center] = [orbiter]
    reverse[orbiter] = center

if args.verbose > 1:
    print orbiting

def orbits(center,level):
    tot = level
    if center not in orbiting:
        return tot
    for p in orbiting[center]:
        tot += orbits(p,level+1)
    return tot

print "Part 1:",orbits('COM',0)

path1 = []
p = "YOU"
while p != "COM":
    path1.append(p)
    p = reverse[p]
if args.verbose > 1:
    print path1

path2 = []
p = "SAN"
while p != "COM":
    path2.append(p)
    p = reverse[p]
if args.verbose > 1:
    print path2

intersect = [p for p in path1 if p in path2]
if args.verbose > 1:
    print intersect
common = intersect[0]
if args.verbose > 1:
    print path1.index(common)
    print path2.index(common)

print "Part 2:",path1.index(common)+path2.index(common)-2




