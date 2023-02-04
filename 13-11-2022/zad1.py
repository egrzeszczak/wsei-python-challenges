# DESC: Zadanie 1
# DESC: Dla danego roku proszę zwrócić wiek. Na przykład dla:
# DESC:     rok = 1905, rozwiązanie(rok) = 20;
# DESC:     dla rok = 1700, rozwiązanie(rok) = 17.
# DESC: Zakres lat 1 ≤ rok ≤ 2022.


def wiek(rok):
    """
    Po podaniu roku zwróć wiek
    1. Sposób - mój
    2. Sposób - p. Maja
    """
    # wiek = 1 + ((rok - 1) // 100)
    wiek = (rok + 99) // 100

    return wiek


print(wiek(int(input("rok: "))))
