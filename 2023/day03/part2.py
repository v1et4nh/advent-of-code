import re


def get_total_sum(engine_arr):
    engine_dict = {}
    for idx_row, engine_row in enumerate(engine_arr):
        tmp_row = re.sub('\d', '', engine_row)
        tmp_row = tmp_row.replace('.', '').replace('\n', '')
        list_symbol = list(set(tmp_row))
        engine_dict[idx_row] = {'idx_symbol': [],
                                'idx_num': {m.start(0):int(m.group(0)) for m in re.finditer("\d+", engine_row)}}
        tmp_symbol_arr = []
        for symbol in list_symbol:
            if symbol == '*':
                tmp_symbol_arr.append([i for i, ltr in enumerate(engine_row) if ltr == symbol])
        engine_dict[idx_row]['idx_symbol'] = [item for sublist in tmp_symbol_arr for item in sublist]  # flatten

    total_sum = 0
    for idx_row in engine_dict:
        for idx_symbol in engine_dict[idx_row]['idx_symbol']:
            gears = []
            if idx_row != 0:
                for idx_num in engine_dict[idx_row - 1]['idx_num']:
                    start = idx_num - 1
                    if start < 0:
                        start = 0
                    end = idx_num + len(str(engine_dict[idx_row - 1]['idx_num'][idx_num]))
                    if start <= idx_symbol <= end:
                        gears.append(engine_dict[idx_row - 1]['idx_num'][idx_num])
            for idx_num in engine_dict[idx_row]['idx_num']:
                start = idx_num - 1
                if start < 0:
                    start = 0
                end = idx_num + len(str(engine_dict[idx_row]['idx_num'][idx_num]))
                if start <= idx_symbol <= end:
                    gears.append(engine_dict[idx_row]['idx_num'][idx_num])
            if idx_row != len(engine_dict) - 1:
                for idx_num in engine_dict[idx_row + 1]['idx_num']:
                    start = idx_num - 1
                    if start < 0:
                        start = 0
                    end = idx_num + len(str(engine_dict[idx_row + 1]['idx_num'][idx_num]))
                    if start <= idx_symbol <= end:
                        gears.append(engine_dict[idx_row + 1]['idx_num'][idx_num])
            if len(gears) == 2:
                total_sum += gears[0] * gears[1]

    return total_sum


if __name__ == '__main__':
    puzzle_input = open('puzzle_input.txt', 'r')
    lines = puzzle_input.readlines()
    input_array = []
    for line in lines:
        input_array.append(line)
    total_sum = get_total_sum(input_array)
    print(total_sum)
