import re


def get_total_sum(engine_arr):
    engine_dict = {}
    for idx_row, engine_row in enumerate(engine_arr):
        tmp_row = re.sub('\d', '', engine_row)
        tmp_row = tmp_row.replace('.', '').replace('\n', '')
        list_symbol = list(tmp_row)
        engine_dict[idx_row] = {'idx_symbol': [],
                                'idx_num': {m.start(0):int(m.group(0)) for m in re.finditer("\d+", engine_row)}}
        tmp_symbol_arr = []
        for symbol in list_symbol:
            tmp_symbol_arr.append([i for i, ltr in enumerate(engine_row) if ltr == symbol])
        engine_dict[idx_row]['idx_symbol'] = [item for sublist in tmp_symbol_arr for item in sublist]  # flatten

    total_sum = 0
    for idx_row in engine_dict:
        for idx_num in engine_dict[idx_row]['idx_num']:
            start = idx_num - 1
            if start < 0:
                start = 0
            end = idx_num + len(str(engine_dict[idx_row]['idx_num'][idx_num]))
            if idx_row != 0 and any(start <= symbol <= end for symbol in engine_dict[idx_row - 1]['idx_symbol']):
                total_sum += engine_dict[idx_row]['idx_num'][idx_num]
            elif any(start <= symbol <= end for symbol in engine_dict[idx_row]['idx_symbol']):
                total_sum += engine_dict[idx_row]['idx_num'][idx_num]
            elif idx_row != len(engine_dict)-1 and any(start <= symbol <= end for symbol in engine_dict[idx_row + 1]['idx_symbol']):
                total_sum += engine_dict[idx_row]['idx_num'][idx_num]

    return total_sum


if __name__ == '__main__':
    data = open('puzzle_input.txt', 'r')
    data = data.readlines()
    input_array = []
    for d in data:
        input_array.append(d)
    result = get_total_sum(input_array)
    print(result)
