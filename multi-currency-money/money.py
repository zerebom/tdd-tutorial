class Money:
    def __init__(self, amount: int, currency: str) -> None:
        self.amount = amount
        self._currency = currency

    def __eq__(self, obj):
        # Pythonの等価性はこれでかける
        return (self.amount == obj.amount) & (self.__class__ == obj.__class__)

    @staticmethod
    def dollor(amount: int):
        # Factory Method
        return Dollor(amount,"USD")

    @staticmethod
    def franc(amount: int):
        return Franc(amount,"CHF")

    def currency(self):
        return self._currency

class Franc(Money):
    def __init__(self,amount,currency) -> None:
        super().__init__(amount,currency)

    def times(self, multiplier):
        return Money.franc(self.amount * multiplier)



class Dollor(Money):
    def __init__(self,amount,currency) -> None:
        super().__init__(amount,currency)

    def times(self, multiplier):
        return Money.dollor(self.amount * multiplier)

