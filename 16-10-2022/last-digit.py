# DESC: Wyświetl ostatnią cyfrę w stringu (right most digit)
print([(char) for char in input("[last-digit] string: ") if char.isdigit()][-1])
