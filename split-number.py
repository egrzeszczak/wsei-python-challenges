# DESC: Podziel libczę cyfrowo na dwie części i zsumuj cyfry dla każdej z części
# DESC: Zakładamy że liczba posiada parzystą ilość cyfr
# DESC: liczba: 123456      1 2 3 | 4 5 6       6, 15

number = input("[split-number] number: ")

print(
    sum([int(x) for x in number[: int(len(number) / 2)]]),
    "\t",
    sum([int(y) for y in number[int(len(number) / 2) :]]),
)

# first_half, second_half = [ number[:int(len(number)/2)], number[int(len(number)/2):] ]
# print(sum([int(x) for x in first_half]), sum([int(y) for y in second_half]))
