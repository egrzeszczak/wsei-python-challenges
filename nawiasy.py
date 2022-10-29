# DESC: Wyrzuć błąd w stringu jeśli posiada nie zamknięte nawiasy

ticket = 0
for char in input("[nawiasy] text: "):
    if ord(char) == 40:
        ticket += 1
    elif ord(char) == 41:
        if ticket == 0:
            raise Exception("Nie zamknięty nawias")
        ticket -= 1

if ticket is not 0:
    raise Exception("Nie zamknięty nawias")
