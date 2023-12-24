def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
        return None

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y


if __name__ == '__main__':
    with open('puzzle_input.txt', 'r') as file:
        lines = [l.strip() for l in file]

    total_intersections = 0
    test_area = (200000000000000, 400000000000000)
    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            A, B       = lines[i], lines[j]

            pos, vel   = A.split(' @ ')
            x, y, z    = tuple(map(int, pos.split(', ')))
            vx, vy, vz = tuple(map(int, vel.split(', ')))
            A          = ((x, y), (x + vx, y + vy))
            A_sign     = -1 if int(vx) < 0 else 1

            pos, vel   = B.split(' @ ')
            x, y, z    = tuple(map(int, pos.split(', ')))
            vx, vy, vz = tuple(map(int, vel.split(', ')))
            B          = ((x, y), (x + vx, y + vy))
            B_sign     = -1 if int(vx) < 0 else 1

            isec = line_intersection(A, B)
            if isec:
                # within test area
                if test_area[0] <= isec[0] <= test_area[1] and test_area[0] <= isec[1] <= test_area[1]:
                    # Past
                    if (A_sign == -1 and isec[0] > A[0][0]) or (A_sign == 1 and isec[0] < A[0][0]) or \
                            (B_sign == -1 and isec[0] > B[0][0]) or (B_sign == 1 and isec[0] < B[0][0]):
                        continue
                    total_intersections += 1

    print(total_intersections)
