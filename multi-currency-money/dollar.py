class Dollor:
    def __init__(self, amount:int) -> None:
        self.amount = amount

    def times(self, multiplier):
        self.amount = self.amount * multiplier