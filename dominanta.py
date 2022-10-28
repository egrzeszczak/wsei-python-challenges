# DESC: Znajdź dominantę w zbiorze
import random

dominanta = {}

# Generowanie zbioru
list_of_numbers = [
    random.randrange(0, 1000) for x in range(0, random.randrange(0, 1000))
]

# Zmienne 
most_occuring = 1   # Liczba która najczęściej występuje
occurances = 1      # Ilość wystąpień

# Logika
for i in list_of_numbers:
    if i in dominanta.keys():
        dominanta[i] += 1
        if dominanta[i] > occurances:
            occurances = dominanta[i]
            most_occuring = i
    else:
        dominanta[i] = 1

print("lista liczb: ", list_of_numbers, "\n\n")
print("dominanta: ", dominanta, "\n\n")
print("most_occuring: ", most_occuring, "occurances: ", occurances)
