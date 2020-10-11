class Money:
    def __init__(self, amount: int) -> None:
        self.amount = amount

    def __eq__(self, obj):
        # Pythonの等価性はこれでかける
        return (self.amount == obj.amount) & (self.__class__ == obj.__class__)

    @staticmethod
    def dollor(amount:int):
        #Factory Method
        return Dollor(amount)

    @staticmethod
    def franc(amount:int):
        return Franc(amount)

class Franc(Money):
    def times(self, multiplier):
        return Franc(self.amount * multiplier)

class Dollor(Money):
    def times(self, multiplier):
        return Dollor(self.amount * multiplier)