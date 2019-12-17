#
# Advent of Code 2019
# Bryan Clair
#
# Day 17
#
# Run with -v option to see the slow animated version.
#
import sys
sys.path.append("..")
import aocutils
from intcode import *

args = aocutils.parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

ASCII = Machine(args.file)

ASCII.runq()


rawmap = ''.join([chr(x) for x in ASCII.output])
map = rawmap.split()

cali = 0
for r in range(len(map)):
    for c in range(len(map[0])):
        if map[r][c] == '#':
            try:
                nbhd = map[r-1][c] + map[r+1][c] + map[r][c+1] + map[r][c-1]
            except:
                continue
            if nbhd == "####":
                cali += r*c

print "Part 1"
print rawmap
print "Calibration:",cali


print "Part 2"

def writeout(out):
    """Write a machine ASCII output to stderr"""
    sys.stderr.write(''.join([chr(x) for x in out]))

def provide(input):
    print 'providing:',input
    for c in input:
        ASCII.input.append(ord(c))

full_path = """
R,12,L,10,L,10,

L,6,L,12,R,12,L,4,

R,12,L,10,L,10,

L,6,L,12,R,12,L,4,

L,12,R,12,L,6,

L,6,L,12,R,12,L,4,

L,12,R,12,L,6,

R,12,L,10,L,10,

L,12,R,12,L,6,

L,12,R,12,L,6
\n"""

char_count = "12345678901234567890"
main_routn = "A,B,A,B,C,B,C,A,C,C\n"
function_A = "R,12,L,10,L,10\n"
function_B = "L,6,L,12,R,12,L,4\n"
function_C = "L,12,R,12,L,6\n"
if args.verbose > 1:
    video = "y\n"
else:
    video = "n\n"


# Restart the program
ASCII.output = []
ASCII[2] = 2
# Feed it inputs as needed
for input in [main_routn,function_A,function_B,function_C,video]:
    try:
        ASCII.runq()
    except EInput:
        writeout(ASCII.output)
        ASCII.output = []
        provide(input)
        pass

if args.verbose <= 1:
    ASCII.runq()
    print 'Dust collected:',ASCII.output[-1]
    sys.exit()

# Verbose/animated version
cr_count = 0
step = 0
view = ''
while True:
    try:
        ASCII.run()
    except EOutput:
        out = ASCII.output.pop()

        if out > 255:
            print 'Dust collected:',out
            sys.exit()

        c = chr(out)
        view += c
        if c == '\n':
            cr_count += 1
        if cr_count == len(map)+1:
            step += 1
            print 'step',step
            print view
            view = ''
            cr_count = 0


