#
# Advent of Code 2019
# Bryan Clair
#
# Day 13
#

# Minimalist version
# Ignore all output except ball and paddle (i.e. no screen)

import sys
sys.path.append("..")
from intcode import *

ball = 0
paddle = 0
score = 0

game = Machine("input.txt")

game[0] = 2 # insert two bits

outparity = 0
while True:
    try:
        game.run()

    except EHalt:
        print 'Final score:',score
        break

    except EOutput:
        outparity += 1
        if outparity == 3:
            outparity = 0
            (x,y,val) = game.output
            game.output.pop()
            game.output.pop()
            game.output.pop()
            if x == -1:
                score = val
            elif val == 3: # paddle
                paddle = x
            elif val == 4: # ball
                ball = x
            
    except EInput:
        v = 0
        if ball < paddle:
            v = -1
        elif ball > paddle:
            v = 1
        game.input.append(v)
