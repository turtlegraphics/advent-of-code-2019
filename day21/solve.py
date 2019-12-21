#
# Advent of Code 2019
# Bryan Clair
#
# Day 21
#
import sys
sys.path.append("..")
import aocutils
from intcode import *

args = aocutils.parse_args()

droid = Machine("springdroid.int")

program = [x.split('#')[0].strip() for x in open(args.file).readlines()]

print 'Running'
print program

while True:
    try:
        droid.run()
    except EOutput:
        c = droid.output.pop()
        if c < 255:
            sys.stdout.write(chr(c))
        else:
            print c
    except EInput:
        for line in program:
            print line
            if line != '':
                for c in line:
                    droid.input.append(ord(c))
                droid.input.append(ord('\n'))
    except EHalt:
        break
