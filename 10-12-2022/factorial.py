# DESC: Przekazywana jest liczba n (int) do funkcji
# DESC: Zwraca najbliższą liczbę k gdzie k to jest silnia
 
import math
import random

def closestToFactorial(n):
    print(f"N: {n}")
    k = 1
    while math.factorial(k) < n:
        print(f"K: {k}, K!: {math.factorial(k)}")
        k += 1
    print(f"K: {k}, K!: {math.factorial(k)}")
    distanceToPrevious = abs(math.factorial(k-1) - n) 
    distanceToNext = abs(math.factorial(k) - n)
    if distanceToNext < distanceToPrevious:
        print(f"N: {n} is closer to {k}! = {math.factorial(k)}")
    elif distanceToNext > distanceToPrevious:
        print(f"N: {n} is closer to {k-1}! = {math.factorial(k-1)}")
    else:
        print(f"N: {n} is in equal distance to {k}! as well as to {k}!")
    
    print()


for i in range(0, 10):
    closestToFactorial(random.randrange(0, 100000))

