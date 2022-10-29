# DESC: Przejdź się po macierzy zaczynając od (0, 0)
# DESC: Kolejny krok to wybrać z komórki S, E albo SE która jest największa i powtórzyć aż do końca
import random

matrix_size = int(input("[matrix] size: "))
matrix = [
    [random.randrange(0, 999) for y in range(0, matrix_size)]
    for x in [int(y) for y in range(0, matrix_size)]
]

for y in matrix:
    print(y)

# TODO: Dokończyć część z przemieszczaniem się S, E, SE
