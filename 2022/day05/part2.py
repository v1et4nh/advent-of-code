import re
from copy import deepcopy

stack_example = [['Z', 'N'], ['M', 'C', 'D'], ['P']]
stack         = [['N', 'B', 'D', 'T', 'V', 'G', 'Z', 'J'],
                 ['S', 'R', 'M', 'D', 'W', 'P', 'F'],
                 ['V', 'C', 'R', 'S', 'Z'],
                 ['R', 'T', 'J', 'Z', 'P', 'H', 'G'],
                 ['T', 'C', 'J', 'N', 'D', 'Z', 'Q', 'F'],
                 ['N', 'V', 'P', 'W', 'G', 'S', 'F', 'M'],
                 ['G', 'C', 'V', 'B', 'P', 'Q'],
                 ['Z', 'B', 'P', 'N'],
                 ['W', 'P', 'J']]


def get_top_stack(move_arr):
    new_stack = deepcopy(stack)
    for move in move_arr:
        step = list(map(int, re.findall(r'\d+', move)))
        source      = new_stack[step[1]-1]
        destination = new_stack[step[2]-1]
        to_move     = source[len(source)-step[0]:]
        source      = source[:len(source)-step[0]]  # remove from old stack
        destination.extend(to_move)                 # add to new stack
        # Save
        new_stack[step[1]-1] = source
        new_stack[step[2]-1] = destination
    print(''.join([row[-1] for row in new_stack if row]))


if __name__ == '__main__':
    puzzle_input = open('puzzle_input.txt', 'r')
    lines = puzzle_input.readlines()
    move_arr = [line for line in lines if 'move' in line]
    get_top_stack(move_arr)
