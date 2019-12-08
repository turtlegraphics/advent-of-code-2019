#
# Advent of Code 2019
# Bryan Clair
#
# Day 8
#
import sys
sys.path.append("..")
import aocutils

args = aocutils.parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

line = inputlines[0]

h = 6
w = 25
i = 0
layers = []
while i < 15000:
    layer = line[i:i+h*w]
    layers.append(layer)
    zeros = layer.count('0')
    i += h*w
    if zeros == 3:  #larceny.. looked at list, saw 3 was smallest
        print 'part 1:',layer.count('1')*layer.count('2')

image = list(layers[0])

for i in range(len(image)):
    l = 0
    while layers[l][i] == '2':
        l += 1
    image[i] = layers[l][i]

for r in range(h):
    out = ''
    for c in range(w):
        out += ' ' if image[r*w + c] == '0' else '#'
    print out

