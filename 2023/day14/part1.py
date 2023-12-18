if __name__ == '__main__':
    with open('puzzle_input.txt', 'r') as file:
        lines = [l.strip() for l in file]

    total_sum = 0
    for i in range(len(lines[0])):
        current_col = [l[i] for l in lines]
        is_sort = True
        while is_sort:
            is_sort = False
            for j in range(len(current_col)-1):
                if current_col[j] == '.' and current_col[j+1] == 'O':
                    current_col[j] = 'O'
                    current_col[j+1] = '.'
                    is_sort = True
        total_sum += sum([len(current_col)-i for i, el in enumerate(current_col) if el == 'O'])
    print(total_sum)