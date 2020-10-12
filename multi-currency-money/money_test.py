import unittest

from money import Money,Bank


class MoneyTest(unittest.TestCase):
    def test_multiplication(self):
        five = Money.dollor(5)
        self.assertTrue(Money.dollor(10) == (five.times(2)))
        self.assertTrue(Money.dollor(15) == (five.times(3)))

    def test_equality(self):
        # Value Objectにするため、等価性のテストを行う
        self.assertTrue(Money.dollor(5) == (Money.dollor(5)))
        self.assertFalse(Money.dollor(5) == (Money.dollor(6)))
        self.assertFalse(Money.dollor(5) == (Money.franc(5)))
        self.assertTrue(Money(5, "CHF") == (Money.franc(5)))

    def test_currency(self):
        self.assertEqual("USD", Money.dollor(1).currency())
        self.assertEqual("CHF", Money.franc(1).currency())

    def test_simple_addition(self):
        five = Money.dollor(5)
        bank = Bank()
        # reduce:式を単純な形に変形するの意.
        _sum = five.plus(five)
        # Imposterパターン
        reduced = bank.reduce(_sum,"USD")
        self.assertTrue(Money.dollor(10) == reduced)


if __name__ == "__main__":
    unittest.main()
