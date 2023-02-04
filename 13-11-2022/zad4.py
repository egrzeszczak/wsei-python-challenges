# DESC: Zadanie 4
# DESC: Mamy liste wartości całkowitych
# DESC: Mamy przekazany klucz

# DESC: Znajdź wszystkie pary których suma da klucz
# DESC: ale zrobić to w czasie liniowym

import random

count = int(input("ile: "))

# Mamy liste wartości całkowitych
values = [random.randrange((-count // 10), (count // 10)) for i in range(0, count)]
# Mamy przekazany klucz
key = random.randrange((-count // 4), (count // 4))

# Znajdź wszystkie pary których suma da klucz
# ale zrobić to w czasie liniowym
pairs = [
    {
        (i, i + 1): (values[i], values[i + 1]),
    }
    for i in range(len(values) - 1)
    if (values[i] + values[i + 1] == key)
]

print(f"Wygenerowany klucz")
print(f"\t{key}")
print()
print(f"Wygenerowane wartości")
print(values)
print()
print(f"Wykryte pary")
for pair in pairs:
    print(pair)
