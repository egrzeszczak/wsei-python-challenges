class Account:
    # Proszę zaimplementować podstawową strukturę:
    # [x]: klasy nadrzędnej Account
    # Klasa Account ma następujące właściwości:
    # [x]: title,
    # [x]: balance.
    _title: str
    _balance: float

    # W klasie Account trzeba zaimplementować metodę:
    # [x]: get_balance(), która zwraca saldo.
    def get_balance(self):
        return self._balance

    # W klasie Account proszę zaimplementować metodę:
    # [x]: deposit(amount), która dodaje kwotę do salda
    # [x]: (kwota musi być nieujemna, należy ustawić odpowiednie zabezpieczenie).
    def deposit(self, _ammount: float):
        if _ammount >= 0:
            self._balance += _ammount
        else:
            print(
                f"error: niepoprawna kwota wpłaty ({_ammount}, powinna być większa albo równa zero)"
            )

    # W klasie Account proszę zaimplementować metodę:
    # [x]: withdraw(amount), która odejmuje kwotę od salda
    # [x]: (kwota musi być nieujemna, należy ustawić odpowiednie zabezpieczenie).
    def withdraw(self, _ammount: float):
        if _ammount >= 0 and _ammount <= self._balance:
            self._balance -= _ammount
        else:
            print(
                f"error: niepoprawna kwota wypłaty ({_ammount}, powinna być mniejsza niż {self._balance} i większa niż / lub równa zero)"
            )

    def __init__(self, _title="Konto", _balance=0.0):
        # Proszę zaimplementować właściwości jako:
        # [x]: zmienne instancji i ustawić je na None lub 0.
        self._title = _title
        self._balance = _balance
        print(f"created: <Account>, name: {self._title}, balance: {self._balance}")


class SavingsAccount(Account):
    # Proszę zaimplementować podstawową strukturę:
    # [x]: i klasy podrzędnej SavingsAccount.
    # SavingsAccount posiada następujące właściwości:
    # [x]: interest_rate.
    _interest_rate: float

    # W klasie SavingsAccount proszę zaimplementować metodę:
    # [x]: interest_amount(), która zwraca kwotę odsetek bieżącego salda według wzoru:
    # [x]: interest_rate ∗ balance/100.
    def interest_ammount(self):
        return self._interest_rate * self._balance / 100

    def __init__(self, _title="Konto", _balance=0.0, _interest_rate=0.015):
        super().__init__(_title, _balance)
        self._interest_rate = _interest_rate
        print(
            f"\t type: <SavingsAccount>, name: {self._title}, balance: {self._balance}, interest: {self._interest_rate}"
        )


# saccount = SavingsAccount("Ernest Grzeszczak - Savings", 12523.45, 0.02)
# saccount.withdraw(-142.0)
# saccount.withdraw(142.4)
# saccount.deposit(-142.4)
# saccount.withdraw(14204.7)
# print(saccount.interest_ammount())
