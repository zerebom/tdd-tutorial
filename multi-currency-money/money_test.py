import unittest

from money import Dollor,Franc,Money

class MoneyTest(unittest.TestCase):
    def test_multiplication(self):
        five = Money.dollor(5)
        self.assertTrue(Money.dollor(10) == (five.times(2)))
        self.assertTrue(Money.dollor(15) == (five.times(3)))

    def test_franc_multiplication(self):
        five = Money.franc(5)
        self.assertTrue(Money.franc(10) == (five.times(2)))
        self.assertTrue(Money.franc(15) == (five.times(3)))

    def test_equality(self):
        # Value Objectにするため、等価性のテストを行う
        self.assertTrue(Money.dollor(5) == (Money.dollor(5)))
        self.assertFalse(Money.dollor(5) == (Money.dollor(6)))
        self.assertFalse(Money.dollor(5) == (Money.franc(5)))
        self.assertTrue(Money(5,"CHF") == (Money.franc(5)))

    def test_currency(self):
        self.assertEqual("USD", Money.dollor(1).currency())
        self.assertEqual("CHF", Money.franc(1).currency())

if __name__ == "__main__":
    unittest.main()