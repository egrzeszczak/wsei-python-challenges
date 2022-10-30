# DESC: # Zadanie 6,
# DESC: Proszę, używając pętli while, zbudować kalkulator:,
# DESC:  1. powinien prosić o dwie liczby od użytkownika,
# DESC:  2. powinien posiadać pewnego rodzaju możliwość wybrania rodzaju działania:,
# DESC:     - w postaci menu,
# DESC:     - bardziej zaawansowana postać może pobierać od użytkownika także znaki (+, -, /, *, **),
# DESC:  3. powinien posiadać jakiś sposób wychodzenia z pętli i wyświetlania podsumowania,
# DESC:  4. *Wyniki kolejnych działań, aż do wyjścia z pętli while powinien zapisywać do stringu,
# DESC:  i na koniec wyświetlić w podsumowaniu stringa złożonego z rozwiązań

DEFOPS = ["+", "-", "/", "*", "**"]
DEFVAL = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", "-"]

# TODO: kill me


while True:
    print(input("kv2: "))


# def detect(args):
#     vals = [
#         val for val in args if val not in DEFOPS and any(char.isdigit() for char in val)
#     ]
#     ops = [val for val in args if val in DEFOPS]
#     print(
#         {
#             "vals": [("".join((filter(lambda x: x in DEFVAL, val)))) for val in vals],
#             "ops": ops,
#         }
#     )


# while True:
#     detect(input("kalkv2: ").split())

# while True:
#     cmdsplit = input("kalkulator: ").split()
#     if len(cmdsplit) == 3:
#         val1 = int(cmdsplit[0])
#         val2 = int(cmdsplit[2])
#         op = cmdsplit[1]
#         if op == "+":
#             print(val1 + val2)
#         elif op == "-":
#             print(val1 - val2)
#         elif op == "/":
#             print(val1 / val2)
#         elif op == "*":
#             print(val1 * val2)
#         elif op == "**":
#             print(val1**val2)
#     elif len(cmdsplit) == 2:
#         vals = [val for val in cmdsplit if val.isnumeric()]
#         if len(vals) == 1:
#             missingval = int(input("input missing val: "))
