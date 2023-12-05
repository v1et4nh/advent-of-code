if __name__ == '__main__':
    puzzle_input = open('puzzle_input.txt', 'r')
    lines = puzzle_input.readlines()
    line = [line for line in lines][0]
    len_distinct_char = 4
    for i in range(len(line)):
        tmp_marker = line[i:i+len_distinct_char]
        if len(set(tmp_marker)) == len_distinct_char:
            print(i+len_distinct_char)
            break