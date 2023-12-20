if __name__ == '__main__':
    with open('puzzle_input.txt', 'r') as file:
        lines = [l.strip() for l in file]

    dict_map    = {}
    broadcaster = []
    conjunction = []
    for l in lines:
        if 'broadcaster' in l:
            broadcaster = l.split(' -> ')[1].split(', ')
        else:
            if l[0] == '%':
                l = l.replace('%', '').split(' -> ')
                dict_map[l[0]] = {'type': 'flip_flop', 'receiver': l[1].split(', '), 'state': 0}
            if l[0] == '&':
                l = l.replace('&', '').replace('%', '').split(' -> ')
                conjunction.append(l[0])
                dict_map[l[0]] = {'type': 'conjunction', 'receiver': l[1].split(', '), 'input': {}}

    for c in conjunction:
        for k in dict_map:
            if c in dict_map[k]['receiver']:
                dict_map[c]['input'][k] = 0

    button      = 1000
    low_pulses  = button
    high_pulses = 0
    for i in range(button):
        pulse = 0
        queue = []
        for signal in broadcaster:
            dict_map[signal]['state'] ^= 1  # Flip state
            queue.append([signal, dict_map[signal]['receiver'], dict_map[signal]['state']])
            low_pulses += 1

        while queue:
            sender, receiver, pulse = queue.pop(0)
            for r in receiver:
                if pulse == 0:
                    low_pulses += 1
                else:
                    high_pulses += 1
                if r not in dict_map:
                    continue
                if dict_map[r]['type'] == 'flip_flop':
                    if pulse == 0:
                        dict_map[r]['state'] ^= 1  # Flip state
                        queue.append([r, dict_map[r]['receiver'], dict_map[r]['state']])
                elif dict_map[r]['type'] == 'conjunction':
                    dict_map[r]['input'][sender] = pulse
                    if all(dict_map[r]['input'][s] for s in dict_map[r]['input']):
                        queue.append([r, dict_map[r]['receiver'], 0])
                    else:
                        queue.append([r, dict_map[r]['receiver'], 1])

    print(low_pulses * high_pulses)
