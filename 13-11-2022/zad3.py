# DESC: Zadanie 3
# DESC: Dla zadanej macierzy proszę zsumować elementy,
# DESC: które są różne od zera i elementy pod nimi nie są zerami.

import random

matrix_size = int(input("[matrix] size: "))
matrix = [
    [random.randrange(-9, 9) for y in range(0, matrix_size)]
    for x in [int(y) for y in range(0, matrix_size)]
]

for y in matrix:
    print("\t".join(map(str, y)))


def sumuj_macierz(macierz, rozmiar):
    """
    Dla zadanej macierzy proszę zsumować elementy,
    które są różne od zera i elementy pod nimi nie są zerami.
    """
    count = 0
    for y in range(rozmiar):
        for x in range(rozmiar):
            if y + 1 < rozmiar:
                if macierz[y + 1][x] != 0:
                    count += macierz[y][x]
            else:
                count += macierz[y][x]
            print(f"f({x}, {y})={macierz[y][x]}\tcount: {count}")
    print(f"Całkowita wartość: {count}")


sumuj_macierz(matrix, matrix_size)
