from money import Money


class Franc(Money):

    def times(self, multiplier):
        return Franc(self.amount * multiplier)


class Dollor(Money):

    def times(self, multiplier):
        return Dollor(self.amount * multiplier)
