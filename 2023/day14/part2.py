from tqdm import tqdm

if __name__ == '__main__':
    with open('puzzle_input.txt', 'r') as file:
        lines = [l.strip() for l in file]

    total_sum = 0
    total_lines = []
    for c, cycle in tqdm(enumerate(range(1000000000))):
        new_lines = ['' for i in range(len(lines))]
        # north
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
            for k, el in enumerate(current_col):
                new_lines[k] += el
        lines = new_lines
        new_lines = []
        # west
        for i in range(len(lines)):
            current_col = [l for l in lines[i]]
            is_sort = True
            while is_sort:
                is_sort = False
                for j in range(len(current_col)-1):
                    if current_col[j] == '.' and current_col[j+1] == 'O':
                        current_col[j] = 'O'
                        current_col[j+1] = '.'
                        is_sort = True
            new_lines.append(''.join(current_col))
        lines = new_lines
        new_lines = ['' for i in range(len(lines))]
        # south
        for i in range(len(lines[0])):
            current_col = [l[i] for l in lines]
            is_sort = True
            while is_sort:
                is_sort = False
                for j in range(len(current_col)-1):
                    if current_col[j] == 'O' and current_col[j+1] == '.':
                        current_col[j] = '.'
                        current_col[j+1] = 'O'
                        is_sort = True
            for k, el in enumerate(current_col):
                new_lines[k] += el
        # east
        lines = new_lines
        new_lines = []
        for i in range(len(lines)):
            current_col = [l for l in lines[i]]
            is_sort = True
            while is_sort:
                is_sort = False
                for j in range(len(current_col)-1):
                    if current_col[j] == 'O' and current_col[j+1] == '.':
                        current_col[j] = '.'
                        current_col[j+1] = 'O'
                        is_sort = True
            new_lines.append(''.join(current_col))
        lines = new_lines
        if lines in total_lines:
            idx = [y for y, l in enumerate(total_lines) if lines == l][0]
            break
        else:
            total_lines.append(lines)

    searched_line = (1000000000-c)%(c-idx)+idx-1
    print(searched_line)
    for i, l in enumerate(total_lines[searched_line]):
        total_sum += sum([el == 'O' for el in l]) * (len(lines)-i)
    print(total_sum)