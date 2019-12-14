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

def how_much_ore(fuel):
    """
    returns amount of ORE needed to make given amount of fuel
    """
    next = stuff.index("FUEL")
    need = [0]*len(stuff)
    need[next] = fuel
    while next:
        making = stuff[next]
        quantity = need[stuff.index(making)]
        if args.verbose > 1:
            print 'Making',quantity,'of',making

        using = reactions[making]
        produces = -using[stuff.index(making)]

        multiplier = quantity // produces
        if multiplier * produces < quantity:
            multiplier += 1
        assert(multiplier * produces >= quantity)

        for i in range(len(stuff)):
            need[i] += multiplier * using[i]

        if args.verbose > 2:
            print need

        most = max(need[1:])
        if most > 0:
            next = need.index(most)
        else:
            next = None
    return need[0]


# Part 1
ore = how_much_ore(1)
print 'Part 1: To make one FUEL, we need',ore,'ORE'

# Part 2
# Refactored this post-contest.  When doing this live, I did the
# binary search by hand!
#
ore_max = 1000000000000
high = 1
low = 1
while how_much_ore(high) <= ore_max:
    high *= 2

while high > low + 1:
    mid = low + (high-low)//2
    if how_much_ore(mid) <= ore_max:
        low = mid
    else:
        high = mid
    if args.verbose > 2:
        print (low,high)

print 'Part 2: With',ore_max,'ORE, we can make',low,'FUEL'
