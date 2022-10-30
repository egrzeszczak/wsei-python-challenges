# DESC: # Zadanie 8,
# DESC: Posiadając następujący kod:
# DESC: ukryta_liczba = random.randint(1,100),
# DESC: Proszę pobrać od użytkownika liczbę i sprawdzić czy jej wartość jest taka sama jak zmiennej `ukryta_liczba`.
# DESC: Pobieranie liczby od użytkownika powinno trwać do momentu trafienia w odpowiednią liczbę.
# DESC: Dodatkowo należy zaprogramować aplikację w taki sposób, że będzie ona informowała użytkownika:
# DESC: jak blisko znajduje się poszukiwanej liczby. ,
# DESC: Zadanie powinno zostać wykonane z użyciem funkcji.

import random

ukryta_liczba = random.randint(1, 100)


def jak_blisko(source, target):
    """Oblicza jak blisko żeś trafił"""
    return abs(source - target)


while True:
    source = int(input("traf liczbę: "))
    if ukryta_liczba == source:
        print("brawo")
        break
    else:
        print(f"pomyliłeś się o {jak_blisko(source, ukryta_liczba)}")
