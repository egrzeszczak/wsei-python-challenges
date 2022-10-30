# DESC: Sprawdź czy kolory dwóch podanych pól na szachownicy są takie same
# DESC: python3 szachownica.py

szachownica = {}
for y in range(1, 9):
    szachownica[y] = {}
    for index, x in enumerate(["a", "b", "c", "d", "e", "f", "g", "h"]):
        if ((index % 2) + (y % 2)) % 2 == 0:
            szachownica[y][x] = "black"
        else:
            szachownica[y][x] = "white"


def board():
    """DESC: Wyświetl szachownicę"""
    for i, a in enumerate(szachownica):
        print(i + 1, szachownica[a])


def check(s1, s2):
    """DESC: Sprawdź czy kolory dwóch podanych pól się zgadzają"""
    key1, val1 = [*s1]
    key2, val2 = [*s2]
    if szachownica[int(val1)][key1] == szachownica[int(val2)][key2]:
        print("Ten sam kolor")
    else:
        print("Różne kolory")


check(input("1: "), input("2: "))
