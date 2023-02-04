# DESC: Zadanie 5
# DESC: Macierz kwardratowa z wartościami spiralnymi
# DESC: 1   2  3  4
# DESC: 12 13 14  5
# DESC: 11 16 15  6
# DESC: 10  9  8  7

import random

matrix_size = int(input("[matrix] size: "))
matrix = [
    [0 for y in range(0, matrix_size)] for x in [int(y) for y in range(0, matrix_size)]
]

# Kierunki
direction = [
    # (x, y)
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1),
]

# Łamanie ścieżki
steps = [matrix_size]
for temp in reversed(range(1, matrix_size)):
    steps.append(temp)
    steps.append(temp)
print(steps)


for y in matrix:
    print("\t".join(map(str, y)))

x, y = 0, 0
line = 0
for n in range(matrix_size**2):
    xa, ya = direction[line % matrix_size]
    print(f"ya: {ya}, xa: {xa}")
    matrix[y][x] = n + 1
    print(f"{x},{y} = {n+1}")
    x += xa
    print(f"x is now {x}")
    y += ya
    print(f"y is now {y}")
    steps[0] -= 1
    print(f"Moves left {steps[0]}")
    if steps[0] == 0:
        line += 1
        steps.pop()


for y in matrix:
    print("\t".join(map(str, y)))
