#
# Advent of Code 2019
# Bryan Clair
#
# Day --
#
import sys

if __name__ == "__main__":
    filename = 'input.txt'
    if len(sys.argv) > 1:
        filename = sys.argv[1]

    data = open(filename).readlines()

    for line in data:
        print line
