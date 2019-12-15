#
# Advent of Code 2019
# Bryan Clair
#
# Day 15
#
import sys
sys.path.append("..")
import aocutils

from intcode import *

args = aocutils.parse_args()

class Droid:
    def __init__(self):
        self.pos = (0,0)
        self.program = Machine(args.file)
        
    def move(self,dir):
        """dir is 0-3"""
        if args.verbose > 1:
            print 'moving',dir,letters[dir]

        self.program.input.append(dir + 1)
        try:
            self.program.run()
        except EOutput:
            pass
        status = self.program.output.pop()
        if status != 0:
            self.pos = (self.pos[0] + dirs[dir][0],
                        self.pos[1] + dirs[dir][1])
        return status

def explore(path):
    """
    Explore the maze from current position,
    then return to current position
    """
    global oxygen

    # print 'exploring:',path

    for dir in range(4):
        goal = (droid.pos[0] + dirs[dir][0],droid.pos[1] + dirs[dir][1])
        status = droid.move(dir)
        if status == 0:
            map[goal] = '#'
            continue

        pos = droid.pos
        if status == 1:
            map[pos] = ' '
        if status == 2:
            map[pos] = 'O'
            oxygen = pos

        newpath = path + letters[dir]

        if pos not in paths or len(newpath) < len(paths[pos]):
            paths[pos] = newpath
            explore(newpath)

        status = droid.move(reverse[dir])
        assert(status != 0)

    return

# Some direction translations
letters = 'NSWE'
reverse = [1,0,3,2]
dirs = [(0,1),(0,-1),(-1,0),(1,0)]

# Init map and shortest path dictionary
map = aocutils.Grid()
map[(0,0)] = ' '
paths = {}
paths[(0,0)] = ''
oxygen = None

# Explore the ship
droid = Droid()
explore('')

map[(0,0)] = 'R'
map.display()

print 'Oxygen location:',oxygen
print 'Distance to oxygen (part 1):',len(paths[oxygen])

# Move the droid to the oxygen
for m in paths[oxygen]:
    droid.move(letters.index(m))

# Re-build the paths list starting at the oxygen
paths = {}
paths[(0,0)] = ''
explore('')

print 'Furthest distance from oxygen (part 2):',
print max([len(p) for p in paths.values()])
