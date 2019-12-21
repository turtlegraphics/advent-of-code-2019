import itertools as it

def jump_or_not(i):
    """Return False if you died, otherwise JUMP or WALK"""
#    print i
    if len(i) == 0:
        return True

    if not i[0]:
        return False

    if jump_or_not(i[1:]):
        return "WALK"

    if len(i) < 4:
        return False

    if jump_or_not(i[4:]):
        return "JUMP"

    return False

NAMES = 'abcdefghij'

def sensors(state):
    out = ''
    for i in range(len(state)):
        if i != 0:
            out += '&&'
        if not state[i]:
            out += '!'
        out += NAMES[i]
    return out

logic = ''
for state in it.product([0,1],repeat=9):
    v = jump_or_not([1]+list(state))
    print v, state, sensors(state)
    if v != 'WALK':
        logic += '('+sensors(state)+')||'

print logic
