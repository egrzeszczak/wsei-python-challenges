# [x]: Proszę zbudować listę składającą się z liczb od 0 do 100 włącznie, a następnie proszę:
# [x]:     • Korzystając z list comprehension zbudować drugą listę zawierającą kwadraty liczb z pierwszej listy.
# [x]:     • Korzystając z funkcji enumerate() i zip() uzyskać następujący efekt i go wyświetlić:
# [x]:         ◦ Liczba 0 podniesiona do kwadratu daje wynik: 0
# [x]:         ◦ Liczba 1 podniesiona do kwadratu daje wynik: 1
# [x]:         ◦ Liczba 2 podniesiona do kwadratu daje wynik: 4
# [x]:         ◦ itd.

list1 = [x for x in range(101)]
list2 = [y**2 for y in list1]

for i, x in enumerate(list2):
    print(f"Liczba {i} podniesiona do kwadratu daje wynik: {x}")
