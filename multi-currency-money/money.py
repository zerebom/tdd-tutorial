class Money:
    def __init__(self, amount: int, currency: str) -> None:
        self.amount = amount
        self._currency = currency

    def __eq__(self, obj):
        # Pythonの等価性はこれでかける
        return (self.amount == obj.amount) & (self.currency() == obj.currency())

    @staticmethod
    def dollor(amount: int):
        # Factory Method
        return Money(amount,"USD")

    @staticmethod
    def franc(amount: int):
        return Money(amount,"CHF")

    def currency(self):
        return self._currency

    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency())

    def plus(self,added):
        return Money(self.amount + added.amount, self.currency())

class Bank:
    def reduce(self,amount,currency):
        return Money.dollor(10)


