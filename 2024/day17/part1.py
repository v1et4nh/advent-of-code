if __name__ == '__main__':
    puzzle_input = open('input.txt', 'r')
    lines = puzzle_input.readlines()
    A = lines[0].strip().split(' ')[-1]
    B = lines[1].strip().split(' ')[-1]
    C = lines[2].strip().split(' ')[-1]
    P = lines[4].strip().split(' ')[-1].split(',')

    instruction_pointer = 0
    output = []
    dict_combo = {0: 0, 1: 1, 2: 2, 3: 3, 4: int(A), 5: int(B), 6: int(C), 7: 'invalid'}

    while instruction_pointer < len(P):
        opcode = int(P[instruction_pointer])
        operand = int(P[instruction_pointer+1])
        if opcode == 0:  # Division
            A = int(int(A) / 2**dict_combo[operand])
        elif opcode == 1:  # Bitwise XOR
            B = int(B) ^ operand
        elif opcode == 2:  # Modulo
            B = dict_combo[operand] % 8
        elif opcode == 3:  # Jumper
            if int(A):
                instruction_pointer = operand
                continue
        elif opcode == 4:  # Bitwise XOR
            B = int(B) ^ int(C)
        elif opcode == 5:  # Output
            output.append(str(dict_combo[operand] % 8))
        elif opcode == 6:  # like 0 stored in B
            B = int(int(A) / 2**dict_combo[operand])
        elif opcode == 7:  # like 0 stored in C
            C = int(int(A) / 2**dict_combo[operand])
        instruction_pointer += 2
        dict_combo = {0: 0, 1: 1, 2: 2, 3: 3, 4: int(A), 5: int(B), 6: int(C), 7: 'invalid'}

    print(''.join(output))