from z3 import Real, Solver, sat


if __name__ == '__main__':
    with open('puzzle_input.txt', 'r') as file:
        lines = [l.strip() for l in file]

    s   = Solver()
    POS = [Real(f'P{i}') for i in range(3)]  # must be same for all lines
    VEL = [Real(f'V{i}') for i in range(3)]  # must be same for all lines
    for i in range(len(lines)):
        A = lines[i]
        pos, vel = A.split(' @ ')
        pos = tuple(map(int, pos.split(',')))
        vel = tuple(map(int, vel.split(',')))
        t   = Real(f't{i}')  # different t for each line
        for el in range(len(pos)):  # for each x, y, z
            # e.g. P0 + V0*t0 == pos[0] + vel[0]*t0
            s.add(POS[el] + VEL[el]*t == pos[el] + vel[el]*t)
    if s.check() == sat:
        m = s.model()
        x, y, z = tuple(map(int, [str(m.evaluate(p)) for p in POS]))
        result = x + y + z
        print(result)