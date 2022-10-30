# DESC: Wyświetl pierwszą cyfrę w stringu (left most digit)
print(next(char for char in input("string: ") if char.isdigit()))
