class Dollor:
    def __init__(self, amount:int) -> None:
        self.amount = amount

    def times(self, multiplier):
        return Dollor(self.amount * multiplier)