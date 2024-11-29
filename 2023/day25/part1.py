import math
import random

# Karger's algorithm:
# https://www.geeksforgeeks.org/introduction-and-implementation-of-kargers-algorithm-for-minimum-cut/


if __name__ == '__main__':
    V = set()
    E = set()

    for line in open('puzzle_input_example.txt'):
        v, *ws = line.replace(':', ' ').split()
        V |= {v, *ws}
        E |= {(v, w) for w in ws}

    ss = lambda v: next(s for s in subsets if v in s)

    while True:
        subsets = [{v} for v in V]

        while len(subsets) > 2:
            s1, s2 = map(ss, random.choice([*E]))
            if s1 != s2:
                s1 |= s2
                subsets.remove(s2)
        if sum(ss(u) != ss(v) for u, v in E) < 4:
            break

    print(math.prod(map(len, subsets)))