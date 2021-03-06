class Money:
    def __init__(self, amount: int, currency: str) -> None:
        self.amount = amount
        self._currency = currency

    def __eq__(self, obj):
        # Pythonの等価性はこれでかける
        return (self.amount == obj.amount) & (self.currency() == obj.currency())

    @staticmethod
    def dollar(amount: int):
        # Factory Method
        return Money(amount, "USD")

    @staticmethod
    def franc(amount: int):
        return Money(amount, "CHF")

    def currency(self):
        return self._currency

    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency())

    def plus(self, added):
        return Sum(self, added)

    def reduce(self,bank,to):
        rate = bank.rate(self.currency(),to,None)
        return Money(self.amount/rate, to)


class Bank:
    def reduce(self, source, to: str):
        return source.reduce(self,to)

    def addRate(self, _from: str, to: str, rate: int):
        pass

    def rate(self, _from: str, to: str, rate: int):
        return 2 if (self.currency() == "CHF" and to == "USD") else 1


class Sum:
    def __init__(self, augend, addend) -> None:
        self.augend = augend
        self.addend = addend

    def reduce(self, bank, to: str):
        amount = self.augend.amount + self.addend.amount
        return Money(amount,to)

