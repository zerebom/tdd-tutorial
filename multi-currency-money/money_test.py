import unittest

from money import Money, Bank, Sum


class MoneyTest(unittest.TestCase):
    def test_multiplication(self):
        five = Money.dollar(5)
        self.assertTrue(Money.dollar(10) == (five.times(2)))
        self.assertTrue(Money.dollar(15) == (five.times(3)))

    def test_equality(self):
        # Value Objectにするため、等価性のテストを行う
        self.assertTrue(Money.dollar(5) == (Money.dollar(5)))
        self.assertFalse(Money.dollar(5) == (Money.dollar(6)))
        self.assertFalse(Money.dollar(5) == (Money.franc(5)))
        self.assertTrue(Money(5, "CHF") == (Money.franc(5)))

    def test_currency(self):
        self.assertEqual("USD", Money.dollar(1).currency())
        self.assertEqual("CHF", Money.franc(1).currency())

    def test_simple_addition(self):
        five = Money.dollar(5)
        bank = Bank()
        # reduce:式を単純な形に変形するの意.
        _sum = five.plus(five)
        # Imposterパターン
        reduced = bank.reduce(_sum, "USD")
        self.assertTrue(Money.dollar(10) == reduced)

    def test_plus_return_sum(self):
        five = Money.dollar(5)
        sum = five.plus(five)
        self.assertTrue(five, sum.augend)
        self.assertTrue(five, sum.addend)

    def test_reduce_sum(self):
        sum = Sum(Money.dollar(3), Money.dollar(4))
        bank = Bank()
        result = bank.reduce(sum, "USD")
        self.assertTrue(Money.dollar(7) == result)

    def test_reduce_money(self):
        bank = Bank()
        result = bank.reduce(Money.dollar(1),"USD")
        self.assertTrue(Money.dollar, result)

    def test_reduce_money_different_currency(self):
        bank = Bank()
        bank.addRate("CHF","USD",2)
        result = bank.reduce(Money.franc(2), "USD")
        self.assertTrue(Money.dollar(1) == result)


if __name__ == "__main__":
    unittest.main()
