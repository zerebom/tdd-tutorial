class Money:
    def __init__(self, amount: int) -> None:
        self.amount = amount


    def equals(self, object):
        money = object
        return (self.amount == money.amount) & (self.__class__ == money.__class__)