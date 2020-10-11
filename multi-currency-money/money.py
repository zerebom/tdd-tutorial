class Money:
    def __init__(self, amount: int) -> None:
        self.amount = amount

    def times(self, multiplier):
        return Money(self.amount * multiplier)

    def equals(self, object):
        money = object
        return self.amount == money.amount