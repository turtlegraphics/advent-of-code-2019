#
# Advent of Code 2019
# Bryan Clair
#
# Day 14
#
import sys
sys.path.append("..")
import aocutils

args = aocutils.parse_args()

stuff = ['ORE']
inputlines = [x.strip() for x in open(args.file).readlines()]
for line in inputlines:
    stuff.append(line.split("=>")[1].split()[1])
print stuff

inputlines = [x.strip() for x in open(args.file).readlines()]

reactions = {}
for line in inputlines:
    reaction = [0]*len(stuff)
    input, output = line.split("=>")

    amount, product = output.split()
    reaction[stuff.index(product)] = -int(amount)

    ingredients = input.split(",")
    for x in ingredients:
        quantity,chemical = x.split()
        reaction[stuff.index(chemical)] = int(quantity)

    reactions[product] = reaction

print reactions

need = [0]*len(stuff)
need[stuff.index("FUEL")] = 8845261
# print need

def firstpos(v):
    """Find maximum required need"""
    most = max(v[1:])
    if most > 0:
        return v.index(most)
    return None

next = firstpos(need)
while next:
    making = stuff[next]
    quantity = need[stuff.index(making)]
    print 'Making',quantity,'of',making
    using = reactions[making]
    produces = -using[stuff.index(making)]

    multiplier = quantity // produces
    if multiplier * produces < quantity:
        multiplier += 1
    assert(multiplier * produces >= quantity)

    print '    multiplier',multiplier
    for i in range(len(stuff)):
        need[i] += multiplier * using[i]

    print need
    next = firstpos(need)

print 'Used ORE =',need[0]
print need[0] <= 1000000000000
