
class Franc:
    def __init__(self, amount: int) -> None:
        self.amount = amount

    def times(self, multiplier):
        return Franc(self.amount * multiplier)

    def equals(self, object):
        franc = object
        return self.amount == franc.amount

class Dollor:
    def __init__(self, amount: int) -> None:
        self.amount = amount

    def times(self, multiplier):
        return Dollor(self.amount * multiplier)

    def equals(self, object):
        dollor = object
        return self.amount == dollor.amount
