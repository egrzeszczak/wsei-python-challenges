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

dirs = [
    (1, 0), # RIGHT
    (0, 1), # DOWN
    (-1, 0), # LEFT
    (0, -1), # UP
]

# Łamanie ścieżki
steps = [matrix_size]
for temp in reversed(range(1, matrix_size)):
    steps.append(temp)
    steps.append(temp)
print(steps)

x, y = 0, 0
line = 0
(xa, ya) = dirs[line % matrix_size]
for n in range(matrix_size**2):
    print(f"\n\n\n[STEP {n+1}] -------------------------------------------------------\n")
    # POSTAW WARTOŚĆ
    print(f"MATRIX AT {y}, {x} will be {n+1}")
    matrix[y][x] = n + 1
    for val in matrix:
        print("\t".join(map(str, val)))
    print(f"\nSTEP IS USED\nBEFORE:\t{steps}")
    steps[0] -= 1
    if steps[0] == 0:
        print(f"SINCE THE HEAD OF STEPS IS ZERO, BREAK THE LINE")
        line += 1
        print(f"LINE IS {line} MOD {matrix_size} IS {line % 4}")
        steps = steps[1:] 
        # OKREŚL KIERUNEK
        (xa, ya) = dirs[line % 4]
        print(f"DIRECTION IS NOW ({ya}, {xa})")
    if (x+xa) != matrix_size or (x+xa) != 0:
        print(f"MOVE X to {x+xa}")
        x += xa
    if (y+ya) != matrix_size or (y+ya) != 0:
        print(f"MOVE Y to {y+ya}")
        y += ya
    print(f"AFTER:\t{steps}")

print(f"\n\n\n[FINISHED for matrix size {matrix_size}] -------------------------------------------------------\n")
for y in matrix:
    print("\t".join(map(str, y)))