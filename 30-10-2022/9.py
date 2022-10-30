# DESC: # Zadanie 9,
# DESC: Proszę napisać skrypt, który pobierze od użytkownika długości boków prostokąta,
# DESC: a następnie wydrukuje na ekranie informację o obwodzie i polu powierzchni zadanej figury. ,
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


def pole(boki):
    pass


def obwod(boki):
    pass


boki = []
while len(boki) < 3:
    boki.append(int(input("bok: ")))
