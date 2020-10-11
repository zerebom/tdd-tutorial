import unittest

from money import Dollor,Franc,Money

class MoneyTest(unittest.TestCase):
    def test_multiplication(self):
        five = Money.dollor(5)
        self.assertTrue(Dollor(10) == (five.times(2)))
        self.assertTrue(Dollor(15) == (five.times(3)))

    def test_franc_multiplication(self):
        five = Money.franc(5)
        self.assertTrue(Franc(10) == (five.times(2)))
        self.assertTrue(Franc(15) == (five.times(3)))

    def test_equality(self):
        # Value Objectにするため、等価性のテストを行う
        self.assertTrue(Dollor(5) == (Dollor(5)))
        self.assertFalse(Dollor(5) == (Dollor(6)))
        self.assertFalse(Dollor(5) == (Franc(5)))

if __name__ == "__main__":
    unittest.main()