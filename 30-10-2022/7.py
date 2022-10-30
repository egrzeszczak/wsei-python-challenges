# DESC: # Zadanie 7,
# DESC: Proszę napisać skrypt, który pobierze trzy długości boków trójkąta, a następnie,
# DESC: * Sprawdzi czy z zadanych długości można utworzyć trójkąt.,
# DESC: * Sprawdzi czy trójkąt będzie prostokątny,
# DESC: Zadanie powinno zostać wykonane z użyciem funkcji.


def mozna(boki):
    """
    Funkacja sprawdza czy można utworzyć trójkąt prosotąkny to tych bokach
    https://zpe.gov.pl/a/konstrukcja-trojkata-o-danych-bokach/DQbhFQFuy
    """
    return (
        (boki[0] + boki[1] > boki[2])
        and (boki[0] + boki[2] > boki[1])
        and (boki[1] + boki[2] > boki[0])
    )


def prostokatny(boki):
    """
    Funkcja sprawdza czy te boki utworzą trójkąt prostokątny
    """
    return (
        (boki[0] ** 2 + boki[1] ** 2 == boki[2] ** 2)
        or (boki[1] ** 2 + boki[2] ** 2 == boki[0] ** 2)
        or (boki[0] ** 2 + boki[2] ** 2 == boki[1] ** 2)
    )


boki = []
while len(boki) < 3:
    boki.append(int(input("bok: ")))

print(
    {
        "boki": boki,
        "utworzą trójkąt?": mozna(boki),
        "utworzą trójkąt prostokątny?": prostokatny(boki),
    }
)
